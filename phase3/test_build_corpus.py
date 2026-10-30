#!/usr/bin/env python3
"""Tests for building the agreed Phase-3 corpus.

Run: python3 -m pytest phase3/test_build_corpus.py -q
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_corpus as bc  # noqa: E402


def unit(digest, parameter, label, visible=True):
    return {"digest_id": digest, "parameter": parameter, "label": label, "agent_visible": visible}


DIGESTS = [{"digest_id": f"stripe:{i:03d}", "source": "stripe", "draw_rank": i,
            "entry_url": f"https://d.test/{i}", "scope": f"S{i}"} for i in range(5)]
DIGESTS += [{"digest_id": "slack:002", "source": "slack", "draw_rank": 2,
             "entry_url": "https://s.test/2", "scope": "T"}]


def test_corpus_is_the_units_both_coders_found(tmp_path):
    a = [unit("stripe:000", "x", "rename"), unit("stripe:001", "y", "required")]
    b = [unit("stripe:000", "x", "rename"), unit("stripe:002", "z", "other")]
    rows = bc.build(a, b, DIGESTS)
    assert [r["parameter"] for r in rows] == ["x"]
    assert rows[0]["source"] == "stripe" and rows[0]["entry_url"] == "https://d.test/0"
    assert rows[0]["draw_rank"] == 0 and rows[0]["scope"] == "S0"


def test_a_label_disagreement_keeps_the_unit_out_of_the_corpus(tmp_path):
    a = [unit("stripe:000", "x", "rename")]
    b = [unit("stripe:000", "x", "type_change")]
    rows = bc.build(a, b, DIGESTS)
    assert rows == []


def test_agent_visible_disagreement_is_recorded_as_unknown_not_dropped():
    a = [unit("stripe:000", "x", "rename", True)]
    b = [unit("stripe:000", "x", "rename", False)]
    rows = bc.build(a, b, DIGESTS)
    assert len(rows) == 1 and rows[0]["agent_visible"] is None
    assert rows[0]["agent_visible_disputed"] is True


def test_the_cap_keeps_the_first_units_in_draw_order():
    a = [unit(f"stripe:{i:03d}", f"p{i}", "other") for i in range(5)]
    rows = bc.build(a, list(a), DIGESTS, cap=3)
    assert [r["draw_rank"] for r in rows] == [0, 1, 2]


def test_the_cap_is_per_source():
    a = [unit(f"stripe:{i:03d}", f"p{i}", "other") for i in range(5)] + [unit("slack:002", "q", "other")]
    rows = bc.build(a, list(a), DIGESTS, cap=2)
    assert sorted(r["source"] for r in rows) == ["slack", "stripe", "stripe"]


def test_index_digests_sort_before_the_drawn_ones():
    digests = [{"digest_id": "github:index", "source": "github", "draw_rank": -1,
                "entry_url": "https://g.test/bc", "scope": "Breaking changes"},
               {"digest_id": "github:004", "source": "github", "draw_rank": 4,
                "entry_url": "https://g.test/4", "scope": "X"}]
    a = [unit("github:004", "b", "other"), unit("github:index", "a", "other")]
    rows = bc.build(a, list(a), digests)
    assert [r["parameter"] for r in rows] == ["a", "b"]


def test_write_corpus_is_byte_stable_and_summarised(tmp_path):
    a = [unit("stripe:000", "x", "rename"), unit("slack:002", "q", "other", None)]
    out, summary_path = tmp_path / "c.jsonl", tmp_path / "s.json"
    summary = bc.write(a, list(a), DIGESTS, out, summary_path)
    first = out.read_bytes()
    bc.write(a, list(a), DIGESTS, out, summary_path)
    assert out.read_bytes() == first
    assert summary["pooled"]["n_units"] == 2
    assert summary["by_source"]["stripe"]["labels"]["rename"] == 1
    assert json.loads(summary_path.read_text())["pooled"]["n_units"] == 2


def test_summary_counts_agent_visible_three_ways():
    a = [unit("stripe:000", "x", "rename", True), unit("stripe:001", "y", "other", False),
         unit("stripe:002", "z", "other", None)]
    summary = bc.summarise(bc.build(a, list(a), DIGESTS))
    assert summary["pooled"]["agent_visible"] == {"true": 1, "false": 1, "unknown": 1}
