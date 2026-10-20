#!/usr/bin/env python3
"""Phase-1 blocks of analysis.json, called by analyze.main (never imports analyze: when
analyze.py runs as __main__ a second import would split ALL_P and the RNG).

`ctx` supplies the statistics bound to the Phase-1 RNG and the one BH family:
  ctx.paired(diffs, label) -> paired_stats dict (sign-flip p joins BH)
  ctx.register(label, p)   -> adds a permutation p-value to BH
  ctx.boot(diffs)          -> bootstrap 95% CI (not tested)
  ctx.rng                  -> numpy Generator (RNG_P1)
Rules: MILESTONES.md Phase 1 pre-registration, addendum pins A1-A9, amendment 1.
"""

import json
import pathlib
from collections import Counter, defaultdict

import numpy as np

import check_phase1_logs as chk
import drift_labels
import harness
import phase1_grid as p1
import phase1_stats as st
from run_gemini import THINKING

LUNA, QWEN = "openai/gpt-5.6-luna", "modal-qwen2.5-7b"
ABLATION_MODELS = (LUNA, QWEN)
REASONING = {**THINKING}  # Gemini thinking level is the record's reasoning; others "default"
ABLATION_COND = harness.ABLATION_CELLS + ["C_decl"]
INFOFORM = {"Dprime-C": ("Dprime", "C"), "Dprime-D": ("Dprime", "D"), "CD-C": ("CD", "C"), "CD-D": ("CD", "D")}
SELECTION_FILE = "thinking_cell_selection.json"
AUDIT_FILE = "audit_labels_sample.json"  # Task 13 hand audit (audit_sample.py)
AUDIT_PASS = 0.9  # below this, fix drift_labels.classify before the final analysis
SEPT_FLOOR_PROXY = {"gemini-3.1-pro-preview": "gemini-3.6-flash"}  # pin A5
EXPECTED_TESTS = 112 + 82  # locked family; the route arm (+2) does not run (amendment 1)


def base_reasoning(model):
    return REASONING.get(model, "default")


def load_phase1_runs(path):
    """runs_*.jsonl minus pilots; dedupe by (model, route, rec_key), last wins. Unparsable lines raise."""
    runs = {}
    for f in sorted(pathlib.Path(path).glob("runs_*.jsonl")):
        if f.name.endswith(".pilot.jsonl"):
            continue
        records, bad = chk.read_records(f)
        if bad:
            raise SystemExit(f"{f.name}: unparsable lines {bad[:5]}; repair before analysing")
        for r in records:
            runs[(r["model"], r.get("route"), *p1.rec_key(r))] = r
    return list(runs.values())


def primary_pairs():
    return sorted((t["id"], cls) for t, cls in p1.primary_pairs())


def model_pairs(model):
    """Pin A1: luna on the 72-pair contrast set, everyone else on all 120."""
    pairs = primary_pairs()
    return st.pairs_in(pairs, st.CONTRAST) if model == LUNA else pairs


def sept_index(runs):
    """{(model, task, class, cond): record} for September phrasing-0, rep-0 records; A keyed by class too."""
    idx, by_task_a = {}, {}
    for r in runs:
        if r["phrasing"] != 0 or r.get("rep", 0) != 0:
            continue
        if r["cond"] == "A":
            by_task_a[(r["model"], r["task"])] = r
        else:
            idx[(r["model"], r["task"], r["class"], r["cond"])] = r
    for t, cls in primary_pairs():
        for (m, task), r in by_task_a.items():
            if task == t:
                idx[(m, t, cls, "A")] = r
    return idx


def build_tab(sept, p1runs, model):
    """cond (or (cond, reasoning) off the model's base level) -> {(task, class): 0|1}."""
    tab = defaultdict(dict)
    for (m, t, cls, cond), r in sept.items():
        if m == model and cond in ("A", "B_strict", "C", "D"):
            tab[cond][(t, cls)] = int(r["success"])
    base = base_reasoning(model)
    for r in p1runs:
        if r["model"] != model or r.get("route") or r.get("rep", 0) != 0:
            continue
        key = r["cond"] if r.get("reasoning") == base else (r["cond"], r.get("reasoning"))
        tab[key][(r["task"], r["class"])] = int(r["success"])
    return dict(tab)


def complete(p1runs, model, arm, cells=None, reasoning=None):
    recs = [r for r in p1runs if r["model"] == model and not r.get("route")]
    return not chk.coverage(recs, arm, reasoning or base_reasoning(model), cells)["missing"]


def _vec(tab, cond, pairs):
    return st.cell_vector(tab, cond, pairs)


def cell_block(ctx, model, tab, pairs, cell):
    a, b, x = _vec(tab, "A", pairs), _vec(tab, "B_strict", pairs), _vec(tab, cell, pairs)
    out = {"vs_B": ctx.paired(x - b, f"p1:{model}:{cell}-B_strict"),
           "recovery": st.recovery(a, b, x, ctx.rng)}
    if cell != st.REPLICATE_C:
        out["vs_Crerun"] = ctx.paired(x - _vec(tab, st.REPLICATE_C, pairs), f"p1:{model}:{cell}-Crerun")
    return out


def ablation(ctx, model, tab):
    pairs = model_pairs(model)
    allp = primary_pairs()
    return {"pairs": len(pairs),
            "cells": {c: cell_block(ctx, model, tab, pairs, c) for c in ABLATION_COND},
            "success_all": {c: float(_vec(tab, c, allp).mean()) for c in ABLATION_COND}}


MAIN_EFFECTS = {"user-sys": ("place", "user", "sys"), "tool-sys": ("place", "tool", "sys"),
                "prose-json": ("fmt", "prose", "json"), "apply-none": ("instr", "apply", "none")}


def main_effects(ctx, model, tab):
    pairs = model_pairs(model)
    return {name: ctx.paired(st.main_effect(tab, pairs, *spec), f"p1:{model}:main:{name}")
            for name, spec in MAIN_EFFECTS.items()}


def interactions(ctx, model, tab):
    pairs = model_pairs(model)
    out = {}
    for factor, name in (("fmt", "place_x_format"), ("instr", "place_x_instruction")):
        E = st.effect_by_place(tab, pairs, factor)
        p = st.perm_within_pairs(E, ctx.rng)
        ctx.register(f"p1:{model}:interaction:{name}", p)
        out[name] = {"p_perm": p, "effect_by_place": dict(zip(harness.PLACES, E.mean(axis=0).tolist()))}
    out["format_x_instruction"] = ctx.paired(st.fmt_instr_contrast(tab, pairs),
                                             f"p1:{model}:interaction:format_x_instruction")
    return out


def thinking_selection(tab):
    """Pin A6, from the luna ablation: recoveries (points) on the contrast set, success on all pairs."""
    pairs = model_pairs(LUNA)
    a, b = _vec(tab, "A", pairs), _vec(tab, "B_strict", pairs)
    rec = {}
    for c in st.BEST_CELL_CANDIDATES:
        denom = (a - b).mean()
        rec[c] = float((_vec(tab, c, pairs) - b).mean() / denom) if denom > 0 else None
    succ = {c: float(_vec(tab, c, primary_pairs()).mean()) for c in st.BEST_CELL_CANDIDATES}
    return {"selected": st.select_best_cell(rec, succ, harness.PHASE1_CONDS),
            "recoveries": rec, "success_all": succ, "rule": "A6"}


def check_selection(tab, phase1_dir, has_thinking=False):
    derived = thinking_selection(tab)
    f = pathlib.Path(phase1_dir) / SELECTION_FILE
    if has_thinking and not f.exists():
        raise SystemExit(f"thinking records exist but {SELECTION_FILE} does not: it must be committed "
                         "before the thinking arm runs (pin A6)")
    if f.exists() and json.loads(f.read_text())["selected"] != derived["selected"]:
        raise SystemExit(f"{SELECTION_FILE} says {json.loads(f.read_text())['selected']!r} but the data "
                         f"select {derived['selected']!r}; the thinking arm ran on the wrong cell")
    return derived


def thinking(ctx, tab, selected):
    pairs = model_pairs(LUNA)
    a, b = _vec(tab, "A", pairs), _vec(tab, "B_strict", pairs)
    out = {}
    for c in (st.REPLICATE_C, selected):
        high = _vec(tab, (c, "high"), pairs)
        out[c] = {"high_vs_default": ctx.paired(high - _vec(tab, c, pairs), f"p1:{LUNA}:thinking:{c}"),
                  "recovery_high": st.recovery(a, b, high, ctx.rng)}
    return out


def infoform(ctx, model, tab):
    pairs = st.pairs_in(primary_pairs(), st.INFO)
    req = st.pairs_in(primary_pairs(), ("required",))
    out = {name: ctx.paired(_vec(tab, x, pairs) - _vec(tab, y, pairs), f"p1:{model}:infoform:{name}")
           for name, (x, y) in INFOFORM.items()}
    d = _vec(tab, "Dprime", req) - _vec(tab, "D", req)
    out["Dprime-D_required"] = {"n": len(req), "mean": float(d.mean()), "ci95": ctx.boot(d)}  # P5, not tested
    return out


def noise_floors(p1runs, sept_noise):
    """Pin A5: luna = Phase-1 noise-arm flip rate; Qwen/Flash September; Pro uses Flash's."""
    reps = defaultdict(dict)
    for r in p1runs:
        if r["model"] == LUNA and r["cond"] == st.REPLICATE_C and not r.get("route") and r.get("reasoning") == "default":
            reps[(r["task"], r["class"])][r.get("rep", 0)] = int(r["success"])
    noise_keys = {(t["id"], t["assigned"][0]) for t in p1.noise_tasks()}
    luna = {k: list(v.values()) for k, v in reps.items() if k in noise_keys}
    floors = {m: (sept_noise.get(SEPT_FLOOR_PROXY.get(m, m)) or {}).get("success_flip_rate")
              for m in st.FAMILIES if m != LUNA}
    return {**floors, LUNA: st.flip_rate(luna), "proxy": SEPT_FLOOR_PROXY}


def drift_over_time(ctx, model, tab, sept, p1runs):
    """Pin A8: C re-run vs September C on all primary pairs ("per class" needs every class),
    paired difference with bootstrap CI; call identity per class."""
    pairs = primary_pairs()
    d = _vec(tab, st.REPLICATE_C, pairs) - _vec(tab, "C", pairs)
    rerun = {(r["task"], r["class"]): r for r in p1runs
             if r["model"] == model and r["cond"] == st.REPLICATE_C and r.get("rep", 0) == 0
             and not r.get("route") and r.get("reasoning") == base_reasoning(model)}
    same = defaultdict(list)
    for t, cls in pairs:
        old = sept[(model, t, cls, "C")]
        same[cls].append(drift_labels.signature(rerun[(t, cls)]) == drift_labels.signature(old))
    return {"n": len(pairs), "mean": float(d.mean()), "ci95": ctx.boot(d),
            "call_identity": {c: float(np.mean(v)) for c, v in same.items()}}


def _main_records(p1runs, model=None):
    """Rep-0, unrouted records at the model's base reasoning level."""
    return [r for r in p1runs if (model is None or r["model"] == model) and not r.get("route")
            and r.get("rep", 0) == 0 and r.get("reasoning") == base_reasoning(r["model"])]


def auto_label(r, sept):
    """drift_labels.classify with the September B_strict record of the same pair as b_rec."""
    return drift_labels.classify(r, sept.get((r["model"], r["task"], r["class"], "B_strict")))[0]


def mechanism(p1runs, sept):
    """classify label counts per model x cell x class."""
    out = defaultdict(lambda: defaultdict(lambda: defaultdict(Counter)))
    for r in _main_records(p1runs):
        out[r["model"]][r["cond"]][r["class"]][auto_label(r, sept)] += 1
    return {m: {c: {k: dict(v) for k, v in cls.items()} for c, cls in conds.items()} for m, conds in out.items()}


def audit_key(r):
    return {"model": r["model"], "task": r["task"], "cond": r["cond"], "class": r["class"],
            "phrasing": r["phrasing"], "rep": r.get("rep", 0), "reasoning": r.get("reasoning", "default")}


def audit_agreement(p1runs, sept, sample):
    """Human vs automatic label on the hand-audit items. The automatic label is recomputed with the
    current labeler, so a fix to drift_labels.classify shows up here without redrawing."""
    index = {json.dumps(audit_key(r), sort_keys=True): r for r in _main_records(p1runs)}
    rows = []
    for it in sample["items"]:
        r = index.get(json.dumps(it["key"], sort_keys=True))
        if r is None:
            raise SystemExit(f"audit item {it['id']}: record {it['key']} is not in the Phase-1 runs")
        rows.append((it["id"], auto_label(r, sept), it["human_label"]))
    labelled = [row for row in rows if row[2] is not None]
    agree = sum(auto == human for _, auto, human in labelled)
    rate = agree / len(labelled) if labelled else None
    complete = len(labelled) == len(rows)
    return {"n_items": len(rows), "n_labelled": len(labelled), "n_agree": agree, "rate": rate,
            "complete": complete, "threshold": AUDIT_PASS, "passes": rate >= AUDIT_PASS if complete else None,
            "disagreements": [{"id": i, "auto": auto, "human": human} for i, auto, human in labelled
                              if auto != human]}


def audit(p1runs, sept, phase1_dir):
    f = pathlib.Path(phase1_dir) / AUDIT_FILE
    return audit_agreement(p1runs, sept, json.loads(f.read_text())) if f.exists() else None


def qwen_p3(ctx, p1runs):
    """Pin A7: per Qwen type_change pair, share of prose cells labelled V2_CORRECT minus share of JSON cells."""
    labels = defaultdict(dict)
    for r in _main_records(p1runs, QWEN):
        if r["class"] == "type_change" and r["cond"] in harness.ABLATION_CELLS:
            labels[r["task"]][r["cond"]] = drift_labels.classify(r)[0]

    def share(task, fmt, label):
        cells = [c for c in harness.ABLATION_CELLS if f":{fmt}:" in c]
        return np.mean([labels[task][c] == label for c in cells])

    d = np.array([share(t, "prose", "V2_CORRECT") - share(t, "json", "V2_CORRECT") for t in sorted(labels)])
    partial = np.array([share(t, "prose", "V2_PARTIAL") - share(t, "json", "V2_PARTIAL") for t in sorted(labels)])
    return {"n": len(d), "mean": float(d.mean()), "ci95": ctx.boot(d), "v2_partial_mean": float(partial.mean())}


def _model_calls(rec):
    calls = [t for t in rec.get("transcript") or [] if t.get("role") == "assistant_tool_call" and not t.get("synthetic")]
    return len(calls) + (rec.get("final_text") is not None)


def _instrument_label(r):
    """cond, plus @<reasoning> off the base level, plus @noise for repetitions 1-4."""
    label = r["cond"] if r.get("reasoning") == base_reasoning(r["model"]) else f"{r['cond']}@{r.get('reasoning')}"
    return label + ("@noise" if r.get("rep", 0) else "")


def instrument(p1runs):
    """check_phase1_logs.cell_report per model and cell (reasoning levels and noise reps kept apart)
    plus mean reasoning tokens over the same rows."""
    out = {}
    for m in sorted({r["model"] for r in p1runs}):
        recs = [{**r, "cond": _instrument_label(r)} for r in p1runs if r["model"] == m and not r.get("route")]
        cells = chk.cell_report(recs)
        for label, c in cells.items():
            c["reasoning_tokens_mean"] = float(np.mean([(r.get("usage") or {}).get("reasoning", 0)
                                                        for r in recs if r["cond"] == label]))
        out[m] = cells
    return out


def accounting(p1runs, phase1_dir):
    """Artifact tokens (Task 9 file, when present) and mean prompt tokens per model call per cell."""
    f = pathlib.Path(phase1_dir) / "artifact_tokens.json"
    per = defaultdict(list)
    for r in _main_records(p1runs):
        n = _model_calls(r)
        if n:
            per[(r["model"], r["cond"])].append((r.get("usage") or {}).get("in", 0) / n)
    return {"artifact_tokens": json.loads(f.read_text()) if f.exists() else None,
            "prompt_tokens_per_call": {f"{m}:{c}": {"mean": float(np.mean(v)), "n": len(v)}
                                       for (m, c), v in sorted(per.items())}}


def _ablation_blocks(ctx, out, p1runs, tabs, sept):
    for m in ABLATION_MODELS:
        if not complete(p1runs, m, "ablation"):
            out["status"][f"{m}:ablation"] = "incomplete"
            continue
        out["ablation"][m] = ablation(ctx, m, tabs[m])
        out["main_effects"][m] = main_effects(ctx, m, tabs[m])
        out["interactions"][m] = interactions(ctx, m, tabs[m])
        out["drift_over_time"][m] = drift_over_time(ctx, m, tabs[m], sept, p1runs)


def _thinking_blocks(ctx, out, p1runs, tabs, phase1_dir):
    if LUNA not in out["ablation"]:
        return
    has_thinking = any(r["model"] == LUNA and r.get("reasoning") == "high" for r in p1runs)
    sel = check_selection(tabs[LUNA], phase1_dir, has_thinking)
    out["thinking_selection"] = sel
    cells = [st.REPLICATE_C, sel["selected"]]
    if complete(p1runs, LUNA, "thinking", cells, "high"):
        out["thinking"] = thinking(ctx, tabs[LUNA], sel["selected"])
    else:
        out["status"][f"{LUNA}:thinking"] = "incomplete"


def analyze(runs, p1runs, ctx, sept_noise, phase1_dir):
    """All Phase-1 blocks; arms with missing jobs are reported as incomplete and add no tests."""
    if not p1runs:
        return None
    sept = sept_index(runs)
    tabs = {m: build_tab(sept, p1runs, m) for m in st.FAMILIES}
    out = {"status": {}, "ablation": {}, "main_effects": {}, "interactions": {}, "drift_over_time": {},
           "infoform": {}}
    _ablation_blocks(ctx, out, p1runs, tabs, sept)
    for m in st.FAMILIES:
        if complete(p1runs, m, "infoform"):
            out["infoform"][m] = infoform(ctx, m, tabs[m])
        else:
            out["status"][f"{m}:infoform"] = "incomplete"
    if not complete(p1runs, LUNA, "noise"):
        out["status"][f"{LUNA}:noise"] = "incomplete"
    out["noise_floor"] = noise_floors(p1runs, sept_noise)
    _thinking_blocks(ctx, out, p1runs, tabs, phase1_dir)
    if QWEN in out["ablation"]:
        out["qwen_p3"] = qwen_p3(ctx, p1runs)
    out["mechanism"] = {**mechanism(p1runs, sept), "audit_agreement": audit(p1runs, sept, phase1_dir)}
    out["instrument"] = instrument(p1runs)
    out["accounting"] = accounting(p1runs, phase1_dir)
    return out


def _luna_stats(block, survivors):
    floor = block["noise_floor"][LUNA]
    cells = {c: {"recovery": b["recovery"]["point"], "ci_low": b["vs_B"]["ci95"][0],
                 "bh": f"p1:{LUNA}:{c}-B_strict" in survivors, "mean": b["vs_B"]["mean"]}
             for c, b in block["ablation"][LUNA]["cells"].items()}
    th = block.get("thinking")
    return {"cells": cells, "floor": floor,
            "main": {k: v["mean"] for k, v in block["main_effects"][LUNA].items()},
            "thinking": {c: {"recovery": v["recovery_high"]["point"]} for c, v in th.items()} if th else None}


def predictions(block, survivors):
    """P1-P9 verdicts after BH; pending until luna's ablation and noise arms are complete."""
    if LUNA not in block["ablation"] or block["noise_floor"][LUNA] is None or f"{LUNA}:noise" in block["status"]:
        return {"pending": "luna ablation and noise arms must be complete"}
    keys = ("Dprime-D_required", "Dprime-C", "CD-C", "CD-D")
    stats = {"luna": _luna_stats(block, survivors),
             "qwen": {"p3": block["qwen_p3"]} if "qwen_p3" in block else None,
             "families": {m: {k: v[k] for k in keys} for m, v in block["infoform"].items()},
             "route": None}  # amendment 1: route arm not run
    return st.verdicts(stats)
