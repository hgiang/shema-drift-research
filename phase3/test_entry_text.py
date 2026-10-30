#!/usr/bin/env python3
"""Tests for turning an archived page into codeable text.

Fixtures are hand-written excerpts, never fetched pages.

Run: python3 -m pytest phase3/test_entry_text.py -q
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import entry_text as et  # noqa: E402

HTML = """<!doctype html>
<html><head><title>t</title>
<script>var x = "parameter removed";</script>
<style>.a { color: red }</style>
</head>
<body>
<h1>REST API: the <code>sort</code> parameter is now required</h1>
<p>The &amp; character and the <code>per_page</code> field changed.</p>
<pre><code>curl -X GET "https://api.test/x?sort=created"</code></pre>
</body></html>
"""

PATCH = """From abc Mon Sep 17 00:00:00 2001
Subject: [PATCH] feat: tighten the search schema

Body of the commit message.
---
 src/search/index.ts | 4 ++--
 README.md           | 2 +-

diff --git a/src/search/index.ts b/src/search/index.ts
index 1111..2222 100644
--- a/src/search/index.ts
+++ b/src/search/index.ts
@@ -10,7 +10,7 @@ const schema = {
-  query: z.string().optional(),
+  query: z.string(),
   limit: z.number().default(10),
 }
diff --git a/README.md b/README.md
index 3333..4444 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,2 @@
-old readme line
+new readme line
"""

MARKDOWN = """---
title: "Release"
url: "https://docs.slack.dev/changelog/2024/03/08/x"
---

# Release

The `channel` parameter is now required.
"""


def test_html_drops_script_and_style_and_keeps_code_as_backticks():
    text = et.from_html(HTML)
    assert "var x" not in text and "color: red" not in text
    assert "`sort`" in text and "`per_page`" in text
    assert "parameter is now required" in text
    assert "&amp;" not in text and "& character" in text


def test_html_keeps_example_snippets_so_agent_visible_can_see_them():
    assert "sort=created" in et.from_html(HTML)


def test_patch_keeps_the_subject_and_only_schema_side_changed_lines():
    text = et.from_patch(PATCH)
    assert "tighten the search schema" in text
    assert "query: z.string().optional()" in text and "query: z.string()," in text
    assert "old readme line" not in text and "new readme line" not in text
    assert "index 1111" not in text


DOCS_ONLY_PATCH = """From abc Mon Sep 17 00:00:00 2001
Subject: [PATCH] docs: reword the readme

diff --git a/README.md b/README.md
index 3333..4444 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,2 @@
-old readme line
+new readme line
"""


def test_patch_without_a_code_file_yields_only_the_message():
    text = et.from_patch(DOCS_ONLY_PATCH)
    assert "readme line" not in text
    assert "reword the readme" in text


def test_markdown_is_passed_through_without_front_matter():
    text = et.from_markdown(MARKDOWN)
    assert "title:" not in text and "`channel` parameter is now required" in text


def test_read_entry_picks_the_reader_from_the_stored_name(tmp_path):
    (tmp_path / "a.md").write_text(MARKDOWN)
    (tmp_path / "b.txt").write_text(HTML)
    (tmp_path / "c.patch").write_text(PATCH)
    (tmp_path / "d.json").write_text('{"a": 1}')
    assert "`channel`" in et.read_entry(tmp_path / "a.md")
    assert "`sort`" in et.read_entry(tmp_path / "b.txt")          # .txt holding HTML
    assert "tighten the search schema" in et.read_entry(tmp_path / "c.patch")
    assert et.read_entry(tmp_path / "d.json") == ""               # JSON index pages are not entries


def test_read_entry_of_a_plain_text_file_is_the_text(tmp_path):
    (tmp_path / "e.txt").write_text("The `limit` parameter now defaults to 20.\n")
    assert "`limit`" in et.read_entry(tmp_path / "e.txt")


def test_sentences_splits_on_terminators_and_list_items():
    text = "The `a` field is now required. The `b` field was renamed.\n* The `c` value was removed\n"
    got = et.sentences(text)
    assert len(got) == 3
    assert got[0].startswith("The `a`") and got[2].startswith("The `c`")
    assert all(s == s.strip() for s in got)


def test_identifiers_reads_backticked_and_quoted_names_only():
    text = 'The `per_page` and "sort_by" fields changed, but not the word field or `two words`.'
    assert et.identifiers(text) == ["per_page", "sort_by"]
