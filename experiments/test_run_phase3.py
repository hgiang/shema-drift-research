#!/usr/bin/env python3
"""Tests for the Phase-3 catalog runner. No model is ever called.

Run: python3 -m pytest test_run_phase3.py -q
"""

import json
import pathlib
import sys
import types

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import phase3_grid as p3  # noqa: E402
import run_phase3 as rp3  # noqa: E402
from test_phase1 import oracle  # noqa: E402

PIN = {"provider": "fake", "strict": None, "endpoint": "fake", "quantization": None, "max_tokens": 700}


def args(**kw):
    base = dict(model="gemini-3.6-flash", provider=None, quantization=None, max_tokens=1024,
                cap=None, limit=None)
    return types.SimpleNamespace(**{**base, **kw})


def test_the_family_decides_which_caller_is_used():
    assert rp3.is_gemini("gemini-3.6-flash") is True
    assert rp3.is_gemini("anthropic/claude-haiku-5.5") is False


def test_an_openrouter_model_without_a_provider_is_refused():
    with pytest.raises(SystemExit, match="provider"):
        rp3.make_caller(args(model="anthropic/claude-haiku-5.5"), [""])


def test_done_keys_reads_the_catalog_size(tmp_path):
    path = tmp_path / "runs.jsonl"
    path.write_text(json.dumps({"task": "t1", "cond": "A", "class": "rename",
                                "catalog": "full"}) + "\n")
    assert rp3._done_keys(path) == {("t1", "A", "rename", "full")}
    assert rp3._done_keys(tmp_path / "missing.jsonl") == set()


def test_a_record_without_a_catalog_field_counts_as_small(tmp_path):
    path = tmp_path / "runs.jsonl"
    path.write_text(json.dumps({"task": "t1", "cond": "A", "class": "rename"}) + "\n")
    assert rp3._done_keys(path) == {("t1", "A", "rename", "small")}


def test_an_episode_records_the_catalog_and_its_declaration_count():
    job = next(j for j in p3.jobs() if j[3] == "full")
    task, cond, cls, _ = job
    rec = p3.run_episode(job, oracle("v2")(task, cls), "fake-model", "default", 700, PIN)
    assert rec["catalog"] == "full" and rec["n_declarations"] == 30
    assert rec["phase"] == "phase3" and rec["arm"] == "catalog"
    assert rec["catalog_seed"] == p3.SEED_P3 and rec["pin"] == PIN

    small = next(j for j in p3.jobs() if j[3] == "small")
    rec2 = p3.run_episode(small, oracle("v2")(small[0], small[2]), "fake", "default", 700, PIN)
    assert rec2["catalog"] == "small" and rec2["n_declarations"] <= 2


def test_every_job_key_is_unique_and_resumable():
    jobs = p3.jobs()
    assert len(jobs) == 240 and len({p3.job_key(j) for j in jobs}) == 240
    rec = {"task": jobs[0][0]["id"], "cond": jobs[0][1], "class": jobs[0][2], "catalog": jobs[0][3]}
    assert p3.rec_key(rec) == p3.job_key(jobs[0])


def test_the_pilot_writes_to_a_separate_file():
    assert p3.out_path("m", pilot=True).name.endswith(".pilot.jsonl")
    assert not p3.out_path("m").name.endswith(".pilot.jsonl")
