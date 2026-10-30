#!/usr/bin/env python3
"""Tests for the blind-coder runner. The coder is always injected; nothing calls a model.

Run: python3 -m pytest phase3/test_run_coder.py -q
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_coder as rc  # noqa: E402

DIGESTS = [{"digest_id": f"stripe:{i:03d}", "source": "stripe",
            "candidates": [{"span": "s", "identifiers": ["a"]}]} for i in range(13)]


def answer_for(prompt):
    body = prompt.split("DIGESTS (", 1)[1]        # the guide shows a "<id>" example; skip it
    ids = [line.split('"digest_id": "')[1].split('"')[0]
           for line in body.splitlines() if '"digest_id"' in line]
    return json.dumps([{"digest_id": i,
                        "units": [{"parameter": "a", "label": "rename", "agent_visible": True}]}
                       for i in ids])


def test_batches_cover_every_digest_once():
    groups = rc.batches(DIGESTS)
    assert sum(len(g) for g in groups) == len(DIGESTS)
    assert [d["digest_id"] for g in groups for d in g] == [d["digest_id"] for d in DIGESTS]
    assert all(len(g) <= rc.BATCH for g in groups)


def test_run_labels_every_digest_and_archives_the_raw_answers(tmp_path):
    path = tmp_path / "answers.jsonl"
    units, problems = rc.run("fake", DIGESTS, answer_for, answers_path=path)
    assert problems == [] and len(units) == len(DIGESTS)
    archived = [json.loads(line) for line in path.read_text().splitlines()]
    assert len(archived) == len(rc.batches(DIGESTS))
    assert archived[0]["digest_ids"] == [d["digest_id"] for d in DIGESTS[:rc.BATCH]]


def test_run_resumes_from_the_archive_without_calling_again(tmp_path):
    path = tmp_path / "answers.jsonl"
    calls = []

    def counting(prompt):
        calls.append(1)
        return answer_for(prompt)

    rc.run("fake", DIGESTS, counting, answers_path=path)
    first = len(calls)
    units, problems = rc.run("fake", DIGESTS, counting, answers_path=path)
    assert len(calls) == first and len(units) == len(DIGESTS) and problems == []


def test_limit_sends_only_the_first_batches(tmp_path):
    path = tmp_path / "answers.jsonl"
    units, _ = rc.run("fake", DIGESTS, answer_for, answers_path=path, limit=1)
    assert len(units) == rc.BATCH


def test_a_bad_answer_is_reported_not_swallowed(tmp_path):
    path = tmp_path / "answers.jsonl"
    units, problems = rc.run("fake", DIGESTS[:2], lambda p: "sorry, no", answers_path=path)
    assert units == [] and problems and "no JSON array" in problems[0]


def test_write_labels_is_sorted_and_stable(tmp_path):
    units = [{"digest_id": "b:1", "parameter": "z", "label": "other", "agent_visible": None},
             {"digest_id": "a:0", "parameter": "y", "label": "rename", "agent_visible": True}]
    out = rc.write_labels("fake", units, out=tmp_path / "labels.jsonl")
    rows = [json.loads(line) for line in out.read_text().splitlines()]
    assert [r["digest_id"] for r in rows] == ["a:0", "b:1"]
    first = out.read_bytes()
    rc.write_labels("fake", list(reversed(units)), out=out)
    assert out.read_bytes() == first


def test_load_digests_reads_the_jsonl(tmp_path):
    path = tmp_path / "d.jsonl"
    path.write_text("".join(json.dumps(d) + "\n" for d in DIGESTS[:3]))
    assert [d["digest_id"] for d in rc.load_digests(path)] == ["stripe:000", "stripe:001", "stripe:002"]
