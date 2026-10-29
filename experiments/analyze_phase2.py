#!/usr/bin/env python3
"""Phase-2 blocks of analysis.json, called by analyze.main (never imports analyze: when
analyze.py runs as __main__ a second import would split ALL_P and the RNGs).

`ctx` supplies the statistics bound to RNG_P2 and the one BH family:
  ctx.paired(diffs, label), ctx.register(label, p), ctx.boot(diffs), ctx.rng   (as in Phase 1)
  ctx.september(records, model) -> analyze.analyze_model, labels "p2:..." (27 tests)
  ctx.phrasing(records, model)  -> analyze.analyze_phrasing, labels "p2:..." (2 tests)
  ctx.arg_style(records, model) -> analyze.analyze_arg_style (descriptive)
Rules: MILESTONES.md "Phase 2 pre-registration", Phase 2 amendments 1 and 2.
"""

import json
import pathlib
from collections import Counter, defaultdict

import numpy as np

import analyze_phase1 as ap1
import check_phase1_logs as chk
import harness
import phase1_grid as p1
import phase1_stats as st
import phase2_grid as p2
import phase2_stats as v

FAMILY_ARMS = ("core", "phrasing", "noise", "infoform", "placement")
PLACEMENT = p2.PLACEMENT_CELL
FLASH_REASONING = "MINIMAL"
EXPECTED_TESTS = 194 + 35 * len(v.NEW_FAMILIES) + 2  # 301; the direct arm (+2) does not run (probe: no lift)
PROBE_FILE, REPLAY_FILE = "probe_decoding.json", "validator_replay.json"
NO_DRIFT = ("A", "A_fill")


def base_reasoning(model):
    return FLASH_REASONING if model == v.FLASH else "default"


def _endpoint(r):
    return (r.get("pin") or {}).get("endpoint")


def load_phase2_runs(path):
    """runs_*.jsonl minus pilots; dedupe by (model, rec_key), last wins. Unparsable lines raise, and so
    does one job served through two endpoints (the tables would silently keep whichever came last)."""
    runs = {}
    for f in sorted(pathlib.Path(path).glob("runs_*.jsonl")):
        if f.name.endswith(".pilot.jsonl"):
            continue
        records, bad = chk.read_records(f)
        if bad:
            raise SystemExit(f"{f.name}: unparsable lines {bad[:5]}; repair before analysing")
        for r in records:
            k = (r["model"], *p1.rec_key(r))
            if k in runs and _endpoint(runs[k]) != _endpoint(r):
                raise SystemExit(f"{f.name}: {k} logged through endpoints {_endpoint(runs[k])} and {_endpoint(r)}")
            runs[k] = r
    return list(runs.values())


def records_of(runs, model):
    return [r for r in runs if r["model"] == model and r.get("reasoning") == base_reasoning(model)]


def complete(runs, model, arm):
    return not chk.coverage(records_of(runs, model), arm, base_reasoning(model), phase=2)["missing"]


def build_tab(recs):
    """cond -> {(task, class): 0|1} over rep-0, phrasing-0 records."""
    tab = defaultdict(dict)
    for r in recs:
        if r.get("rep", 0) == 0 and r["phrasing"] == 0:
            tab[r["cond"]][(r["task"], r["class"])] = int(r["success"])
    return dict(tab)


def _vec(tab, cond, pairs):
    return st.cell_vector(tab, cond, pairs)


def infoform(ctx, model, tab):
    """Four tests on the 48 information pairs; D' - D on the 24 required pairs for P12 (not tested)."""
    pairs = st.pairs_in(ap1.primary_pairs(), st.INFO)
    req = st.pairs_in(ap1.primary_pairs(), ("required",))
    out = {name: ctx.paired(_vec(tab, x, pairs) - _vec(tab, y, pairs), f"p2:{model}:infoform:{name}")
           for name, (x, y) in ap1.INFOFORM.items()}
    d = _vec(tab, "Dprime", req) - _vec(tab, "D", req)
    out["Dprime-D_required"] = {"n": len(req), "mean": float(d.mean()), "ci95": ctx.boot(d)}
    return out


def placement(ctx, model, tab):
    """C:user:prose:apply on all 120 pairs: two tests, its recovery and the P11 gain over C."""
    pairs = ap1.primary_pairs()
    a, b, c, x = (_vec(tab, k, pairs) for k in ("A", "B_strict", "C", PLACEMENT))
    denom = (a - b).mean()
    return {"vs_B": ctx.paired(x - b, f"p2:{model}:{PLACEMENT}-B_strict"),
            "vs_C": ctx.paired(x - c, f"p2:{model}:{PLACEMENT}-C"),
            "recovery": st.recovery(a, b, x, ctx.rng),
            "gain_over_C": float((x - c).mean() / denom) if denom > 0 else None}


def noise_floor(runs, model):
    """The family's own noise arm: B_strict on the 30 stratified tasks x 5 reps (rep 0 is core)."""
    keys = {(t["id"], t["assigned"][0]) for t in p1.noise_tasks()}
    reps = defaultdict(list)
    for r in records_of(runs, model):
        if r["cond"] == "B_strict" and r["phrasing"] == 0 and (r["task"], r["class"]) in keys:
            reps[(r["task"], r["class"])].append(int(r["success"]))
    return st.flip_rate(reps)


def optional_fill_rate(recs, cond):
    """Share of optional v1 parameters passed explicitly in executed calls (fill manipulation check)."""
    params = harness.frozen()["tools_v1"]
    passed = total = 0
    for r in recs:
        if r["cond"] != cond or r.get("rep", 0) or r["phrasing"]:
            continue
        for ex in r["executed"]:
            optional = [p for p, spec in params[ex["tool"]]["params"].items() if not spec.get("required")]
            total += len(optional)
            passed += sum(p in ex["args"] for p in optional)
    return passed / total if total else None


def fill(ctx, recs):
    """Flash: B_fill - B_strict (re-run) on the 48 information and the 72 contrast pairs."""
    tab, allp = build_tab(recs), ap1.primary_pairs()
    out = {"success": {c: float(_vec(tab, c, allp).mean()) for c in p2.FILL_CONDS},
           "optional_fill_rate_A_fill": optional_fill_rate(recs, "A_fill"), "tests": {}}
    for name, classes in (("info", st.INFO), ("contrast", st.CONTRAST)):
        pairs = st.pairs_in(allp, classes)
        d = _vec(tab, "B_fill", pairs) - _vec(tab, "B_strict", pairs)
        out["tests"][name] = ctx.paired(d, f"p2:{v.FLASH}:fill:B_fill-B_strict:{name}")
    return out


def _read(phase2_dir, name):
    f = pathlib.Path(phase2_dir) / name
    return json.loads(f.read_text()) if f.exists() else None


def probe(phase2_dir):
    d = _read(phase2_dir, PROBE_FILE)
    return {"date": d["date"], "spec": d["spec"], "finished": d["finished"], **d["summary"]} if d else None


def direct_block(probe_summary, runs):
    """The direct arm runs only on a lifting luna direct route. The 2026-10-28 probe found none,
    so its analysis is not implemented and direct records or a lifting probe stop the analysis."""
    if (probe_summary and probe_summary["decision"]["lifts"]) or any(r.get("arm") == "direct" for r in runs):
        raise SystemExit("direct-arm records or a lifting probe: the direct arm's analysis is not "
                         "implemented (the 2026-10-28 probe found no lift)")
    return {"run": False, "basis": probe_summary["decision"]["status"] if probe_summary else "decoding probe missing"}


def validator_replay(phase2_dir):
    d = _read(phase2_dir, REPLAY_FILE)
    if d is None:
        return None
    return {"n_calls": d["n_calls"], "versions": d["versions"], "p16_profile": d["p16_profile"],
            "agreement": {name: {"vs_strict": a["vs_strict"]["rate"], "vs_lenient": a["vs_lenient"]["rate"]}
                          for name, a in d["agreement"].items()},
            "by_error_type": {name: a["by_error_type"] for name, a in d["agreement"].items()}}


def main_records(runs):
    """The records the mechanism block labels: rep 0, phrasing 0, base reasoning, a drifted condition."""
    return [r for r in runs if r.get("rep", 0) == 0 and r["phrasing"] == 0 and r["cond"] not in NO_DRIFT
            and r.get("reasoning") == base_reasoning(r["model"])]


def b_index(runs):
    """(model, task, class, "B_strict") -> the same model's Phase-2 B_strict record (ap1.auto_label's b_rec)."""
    return {(r["model"], r["task"], r["class"], r["cond"]): r for r in main_records(runs) if r["cond"] == "B_strict"}


def mechanism(runs):
    """drift_labels.classify counts per model x condition x class on the main records."""
    idx = b_index(runs)
    out = defaultdict(lambda: defaultdict(lambda: defaultdict(Counter)))
    for r in main_records(runs):
        out[r["model"]][r["cond"]][r["class"]][ap1.auto_label(r, idx)] += 1
    return {m: {c: {k: dict(x) for k, x in cls.items()} for c, cls in conds.items()} for m, conds in out.items()}


def audit(runs, phase2_dir):
    """Label-audit agreement (Task 9) when the sample file exists, recomputed with the current labeler."""
    sample = _read(phase2_dir, ap1.AUDIT_FILE)
    return ap1.audit_agreement_on(main_records(runs), b_index(runs), sample) if sample else None


def _instrument_label(r):
    return r["cond"] + ("@phrasing1" if r["phrasing"] else "") + ("@noise" if r.get("rep", 0) else "")


def instrument(runs):
    """check_phase1_logs.cell_report per model and cell, plus mean reasoning tokens (amendment 2)."""
    out = {}
    for m in sorted({r["model"] for r in runs}):
        recs = [{**r, "cond": _instrument_label(r)} for r in runs if r["model"] == m]
        cells = chk.cell_report(recs)
        for label, c in cells.items():
            c["reasoning_tokens_mean"] = float(np.mean([(r.get("usage") or {}).get("reasoning", 0)
                                                        for r in recs if r["cond"] == label]))
        out[m] = cells
    return out


def _family_blocks(ctx, out, runs, model):
    recs = records_of(runs, model)
    done = {arm: complete(runs, model, arm) for arm in FAMILY_ARMS}
    out["status"].update({f"{model}:{arm}": "incomplete" for arm, ok in done.items() if not ok})
    out["noise_floor"][model] = noise_floor(runs, model) if done["noise"] else None
    if not done["core"]:
        return
    tab = build_tab(recs)
    out["models"][model] = {**ctx.september([r for r in recs if r["cond"] in p2.CORE_CONDS], model),
                            "arg_style": ctx.arg_style(recs, model)}
    if done["phrasing"]:
        out["models"][model]["phrasing_battery"] = ctx.phrasing(recs, model)
    if done["infoform"]:
        out["infoform"][model] = infoform(ctx, model, tab)
    if done["placement"]:
        out["placement"][model] = placement(ctx, model, tab)


def analyze(runs, ctx, sept_noise, phase2_dir):
    """All Phase-2 blocks; arms with missing jobs are reported as incomplete and add no tests."""
    if not runs:
        return None
    out = {"status": {}, "models": {}, "infoform": {}, "placement": {}, "noise_floor": {}}
    for m in v.NEW_FAMILIES:
        _family_blocks(ctx, out, runs, m)
    out["noise_floor"][v.FLASH] = (sept_noise.get(v.FLASH) or {}).get("success_flip_rate")  # Flash keeps September's
    out["fill"] = fill(ctx, records_of(runs, v.FLASH)) if complete(runs, v.FLASH, "fill") else None
    if out["fill"] is None:
        out["status"][f"{v.FLASH}:fill"] = "incomplete"
    out["probe"] = probe(phase2_dir)
    out["direct"] = direct_block(out["probe"], runs)
    out["validator_replay"] = validator_replay(phase2_dir)
    out["mechanism"] = {**mechanism(runs), "audit_agreement": audit(runs, phase2_dir)}
    out["instrument"] = instrument(runs)
    return out


def _claude_stats(block, survivors):
    out = {}
    for m in (m for m in v.CLAUDE if m in block["models"]):
        lever = block["models"][m]["levers"]["C"]
        rec, vs = lever["recovery_fraction"].get("overall"), lever["vs_B"]["overall"]
        out[m] = {"recovery": rec["point"] if rec else None, "ci_low": vs["ci95"][0],
                  "bh": f"p2:{m}:C-B:overall" in survivors, "mean": vs["mean"], "floor": block["noise_floor"].get(m)}
    return out


def _llama_stats(block, survivors):
    m = v.LLAMA
    if m not in block["models"] or m not in block["placement"]:
        return None
    rec, plc = block["models"][m]["levers"]["C"]["recovery_fraction"].get("overall"), block["placement"][m]
    return {"c_recovery": rec["point"] if rec else None, "gain": plc["gain_over_C"],
            "bh": f"p2:{m}:{PLACEMENT}-C" in survivors, "mean": plc["vs_C"]["mean"],
            "floor": block["noise_floor"].get(m)}


def _fill_stats(block, survivors):
    f = block["fill"]
    if not f:
        return None
    info = f["tests"]["info"]
    return {"info": {"mean": info["mean"], "ci95": info["ci95"],
                     "bh": f"p2:{v.FLASH}:fill:B_fill-B_strict:info" in survivors},
            "contrast": {"ci95": f["tests"]["contrast"]["ci95"]}, "floor": block["noise_floor"].get(v.FLASH)}


def predictions(block, survivors):
    """P10-P16 after BH over the one family (survivors: labels that pass)."""
    keys = ("Dprime-D_required", "CD-C", "CD-D")
    replay = block["validator_replay"]
    stats = {"claude": _claude_stats(block, survivors), "llama": _llama_stats(block, survivors),
             "families": {m: {k: s[k] for k in keys} for m, s in block["infoform"].items()},
             "fill": _fill_stats(block, survivors), "direct": block["direct"],
             "replay": replay["agreement"] if replay else None}
    return v.verdicts(stats)
