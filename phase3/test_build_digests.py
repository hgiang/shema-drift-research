#!/usr/bin/env python3
"""Tests for the Phase-3 digest builder (MILESTONES.md "Phase 3 amendment 1").

A digest is what the two blind coders read. It must be deterministic, it must carry no label
and no `agent_visible`, and it must not leak the predictions.

Run: python3 -m pytest phase3/test_build_digests.py -q
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_digests as bd  # noqa: E402
import web_archive as wa  # noqa: E402

ENTRIES = {
    "https://docs.stripe.com/changelog/a.md":
        "# Charges\n\nThe `source` parameter has been renamed to `origin`.\n"
        "We also improved the billing guides.\n",
    "https://docs.stripe.com/changelog/b.md":
        "# Refunds\n\nThe `limit` parameter now defaults to 20.\n",
    "https://docs.stripe.com/changelog/c.md":
        "# Docs\n\nWe improved the guides for billing.\n",
}

SCHEMA_PATCH = """From abc Mon Sep 17 00:00:00 2001
Subject: [PATCH] feat: tighten search

diff --git a/src/search/schema.ts b/src/search/schema.ts
--- a/src/search/schema.ts
+++ b/src/search/schema.ts
@@ -1,4 +1,4 @@
 const inputSchema = {
-  query: z.string().optional(),
+  query: z.string(),
 }
diff --git a/src/ui/render.ts b/src/ui/render.ts
--- a/src/ui/render.ts
+++ b/src/ui/render.ts
@@ -1,2 +1,2 @@
-  const colour = "Guitar";
+  const colour = "Banjo";
"""


def build_archive(tmp_path, entries=ENTRIES, source="stripe", ext=".md"):
    manifest = {}
    for i, (url, body) in enumerate(entries.items()):
        manifest[url] = wa.store(tmp_path, source, i, url, body.encode(), 200, now="t")
    wa.save_manifest(tmp_path, source, manifest)
    (tmp_path / f"{source}.fetch.json").write_text(json.dumps(
        {"source": source, "n_enumerated": len(entries), "drawn": list(entries)}))
    return tmp_path


def test_a_digest_carries_no_label_and_no_agent_visible(tmp_path):
    digests = bd.digests_for(build_archive(tmp_path), "stripe", max_entries=10)
    assert digests
    for d in digests:
        assert set(d) == set(bd.DIGEST_FIELDS)
        blob = json.dumps(d).lower()
        for leak in ("label", "agent_visible", "rename", "enum_tighten", "default_change",
                     "compound", "p17", "p18", "p19", "p20", "prevalence"):
            assert leak not in set(d), leak
        assert "candidates" in d and d["candidates"]


def test_entries_with_no_candidate_span_are_counted_but_not_digested(tmp_path):
    digests = bd.digests_for(build_archive(tmp_path), "stripe", max_entries=10)
    assert [d["entry_url"].rsplit("/", 1)[-1] for d in digests] == ["a.md", "b.md"]


def test_candidates_keep_the_locked_draw_order(tmp_path):
    digests = bd.digests_for(build_archive(tmp_path), "stripe", max_entries=10)
    assert [d["draw_rank"] for d in digests] == [0, 1]
    assert digests[0]["scope"] == "Charges"


def test_a_candidate_names_its_identifiers_without_judging_them(tmp_path):
    digests = bd.digests_for(build_archive(tmp_path), "stripe", max_entries=10)
    first = digests[0]["candidates"][0]
    assert set(first) == {"span", "identifiers"}
    assert "source" in first["identifiers"] and "renamed" in first["span"]


def test_patch_digests_keep_only_schema_bearing_hunks(tmp_path):
    build_archive(tmp_path, {"https://github.com/x/commit/aa.patch": SCHEMA_PATCH},
                  source="mcp")
    digests = bd.digests_for(tmp_path, "mcp", max_entries=10)
    blob = json.dumps(digests)
    assert "query" in blob and "Guitar" not in blob and "Banjo" not in blob


def test_write_digests_is_byte_stable(tmp_path):
    build_archive(tmp_path)
    out = tmp_path / "digests.jsonl"
    summary = bd.write_digests(tmp_path, out, sources=["stripe"], max_entries=10)
    first = out.read_bytes()
    bd.write_digests(tmp_path, out, sources=["stripe"], max_entries=10)
    assert out.read_bytes() == first
    assert summary["stripe"]["n_digests"] == 2 and summary["stripe"]["n_entries_read"] == 3


def test_digest_ids_are_unique_and_name_their_source(tmp_path):
    digests = bd.digests_for(build_archive(tmp_path), "stripe", max_entries=10)
    ids = [d["digest_id"] for d in digests]
    assert len(set(ids)) == len(ids) and all(i.startswith("stripe:") for i in ids)


def test_spans_are_trimmed_so_a_coder_reads_a_bounded_page(tmp_path):
    long_entry = {"https://d.test/x.md": "# T\n\n" + "The `a` parameter is now required. " * 200}
    digests = bd.digests_for(build_archive(tmp_path, long_entry), "stripe", max_entries=10)
    assert len(digests[0]["candidates"]) <= bd.MAX_SPANS
    assert all(len(c["span"]) <= bd.MAX_SPAN_CHARS for c in digests[0]["candidates"])


def test_a_source_can_declare_an_index_page_as_a_codeable_entry(tmp_path):
    """Phase 3 amendment 2: GitHub's own breaking-changes page is an index URL but a real
    entry, so the builder reads the index pages a source declares codeable."""
    url = "https://docs.github.com/en/rest/about-the-rest-api/breaking-changes"
    assert url in bd.CODEABLE_INDEX["github"]
    entries = {url: "# Breaking changes\n\nThe `permission` parameter is now required.\n"}
    build_archive(tmp_path, entries, source="github")
    (tmp_path / "github.fetch.json").write_text(json.dumps(
        {"source": "github", "n_enumerated": 0, "drawn": []}))      # an index page is not drawn
    digests = bd.digests_for(tmp_path, "github", max_entries=10)
    assert len(digests) == 1 and digests[0]["draw_rank"] == -1
    assert digests[0]["candidates"][0]["identifiers"] == ["permission"]


def test_a_sources_other_index_pages_are_not_coded(tmp_path):
    assert "https://github.blog/changelog-sitemap.xml" not in bd.CODEABLE_INDEX["github"]
    assert bd.CODEABLE_INDEX.get("stripe", ()) == ()
