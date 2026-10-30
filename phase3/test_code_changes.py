#!/usr/bin/env python3
"""Tests for building the Phase-3 corpus from an archive.

Run: python3 -m pytest phase3/test_code_changes.py -q
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import code_changes as cc  # noqa: E402
import web_archive as wa  # noqa: E402

ENTRIES = {
    "https://docs.stripe.com/changelog/a.md":
        "# Charges\n\nThe `source` parameter has been renamed to `origin`.\n",
    "https://docs.stripe.com/changelog/b.md":
        "# Refunds\n\nThe `limit` parameter now defaults to 20.\nThe `status` parameter is now required.\n",
    "https://docs.stripe.com/changelog/c.md":
        "# Docs\n\nWe improved the guides for billing.\n",
}


def build_archive(tmp_path, entries=ENTRIES, source="stripe"):
    for i, (url, body) in enumerate(entries.items()):
        wa.store(tmp_path, source, i, url, body.encode(), 200, now="t")
    manifest = {url: wa.store(tmp_path, source, i, url, body.encode(), 200, now="t")
                for i, (url, body) in enumerate(entries.items())}
    wa.save_manifest(tmp_path, source, manifest)
    (tmp_path / f"{source}.fetch.json").write_text(json.dumps(
        {"source": source, "n_enumerated": len(entries), "drawn": list(entries)}))
    return tmp_path


def test_units_carry_the_locked_fields(tmp_path):
    units = cc.code_source(build_archive(tmp_path), "stripe", cap=60)
    assert len(units) == 3
    for u in units:
        assert set(u) == set(cc.FIELDS)
        assert u["source"] == "stripe" and u["entry_url"].startswith("https://")
        assert u["label"] in cc.dr.LABELS and u["evidence"] and u["rule"]
    assert [(u["parameter"], u["label"]) for u in units] == [
        ("source", "rename"), ("limit", "default_change"), ("status", "required")]


def test_entries_are_read_in_the_drawn_order_and_ranked(tmp_path):
    units = cc.code_source(build_archive(tmp_path), "stripe", cap=60)
    assert [u["draw_rank"] for u in units] == [0, 1, 1]
    assert units[0]["entry_url"].endswith("a.md")


def test_the_cap_stops_at_a_whole_entry(tmp_path):
    units = cc.code_source(build_archive(tmp_path), "stripe", cap=2)
    assert len(units) == 3          # entry b yields two units and is not cut in half
    assert cc.code_source(build_archive(tmp_path), "stripe", cap=1) == units[:1]


def test_an_entry_with_no_qualifying_change_contributes_nothing(tmp_path):
    units = cc.code_source(build_archive(tmp_path), "stripe", cap=60)
    assert not any(u["entry_url"].endswith("c.md") for u in units)


def test_scope_is_the_entry_heading(tmp_path):
    units = cc.code_source(build_archive(tmp_path), "stripe", cap=60)
    assert units[0]["scope"] == "Charges" and units[1]["scope"] == "Refunds"


def test_write_corpus_is_byte_stable_and_sorted(tmp_path):
    build_archive(tmp_path)
    out = tmp_path / "corpus.jsonl"
    summary = cc.write_corpus(tmp_path, out, sources=["stripe"], cap=60)
    first = out.read_bytes()
    cc.write_corpus(tmp_path, out, sources=["stripe"], cap=60)
    assert out.read_bytes() == first
    rows = [json.loads(line) for line in first.decode().splitlines()]
    assert [r["unit_id"] for r in rows] == sorted(r["unit_id"] for r in rows)
    assert summary["stripe"]["n_units"] == 3 and summary["stripe"]["n_entries_read"] == 3


def test_unit_ids_are_unique_and_rebuildable(tmp_path):
    units = cc.code_source(build_archive(tmp_path), "stripe", cap=60)
    ids = [u["unit_id"] for u in units]
    assert len(set(ids)) == len(ids)
    assert all(u["source"] in u["unit_id"] and u["parameter"] in u["unit_id"] for u in units)


def test_a_missing_source_is_an_error_not_an_empty_corpus(tmp_path):
    try:
        cc.code_source(tmp_path, "slack", cap=60)
    except SystemExit as e:
        assert "slack" in str(e)
    else:
        raise AssertionError("a source with no fetch report should stop the build")
