#!/usr/bin/env python3
"""Phase-3 catalog arm: the block, its six BH tests and P21.

Paired within one run: for each of the 40 pairs and each condition, the same episode at the
large catalog minus the same episode at the small one. P21 is an equivalence claim, so it is
judged on the CI lying inside the band, never on a p-value (MILESTONES.md "Phase 3
pre-registration", amendment 4).

`ctx` supplies the statistics bound to RNG_P3 and the one BH family:
  ctx.paired(diffs, label), ctx.rng   (as in Phases 1 and 2)
"""

import collections
import json
import pathlib

import numpy as np

import check_phase1_logs as chk
import phase3_grid as p3

CONDS = p3.CONDS
BAND = 0.10          # P21: C(full) - C(small) must sit inside [-BAND, +BAND]
FAMILIES = ("gemini-3.6-flash", "anthropic/claude-haiku-5.5")
REASONING = {"gemini-3.6-flash": "MINIMAL", "anthropic/claude-haiku-5.5": "default"}
EXPECTED_TESTS = 301 + len(CONDS) * 2  # 307: three paired tests in each of two families


def load_catalog_runs(path):
    """runs_*.jsonl minus pilots; dedupe on the catalog-aware key, last wins."""
    runs = {}
    for f in sorted(pathlib.Path(path).glob("runs_*.jsonl")):
        if f.name.endswith(".pilot.jsonl"):
            continue
        records, bad = chk.read_records(f)
        if bad:
            raise SystemExit(f"{f.name}: unparsable lines {bad[:5]}; repair before analysing")
        for r in records:
            runs[(r["model"], *p3.rec_key(r))] = r
    return list(runs.values())


def complete(runs, model):
    records = [r for r in runs if r["model"] == model]
    return not chk.coverage(records, "catalog", REASONING.get(model, "default"), phase=3)["missing"]


def _table(records, catalog):
    """(task, class) -> 0|1 for one catalog size and condition."""
    return {(r["task"], r["class"]): int(r["success"]) for r in records if r["catalog"] == catalog}


def _vector(records, cond, catalog, pairs):
    table = _table([r for r in records if r["cond"] == cond], catalog)
    return np.array([table[p] for p in pairs], dtype=float)


def pair_keys():
    return [(t["id"], cls) for t, cls in p3.PAIRS]


def family_block(ctx, model, records):
    """Three paired tests (full - small) at A, B_strict and C, plus the success rates."""
    pairs = pair_keys()
    out = {"n_pairs": len(pairs), "success": {}, "tests": {}, "declarations": {}}
    for catalog in p3.CATALOGS:
        out["success"][catalog] = {c: float(_vector(records, c, catalog, pairs).mean()) for c in CONDS}
        counts = [r["n_declarations"] for r in records if r["catalog"] == catalog]
        out["declarations"][catalog] = float(np.mean(counts)) if counts else None
    for cond in CONDS:
        diffs = _vector(records, cond, "full", pairs) - _vector(records, cond, "small", pairs)
        out["tests"][cond] = ctx.paired(diffs, f"p3:{model}:catalog:{cond}:full-small")
    out["wrong_tool"] = wrong_tool(records)
    return out


def _task_tools():
    """task id -> the tools its own steps use, which are the only right ones to call."""
    import harness
    return {t["id"]: {s["tool"] for s in t["steps"]} for t in harness.frozen()["tasks"]}


def wrong_tool(records, task_tools=None):
    """A 30-tool catalog can fail in a way a 1-tool one cannot: calling a tool off the task.

    In the small catalog this rate is 0 by construction — no other tool is declared — so the
    pair of rates is what says whether a large catalog introduces a new failure mode.
    """
    task_tools = task_tools if task_tools is not None else _task_tools()
    out = {}
    for catalog in p3.CATALOGS:
        rows = [r for r in records if r["catalog"] == catalog]
        if not rows:
            continue
        wrong = sum(any(ex["tool"] not in task_tools.get(r["task"], set()) for ex in r["executed"])
                    for r in rows)
        no_call = sum(not r["executed"] for r in rows)
        out[catalog] = {"n": len(rows), "no_call_rate": no_call / len(rows),
                        "wrong_tool_rate": wrong / len(rows)}
    return out


def analyze(runs, ctx, noise_floors):
    """The catalog block; a family with missing jobs is reported incomplete and adds no test."""
    if not runs:
        return None
    out = {"status": {}, "families": {}, "noise_floor": {}}
    for model in sorted({r["model"] for r in runs}):
        if not complete(runs, model):
            out["status"][model] = "incomplete"
            continue
        out["families"][model] = family_block(ctx, model, [r for r in runs if r["model"] == model])
        out["noise_floor"][model] = noise_floors.get(model)
    out["n_tests"] = len(CONDS) * len(out["families"])
    return out


def p21(block, survivors, band=BAND):
    """C(full) - C(small) equivalent within the band, in every family that ran."""
    if not block or not block["families"]:
        return {"holds": None, "basis": "catalog arm incomplete"}
    verdicts, basis = {}, {}
    for model, fam in block["families"].items():
        low, high = fam["tests"]["C"]["ci95"]
        verdicts[model] = -band <= low and high <= band
        basis[model] = (f"{fam['tests']['C']['mean']:+.3f} CI [{low:.3f}, {high:.3f}], "
                        f"BH {f'p3:{model}:catalog:C:full-small' in survivors}")
    holds = all(verdicts.values()) if len(verdicts) == len(FAMILIES) else None
    if False in verdicts.values():
        holds = False
    return {"holds": holds,
            "basis": f"C(full) - C(small) inside [-{band}, {band}] in every family: {basis}"}


def predictions(block, survivors):
    return {"P21": p21(block, survivors)}
