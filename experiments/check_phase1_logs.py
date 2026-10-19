#!/usr/bin/env python3
"""Phase-1 log checker: the gate every pilot and full run must pass before it counts.

Fails on unparsable lines, incomplete records, duplicate keys, more than one serving
provider in a cell, a cell with > 5% truncated outputs, more than one model version in
the file, and (full runs) any missing job. Coverage is matched by key, not by the record's
`arm` field: a noise rep-0 job is the same request as the ablation C:sys:json:none record.

Usage:
  python3 check_phase1_logs.py ../results/phase1/runs_openai_gpt-5.6-luna.pilot.jsonl --arm ablation --pilot
  python3 check_phase1_logs.py ../results/phase1/runs_gemini-3.6-flash.jsonl --arm infoform --reasoning MINIMAL
"""

import argparse
import json
import pathlib
import sys
from collections import Counter
from datetime import datetime

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402
from cost_tracker import COST_LOG  # noqa: E402

REQUIRED = ("transcript", "usage", "meta", "reasoning", "arm", "phase")
TRUNCATED = {"length", "MAX_TOKENS"}  # OpenRouter/vLLM, Gemini
MAX_LENGTH_RATE = 0.05
NONE = "(none)"


def read_records(path):
    """(records, 1-based numbers of lines that are not one JSON object)."""
    records, bad = [], []
    for n, line in enumerate(pathlib.Path(path).read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            bad.append(n)
            continue
        if isinstance(rec, dict):
            records.append(rec)
        else:
            bad.append(n)
    return records, bad


def safe_key(rec):
    try:
        k = p1.rec_key(rec)
        hash(k)
        return k
    except (KeyError, TypeError):
        return None


def expected_keys(arm, reasoning, cells=None):
    return {p1.key(t["id"], c, cls, ph, rep, reasoning) for t, c, cls, ph, rep in p1.jobs(arm, cells)}


def coverage(records, arm, reasoning, cells=None):
    expected = expected_keys(arm, reasoning, cells)
    present = expected & {safe_key(r) for r in records}
    return {"expected": len(expected), "present": len(present), "missing": sorted(expected - present)}


def duplicates(records):
    counts = Counter(safe_key(r) for r in records)
    return sorted(k for k, n in counts.items() if k is not None and n > 1)


def _who(rec):
    return f"{rec.get('task')}/{rec.get('cond')}/{rec.get('class')}/r{rec.get('rep')}"


def _record_problems(rec):
    missing = [f for f in REQUIRED if rec.get(f) is None]
    if missing:
        return [f"{_who(rec)}: missing {', '.join(missing)}"]
    problems = []
    for field in ("model", "finish_reason") + (("provider",) if "/" in str(rec.get("model")) else ()):
        if rec["meta"].get(field) is None:  # OpenRouter ids are vendor/model and must name a provider
            problems.append(f"{_who(rec)}: meta.{field} missing")
    if not (rec["usage"].get("in") or 0):
        problems.append(f"{_who(rec)}: usage.in is 0")
    if str(rec.get("cond", "")).startswith("C:tool:"):
        head = [(t.get("role"), t.get("synthetic", False)) for t in rec["transcript"][:2]]
        if head != [("assistant_tool_call", True), ("tool_result", True)]:
            problems.append(f"{_who(rec)}: tool placement without the synthetic changelog preamble")
    return problems


def completeness(records):
    return [p for rec in records for p in _record_problems(rec)]


def _meta(rec, field):
    value = (rec.get("meta") or {}).get(field)
    return NONE if value is None else value


def _recalled_changelog(rec):
    return any(t.get("role") == "assistant_tool_call" and not t.get("synthetic")
               and t.get("name") == harness.CHANGELOG_TOOL for t in rec.get("transcript") or [])


def cell_report(records):
    cells = {}
    for cond in sorted({r.get("cond") for r in records}, key=str):
        rows = [r for r in records if r.get("cond") == cond]
        is_tool = str(cond).startswith("C:tool:")
        cells[cond] = {
            "n": len(rows),
            "length_rate": sum(_meta(r, "finish_reason") in TRUNCATED for r in rows) / len(rows),
            "providers": dict(Counter(_meta(r, "provider") for r in rows)),
            "versions": dict(Counter(_meta(r, "model") for r in rows)),
            "changelog_recall_rate": sum(map(_recalled_changelog, rows)) / len(rows) if is_tool else None,
        }
    return cells


def spend_report(model, n_records, cost_log=COST_LOG):
    """Phase-1 API spend logged for this model (probe excluded), per episode and per minute."""
    rows, _ = read_records(cost_log) if pathlib.Path(cost_log).exists() else ([], [])
    rows = [r for r in rows if r.get("phase") == "phase1" and r.get("model") == model
            and str(r.get("tag", "")).startswith("p1-") and not str(r.get("tag")).startswith("p1-probe")]
    usd = round(sum(r.get("est_cost_usd", 0) for r in rows), 6)
    stamps = sorted(datetime.fromisoformat(r["ts"]) for r in rows if r.get("ts"))
    minutes = (stamps[-1] - stamps[0]).total_seconds() / 60 if len(stamps) > 1 else 0
    episodes = len({r["tag"] for r in rows})
    return {"usd": usd, "usd_per_episode": round(usd / n_records, 6) if n_records else None,
            "episodes_per_minute": round(episodes / minutes, 3) if minutes else None}


def _failures(bad, keyless, problems, dups, cells, versions, cov, pilot):
    out = [f"unparsable lines: {bad}"] if bad else []
    out += [f"record without a full key: {w}" for w in keyless]
    out += problems
    out += [f"duplicate key: {k}" for k in dups]
    for cond, c in cells.items():
        if len(c["providers"]) > 1:
            out.append(f"{cond}: {len(c['providers'])} providers {c['providers']}")
        if c["length_rate"] > MAX_LENGTH_RATE:
            out.append(f"{cond}: length_rate {c['length_rate']:.3f} > {MAX_LENGTH_RATE}")
    if len(versions) > 1:
        out.append(f"model versions in file: {versions}")
    if not pilot and cov["missing"]:
        out.append(f"coverage: {len(cov['missing'])} of {cov['expected']} jobs missing")
    if cov["present"] == 0:
        out.append("no record matches this arm/reasoning/cells (wrong --reasoning or --arm?)")
    return out


def gate(path, arm, reasoning, cells=None, pilot=False):
    """(ok, report). File-wide checks: parse, duplicates, versions; the rest on this arm's records."""
    records, bad = read_records(path)
    expected = expected_keys(arm, reasoning, cells)
    arm_records = [r for r in records if safe_key(r) in expected]
    cov = coverage(records, arm, reasoning, cells)
    cell_rows = cell_report(arm_records)
    versions = dict(Counter(_meta(r, "model") for r in records))
    dups = duplicates(records)
    keyless = [_who(r) for r in records if safe_key(r) is None]
    failures = _failures(bad, keyless, completeness(arm_records), dups, cell_rows, versions, cov, pilot)
    model = Counter(r.get("model") for r in records).most_common(1)[0][0] if records else None
    report = {"file": str(path), "arm": arm, "reasoning": reasoning, "pilot": pilot,
              "records": len(records), "unparsable_lines": bad, "coverage": cov, "duplicates": dups,
              "excluded_other_arms": len(records) - len(arm_records) - len(keyless),
              "cells": cell_rows, "versions": versions, "spend": spend_report(model, len(records)),
              "failures": failures}
    return not failures, report


def _print(ok, report):  # pragma: no cover - formatting only
    cov = report["coverage"]
    print(f"{report['file']}  arm={report['arm']} reasoning={report['reasoning']} records={report['records']}")
    print(f"coverage {cov['present']}/{cov['expected']}  versions {report['versions']}  spend {report['spend']}")
    for cond, c in report["cells"].items():
        recall = "" if c["changelog_recall_rate"] is None else f" recall={c['changelog_recall_rate']:.2f}"
        print(f"  {cond:<22} n={c['n']:<4} length={c['length_rate']:.3f} providers={c['providers']}{recall}")
    for f in report["failures"][:40]:
        print(f"  FAIL {f}")
    print("PASS" if ok else f"FAIL ({len(report['failures'])} problems)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--arm", required=True, choices=p1.ARMS)
    ap.add_argument("--reasoning", default="default")
    ap.add_argument("--cells", default="")
    ap.add_argument("--pilot", action="store_true", help="partial run: skip the 100% coverage check")
    args = ap.parse_args()
    ok, report = gate(args.file, args.arm, args.reasoning, args.cells.split(",") if args.cells else None,
                      pilot=args.pilot)
    _print(ok, report)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
