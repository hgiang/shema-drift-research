#!/usr/bin/env python3
"""Run one blind coder over the Phase-3 digests (MILESTONES.md "Phase 3 amendment 1").

Two coders, neither of which has seen the predictions:
  --coder codex    `codex exec`, read-only sandbox, run in an empty directory, prompt on stdin
  --coder sonnet   Claude Sonnet 5.5 on OpenRouter, provider `anthropic` pinned, temperature 0

Both read the same digests and the same guide, and both write the same shape:
`results/phase3/labels_<coder>.jsonl`. Raw answers are archived beside it, so a coder's
output can be re-parsed without paying for it again. Resume-safe: a batch already answered
is not sent a second time.

Usage:
  python3 phase3/run_coder.py --coder codex
  python3 phase3/run_coder.py --coder sonnet --cap 2 --limit 2    # pilot
"""

import argparse
import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "experiments"))
import coding_guide as cg  # noqa: E402

PHASE3 = HERE.parent / "results" / "phase3"
DIGESTS = PHASE3 / "digests.jsonl"
BATCH = 6
SONNET = "anthropic/claude-sonnet-5.5"
MAX_TOKENS = 4000
CODEX_MODEL = "gpt-6-sol"
CODERS = ("codex", "sonnet")


def load_digests(path=DIGESTS):
    return [json.loads(line) for line in pathlib.Path(path).read_text().splitlines() if line.strip()]


def batches(digests, size=BATCH):
    return [digests[i:i + size] for i in range(0, len(digests), size)]


def call_codex(prompt, model=CODEX_MODEL):
    """Non-interactive Codex in a throwaway empty directory; it may read nothing on disk."""
    with tempfile.TemporaryDirectory() as empty:
        done = subprocess.run(
            ["codex", "exec", "--sandbox", "read-only", "--model", model, "-"],
            input=prompt, capture_output=True, text=True, cwd=empty, timeout=900)
    if done.returncode != 0:
        raise RuntimeError(f"codex exec failed: {done.stderr[-400:]}")
    return done.stdout


def call_sonnet(prompt, model=SONNET):
    """One pinned OpenRouter call, temperature 0, no fallbacks. Returns (text, usage)."""
    import run_openrouter as ro
    from cost_tracker import check_budget, log_cost
    check_budget()
    body = {"model": model, "temperature": 0, "max_tokens": MAX_TOKENS,
            "messages": [{"role": "user", "content": prompt}],
            "provider": {"order": ["anthropic"], "allow_fallbacks": False}}
    resp = ro.or_call(model, body)
    text = ((resp.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
    log_cost(model, "p3-coder-sonnet", resp.get("usage") or {}, phase="phase3")
    return text


def _answers_path(coder):
    return PHASE3 / f"coder_{coder}_answers.jsonl"


def _done_batches(path):
    if not path.exists():
        return {}
    return {row["batch"]: row for row in
            (json.loads(line) for line in path.read_text().splitlines() if line.strip())}


def run(coder, digests, caller, answers_path=None, limit=None):
    """Send each unanswered batch, archive the raw answer, and return (units, problems)."""
    answers_path = answers_path or _answers_path(coder)
    done = _done_batches(answers_path)
    groups = batches(digests)[:limit] if limit else batches(digests)
    units, problems = [], []
    for i, batch in enumerate(groups):
        if i not in done:
            answer = caller(cg.prompt_for(batch))
            answers_path.parent.mkdir(parents=True, exist_ok=True)
            with answers_path.open("a") as f:
                f.write(json.dumps({"batch": i, "digest_ids": [d["digest_id"] for d in batch],
                                    "answer": answer}) + "\n")
            done[i] = {"batch": i, "answer": answer}
        got, bad = cg.parse(done[i]["answer"], batch)
        units += got
        problems += [f"batch {i}: {p}" for p in bad]
    return units, problems


def write_labels(coder, units, out=None):
    out = out or PHASE3 / f"labels_{coder}.jsonl"
    rows = sorted(units, key=lambda u: (u["digest_id"], u["parameter"]))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(u) + "\n" for u in rows))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--coder", choices=CODERS, required=True)
    ap.add_argument("--digests", type=pathlib.Path, default=DIGESTS)
    ap.add_argument("--limit", type=int, help="send only the first N batches (pilot)")
    args = ap.parse_args(argv)
    digests = load_digests(args.digests)
    caller = call_codex if args.coder == "codex" else call_sonnet
    units, problems = run(args.coder, digests, caller, limit=args.limit)
    out = write_labels(args.coder, units)
    print(f"{args.coder}: {len(units)} units from {len(digests)} digests -> {out}")
    for p in problems:
        print("  PROBLEM:", p)


if __name__ == "__main__":
    main()
