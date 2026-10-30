#!/usr/bin/env python3
"""Turn one archived Phase-3 page into text a coding rule can read.

The three archived formats need three readers: Stripe and Slack serve markdown, GitHub blog
posts are full HTML pages, and MCP entries are git patches. Each reader keeps the words that
carry a schema change and drops the furniture; `<code>` spans become backticks so one
identifier rule works across all three.

Archived pages are untrusted data. Nothing here evaluates, imports or executes what it
reads; a page is only ever text.
"""

import html
import re

_SCRIPT = re.compile(r"<(script|style|svg|noscript)\b.*?</\1>", re.S | re.I)
_CODE = re.compile(r"<code\b[^>]*>(.*?)</code>", re.S | re.I)
_TAG = re.compile(r"<[^>]+>")
_BLANKS = re.compile(r"[ \t]*\n[ \t]*")
_FRONT_MATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
_SENTENCE = re.compile(r"(?<=[.!?])\s+|\n+")
_IDENT = re.compile(r"`([A-Za-z_][A-Za-z0-9_.\[\]-]*)`|\"([A-Za-z_][A-Za-z0-9_.-]*)\"")
_CODE_FILE = re.compile(r"\.(ts|tsx|js|jsx|py|go|rs|java|kt|rb|json|ya?ml|proto)$", re.I)
_DIFF_HEADER = re.compile(r"^diff --git a/(\S+) b/\S+", re.M)


def from_html(page):
    """Visible text of an HTML page, with `<code>` spans marked by backticks."""
    body = _SCRIPT.sub(" ", page)
    body = _CODE.sub(lambda m: f"`{_TAG.sub('', m.group(1)).strip()}`", body)
    return _BLANKS.sub("\n", html.unescape(_TAG.sub(" ", body))).strip()


def from_markdown(page):
    """Markdown as written, without the front matter the docs sites prepend."""
    return _FRONT_MATTER.sub("", page).strip()


def _patch_message(patch):
    head = patch.split("\ndiff --git ", 1)[0]
    head = head.split("\n---\n", 1)[0]
    return re.sub(r"^(From|Date|Subject:?)\b.*$", lambda m: m.group(0).removeprefix("Subject: "),
                  head, flags=re.M)


def from_patch(patch):
    """The commit message plus the changed lines of code files only.

    A changelog unit has to come from a schema, so README and documentation hunks are
    dropped; `index`, `@@` and file-header lines carry no wording and are dropped too.
    """
    out = [_patch_message(patch).strip()]
    parts = _DIFF_HEADER.split(patch)
    for path, body in zip(parts[1::2], parts[2::2]):
        if not _CODE_FILE.search(path):
            continue
        out += [line[1:].strip() for line in body.splitlines()
                if line[:1] in "+-" and not line.startswith(("+++", "---")) and line[1:].strip()]
    return "\n".join(x for x in out if x).strip()


def read_entry(path):
    """Read one archived file as text, choosing the reader from its stored name and content."""
    text = path.read_text(errors="replace")
    if path.suffix in (".patch", ".diff"):
        return from_patch(text)
    if path.suffix in (".json", ".xml"):
        return ""                                   # index pages, not entries
    if path.suffix in (".html", ".htm") or text.lstrip()[:400].lower().startswith("<!doctype"):
        return from_html(text)
    return from_markdown(text)


def sentences(text):
    """Codeable spans: sentences, list items and changed lines, trimmed, in order."""
    return [s.strip(" \t*-+") for s in _SENTENCE.split(text) if s.strip(" \t*-+")]


def identifiers(span):
    """Parameter-like names: backticked or double-quoted single tokens, in order, deduped."""
    out = []
    for backticked, quoted in _IDENT.findall(span):
        name = backticked or quoted
        if name and name not in out:
            out.append(name)
    return out
