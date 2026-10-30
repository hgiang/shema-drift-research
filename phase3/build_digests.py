#!/usr/bin/env python3
"""Build the digests the two blind coders read (MILESTONES.md "Phase 3 amendment 1").

A digest is one archived entry, reduced to the spans that could describe a request-parameter
change, with the identifiers each span names. It carries **no label and no `agent_visible`**,
and it never mentions a prediction: the coders must not be able to guess what the study hopes
to find.

`drift_rules` is used here only to propose candidate spans. It proposes; the coders decide.

Deterministic — the same archive gives the same `digests.jsonl` byte for byte.

Usage:
  python3 phase3/build_digests.py                       # all four sources
  python3 phase3/build_digests.py --source stripe --max-entries 10 --out /tmp/d.jsonl
"""

import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import code_changes as cc  # noqa: E402
import drift_rules as dr  # noqa: E402
import entry_text as et  # noqa: E402

DIGESTS = HERE.parent / "results" / "phase3" / "digests.jsonl"
SUMMARY = HERE.parent / "results" / "phase3" / "digests_summary.json"
DIGEST_FIELDS = ("digest_id", "source", "entry_url", "entry_path", "draw_rank", "scope",
                 "candidates")
MAX_SPANS = 12
MAX_SPAN_CHARS = 400
MAX_ENTRIES = 60
# Phase 3 amendment 2: an index page is normally an enumeration, but GitHub publishes its own
# list of REST schema changes, which is an entry in its own right. It is coded at rank -1.
CODEABLE_INDEX = {
    "github": ("https://docs.github.com/en/rest/about-the-rest-api/breaking-changes",),
    "stripe": (), "slack": (), "mcp": (),
}
# A patch hunk is worth reading only when it touches a schema, not any line of code.
_SCHEMA_CUE = re.compile(r"\b(inputSchema|outputSchema|jsonSchema|zodToJsonSchema|z\.[a-z]|"
                         r"required|properties|parameters|\.optional\(|\.default\(|"
                         r"type\s*:\s*[\"']?(string|number|integer|boolean|array|object))", re.I)


_CODE_IDENT = re.compile(r"^\s*[\"\']?([A-Za-z_][A-Za-z0-9_]*)[\"\']?\s*[:=]")
_CODE_LINE = re.compile(r"[{};]|=>|\bconst\b|\bimport\b|\breturn\b")


def _schema_lines(text):
    """`from_patch` already dropped doc hunks and the +/- markers; most of what is left is
    still unrelated code, so keep the subject line and the lines that touch a schema."""
    return "\n".join(line for line in text.splitlines()
                     if not _CODE_LINE.search(line) and not _CODE_IDENT.match(line)
                     or _SCHEMA_CUE.search(line))


def _code_identifiers(span):
    """A changed schema line names its parameter as `name:` or `name =`, not in backticks."""
    found = _CODE_IDENT.match(span)
    return [found.group(1)] if found else []


def candidates(text, is_patch=False):
    """Spans that could describe a request-parameter change, with the names they mention."""
    body = _schema_lines(text) if is_patch else text
    out = []
    for span in et.sentences(body):
        names = dr.parameters_in(span) or (_code_identifiers(span) if is_patch else [])
        if names and dr.qualifies(span, names):
            out.append({"span": span[:MAX_SPAN_CHARS], "identifiers": names})
        if len(out) >= MAX_SPANS:
            break
    return out


def _codeable_index_entries(root, source):
    """(rank -1, url, path) for the index pages this source declares to be real entries."""
    import web_archive as wa
    manifest = wa.load_manifest(root, source)
    folder = wa.archive_path(root, source, 0, "x").parent
    return [(-1, url, folder / manifest[url]["path"])
            for url in CODEABLE_INDEX.get(source, ()) if url in manifest]


def digests_for(root, source, max_entries=MAX_ENTRIES):
    """One digest per entry that has at least one candidate span, in the drawn order."""
    out = []
    entries = _codeable_index_entries(root, source) + cc._entry_paths(root, source)[:max_entries]
    for rank, url, path in entries:
        text = et.read_entry(path)
        if not text:
            continue
        found = candidates(text, is_patch=path.suffix in (".patch", ".diff"))
        if not found:
            continue
        scope = cc._scope(text, url)
        out.append({"digest_id": f"{source}:{rank:03d}" if rank >= 0 else f"{source}:index", "source": source, "entry_url": url,
                    "entry_path": path.name, "draw_rank": rank, "scope": scope,
                    "candidates": found})
    return out


def write_digests(root, out, sources=cc.SOURCES, max_entries=MAX_ENTRIES, summary_path=None):
    rows, summary = [], {}
    for source in sorted(sources):
        read = len(cc._entry_paths(root, source)[:max_entries]) + len(_codeable_index_entries(root, source))
        found = digests_for(root, source, max_entries)
        summary[source] = {"n_entries_read": read, "n_digests": len(found),
                           "n_candidates": sum(len(d["candidates"]) for d in found)}
        rows += found
    rows.sort(key=lambda r: r["digest_id"])
    pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(out).write_text("".join(
        json.dumps({k: r[k] for k in DIGEST_FIELDS}) + "\n" for r in rows))
    if summary_path:
        pathlib.Path(summary_path).write_text(json.dumps(summary, indent=1) + "\n")
    return summary


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", choices=cc.SOURCES, action="append")
    ap.add_argument("--max-entries", type=int, default=MAX_ENTRIES)
    ap.add_argument("--root", type=pathlib.Path, default=cc.ARCHIVE)
    ap.add_argument("--out", type=pathlib.Path, default=DIGESTS)
    ap.add_argument("--summary", type=pathlib.Path, default=SUMMARY)
    args = ap.parse_args(argv)
    summary = write_digests(args.root, args.out, args.source or cc.SOURCES,
                            args.max_entries, args.summary)
    for source, s in summary.items():
        print(f"{source:8s} entries {s['n_entries_read']:3d}  digests {s['n_digests']:3d}  "
              f"candidate spans {s['n_candidates']:4d}")
    print(f"total {sum(s['n_digests'] for s in summary.values())} digests -> {args.out}")


if __name__ == "__main__":
    main()
