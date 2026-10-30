#!/usr/bin/env python3
"""Tests for the Phase-3 catalog analysis and P21.

Run: python3 -m pytest test_analyze_phase3_catalog.py -q
"""

import pathlib
import sys
import types

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze_phase3_catalog as ap3c  # noqa: E402
import phase3_grid as p3  # noqa: E402

FLASH, HAIKU = ap3c.FAMILIES


def rec(task, cond, cls, catalog, success, model=FLASH, executed=None):
    return {"model": model, "task": task, "cond": cond, "class": cls, "catalog": catalog,
            "success": success, "n_declarations": 30 if catalog == "full" else 1,
            "executed": executed if executed is not None else [{"tool": "save_bookmark"}],
            "reasoning": ap3c.REASONING[model], "arm": "catalog", "phase": "phase3"}


def full_run(model, success_full=1, success_small=1):
    out = []
    for task, cls in p3.PAIRS:
        for cond in p3.CONDS:
            out.append(rec(task["id"], cond, cls, "small", success_small, model))
            out.append(rec(task["id"], cond, cls, "full", success_full, model))
    return out


def ctx(labels=None):
    labels = labels if labels is not None else []
    return types.SimpleNamespace(
        rng=np.random.default_rng(1),
        paired=lambda d, label: labels.append(label) or {
            "n": len(d), "mean": float(np.mean(d)), "ci95": [float(np.mean(d)), float(np.mean(d))],
            "p_signflip": 0.5})


def test_each_family_registers_three_tests():
    labels = []
    block = ap3c.analyze(full_run(FLASH) + full_run(HAIKU), ctx(labels), {})
    assert len(labels) == 6 and len(set(labels)) == 6
    assert all(x.startswith("p3:") and ":catalog:" in x for x in labels)
    assert block["n_tests"] == 6
    assert ap3c.EXPECTED_TESTS == 307


def test_an_incomplete_family_adds_no_test():
    labels = []
    runs = full_run(FLASH)[:-2] + full_run(HAIKU)
    block = ap3c.analyze(runs, ctx(labels), {})
    assert block["status"] == {FLASH: "incomplete"}
    assert set(block["families"]) == {HAIKU} and len(labels) == 3


def test_success_and_declaration_counts_are_reported_per_catalog():
    block = ap3c.analyze(full_run(FLASH, success_full=0, success_small=1), ctx(), {})
    fam = block["families"][FLASH]
    assert fam["n_pairs"] == 40
    assert fam["success"]["small"]["C"] == 1.0 and fam["success"]["full"]["C"] == 0.0
    assert fam["declarations"] == {"small": 1.0, "full": 30.0}


def test_p21_holds_when_every_family_is_inside_the_band():
    block = ap3c.analyze(full_run(FLASH) + full_run(HAIKU), ctx(), {})
    assert ap3c.p21(block, survivors=set())["holds"] is True


def test_p21_fails_when_a_family_leaves_the_band():
    runs = full_run(FLASH, success_full=0, success_small=1) + full_run(HAIKU)
    out = ap3c.p21(ap3c.analyze(runs, ctx(), {}), survivors=set())
    assert out["holds"] is False and "-1.000" in out["basis"]


def test_p21_is_pending_while_only_one_family_has_run():
    block = ap3c.analyze(full_run(FLASH), ctx(), {})
    assert ap3c.p21(block, survivors=set())["holds"] is None
    assert ap3c.p21(None, survivors=set())["holds"] is None


def test_wrong_tool_is_zero_in_the_small_catalog_by_construction():
    task_tools = {t["id"]: {"save_bookmark"} for t, _ in p3.PAIRS}
    records = full_run(FLASH)
    out = ap3c.wrong_tool(records, task_tools)
    assert out["small"]["wrong_tool_rate"] == 0.0 and out["full"]["wrong_tool_rate"] == 0.0
    off = [{**r, "executed": [{"tool": "web_search"}]} for r in records if r["catalog"] == "full"]
    out2 = ap3c.wrong_tool(off + [r for r in records if r["catalog"] == "small"], task_tools)
    assert out2["full"]["wrong_tool_rate"] == 1.0 and out2["small"]["wrong_tool_rate"] == 0.0


def test_no_call_is_counted_separately():
    task_tools = {t["id"]: {"save_bookmark"} for t, _ in p3.PAIRS}
    records = [{**r, "executed": []} for r in full_run(FLASH)]
    out = ap3c.wrong_tool(records, task_tools)
    assert out["full"]["no_call_rate"] == 1.0 and out["full"]["wrong_tool_rate"] == 0.0
