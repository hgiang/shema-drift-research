#!/usr/bin/env python3
"""Replay logged accepted calls through the frozen executor and compare their
effective semantics with ground truth, field by field.

Read-only: uses experiments/executor.py and experiments/harness.py exactly as
the runners did, so the recomputed outcome must equal the logged one (the test
suite checks this for every episode). Rejected calls are not in the logs, so
only accepted calls can be compared.

Field status vocabulary:
  ok       effective value matches ground truth
  wrong    effective value differs from ground truth
  missing  ground truth expects the field, the effective call lacks it
  extra    effective call has a field ground truth does not
  dropped  sent by the model, unknown to the schema, silently discarded
"""

import pathlib
import sys

EXPERIMENTS = pathlib.Path(__file__).resolve().parent.parent / "experiments"
sys.path.insert(0, str(EXPERIMENTS))
import executor as ex  # noqa: E402
import harness  # noqa: E402

REF_PREFIX = "$1."  # ground-truth reference to a step-1 result value


def result_payload(tool_v1, task_id):
    """The mock result the executor returned for an accepted call."""
    return {k: v.replace("{tid}", task_id) if isinstance(v, str) else v
            for k, v in tool_v1["result"].items()}


def resolve_refs(gt_args, first_result):
    """Substitute $1.<key> references with the actual step-1 result values."""
    if first_result is None:
        return dict(gt_args)
    return {k: first_result.get(v[len(REF_PREFIX):], v)
            if isinstance(v, str) and v.startswith(REF_PREFIX) else v
            for k, v in gt_args.items()}


def _field(param, effective, expected):
    row = {"param": param}  # the sent value stays in the step's own `args`
    if param in effective:
        row["effective"] = effective[param]
    if param in expected:
        row["expected"] = expected[param]

    if param in effective and param in expected:
        ok = harness.semantically_equal(effective[param], expected[param])
        row["status"] = "ok" if ok else "wrong"
    elif param in expected:
        row["status"] = "missing"
    elif param in effective:
        row["status"] = "extra"
    else:
        row["status"] = "dropped"
    return row


def compare_call(sent_args, gt_args, active_params, profile):
    """Field-level comparison of one accepted call against ground truth."""
    status, payload = ex.execute(active_params, sent_args, profile, {})
    if status != "accepted":
        return {"outcome": "REPLAY_REJECTED", "error": payload, "fields": []}
    effective = payload["effective_args"]
    expected = harness.effective_gt(gt_args, active_params)
    params = sorted(set(sent_args) | set(effective) | set(expected))
    fields = [_field(p, effective, expected) for p in params]
    correct = all(f["status"] in ("ok", "dropped") for f in fields)
    return {"outcome": "ACCEPTED_CORRECT" if correct else "ACCEPTED_WRONG",
            "fields": fields}


def annotate_executed(record, task, setup, tools_v1):
    """Return the record's executed steps, each with a `check` comparison.

    Mirrors harness.run_episode: the i-th accepted call is matched to the i-th
    ground-truth step, and only scored when it called the expected tool.
    """
    gt_steps = task["gt_v1"] if record["cond"] == "A" else task["gt_v2"][record["class"]]
    executed = record["executed"]
    first_result = (result_payload(tools_v1[executed[0]["tool"]], task["id"])
                    if executed else None)
    out = []
    for i, step in enumerate(executed):
        check = None
        expected_tool = task["steps"][i]["tool"] if i < len(task["steps"]) else None
        if step["outcome"] is not None and step["tool"] == expected_tool and i < len(gt_steps):
            gt = resolve_refs(gt_steps[i], first_result if i > 0 else None)
            check = compare_call(step["args"], gt, setup["active"][step["tool"]],
                                 setup["profile"])
        out.append({**step, "check": check})
    return out
