#!/usr/bin/env python3
"""Single source of truth: reads results/runs_*.jsonl -> results/analysis.json.
Conventions copied from the predecessor projects: paired per-task-drift-pair
differences, bootstrap 95% CIs (10,000 resamples), two-sided sign-flip
permutation tests (20,000), paired d_z, direct drift-class x condition
interaction permutation, Benjamini-Hochberg over the FULL reported family.
"""

import argparse
import json
import pathlib
import sys
from types import SimpleNamespace

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
sys.path.insert(0, str(HERE))
import harness  # noqa: E402

RNG = np.random.default_rng(20260909)
RNG_P1 = np.random.default_rng(20261019)  # Phase 1 draws never touch the September stream
RNG_P2 = np.random.default_rng(20261020)  # Phase 2 likewise (MILESTONES.md "Phase 2 pre-registration")
RNG_P3 = np.random.default_rng(20261030)  # Phase 3 likewise (MILESTONES.md "Phase 3 pre-registration")
N_BOOT, N_PERM = 10_000, 20_000
PHASE1 = RESULTS / "phase1"
PHASE2 = RESULTS / "phase2"
PHASE3 = RESULTS / "phase3"
P1_PREFIX, P2_PREFIX = "p1:", "p2:"
CLASSES = ["rename", "enum_tighten", "required", "type_change", "default_change"]
CONDS = ["A", "B_strict", "B_lenient", "C", "D", "E"]
LEVERS = ["C", "D", "E"]

ALL_P = []  # (label, p) for BH


def load_runs():
    runs = {}
    for f in sorted(RESULTS.glob("runs_*.jsonl")):
        for line in f.read_text().splitlines():
            r = json.loads(line)
            key = (r["model"], r["task"], r["cond"], r["class"], r["phrasing"], r.get("rep", 0))
            runs[key] = r  # last write wins (resume-safe dedupe)
    return list(runs.values())


def boot_ci(diffs, rng=RNG):
    diffs = np.asarray(diffs, dtype=float)
    idx = rng.integers(0, len(diffs), size=(N_BOOT, len(diffs)))
    means = diffs[idx].mean(axis=1)
    return [float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))]


def signflip_p(diffs, rng=RNG):
    diffs = np.asarray(diffs, dtype=float)
    obs = abs(diffs.mean())
    if np.all(diffs == 0):
        return 1.0
    flips = rng.choice([-1.0, 1.0], size=(N_PERM, len(diffs)))
    perm = (diffs * flips).mean(axis=1)
    return float((np.abs(perm) >= obs - 1e-12).mean())


def paired_stats(diffs, label, rng=RNG):
    diffs = np.asarray(diffs, dtype=float)
    if len(diffs) == 0:
        return None
    p = signflip_p(diffs, rng)
    ALL_P.append((label, p))
    sd = diffs.std(ddof=1) if len(diffs) > 1 else 0.0
    return {"n": int(len(diffs)), "mean": float(diffs.mean()), "ci95": boot_ci(diffs, rng),
            "p_signflip": p, "dz": float(diffs.mean() / sd) if sd > 0 else None}


def interaction_p(pairs_by_class, cond_diffs, rng=RNG):
    """Permutation test: does the lever effect differ across drift classes?
    Statistic: between-class variance of mean paired diffs, class labels
    permuted across pairs."""
    labels, values = [], []
    for cls, dd in cond_diffs.items():
        labels += [cls] * len(dd)
        values += list(dd)
    values = np.asarray(values, dtype=float)
    labels = np.asarray(labels)

    def stat(lab):
        return np.var([values[lab == c].mean() for c in CLASSES if (lab == c).any()])

    obs = stat(labels)
    cnt = 0
    for _ in range(2000):  # 2k label permutations is plenty for var-statistic
        perm = rng.permutation(labels)
        if stat(perm) >= obs - 1e-12:
            cnt += 1
    return float(cnt / 2000)


SEPT_CTX = SimpleNamespace(rng=RNG, prefix="", paired=lambda d, label: paired_stats(d, label, RNG),
                           register=lambda label, p: ALL_P.append((label, p)))


def analyze_model(runs, model, ctx=SEPT_CTX):
    """September blocks for one model; `ctx` (rng, prefix, paired, register) defaults to the
    September stream, and Phase 2 passes its own (RNG_P2, labels prefixed "p2:")."""
    mruns = [r for r in runs if r["model"] == model and r.get("rep", 0) == 0 and r["phrasing"] == 0]
    # success lookup: cond -> {(task, class): 0/1}; A is class-independent
    succ = {c: {} for c in CONDS}
    ledger = {c: {} for c in ("B_strict", "B_lenient")}
    for r in mruns:
        if r["cond"] == "A":
            succ["A"][r["task"]] = int(r["success"])
        else:
            succ[r["cond"]][(r["task"], r["class"])] = int(r["success"])
            if r["cond"] in ledger:
                ledger[r["cond"]].setdefault(r["class"], []).append(r["drift_outcome"])

    pairs = sorted(succ["B_strict"].keys())
    out = {"n_pairs": len(pairs), "success_rate": {}, "drop": {}, "levers": {},
           "ledger": {}, "interaction": {}}
    out["success_rate"]["A"] = (float(np.mean(list(succ["A"].values()))) if succ["A"] else None)
    for cond in CONDS[1:]:
        vals = [succ[cond][p] for p in pairs if p in succ[cond]]
        out["success_rate"][cond] = float(np.mean(vals)) if vals else None
    out["success_by_class"] = {}
    for cond in CONDS[1:]:
        out["success_by_class"][cond] = {}
        for cls in CLASSES:
            vals = [succ[cond][p] for p in pairs if p[1] == cls and p in succ[cond]]
            if vals:
                out["success_by_class"][cond][cls] = float(np.mean(vals))

    # drop A -> B_strict, paired per pair (A per task)
    drop = [succ["A"].get(t, 0) - succ["B_strict"][(t, c)] for (t, c) in pairs if t in succ["A"]]
    out["drop"]["overall"] = ctx.paired(drop, f"{ctx.prefix}{model}:drop:overall")
    for cls in CLASSES:
        d = [succ["A"].get(t, 0) - succ["B_strict"][(t, c)]
             for (t, c) in pairs if c == cls and t in succ["A"]]
        if d:
            out["drop"][cls] = ctx.paired(d, f"{ctx.prefix}{model}:drop:{cls}")

    # levers vs B_strict + recovery fractions
    for lever in LEVERS:
        lv = {"vs_B": {}, "recovery_fraction": {}}
        cond_diffs = {}
        for cls in CLASSES + ["overall"]:
            sel = [p for p in pairs if (cls == "overall" or p[1] == cls) and p in succ[lever]]
            d = [succ[lever][p] - succ["B_strict"][p] for p in sel]
            if not d:
                continue
            key = f"{ctx.prefix}{model}:{lever}-B:{cls}"
            lv["vs_B"][cls] = ctx.paired(d, key)
            if cls != "overall":
                cond_diffs[cls] = d
            # recovery fraction with bootstrap CI over pairs
            a = np.array([succ["A"].get(p[0], 0) for p in sel], dtype=float)
            b = np.array([succ["B_strict"][p] for p in sel], dtype=float)
            x = np.array([succ[lever][p] for p in sel], dtype=float)
            denom = (a - b).mean()
            if denom > 0:
                idx = ctx.rng.integers(0, len(sel), size=(N_BOOT, len(sel)))
                num_bs = (x[idx] - b[idx]).mean(axis=1)
                den_bs = (a[idx] - b[idx]).mean(axis=1)
                ok = den_bs > 0
                rf = num_bs[ok] / den_bs[ok]
                lv["recovery_fraction"][cls] = {
                    "point": float((x - b).mean() / denom),
                    "ci95": [float(np.percentile(rf, 2.5)), float(np.percentile(rf, 97.5))]}
        out["levers"][lever] = lv
        if cond_diffs:
            p = interaction_p(pairs, cond_diffs, ctx.rng)
            ctx.register(f"{ctx.prefix}{model}:interaction:{lever}", p)
            out["interaction"][lever] = p

    # outcome ledger per class x profile
    for prof in ("B_strict", "B_lenient"):
        out["ledger"][prof] = {}
        for cls in CLASSES:
            outcomes = ledger[prof].get(cls, [])
            n = len(outcomes)
            if not n:
                continue
            counts = {o: outcomes.count(o) for o in
                      ("ACCEPTED_CORRECT", "ERROR_SURFACED", "ACCEPTED_WRONG", None)}
            fails = counts["ERROR_SURFACED"] + counts["ACCEPTED_WRONG"]
            out["ledger"][prof][cls] = {
                "n": n,
                "accepted_correct": counts["ACCEPTED_CORRECT"] / n,
                "error_surfaced": counts["ERROR_SURFACED"] / n,
                "accepted_wrong": counts["ACCEPTED_WRONG"] / n,
                "no_call": counts[None] / n,
                "silent_share_of_failures": (counts["ACCEPTED_WRONG"] / fails) if fails else None}
    return out


def analyze_arg_style(runs, model):
    """Fraction of optional parameters passed explicitly in baseline (A) calls,
    and B_strict success split into style-immune (required+default_change) vs
    style-exposed (rename/enum/type) classes."""
    fz = harness.frozen()
    passed = total = 0
    for r in runs:
        if r["model"] != model or r["cond"] != "A" or r.get("rep", 0) or r["phrasing"]:
            continue
        for ex in r["executed"]:
            params = fz["tools_v1"][ex["tool"]]["params"]
            for p, spec in params.items():
                if not spec.get("required"):
                    total += 1
                    if p in ex["args"]:
                        passed += 1
    imm, exp_ = [], []
    for r in runs:
        if r["model"] == model and r["cond"] == "B_strict" and not r.get("rep", 0) and not r["phrasing"]:
            (imm if r["class"] in ("required", "default_change") else exp_).append(int(r["success"]))
    return {"optional_fill_rate": passed / total if total else None,
            "b_strict_success_immune_classes": float(np.mean(imm)) if imm else None,
            "b_strict_success_exposed_classes": float(np.mean(exp_)) if exp_ else None}


def analyze_noise(runs, model):
    reps = {}
    for r in runs:
        if r["model"] == model and r.get("rep", 0) is not None and r["cond"] == "B_strict":
            reps.setdefault((r["task"], r["class"]), {})[r.get("rep", 0)] = r
    stab = []
    for key, d in reps.items():
        if len(d) == 5:
            succs = [d[i]["success"] for i in range(5)]
            outs = [d[i]["drift_outcome"] for i in range(5)]
            stab.append({"pair": list(key), "success_flips": int(len(set(succs)) > 1),
                         "outcome_flips": int(len(set(outs)) > 1)})
    if not stab:
        return None
    return {"n_pairs": len(stab),
            "success_flip_rate": float(np.mean([s["success_flips"] for s in stab])),
            "outcome_flip_rate": float(np.mean([s["outcome_flips"] for s in stab]))}


def analyze_phrasing(runs, model, ctx=SEPT_CTX):
    by = {}
    for r in runs:
        if r["model"] == model and r.get("rep", 0) == 0 and r["cond"] in ("A", "B_strict"):
            by[(r["cond"], r["task"], r["class"], r["phrasing"])] = int(r["success"])
    res = {}
    for cond in ("A", "B_strict"):
        d = []
        for (c, t, cls, ph), v in by.items():
            if c == cond and ph == 1 and (cond, t, cls, 0) in by:
                d.append(v - by[(cond, t, cls, 0)])
        if d:
            res[cond] = ctx.paired(d, f"{ctx.prefix}{model}:phrasing:{cond}")
    return res or None


def token_costs():
    """Artifact sizes: diff JSON vs full v2 declaration, chars/4 ~ tokens; plus
    measured per-condition prompt tokens from cost_log.jsonl."""
    fz = harness.frozen()
    diffs_t, decls_t = [], []
    for key, diff in fz["diffs"].items():
        tool = key.split("::")[0]
        decl = harness.declaration(tool, fz["tools_v1"][tool], fz["v2_schemas"][key])
        diffs_t.append(len(json.dumps(diff["changes"])) / 4)
        decls_t.append(len(json.dumps(decl)) / 4)
    res = {"diff_artifact_tokens_mean": float(np.mean(diffs_t)),
           "full_schema_artifact_tokens_mean": float(np.mean(decls_t)),
           "ratio": float(np.mean(diffs_t) / np.mean(decls_t))}
    log = HERE / "cost_log.jsonl"
    if log.exists():
        per_cond = {}
        for line in log.read_text().splitlines():
            r = json.loads(line)
            if r.get("phase", "experiments") != "experiments":
                continue  # September only; later phases have their own accounting
            tag = r.get("tag", "")
            parts = tag.split("-")
            if len(parts) >= 3 and "tokens_in" in r:
                cond = parts[1] if parts[1] in ("A", "C", "D", "E") else (
                    "B_strict" if tag.find("-B_strict-") >= 0 else
                    "B_lenient" if tag.find("-B_lenient-") >= 0 else None)
                if cond:
                    per_cond.setdefault((r["model"], cond), []).append(r["tokens_in"])
        res["measured_prompt_tokens"] = {
            f"{m}:{c}": {"mean": float(np.mean(v)), "n": len(v)}
            for (m, c), v in sorted(per_cond.items())}
    return res


def bh(alpha=0.05, tests=None):
    ps = sorted(ALL_P if tests is None else tests, key=lambda x: x[1])
    m = len(ps)
    thresh, survivors = 0.0, []
    for i, (lab, p) in enumerate(ps, 1):
        if p <= alpha * i / m:
            thresh = p
    for lab, p in ps:
        if p <= thresh:
            survivors.append(lab)
    return {"n_tests": m, "effective_threshold": thresh, "n_survive": len(survivors),
            "survivors": survivors}


def phase1_ctx():
    return SimpleNamespace(rng=RNG_P1, boot=lambda d: boot_ci(d, RNG_P1),
                           paired=lambda d, label: paired_stats(d, label, RNG_P1),
                           register=lambda label, p: ALL_P.append((label, p)))


def phase2_ctx():
    ctx = SimpleNamespace(rng=RNG_P2, prefix=P2_PREFIX, boot=lambda d: boot_ci(d, RNG_P2),
                          paired=lambda d, label: paired_stats(d, label, RNG_P2),
                          register=lambda label, p: ALL_P.append((label, p)), arg_style=analyze_arg_style)
    ctx.september = lambda recs, model: analyze_model(recs, model, ctx)
    ctx.phrasing = lambda recs, model: analyze_phrasing(recs, model, ctx)
    return ctx


def _refuse_partial(args, name, family, status):
    if (not family["complete"] and args.out.resolve() == (RESULTS / "analysis.json").resolve()
            and not args.allow_partial):
        raise SystemExit(f"{name} family has {family['n_tests']} of {family['expected']} tests "
                         f"(incomplete: {sorted(status)}); not overwriting results/analysis.json. "
                         "Use --out <file> for an interim look, or --allow-partial.")


def _bh_changes(before, after):
    """Earlier tests whose BH verdict moves when the Phase-2 tests join the family."""
    old = set(before["survivors"])
    new = {lab for lab in after["survivors"] if not lab.startswith(P2_PREFIX)}
    return {"lost": sorted(old - new), "gained": sorted(new - old)}


def _families(args, out, phase1, phase2):
    """One BH family over everything; Phase 1 keeps the verdicts of its own 194-test family."""
    import analyze_phase1 as ap1
    import analyze_phase2 as ap2
    out["bh"] = bh()
    before = bh(tests=[t for t in ALL_P if not t[0].startswith(P2_PREFIX)])
    if phase1:
        out["bh_original_family"] = bh(tests=[t for t in ALL_P if not t[0].startswith((P1_PREFIX, P2_PREFIX))])
        phase1["predictions"] = ap1.predictions(phase1, set(before["survivors"]))
        phase1["family"] = {"n_tests": before["n_tests"], "expected": ap1.EXPECTED_TESTS,
                            "complete": before["n_tests"] == ap1.EXPECTED_TESTS}
        _refuse_partial(args, "Phase-1", phase1["family"], phase1["status"])
    if phase2:
        phase2["predictions"] = ap2.predictions(phase2, set(out["bh"]["survivors"]))
        phase2["family"] = {"n_tests": out["bh"]["n_tests"], "expected": ap2.EXPECTED_TESTS,
                            "complete": out["bh"]["n_tests"] == ap2.EXPECTED_TESTS}
        phase2["bh_changes"] = _bh_changes(before, out["bh"])
        _refuse_partial(args, "Phase-2", phase2["family"], phase2["status"])


def share_ci(flags, rng=RNG_P3, n_boot=N_BOOT):
    """Bootstrap CI for a proportion (Phase 3; the corpus registers no BH test)."""
    import numpy as _np
    vec = _np.asarray(flags, dtype=float)
    if not vec.size:
        return {"point": None, "ci95": None, "n": 0}
    draws = rng.integers(0, vec.size, size=(n_boot, vec.size))
    means = vec[draws].mean(axis=1)
    return {"point": float(vec.mean()),
            "ci95": [float(_np.percentile(means, 2.5)), float(_np.percentile(means, 97.5))],
            "n": int(vec.size)}


def phase3_ctx():
    return SimpleNamespace(rng=RNG_P3, share=lambda flags: share_ci(flags, RNG_P3))


def _print_summary(out, models):
    print(f"analysis.json written: {out['n_records']} records, {len(models)} models, "
          f"{out['bh']['n_tests']} tests, {out['bh']['n_survive']} survive BH")
    for m in models:
        sm = out["models"][m]
        print(f"\n== {m} ==  pairs={sm['n_pairs']}")
        print("  success:", {k: (round(v, 3) if v is not None else None)
                             for k, v in sm["success_rate"].items()})
        for lever in LEVERS:
            rf = sm["levers"][lever].get("recovery_fraction", {}).get("overall")
            if rf:
                print(f"  recovery {lever}: {rf['point']:.2f} CI {rf['ci95']}")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=pathlib.Path, default=RESULTS / "analysis.json")
    ap.add_argument("--phase1-dir", type=pathlib.Path, default=PHASE1)
    ap.add_argument("--phase2-dir", type=pathlib.Path, default=PHASE2)
    ap.add_argument("--phase3-dir", type=pathlib.Path, default=PHASE3)
    ap.add_argument("--allow-partial", action="store_true",
                    help="write results/analysis.json even if a phase's BH family is incomplete")
    args = ap.parse_args(argv)
    runs = load_runs()
    models = sorted({r["model"] for r in runs})
    out = {"generated": "analyze.py", "n_records": len(runs), "models": {}}
    for m in models:
        out["models"][m] = analyze_model(runs, m)
        out["models"][m]["arg_style"] = analyze_arg_style(runs, m)
        nz = analyze_noise(runs, m)
        if nz:
            out["models"][m]["noise_floor"] = nz
        ph = analyze_phrasing(runs, m)
        if ph:
            out["models"][m]["phrasing_battery"] = ph
    out["token_costs"] = token_costs()
    import analyze_phase1 as ap1  # after the September blocks: they keep their RNG draws
    import analyze_phase2 as ap2
    sept_noise = {m: out["models"][m].get("noise_floor") for m in models}
    p1runs = ap1.load_phase1_runs(args.phase1_dir) if args.phase1_dir.exists() else []
    phase1 = ap1.analyze(runs, p1runs, phase1_ctx(), sept_noise, args.phase1_dir)
    if phase1:
        out["phase1"] = phase1
    p2runs = ap2.load_phase2_runs(args.phase2_dir) if args.phase2_dir.exists() else []
    phase2 = ap2.analyze(p2runs, phase2_ctx(), sept_noise, args.phase2_dir)
    if phase2:
        out["phase2"] = phase2
    import analyze_phase3 as ap3  # after Phase 2: the earlier blocks keep their RNG draws
    phase3 = ap3.analyze(args.phase3_dir, phase3_ctx()) if args.phase3_dir.exists() else None
    if phase3:
        phase3["predictions"] = ap3.predictions(phase3)
        out["phase3"] = phase3
    _families(args, out, phase1, phase2)
    args.out.write_text(json.dumps(out, indent=1))
    _print_summary(out, models)


if __name__ == "__main__":
    main()
