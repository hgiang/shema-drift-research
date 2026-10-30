#!/usr/bin/env python3
"""Build the agreed Phase-3 corpus (MILESTONES.md "Phase 3 amendment 1" and "amendment 2").

A unit enters the corpus when **both** blind coders returned it for the same digest and
parameter **and** gave it the same label. Everything else — a unit one coder found alone, or
a unit they labelled differently — stays out and is reported by `agreement.py`, so a
disagreement can never be resolved in the direction a prediction wants.

`agent_visible` is the one field where the coders may differ without losing the unit: the
disagreement is recorded as unknown and flagged, because the locked rule already allows
"neither is shown".

The locked cap of 60 units per source is applied in the draw order, which gives exactly the
corpus that stopping the coders at the cap would have given.

Usage:
  python3 phase3/build_corpus.py
"""

import argparse
import collections
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import agreement as ag  # noqa: E402

PHASE3 = HERE.parent / "results" / "phase3"
CAP = 60
FIELDS = ("unit_id", "source", "entry_url", "draw_rank", "scope", "parameter", "label",
          "agent_visible", "agent_visible_disputed")


def build(a, b, digests, cap=CAP):
    """Units both coders found and labelled the same, in draw order, capped per source."""
    index = {d["digest_id"]: d for d in digests}
    ia, ib = ag._index(a), ag._index(b)
    rows = []
    for key in sorted(set(ia) & set(ib)):
        ua, ub = ia[key], ib[key]
        if ua["label"] != ub["label"]:
            continue
        digest = index.get(key[0])
        if digest is None:
            continue
        disputed = ua["agent_visible"] != ub["agent_visible"]
        rows.append({"unit_id": f"{key[0]}:{key[1]}", "source": digest["source"],
                     "entry_url": digest["entry_url"], "draw_rank": digest["draw_rank"],
                     "scope": digest["scope"], "parameter": key[1], "label": ua["label"],
                     "agent_visible": None if disputed else ua["agent_visible"],
                     "agent_visible_disputed": disputed})
    rows.sort(key=lambda r: (r["source"], r["draw_rank"], r["parameter"]))
    kept, seen = [], collections.Counter()
    for row in rows:
        if seen[row["source"]] < cap:
            seen[row["source"]] += 1
            kept.append(row)
    return kept


def _block(rows):
    visible = collections.Counter("unknown" if r["agent_visible"] is None
                                  else str(r["agent_visible"]).lower() for r in rows)
    return {"n_units": len(rows),
            "n_entries": len({(r["source"], r["draw_rank"]) for r in rows}),
            "labels": dict(sorted(collections.Counter(r["label"] for r in rows).items())),
            "agent_visible": {k: visible.get(k, 0) for k in ("true", "false", "unknown")},
            "n_agent_visible_disputed": sum(r["agent_visible_disputed"] for r in rows)}


def summarise(rows):
    by_source = {s: _block([r for r in rows if r["source"] == s])
                 for s in sorted({r["source"] for r in rows})}
    return {"pooled": _block(rows), "by_source": by_source,
            "note": "pooled shares are source-weighted; read them next to by_source"}


def write(a, b, digests, out, summary_path=None, cap=CAP):
    rows = build(a, b, digests, cap)
    pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(out).write_text("".join(
        json.dumps({k: r[k] for k in FIELDS}) + "\n" for r in rows))
    summary = summarise(rows)
    if summary_path:
        pathlib.Path(summary_path).write_text(json.dumps(summary, indent=1) + "\n")
    return summary


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--a", type=pathlib.Path, default=PHASE3 / "labels_codex.jsonl")
    ap.add_argument("--b", type=pathlib.Path, default=PHASE3 / "labels_sonnet.jsonl")
    ap.add_argument("--digests", type=pathlib.Path, default=PHASE3 / "digests.jsonl")
    ap.add_argument("--out", type=pathlib.Path, default=PHASE3 / "corpus.jsonl")
    ap.add_argument("--summary", type=pathlib.Path, default=PHASE3 / "corpus_summary.json")
    ap.add_argument("--cap", type=int, default=CAP)
    args = ap.parse_args(argv)
    digests = [json.loads(line) for line in args.digests.read_text().splitlines() if line.strip()]
    summary = write(ag.load(args.a), ag.load(args.b), digests, args.out, args.summary, args.cap)
    print(f"corpus: {summary['pooled']['n_units']} units from "
          f"{summary['pooled']['n_entries']} entries -> {args.out}")
    for source, block in summary["by_source"].items():
        print(f"  {source:8s} {block['n_units']:3d} units  {block['labels']}")
    print(f"  pooled labels {summary['pooled']['labels']}")
    print(f"  agent_visible {summary['pooled']['agent_visible']} "
          f"(disputed {summary['pooled']['n_agent_visible_disputed']})")


if __name__ == "__main__":
    main()
