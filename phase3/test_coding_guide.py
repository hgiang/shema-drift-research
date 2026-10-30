#!/usr/bin/env python3
"""Tests for the coding guide and its answer parser.

Run: python3 -m pytest phase3/test_coding_guide.py -q
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import coding_guide as cg  # noqa: E402

BATCH = [{"digest_id": "stripe:000", "candidates": [{"span": "x", "identifiers": ["a"]}]},
         {"digest_id": "slack:004", "candidates": [{"span": "y", "identifiers": ["b"]}]}]


def test_the_guide_never_leaks_a_prediction():
    text = cg.GUIDE.lower()
    for leak in ("p17", "p18", "p19", "p20", "p21", "prevalence", "we expect", "hypothes",
                 "at least", "schemadrift", "%"):
        assert leak not in text, leak


def test_the_guide_states_every_locked_label_and_the_agent_visible_rule():
    for label in cg.LABELS:
        assert f'"{label}"' in cg.GUIDE
    assert "WITHOUT looking at the label" in cg.GUIDE
    assert "2023-01-01 to 2026-09-30" in cg.GUIDE


def test_the_guide_warns_that_the_candidates_are_unreliable():
    assert "often wrong" in cg.GUIDE and "error codes" in cg.GUIDE


def test_prompt_contains_the_guide_and_every_digest():
    prompt = cg.prompt_for(BATCH)
    assert cg.GUIDE in prompt
    for d in BATCH:
        assert d["digest_id"] in prompt


def test_parse_reads_a_clean_answer():
    answer = json.dumps([{"digest_id": "stripe:000",
                          "units": [{"parameter": "a", "label": "rename", "agent_visible": True}]},
                         {"digest_id": "slack:004", "units": []}])
    units, problems = cg.parse(answer, BATCH)
    assert problems == []
    assert units == [{"digest_id": "stripe:000", "parameter": "a", "label": "rename",
                      "agent_visible": True}]


def test_parse_strips_a_code_fence_and_surrounding_prose():
    answer = ('Sure, here it is:\n```json\n[{"digest_id": "stripe:000", "units": []},'
              '{"digest_id": "slack:004", "units": []}]\n```\n')
    units, problems = cg.parse(answer, BATCH)
    assert units == [] and problems == []


def test_parse_reports_a_bad_label_instead_of_keeping_it():
    answer = json.dumps([{"digest_id": "stripe:000",
                          "units": [{"parameter": "a", "label": "renamed", "agent_visible": True}]},
                         {"digest_id": "slack:004", "units": []}])
    units, problems = cg.parse(answer, BATCH)
    assert units == [] and any("bad unit" in p for p in problems)


def test_parse_reports_a_missing_and_an_unknown_digest():
    answer = json.dumps([{"digest_id": "stripe:000", "units": []},
                         {"digest_id": "ghost:999", "units": []}])
    _, problems = cg.parse(answer, BATCH)
    assert any("ghost:999" in p for p in problems) and any("slack:004" in p for p in problems)


def test_parse_survives_an_answer_that_is_not_json():
    units, problems = cg.parse("I cannot do that.", BATCH)
    assert units == [] and problems and "no JSON array" in problems[0]


def test_parse_normalises_a_non_boolean_agent_visible():
    answer = json.dumps([{"digest_id": "stripe:000",
                          "units": [{"parameter": "a", "label": "other", "agent_visible": "yes"}]},
                         {"digest_id": "slack:004", "units": []}])
    units, _ = cg.parse(answer, BATCH)
    assert units[0]["agent_visible"] is None
