#!/usr/bin/env python3
"""Phase-3 changelog collection: enumerate the locked sources, then archive the drawn
entries verbatim (MILESTONES.md "Phase 3 pre-registration", `phase3/PLAN.md` Task 2).

Four sources, one entry point each, one window, one draw order per source. Every enumerator
is a pure function from archived index text to `[(date, url)]`, so it is tested on fixtures
and never needs the network. The archive itself is `web_archive`: untrusted bytes under one
root, with a per-source manifest.

Usage:
  python3 phase3/fetch_sources.py --source stripe --max-entries 40
  python3 phase3/fetch_sources.py --all --max-entries 40
  python3 phase3/fetch_sources.py --source mcp --max-entries 40 --dry-run
"""

import argparse
import json
import pathlib
import re
import sys
import urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import web_archive as wa  # noqa: E402
import sampling  # noqa: E402

ROOT = HERE.parent / "results" / "phase3" / "sources"
WINDOW = ("2023-01-01", "2026-09-30")
MCP_REPO = "modelcontextprotocol/servers"
MCP_PAGES = 10  # 100 commits each; the window is filtered after enumeration

_STRIPE_VERSION = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})")
_STRIPE_ROW = re.compile(r"^\|\s*\[[^\]]*\]\((https://docs\.stripe\.com/changelog/[^)]+\.md)\)")
_SLACK_URL = re.compile(r"https://docs\.slack\.dev/changelog/(\S+?\.md)")
_SLACK_DATE = re.compile(r"^(\d{4})[-/](\d{2})[-/](\d{2})[-/]")
_GH_LOC = re.compile(r"<loc>(https://github\.blog/changelog/(\d{4}-\d{2}-\d{2})-[^<]+)</loc>")


def in_window(date, window=WINDOW):
    return window[0] <= date[:10] <= window[1]


def _in_window_sorted(pairs):
    return sorted({p for p in pairs if in_window(p[0])})


def stripe_entries(index_text):
    """Rows of the changelog index, dated by the API-version heading they sit under."""
    date, out = None, []
    for line in index_text.splitlines():
        version = _STRIPE_VERSION.match(line)
        if version:
            date = version.group(1)
            continue
        row = _STRIPE_ROW.match(line)
        if row and date:
            out.append((date, row.group(1)))
    return _in_window_sorted(out)


def slack_entries(sitemap_text):
    """Changelog pages from the markdown sitemap; tag pages and the index are not entries."""
    out = []
    for tail in _SLACK_URL.findall(sitemap_text):
        if tail.startswith("tags/"):
            continue
        date = _SLACK_DATE.match(tail)
        if date:
            out.append(("-".join(date.groups()), f"https://docs.slack.dev/changelog/{tail}"))
    return _in_window_sorted(out)


def github_entries(sitemap_text):
    """Changelog posts from the changelog sitemap; the date is the first part of the slug."""
    return _in_window_sorted((date, url) for url, date in _GH_LOC.findall(sitemap_text))


def mcp_entries(pages):
    """Commits listed by the GitHub API, as patch URLs."""
    out = []
    for page in pages:
        for commit in json.loads(page):
            date = (commit.get("commit", {}).get("committer") or {}).get("date", "")
            if date and commit.get("sha"):
                out.append((date[:10], f"https://github.com/{MCP_REPO}/commit/{commit['sha']}.patch"))
    return _in_window_sorted(out)


SOURCES = {
    "stripe": {"index": ["https://docs.stripe.com/changelog.md"], "enumerate": stripe_entries},
    "slack": {"index": ["https://docs.slack.dev/llms-sitemap.md"], "enumerate": slack_entries},
    "github": {"index": ["https://github.blog/changelog-sitemap.xml",
                         "https://docs.github.com/en/rest/about-the-rest-api/breaking-changes"],
               "enumerate": github_entries},
    "mcp": {"index": [f"https://api.github.com/repos/{MCP_REPO}/commits?per_page=100&page={n}"
                      for n in range(1, MCP_PAGES + 1)], "enumerate": mcp_entries},
}


def _read_archived(root, source, entry):
    return (wa.archive_path(root, source, 0, "x").parent / entry["path"]).read_text(errors="replace")


def _fetch_index(root, source, getter, pacer, allows, now):
    """Archive every index page and return their texts, in the order `SOURCES` lists them."""
    texts = []
    for i, url in enumerate(SOURCES[source]["index"]):
        if pacer:
            pacer.wait()
        entry = wa.fetch_one(root, source, i, url, getter, allows, now)
        if entry:
            texts.append(_read_archived(root, source, entry))
    return texts


def _enumerate(source, texts):
    """Stripe, Slack and GitHub read one index; `mcp_entries` takes the list of pages."""
    fn = SOURCES[source]["enumerate"]
    return fn(texts) if source == "mcp" else _in_window_sorted(
        p for text in texts for p in fn(text))


def fetch_source(root, source, getter=wa.http_get, pacer=None, allows=None,
                 max_entries=60, now=None):
    """Archive the index, draw the entry order, then archive up to `max_entries` entries."""
    texts = _fetch_index(root, source, getter, pacer, allows, now)
    entries = _enumerate(source, texts)
    drawn = [url for _, url in sampling.draw_order(entries, source)][:max_entries]
    offset, fetched = len(SOURCES[source]["index"]), 0
    for i, url in enumerate(drawn):
        if pacer:
            pacer.wait()
        if wa.fetch_one(root, source, offset + i, url, getter, allows, now):
            fetched += 1
    return {"source": source, "window": list(WINDOW), "n_enumerated": len(entries),
            "n_drawn": len(drawn), "n_fetched": fetched, "drawn": drawn}


def _allows_for(url, getter, pacer):
    """One robots.txt per host, fetched before anything else on it."""
    parts = urllib.parse.urlsplit(url)
    if pacer:
        pacer.wait()
    status, body = getter(f"{parts.scheme}://{parts.netloc}/robots.txt")
    text = body.decode(errors="replace") if status == 200 else ""
    return lambda path: wa.robots_allows(text, path)


def _report(root, summary):
    path = pathlib.Path(root) / f"{summary['source']}.fetch.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=1) + "\n")
    print(f"{summary['source']:8s} enumerated {summary['n_enumerated']:5d}  "
          f"drawn {summary['n_drawn']:4d}  archived {summary['n_fetched']:4d}  -> {path}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", choices=sorted(SOURCES))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--max-entries", type=int, default=60)
    ap.add_argument("--root", type=pathlib.Path, default=ROOT)
    ap.add_argument("--dry-run", action="store_true", help="enumerate only; archive no entry")
    args = ap.parse_args(argv)
    names = sorted(SOURCES) if args.all else ([args.source] if args.source else [])
    if not names:
        ap.error("pass --source <name> or --all")
    pacer = wa.Pacer()
    for name in names:
        allows = _allows_for(SOURCES[name]["index"][0], wa.http_get, pacer)
        _report(args.root, fetch_source(args.root, name, wa.http_get, pacer, allows,
                                        0 if args.dry_run else args.max_entries))


if __name__ == "__main__":
    main()
