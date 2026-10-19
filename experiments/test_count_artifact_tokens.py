#!/usr/bin/env python3
"""Tests for tokenizer-measured artifact sizes. No network: fake encoder only.

Run: python3 -m pytest test_count_artifact_tokens.py -q
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import count_artifact_tokens as cat  # noqa: E402
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402


def test_diff_json_matches_condition_C_text():
    for t, cls in p1.primary_pairs()[:10]:
        key = f"{t['drift_tool']}::{cls}"
        system = harness.build_condition(t, "C", cls)["system"]
        assert system.endswith("\n" + cat.artifacts(key)["diff_json"])


def test_artifacts_are_the_texts_the_conditions_use():
    t, cls = next((t, c) for t, c in p1.primary_pairs() if c == "default_change")
    key = f"{t['drift_tool']}::{cls}"
    a = cat.artifacts(key)
    assert set(a) == set(cat.ARTIFACTS)
    decl = next(d for d in harness.build_condition(t, "D", cls)["declarations"] if d["name"] == t["drift_tool"])
    assert a["v2_declaration"] == json.dumps(decl)
    prose = harness.build_phase1(t, "C:user:prose:none", cls)["user_suffix"]
    assert a["diff_prose"] in prose
    assert a["cd_note"] in harness.build_phase1(t, "CD", cls)["system"]
    dprime = harness.build_phase1(t, "Dprime", cls)["declarations"]
    assert any(a["dprime_suffix"] in json.dumps(d) for d in dprime)


def test_count_with_fake_encoder():
    assert cat.count({"a": "one two three", "b": ""}, str.split) == {"a": 3, "b": 0}


def test_summary_means_and_ratio():
    per_key = {"k1": {"diff_json": 10, "v2_declaration": 100}, "k2": {"diff_json": 30, "v2_declaration": 100}}
    s = cat.summarize(per_key)
    assert s["means"] == {"diff_json": 20.0, "v2_declaration": 100.0}
    assert s["ratio_diff_json_to_v2_declaration"] == 0.2
