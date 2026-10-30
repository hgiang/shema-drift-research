#!/usr/bin/env python3
"""Build the Phase-3 corpus from the archive (`phase3/PLAN.md` Task 3).

Entries are read in the order `sampling.draw_order` fixed and recorded in each source's
`<source>.fetch.json`, so the sample can be rebuilt from the archive alone. Coding stops
when a source reaches its cap of qualifying units, and it stops on a whole entry: cutting an
entry in half would drop one of its parameters for no reason but arrival order.

Deterministic by construction — the same archive gives the same `corpus.jsonl` byte for
byte. Nothing here reaches the network, and archived pages are only ever read as text.

Usage:
  python3 phase3/code_changes.py                      # all four sources, cap 60
  python3 phase3/code_changes.py --source stripe --cap 10 --out /tmp/pilot.jsonl
"""

import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import drift_rules as dr  # noqa: E402
import entry_text as et  # noqa: E402
import web_archive as wa  # noqa: E402

ARCHIVE = HERE.parent / "results" / "phase3" / "sources"
CORPUS = HERE.parent / "results" / "phase3" / "corpus.jsonl"
SUMMARY = HERE.parent / "results" / "phase3" / "corpus_summary.json"
CAP = 60
SOURCES = ("github", "mcp", "slack", "stripe")
FIELDS = ("unit_id", "source", "entry_url", "entry_path", "draw_rank", "scope", "parameter",
          "label", "classes", "rule", "agent_visible", "evidence")
_HEADING = re.compile(r"^#{1,3}\s+(.+?)\s*$|^Subject:\s*(?:\[PATCH\]\s*)?(.+?)\s*$", re.M)
_SLUG = re.compile(r"[^a-z0-9]+")


def _scope(text, url):
    """The entry's own heading, which is as close to "the endpoint" as a changelog gets."""
    match = _HEADING.search(text)
    if match:
        return (match.group(1) or match.group(2)).strip()
    return url.rstrip("/").rsplit("/", 1)[-1]


def _unit_id(source, rank, scope, parameter):
    return f"{source}:{rank:03d}:{_SLUG.sub('-', scope.lower()).strip('-')[:40]}:{parameter}"


def _fetch_report(root, source):
    path = pathlib.Path(root) / f"{source}.fetch.json"
    if not path.exists():
        raise SystemExit(f"no fetch report for {source}: run phase3/fetch_sources.py first")
    return json.loads(path.read_text())


def _entry_paths(root, source):
    """(draw_rank, url, path) for the drawn entries that were archived, in the drawn order."""
    report, manifest = _fetch_report(root, source), wa.load_manifest(root, source)
    folder = wa.archive_path(root, source, 0, "x").parent
    out = []
    for rank, url in enumerate(report["drawn"]):
        entry = manifest.get(url)
        if entry:
            out.append((rank, url, folder / entry["path"]))
    return out


def _code(root, source, cap):
    """(units, entries read). Entries read is the denominator of the hit rate, so it counts
    every entry opened before the cap stopped the source, not only the ones that yielded."""
    units, read = [], 0
    for rank, url, path in _entry_paths(root, source):
        if len(units) >= cap:
            break
        read += 1
        text = et.read_entry(path)
        if not text:
            continue
        scope = _scope(text, url)
        for unit in dr.units_of_entry(text):
            units.append({"unit_id": _unit_id(source, rank, scope, unit["parameter"]),
                          "source": source, "entry_url": url, "entry_path": path.name,
                          "draw_rank": rank, "scope": scope, **unit})
    return units, read


def code_source(root, source, cap=CAP):
    """Code one source's drawn entries until it reaches `cap` qualifying units."""
    return _code(root, source, cap)[0]


def _counts(units):
    labels = {}
    for unit in units:
        labels[unit["label"]] = labels.get(unit["label"], 0) + 1
    return {label: labels.get(label, 0) for label in dr.LABELS if labels.get(label)}


def write_corpus(root, out, sources=SOURCES, cap=CAP, summary_path=None):
    """Write `corpus.jsonl` sorted by unit id, and return the per-source summary."""
    rows, summary = [], {}
    for source in sorted(sources):
        units, read = _code(root, source, cap)
        report = _fetch_report(root, source)
        summary[source] = {"n_units": len(units), "n_entries_read": read,
                           "n_entries_with_units": len({u["draw_rank"] for u in units}),
                           "n_entries_drawn": len(report["drawn"]),
                           "n_enumerated": report["n_enumerated"],
                           "cap": cap, "reached_cap": len(units) >= cap, "labels": _counts(units)}
        rows += units
    rows.sort(key=lambda r: r["unit_id"])
    pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(out).write_text("".join(
        json.dumps({k: r[k] for k in FIELDS}, sort_keys=False) + "\n" for r in rows))
    if summary_path:
        pathlib.Path(summary_path).write_text(json.dumps(summary, indent=1) + "\n")
    return summary


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", choices=SOURCES, action="append")
    ap.add_argument("--cap", type=int, default=CAP)
    ap.add_argument("--root", type=pathlib.Path, default=ARCHIVE)
    ap.add_argument("--out", type=pathlib.Path, default=CORPUS)
    ap.add_argument("--summary", type=pathlib.Path, default=SUMMARY)
    args = ap.parse_args(argv)
    summary = write_corpus(args.root, args.out, args.source or SOURCES, args.cap, args.summary)
    total = sum(s["n_units"] for s in summary.values())
    for source, s in summary.items():
        print(f"{source:8s} units {s['n_units']:4d}  from {s['n_entries_read']:3d}/"
              f"{s['n_entries_drawn']:3d} entries  cap {'hit' if s['reached_cap'] else 'not hit'}"
              f"  {s['labels']}")
    print(f"total {total} units -> {args.out}")


if __name__ == "__main__":
    main()
