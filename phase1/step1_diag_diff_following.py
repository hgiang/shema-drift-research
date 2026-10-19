#!/usr/bin/env python3
"""Phase 1, step 1: free diagnostic on the EXISTING logs (no API calls).

Question: under condition C (v1 schema + JSON diff in the system prompt), do the
models that "ignore the diff" (GPT-5.6-luna, Qwen2.5-7B) still emit v1-form calls
on the drifted parameter, or do they try v2 and get it wrong?

For every C episode we classify the drift-step call:
  V2_CORRECT     accepted, correct semantics (the diff was applied)
  V2_PARTIAL     model moved off the v1 form but got it wrong
                 (e.g. type_change: sent a string but kept the old unit)
  V1_FORM        the call used the v1 contract on the drifted param
                 (old name / old enum value / int instead of string /
                 omitted the newly-required or default-changed param)
  V1_SAFE        correct, but the same pair also succeeded in B_strict (no diff):
                 the model fills optional params explicitly anyway, so the
                 success says nothing about reading the diff (required/default)
  OTHER_ERROR    executor error on a parameter that is NOT the drifted one
  OTHER_WRONG    accepted and wrong, but not because of the drifted param's form:
                 another argument is wrong, or a renamed param was left out
                 under both names
  NO_DRIFT_CALL  the drifted step was never reached / no tool call

Second check: pairwise identity of the drift-step call between C and B_strict on
the same (task, class) pair. If the diff is ignored, the C call should be the same
call the model made with no diff at all.

Limits: the logs keep accepted calls' args but only the error STRING for rejected
calls, so rejected calls are classified from the error text.

The explorer (viz/build_explorer_data.py) imports classify() and signature()
from here, so the explorer's "diff following" field and this report agree.

Usage:  python3 phase1/step1_diag_diff_following.py
Writes: phase1/step1_diag_diff_following.json
"""

import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "experiments"))
from harness import semantically_equal  # noqa: E402
import analyze  # noqa: E402  (load_runs: the exact dedupe analysis.json uses)
OUT = ROOT / "phase1" / "step1_diag_diff_following.json"
FROZEN = json.loads((ROOT / "experiments" / "testbed_frozen.json").read_text())

MODELS = ["openai/gpt-5.6-luna", "modal-qwen2.5-7b", "gemini-3.6-flash",
          "gemini-3.1-pro-preview"]
CLASSES = ["rename", "enum_tighten", "required", "type_change", "default_change"]
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


def main():
    report = {}
    ALL_RUNS = analyze.load_runs()
    for model in MODELS:
        # same deduplicated records as analysis.json (last write wins across
        # runs_*.jsonl, so a noise-battery rep 0 replaces the core record)
        recs = [r for r in ALL_RUNS if r["model"] == model
                and r.get("rep", 0) == 0 and r["phrasing"] == 0]
        by = {(r["cond"], r["task"], r["class"]): r for r in recs}
        cs = [r for r in recs if r["cond"] == "C"]

        tab = defaultdict(Counter)
        examples = defaultdict(list)
        for r in cs:
            lab, detail = classify(r, by.get(("B_strict", r["task"], r["class"])))
            tab[r["class"]][lab] += 1
            if len(examples[(r["class"], lab)]) < 2:
                examples[(r["class"], lab)].append({"task": r["task"], "detail": detail})

        ident = {}
        for cond in ("B_strict", "D"):
            per_cls = {}
            for cls in CLASSES:
                same = n = 0
                for r in cs:
                    if r["class"] != cls:
                        continue
                    o = by.get((cond, r["task"], cls))
                    if o is None:
                        continue
                    n += 1
                    same += signature(r) == signature(o)
                per_cls[cls] = {"identical": same, "n": n}
            ident[f"C_vs_{cond}"] = per_cls

        succ = {}
        for cond in ("B_strict", "C", "D"):
            succ[cond] = {}
            for cls in CLASSES:
                v = [r["success"] for r in recs if r["cond"] == cond and r["class"] == cls]
                succ[cond][cls] = round(sum(v) / len(v), 3) if v else None

        report[model] = {
            "n_C": len(cs),
            "C_drift_call_labels": {c: dict(tab[c]) for c in CLASSES},
            "identity": ident,
            "success_by_class": succ,
            "examples": {f"{c}|{l}": v for (c, l), v in examples.items()},
        }

    OUT.write_text(json.dumps(report, indent=1, ensure_ascii=False))

    # ---- console summary ----
    for model, rep in report.items():
        print(f"\n=== {model}  (C episodes: {rep['n_C']})")
        print(f"{'class':15s}" + "".join(f"{l:>14s}" for l in LABELS)
              + f"{'=B_strict':>11s}{'succ B/C/D':>18s}")
        for c in CLASSES:
            row = rep["C_drift_call_labels"][c]
            idt = rep["identity"]["C_vs_B_strict"][c]
            s = rep["success_by_class"]
            print(f"{c:15s}" + "".join(f"{row.get(l, 0):>14d}" for l in LABELS)
                  + f"{idt['identical']:>5d}/{idt['n']:<5d}"
                  + f"   {s['B_strict'][c]:.2f}/{s['C'][c]:.2f}/{s['D'][c]:.2f}")
    print(f"\nwrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
