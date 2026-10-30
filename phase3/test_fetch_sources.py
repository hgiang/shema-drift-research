#!/usr/bin/env python3
"""Tests for the Phase-3 source enumerators and the pre-registered draw order.

Fixtures are hand-written excerpts in this file; nothing here touches the network.

Run: python3 -m pytest phase3/test_fetch_sources.py -q
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fetch_sources as fs  # noqa: E402
import sampling  # noqa: E402

STRIPE_INDEX = """# Changelog

# Endive
## 2026-09-28.preview

### Payments

| Title | Affected Products | Breaking change? | Category |
| --- | --- | --- | --- |
| [Adds Wero](https://docs.stripe.com/changelog/endive/2026-09-28/wero.md) | Payments | Non-breaking | api |
| [Renames wire to fedwire](https://docs.stripe.com/changelog/endive/2026-09-28/fedwire.md) | All | Non-breaking | api |

# 2022
## 2022-11-15

| Title | Affected Products | Breaking change? | Category |
| --- | --- | --- | --- |
| [Too old](https://docs.stripe.com/changelog/2022-11-15/old.md) | All | Breaking | api |

# 2024
## 2024-06-20

| Title | Affected Products | Breaking change? | Category |
| --- | --- | --- | --- |
| [In window](https://docs.stripe.com/changelog/2024-06-20/mid.md) | Billing | Breaking | api |
| [Not markdown](https://docs.stripe.com/changelog/2024-06-20/mid) | Billing | Breaking | api |
"""

SLACK_SITEMAP = """- https://docs.slack.dev/quickstart.md
- https://docs.slack.dev/changelog.md
- https://docs.slack.dev/changelog/tags/new-feature.md
- https://docs.slack.dev/changelog/2016-05-17-changes-to-errors.md
- https://docs.slack.dev/changelog/2024/03/08/scopes-tightened.md
- https://docs.slack.dev/changelog/2025-11-02-new-required-field.md
"""

GITHUB_SITEMAP = """<?xml version="1.0"?>
<urlset>
<url><loc>https://github.blog/changelog/</loc></url>
<url><loc>https://github.blog/changelog/2024-01-30-actions-macos-14</loc></url>
<url><loc>https://github.blog/changelog/2022-12-04-too-old</loc></url>
<url><loc>https://github.blog/changelog/2026-02-11-rest-api-parameter-required</loc></url>
</urlset>
"""

MCP_COMMITS = json.dumps([
    {"sha": "a" * 40, "commit": {"committer": {"date": "2024-05-02T10:00:00Z"}}},
    {"sha": "b" * 40, "commit": {"committer": {"date": "2021-01-02T10:00:00Z"}}},
])


def test_in_window_uses_the_locked_dates():
    assert fs.WINDOW == ("2023-01-01", "2026-09-30")
    assert fs.in_window("2023-01-01") and fs.in_window("2026-09-30")
    assert not fs.in_window("2022-12-31") and not fs.in_window("2026-10-01")


def test_stripe_entries_takes_markdown_rows_under_their_version_date():
    got = fs.stripe_entries(STRIPE_INDEX)
    assert ("2024-06-20", "https://docs.stripe.com/changelog/2024-06-20/mid.md") in got
    assert all(u.endswith(".md") for _, u in got)
    assert [d for d, _ in got] == sorted(d for d, _ in got)          # deterministic order
    assert all(fs.in_window(d) for d, _ in got)                      # 2022 row dropped
    assert len(got) == 3                                             # 2 Endive + 1 in 2024


def test_slack_entries_reads_both_date_shapes_and_skips_tags_and_the_index():
    got = fs.slack_entries(SLACK_SITEMAP)
    assert got == [("2024/03/08".replace("/", "-"),
                    "https://docs.slack.dev/changelog/2024/03/08/scopes-tightened.md"),
                   ("2025-11-02",
                    "https://docs.slack.dev/changelog/2025-11-02-new-required-field.md")]


def test_github_entries_reads_the_date_from_the_slug():
    got = fs.github_entries(GITHUB_SITEMAP)
    assert got == [("2024-01-30", "https://github.blog/changelog/2024-01-30-actions-macos-14"),
                   ("2026-02-11", "https://github.blog/changelog/2026-02-11-rest-api-parameter-required")]


def test_mcp_entries_turns_commits_into_patch_urls():
    got = fs.mcp_entries([MCP_COMMITS])
    assert got == [("2024-05-02", f"https://github.com/{fs.MCP_REPO}/commit/{'a' * 40}.patch")]


def test_every_locked_source_has_an_index_and_an_enumerator():
    assert set(fs.SOURCES) == {"stripe", "slack", "github", "mcp"}
    for name, spec in fs.SOURCES.items():
        assert spec["index"] and callable(spec["enumerate"])
        assert all(u.startswith("https://") for u in spec["index"])


def test_draw_order_is_a_fixed_permutation_of_the_whole_list():
    entries = [(f"2024-01-{i:02d}", f"https://d.test/{i}") for i in range(1, 21)]
    first = sampling.draw_order(entries, "stripe")
    assert sorted(first) == sorted(entries)
    assert first == sampling.draw_order(list(reversed(entries)), "stripe")   # input order cannot matter
    assert first != entries                                                  # it really shuffles
    assert sampling.draw_order(entries, "slack") != first                    # per-source stream


def test_draw_order_is_stable_as_the_enumeration_grows_at_the_end():
    assert sampling.SEED_P3 == 20261030
    small = [(f"2024-01-{i:02d}", f"https://d.test/{i}") for i in range(1, 6)]
    assert sampling.draw_order(small, "mcp") == sampling.draw_order(list(reversed(small)), "mcp")


def test_fetch_source_fetches_the_index_then_the_drawn_entries(tmp_path):
    calls = []

    def getter(url):
        calls.append(url)
        return (200, STRIPE_INDEX.encode()) if url in fs.SOURCES["stripe"]["index"] else (200, b"entry")

    out = fs.fetch_source(tmp_path, "stripe", getter=getter, pacer=None, allows=None,
                          max_entries=2, now="t")
    assert out["n_enumerated"] == 3 and out["n_fetched"] == 2
    assert calls[0] in fs.SOURCES["stripe"]["index"] and len(calls) == 3
    assert out["drawn"] == [u for _, u in sampling.draw_order(fs.stripe_entries(STRIPE_INDEX), "stripe")][:2]
    manifest = fs.wa.load_manifest(tmp_path, "stripe")
    assert set(out["drawn"]) <= set(manifest)


def test_fetch_source_resumes_without_refetching(tmp_path):
    def getter(url):
        getter.n += 1
        return (200, STRIPE_INDEX.encode()) if url in fs.SOURCES["stripe"]["index"] else (200, b"entry")
    getter.n = 0

    kw = dict(getter=getter, pacer=None, allows=None, max_entries=2, now="t")
    fs.fetch_source(tmp_path, "stripe", **kw)
    first = getter.n
    fs.fetch_source(tmp_path, "stripe", **kw)
    assert getter.n == first


def test_allows_for_reads_robots_once_for_the_host_and_paces_it():
    got, waits = [], []

    def getter(url):
        got.append(url)
        return 200, b"User-agent: *\nDisallow: /private\n"

    allows = fs._allows_for("https://docs.stripe.com/changelog.md", getter,
                            pacer=type("P", (), {"wait": lambda self: waits.append(1)})())
    assert got == ["https://docs.stripe.com/robots.txt"] and waits == [1]
    assert allows("/changelog") is True and allows("/private/x") is False


def test_allows_for_allows_everything_when_robots_is_missing():
    assert fs._allows_for("https://d.test/x", lambda u: (404, b""), pacer=None)("/anything") is True


def test_report_writes_a_summary_file(tmp_path, capsys):
    fs._report(tmp_path, {"source": "slack", "n_enumerated": 9, "n_drawn": 2, "n_fetched": 2})
    saved = json.loads((tmp_path / "slack.fetch.json").read_text())
    assert saved["n_enumerated"] == 9
    assert "slack" in capsys.readouterr().out


def test_main_dry_run_enumerates_and_archives_no_entry(tmp_path, monkeypatch, capsys):
    def getter(url):
        if url.endswith("/robots.txt"):
            return 200, b"User-agent: *\nAllow: /\n"
        return (200, STRIPE_INDEX.encode()) if url in fs.SOURCES["stripe"]["index"] else (200, b"e")

    monkeypatch.setattr(fs.wa, "http_get", getter)
    monkeypatch.setattr(fs.wa.Pacer, "wait", lambda self: None)
    fs.main(["--source", "stripe", "--root", str(tmp_path), "--dry-run"])
    summary = json.loads((tmp_path / "stripe.fetch.json").read_text())
    assert summary["n_enumerated"] == 3 and summary["n_drawn"] == 0 and summary["n_fetched"] == 0
    assert "enumerated" in capsys.readouterr().out


def test_main_needs_a_source():
    try:
        fs.main([])
    except SystemExit as e:
        assert e.code != 0
    else:
        raise AssertionError("main accepted no source")
