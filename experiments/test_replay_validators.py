#!/usr/bin/env python3
"""Tests for the real-validator replay (phase2/PLAN.md Task 4). In-process only, no network.

Run: ../.venv/bin/python -m pytest test_replay_validators.py -q
"""

import copy
import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import executor as ex  # noqa: E402
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402
import replay_validators as rv  # noqa: E402
from test_phase1 import oracle  # noqa: E402

PARAMS = {
    "room": {"type": "string", "required": True, "desc": "Room"},
    "seats": {"type": "integer", "default": 4, "desc": "Seats"},
    "layout": {"type": "string", "enum": ["conference", "theater"], "default": "conference", "desc": "Layout"},
    "catering": {"type": "boolean", "default": False, "desc": "Catering"},
}
NAMES = ("pydantic_default", "pydantic_strict", "fastapi_default", "jsonschema_closed")


@pytest.fixture(scope="module")
def vals():
    return rv.validators()


def outcomes(vals, params, args):
    return {name: vals[name](params, args) for name in NAMES}


# ---------------- one test per executor rule, against what each validator documents ----------------

def test_validator_names(vals):
    assert set(vals) == set(NAMES)


def test_valid_call_accepted_by_all(vals):
    args = {"room": "Cascade", "seats": 6, "layout": "theater", "catering": True}
    assert ex.execute(PARAMS, args, "strict", {})[0] == "accepted"
    assert all(o == (True, None) for o in outcomes(vals, PARAMS, args).values())


def test_unknown_parameter(vals):
    args = {"room": "Cascade", "colour": "red"}
    assert ex.execute(PARAMS, args, "strict", {})[0] == "error"
    assert ex.execute(PARAMS, args, "lenient", {})[0] == "accepted"
    got = outcomes(vals, PARAMS, args)
    assert got["pydantic_default"] == (True, None)      # extra="ignore" drops it
    assert got["fastapi_default"] == (True, None)
    assert got["pydantic_strict"] == (False, "unknown")  # extra="forbid"
    assert got["jsonschema_closed"] == (False, "unknown")  # additionalProperties: false


def test_missing_required(vals):
    args = {"seats": 3}
    assert all(o == (False, "missing") for o in outcomes(vals, PARAMS, args).values())


def test_string_digits_for_integer(vals):
    args = {"room": "Cascade", "seats": "3"}
    assert ex.execute(PARAMS, args, "lenient", {})[0] == "accepted"
    got = outcomes(vals, PARAMS, args)
    assert got["pydantic_default"] == (True, None)      # lax mode parses "3"
    assert got["fastapi_default"] == (True, None)
    assert got["pydantic_strict"] == (False, "type")
    assert got["jsonschema_closed"] == (False, "type")


def test_integer_for_string(vals):
    """The mock's lenient profile turns 500 into "500"; pydantic v2 lax mode does not
    (numbers reach a str field only with coerce_numbers_to_str)."""
    params = {**PARAMS, "room": {"type": "string", "required": True, "desc": "Room"}}
    args = {"room": 500}
    assert ex.execute(params, args, "lenient", {})[0] == "accepted"
    assert all(o == (False, "type") for o in outcomes(vals, params, args).values())


def test_enum_violation(vals):
    args = {"room": "Cascade", "layout": "boardroom"}
    assert all(o == (False, "enum") for o in outcomes(vals, PARAMS, args).values())


def test_error_priority_follows_executor(vals):
    """Several violations: the reported type is the executor's first (unknown > missing > type > enum)."""
    args = {"seats": "x", "layout": "boardroom", "colour": "red"}
    got = outcomes(vals, PARAMS, args)
    assert got["pydantic_strict"] == (False, "unknown")
    assert got["jsonschema_closed"] == (False, "unknown")
    assert got["pydantic_default"] == (False, "missing")


def test_names_that_shadow_basemodel(vals):
    params = {"schema": {"type": "string", "required": True, "desc": "s"},
              "copy": {"type": "integer", "default": 0, "desc": "c"}}
    assert all(o == (True, None) for o in outcomes(vals, params, {"schema": "x"}).values())
    assert all(o[0] is False for o in outcomes(vals, params, {"schema": "x", "copy": "a"}).values())


def test_inputs_not_mutated(vals):
    params, args = copy.deepcopy(PARAMS), {"room": "Cascade", "seats": "3", "extra": 1}
    before = (copy.deepcopy(params), copy.deepcopy(args))
    outcomes(vals, params, args)
    assert (params, args) == before


# ---------------- drift_calls ----------------

def _task_and_class(cls="rename"):
    return next((t, c) for t, c in p1.primary_pairs() if c == cls)


def _record(cond, gt_key, cls="rename"):
    task, c = _task_and_class(cls)
    return harness.run_episode(task, cond, c, oracle(gt_key)(task, c)), task


def test_drift_call_from_transcript_includes_rejected():
    rec, task = _record("B_strict", "v1")  # v1 args after a rename: the strict executor rejects
    assert rec["drift_outcome"] == "ERROR_SURFACED"
    [row] = rv.drift_calls([{**rec, "model": "m"}], source="phase1")
    gt = task["gt_v1"][task["drift_step_index"]]
    assert row["args"] == gt and row["tool"] == task["drift_tool"]
    assert row["mock_strict"] == {"accepted": False, "error_type": "unknown"}
    assert row["mock_lenient"]["accepted"] is True
    assert (row["source"], row["model"], row["cond"], row["class"], row["task"]) == \
        ("phase1", "m", "B_strict", "rename", task["id"])
    assert row["params"] == harness.frozen()["v2_schemas"][f"{task['drift_tool']}::rename"]


def test_drift_call_from_executed_when_no_transcript():
    rec, task = _record("B_strict", "v2")
    sept = {k: v for k, v in rec.items() if k != "transcript"}
    [row] = rv.drift_calls([{**sept, "model": "m"}], source="september")
    assert row["args"] == task["gt_v2"]["rename"][task["drift_step_index"]]
    assert row["mock_strict"] == {"accepted": True, "error_type": None}


def test_rejected_call_without_transcript_is_skipped():
    rec, _ = _record("B_strict", "v1")
    sept = {k: v for k, v in rec.items() if k != "transcript"}
    assert rv.drift_calls([{**sept, "model": "m"}], source="september") == []


def test_no_drift_condition_is_skipped():
    rec, _ = _record("A", "v1")
    assert rv.drift_calls([{**rec, "model": "m"}], source="phase1") == []


def test_changelog_preamble_is_not_the_drift_call():
    rec, task = _record("C:tool:prose:apply", "v2")
    assert rec["transcript"][0].get("synthetic")
    [row] = rv.drift_calls([{**rec, "model": "m"}], source="phase1")
    assert row["tool"] == task["drift_tool"]
    assert row["mock_strict"]["accepted"] is True


def test_logged_outcome_must_match_replayed_mock():
    rec, _ = _record("B_strict", "v1")
    with pytest.raises(SystemExit, match="mock replay"):
        rv.drift_calls([{**rec, "model": "m", "drift_outcome": "ACCEPTED_CORRECT"}], source="phase1")


# ---------------- agreement ----------------

def _row(strict, lenient, val, etype=None):
    return {"mock_strict": {"accepted": strict, "error_type": etype},
            "mock_lenient": {"accepted": lenient, "error_type": None if lenient else etype},
            "validators": {"v": {"accepted": val, "error_type": None if val else "x"}}}


def test_agreement_counts():
    rows = [_row(True, True, True), _row(False, True, True, "unknown"),
            _row(False, True, False, "unknown"), _row(False, False, False, "enum")]
    got = rv.agreement(rows)["v"]
    assert got["vs_strict"] == {"n": 4, "agree": 3, "rate": 0.75}
    assert got["vs_lenient"] == {"n": 4, "agree": 3, "rate": 0.75}
    assert got["by_error_type"] == {
        "none": {"n": 1, "agree_strict": 1, "agree_lenient": 1},
        "unknown": {"n": 2, "agree_strict": 1, "agree_lenient": 1},
        "enum": {"n": 1, "agree_strict": 1, "agree_lenient": 1},
    }


def test_agreement_empty():
    assert rv.agreement([]) == {}


def test_replay_summary_and_disagreements():
    rejected, _ = _record("B_strict", "v1")
    accepted, _ = _record("B_strict", "v2")
    rows = rv.replay(rv.drift_calls([{**rejected, "model": "m"}, {**accepted, "model": "m"}], source="phase1"))
    out = rv.summary(rows)
    assert out["n_calls"] == 2 and out["n_by_source"] == {"phase1": 2}
    assert out["n_by_strict_error_type"] == {"unknown": 1, "none": 1}
    assert set(out["agreement_by_source"]["phase1"]) == set(NAMES)
    # the v1 call after a rename: pydantic/FastAPI drop the old name like the lenient profile
    flagged = {(d["validator"], d["task"]) for d in out["disagreements"]}
    assert all(name in ("pydantic_default", "fastapi_default") for name, _ in flagged)
    assert "params" not in (out["disagreements"] or [{}])[0]
