#!/usr/bin/env python3
"""Drift-call labeler: what a model did at the drifted step of one episode.

Moved verbatim from phase1/step1_diag_diff_following.py (where the labels are
documented) so the step-1 report, the explorer (viz/) and the Phase-1 analysis
share one implementation. Works on September and Phase-1 records alike.
"""

import json
import re

from harness import frozen, semantically_equal

FROZEN = frozen()
LABELS = ["V2_CORRECT", "V2_PARTIAL", "V1_FORM", "V1_SAFE", "OTHER_ERROR", "OTHER_WRONG",
          "NO_DRIFT_CALL"]
TASKS = {t["id"]: t for t in FROZEN["tasks"]}

ERR_PARAM = re.compile(r"'([^']+)'")


def drift_change(task, cls):
    return FROZEN["diffs"][f"{task['drift_tool']}::{cls}"]["changes"][0]


def drift_call_args(rec, task):
    """Args of the accepted drift-step call, if it was accepted."""
    calls = [e for e in rec["executed"] if e["tool"] == task["drift_tool"]]
    if not calls:
        return None
    # two-step tasks: the drift step is the call to drift_tool; it appears once
    return calls[0]["args"]


def error_param(err):
    """Parameter named in an executor error string."""
    if err.startswith("Invalid value"):
        m = re.search(r"for parameter '([^']+)'", err)
        return m.group(1) if m else None
    m = ERR_PARAM.search(err)
    return m.group(1) if m else None


def classify(rec, b_rec=None):
    task = TASKS[rec["task"]]
    cls = rec["class"]
    ch = drift_change(task, cls)
    p_old = ch["param"]
    p_new = ch["new"] if cls == "rename" else p_old
    out = rec["drift_outcome"]

    if out is None:
        return "NO_DRIFT_CALL", None

    if out == "ERROR_SURFACED":
        err = rec["error_seen"] or ""
        ep = error_param(err)
        if cls == "rename" and err.startswith("Received unknown parameter") and ep == p_old:
            return "V1_FORM", err
        if cls == "required" and err.startswith("Missing required") and ep == p_old:
            return "V1_FORM", err
        if cls == "type_change" and err.startswith("Invalid type") and ep == p_old:
            return "V1_FORM", err
        if cls == "enum_tighten" and err.startswith("Invalid value") and ep == p_old:
            bad = re.match(r"Invalid value '([^']*)'", err).group(1)
            return ("V1_FORM" if bad == ch["old"] else "V2_PARTIAL"), err
        if ep in (p_old, p_new):
            return "V2_PARTIAL", err
        return "OTHER_ERROR", err

    # accepted (works for both executor profiles; the logged args are the args
    # the model SENT, before lenient dropping/coercion)
    args = drift_call_args(rec, task) or {}
    if out == "ACCEPTED_CORRECT":
        if cls in ("required", "default_change"):
            # correct because the param was filled explicitly. Was the value the
            # one the diff implies, or the one the v1 schema documents?
            safe = b_rec is not None and b_rec["success"]
            return ("V1_SAFE" if safe else "V2_CORRECT"), args.get(p_old)
        return "V2_CORRECT", args.get(p_new)

    # ACCEPTED_WRONG
    if cls == "rename" and p_old in args:
        return "V1_FORM", {p_old: args[p_old]}  # lenient: old name silently dropped
    if cls == "rename" and p_new not in args:
        return "OTHER_WRONG", "drifted parameter left out under both names"
    gt = task["gt_v2"][cls][task["drift_step_index"]]
    if p_new in args and p_new in gt and _same(args[p_new], gt[p_new]):
        return "OTHER_WRONG", {p_new: args[p_new]}
    if cls == "default_change":
        return ("V1_FORM" if p_old not in args else "V2_PARTIAL"), args.get(p_old)
    if cls == "type_change":
        v = args.get(p_old)
        return ("V2_PARTIAL" if isinstance(v, str) else "V1_FORM"), v
    return "V2_PARTIAL", args.get(p_new)


def _same(a, b):
    return semantically_equal(a, b)


def signature(rec):
    """Comparable fingerprint of what the model did at the drift step."""
    task = TASKS[rec["task"]]
    return json.dumps({"o": rec["drift_outcome"], "e": rec["error_seen"],
                       "a": drift_call_args(rec, task)}, sort_keys=True)
