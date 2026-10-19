#!/usr/bin/env python3
"""Tests for the shared drift-call labeler. No API calls.

Run: python3 -m pytest test_drift_labels.py -q
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import drift_labels as dl  # noqa: E402
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402
from test_phase1 import oracle  # noqa: E402

TASKS = {t["id"]: t for t in harness.frozen()["tasks"]}


def accepted(task_id, cls, outcome, args):
    t = TASKS[task_id]
    return {"task": task_id, "class": cls, "drift_outcome": outcome, "error_seen": None,
            "success": outcome == "ACCEPTED_CORRECT",
            "executed": [{"tool": t["drift_tool"], "args": args, "outcome": "ok"}]}


def test_rename_error_is_v1_form():
    t, cls = next((t, c) for t, c in p1.primary_pairs() if c == "rename")
    rec = harness.run_episode(t, p1.REPLICATE_C, cls, oracle("v1")(t, cls))
    assert rec["drift_outcome"] == "ERROR_SURFACED"
    label, detail = dl.classify(rec)
    assert label == "V1_FORM" and detail.startswith("Received unknown parameter")


def test_type_string_with_wrong_value_is_v2_partial():
    gt = TASKS["bmk03"]["gt_v2"]["type_change"][TASKS["bmk03"]["drift_step_index"]]
    wrong = {**gt, "rating": "three stars"}
    assert dl.classify(accepted("bmk03", "type_change", "ACCEPTED_WRONG", wrong))[0] == "V2_PARTIAL"
    as_int = {**gt, "rating": 4}
    assert dl.classify(accepted("bmk03", "type_change", "ACCEPTED_WRONG", as_int))[0] == "V1_FORM"


def test_required_filled_is_v1_safe_when_b_succeeded():
    t = TASKS["cal02"]
    args = t["gt_v2"]["required"][t["drift_step_index"]]
    rec = accepted("cal02", "required", "ACCEPTED_CORRECT", args)
    assert dl.classify(rec, b_rec={"success": True})[0] == "V1_SAFE"
    assert dl.classify(rec, b_rec={"success": False})[0] == "V2_CORRECT"
    assert dl.classify(rec)[0] == "V2_CORRECT"


def test_classify_accepts_phase1_records():
    t, cls = next((t, c) for t, c in p1.primary_pairs() if c == "enum_tighten")
    rec = p1.run_episode((t, "C:user:prose:none", cls, 0, 0), oracle("v2")(t, cls), "m/x", "ablation",
                         "default", 700)
    assert rec["drift_outcome"] == "ACCEPTED_CORRECT"
    assert dl.classify(rec)[0] == "V2_CORRECT"
    assert dl.signature(rec) == dl.signature(dict(rec))
    assert set(dl.LABELS) >= {"V2_CORRECT", "V1_FORM", "NO_DRIFT_CALL"}


def test_no_drift_call_and_error_param():
    rec = {**accepted("bmk03", "type_change", None, {}), "drift_outcome": None}
    assert dl.classify(rec) == ("NO_DRIFT_CALL", None)
    assert dl.error_param("Invalid value 'x' for parameter 'mode'") == "mode"
    assert dl.error_param("Missing required parameter 'when'") == "when"
