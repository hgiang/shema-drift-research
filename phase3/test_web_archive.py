#!/usr/bin/env python3
"""Tests for the Phase-3 web archive: path safety, manifests, resume and pacing.

Nothing here touches the network; the getter is always injected.

Run: python3 -m pytest phase3/test_web_archive.py -q
"""

import json
import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import web_archive as wa  # noqa: E402

HOSTILE = [
    "https://x.test/../../etc/passwd",
    "https://x.test/a/../../../../../../tmp/evil",
    "https://x.test/%2e%2e%2f%2e%2e%2fetc/passwd",
    "https://x.test/a\x00b",
    "https://x.test/" + "n" * 500,
    "https://x.test/~/.ssh/id_rsa",
]


def test_slug_is_filesystem_safe_and_stable():
    for url in HOSTILE:
        s = wa.slug(url)
        assert s == wa.slug(url)
        assert s and "/" not in s and "\\" not in s and ".." not in s
        assert "\x00" not in s and len(s) <= wa.SLUG_MAX
        assert all(c.isalnum() or c in "._-" for c in s)


def test_archive_path_never_escapes_the_root(tmp_path):
    root = tmp_path / "sources"
    for i, url in enumerate(HOSTILE):
        p = wa.archive_path(root, "stripe", i, url)
        assert root.resolve() in p.resolve().parents


def test_archive_path_is_unique_per_index_and_keeps_a_safe_extension(tmp_path):
    root = tmp_path / "sources"
    a = wa.archive_path(root, "slack", 0, "https://d.test/changelog/x.md")
    b = wa.archive_path(root, "slack", 1, "https://d.test/changelog/x.md")
    assert a != b and a.suffix == ".md" and b.suffix == ".md"
    assert wa.archive_path(root, "s", 0, "https://d.test/a.exe").suffix == wa.FALLBACK_EXT
    assert wa.archive_path(root, "s", 0, "https://d.test/a").suffix == wa.FALLBACK_EXT
    assert wa.archive_path(root, "s", 0, "https://api.test/x.json").suffix == ".json"


def test_store_writes_the_bytes_verbatim_and_returns_a_manifest_entry(tmp_path):
    body = b"# Changelog\n\xe2\x80\x94 em dash\n"
    entry = wa.store(tmp_path, "stripe", 3, "https://d.test/c.md", body, 200, now="2026-10-30T00:00:00Z")
    p = tmp_path / "stripe" / entry["path"]
    assert p.read_bytes() == body
    assert entry["url"] == "https://d.test/c.md" and entry["status"] == 200
    assert entry["sha256"] == wa.sha256_bytes(body) and entry["fetched_at"] == "2026-10-30T00:00:00Z"
    assert entry["n_bytes"] == len(body)


def test_manifest_round_trips_and_is_byte_stable(tmp_path):
    entries = {"https://b.test/2": {"path": "001-b.md"}, "https://a.test/1": {"path": "000-a.md"}}
    wa.save_manifest(tmp_path, "slack", entries)
    first = (tmp_path / "slack" / wa.MANIFEST).read_bytes()
    assert wa.load_manifest(tmp_path, "slack") == entries
    wa.save_manifest(tmp_path, "slack", dict(reversed(list(entries.items()))))
    assert (tmp_path / "slack" / wa.MANIFEST).read_bytes() == first
    assert list(json.loads(first)) == sorted(entries)


def test_load_manifest_is_empty_for_an_unfetched_source(tmp_path):
    assert wa.load_manifest(tmp_path, "nothing-here") == {}


def test_needs_fetch_is_false_only_when_the_stored_file_still_matches(tmp_path):
    url, body = "https://d.test/c.md", b"hello"
    assert wa.needs_fetch(tmp_path, "stripe", {}, url) is True
    entry = wa.store(tmp_path, "stripe", 0, url, body, 200, now="t")
    manifest = {url: entry}
    assert wa.needs_fetch(tmp_path, "stripe", manifest, url) is False
    (tmp_path / "stripe" / entry["path"]).write_bytes(b"tampered")
    assert wa.needs_fetch(tmp_path, "stripe", manifest, url) is True
    (tmp_path / "stripe" / entry["path"]).unlink()
    assert wa.needs_fetch(tmp_path, "stripe", manifest, url) is True


ROBOTS = """
User-agent: BadBot
Disallow: /

User-agent: *
Disallow: /private
Disallow: /go/
Allow: /
"""


def test_robots_allows_reads_only_the_star_section():
    assert wa.robots_allows(ROBOTS, "/changelog") is True
    assert wa.robots_allows(ROBOTS, "/private/thing") is False
    assert wa.robots_allows(ROBOTS, "/go/x") is False
    assert wa.robots_allows("User-agent: *\nDisallow:\n", "/anything") is True
    assert wa.robots_allows("User-agent: *\nDisallow: /\n", "/anything") is False
    assert wa.robots_allows("", "/anything") is True


def test_pacer_spaces_requests_by_at_least_the_minimum():
    clock, slept = [0.0], []

    def sleep(s):
        slept.append(s)
        clock[0] += s

    pacer = wa.Pacer(min_interval=1.0, clock=lambda: clock[0], sleep=sleep)
    pacer.wait()
    assert slept == []          # the first request waits for nothing
    pacer.wait()
    assert slept and slept[0] == pytest.approx(1.0)
    clock[0] += 5.0
    pacer.wait()
    assert len(slept) == 1      # already past the interval


def test_fetch_one_skips_a_disallowed_path_without_calling_the_getter(tmp_path):
    calls = []

    def getter(url):
        calls.append(url)
        return 200, b"x"

    out = wa.fetch_one(tmp_path, "slack", 0, "https://d.test/private/x", getter,
                       allows=lambda path: not path.startswith("/private"))
    assert out is None and calls == []


def test_fetch_one_stores_and_then_resumes_without_a_second_get(tmp_path):
    calls = []

    def getter(url):
        calls.append(url)
        return 200, b"body"

    url = "https://d.test/c.md"
    first = wa.fetch_one(tmp_path, "stripe", 0, url, getter, now="t")
    manifest = wa.load_manifest(tmp_path, "stripe")
    assert manifest == {url: first} and len(calls) == 1
    again = wa.fetch_one(tmp_path, "stripe", 0, url, getter, now="t2")
    assert again == first and len(calls) == 1


def test_fetch_one_does_not_store_a_failed_response(tmp_path):
    out = wa.fetch_one(tmp_path, "stripe", 0, "https://d.test/x.md", lambda u: (404, b"nope"), now="t")
    assert out is None
    assert wa.load_manifest(tmp_path, "stripe") == {}
    assert not (tmp_path / "stripe").exists() or not any((tmp_path / "stripe").glob("*.md"))


def test_archive_path_does_not_double_the_extension(tmp_path):
    for url, want in (("https://d.test/changelog.md", ".md"),
                      ("https://d.test/changelog-sitemap.xml", ".xml"),
                      ("https://d.test/a/b.json", ".json")):
        p = wa.archive_path(tmp_path, "s", 0, url)
        assert p.suffix == want and not p.stem.endswith(want)
