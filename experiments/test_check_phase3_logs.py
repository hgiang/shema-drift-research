#!/usr/bin/env python3
"""Phase-3 gate: the log checker must count the catalog arm's own keys.

Run: python3 -m pytest test_check_phase3_logs.py -q
"""

import json
import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_phase1_logs as chk  # noqa: E402
import phase3_grid as p3  # noqa: E402


def record(job, reasoning="MINIMAL", **kw):
    t, cond, cls, cat = job
    base = {"task": t["id"], "cond": cond, "class": cls, "catalog": cat, "phase": "phase3",
            "arm": "catalog", "reasoning": reasoning, "transcript": [], "usage": {"in": 1, "out": 1},
            "meta": {"model": "gemini-3.6-flash", "finish_reason": "STOP"},
            "model": "gemini-3.6-flash", "success": True, "executed": []}
    return {**base, **kw}


def test_phase_three_is_a_known_phase():
    assert 3 in chk.PHASES


def test_expected_keys_cover_every_catalog_job():
    keys = chk.expected_keys("catalog", "MINIMAL", phase=3)
    assert len(keys) == 240
    assert len({k for k in keys if k[3] == "full"}) == 120


def test_coverage_is_complete_when_every_job_is_logged():
    records = [record(j) for j in p3.jobs()]
    cov = chk.coverage(records, "catalog", "MINIMAL", phase=3)
    assert cov["expected"] == 240 and cov["present"] == 240 and cov["missing"] == []


def test_a_missing_catalog_size_is_reported_as_missing():
    records = [record(j) for j in p3.jobs() if j[3] == "small"]
    cov = chk.coverage(records, "catalog", "MINIMAL", phase=3)
    assert cov["present"] == 120 and len(cov["missing"]) == 120
    assert all(k[3] == "full" for k in cov["missing"])


def test_the_small_and_full_records_of_one_pair_are_not_duplicates():
    jobs = [j for j in p3.jobs() if j[0]["id"] == p3.PAIRS[0][0]["id"]]
    assert chk.duplicates([record(j) for j in jobs], phase=3) == []


def test_a_repeated_key_is_still_a_duplicate():
    job = p3.jobs()[0]
    assert chk.duplicates([record(job), record(job)], phase=3)


def test_an_unknown_phase_three_arm_is_refused():
    with pytest.raises(SystemExit, match="catalog"):
        chk.expected_keys("core", "MINIMAL", phase=3)


def test_the_gate_passes_a_complete_phase_three_file(tmp_path):
    path = tmp_path / "runs_gemini-3.6-flash.jsonl"
    path.write_text("".join(json.dumps(record(j)) + "\n" for j in p3.jobs()))
    ok, report = chk.gate(path, "catalog", "MINIMAL", phase=3)
    assert report["coverage"]["missing"] == [] and report["duplicates"] == []
    assert report["excluded_other_arms"] == 0 and ok is True
