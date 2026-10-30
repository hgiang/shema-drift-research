#!/usr/bin/env python3
"""Phase-3 catalog arm runner (MILESTONES.md "Phase 3 amendment 4", `phase3/PLAN.md` Task 7).

One arm, two families, two catalog sizes. The model callers are the existing ones — Gemini
for Flash, OpenRouter for Haiku — so the only thing this arm changes is how many tool
declarations go into the prompt.

Usage:
  python3 run_phase3.py --model gemini-3.6-flash --cap 2 --limit 5        # pilot
  python3 run_phase3.py --model gemini-3.6-flash --cap 2
  python3 run_phase3.py --model anthropic/claude-haiku-5.5 --provider anthropic --cap 2
"""

import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import phase1_grid as p1  # noqa: E402
import phase3_grid as p3  # noqa: E402
from cost_tracker import check_budget, total_spend  # noqa: E402

GEMINI_PREFIX = "gemini-"


def is_gemini(model):
    return model.startswith(GEMINI_PREFIX)


def make_caller(args, tag_holder):
    """The family's existing call_model, plus the pin every record carries."""
    if is_gemini(args.model):
        import run_gemini as rg
        pin = {"provider": "google", "strict": None, "endpoint": "gemini",
               "quantization": None, "max_tokens": args.max_tokens}
        return rg.make_call_model(args.model, tag_holder, phase="phase3"), rg.THINKING[args.model], pin
    import run_openrouter as ro
    if not args.provider:
        raise SystemExit("an OpenRouter model needs --provider (one provider, no fallbacks)")
    pin = {"provider": args.provider, "strict": None, "endpoint": "openrouter",
           "quantization": args.quantization, "max_tokens": args.max_tokens}
    caller = ro.make_call_model(args.model, tag_holder, reasoning="default",
                                max_tokens=args.max_tokens, provider=args.provider,
                                phase="phase3", quantization=args.quantization)
    return caller, "default", pin


def run(args):
    out_path = p3.out_path(args.model, pilot=bool(args.limit))
    tag_holder = [""]
    caller, reasoning, pin = make_caller(args, tag_holder)
    trimmed = p1.repair_tail(out_path)
    if trimmed:
        print(f"repaired {out_path.name}: dropped a {trimmed}-byte partial last line")
    if p1.load_pins(out_path) - {p1.pin_id(pin)}:
        raise SystemExit(f"{out_path.name} was written with other request settings than {pin}")
    done = _done_keys(out_path)
    jobs = [j for j in p3.jobs() if p3.job_key(j) not in done]
    jobs = jobs[:args.limit] if args.limit else jobs
    print(f"{args.model}: {len(jobs)} episodes to run, {len(done)} already done -> {out_path.name}")
    started = total_spend()
    with out_path.open("a") as f:
        for i, job in enumerate(jobs, 1):
            check_budget()
            if args.cap and total_spend() - started >= args.cap:
                raise SystemExit(f"per-run cap ${args.cap} reached after {i - 1} episodes; "
                                 f"re-run with a higher --cap to continue (the file resumes)")
            tag_holder[0] = p3.tag(job, reasoning)
            rec = p3.run_episode(job, caller, args.model, reasoning, args.max_tokens, pin)
            f.write(json.dumps(rec) + "\n")
            f.flush()
            if i % 20 == 0 or i == len(jobs):
                print(f"  {i}/{len(jobs)}")


def _done_keys(out_path):
    if not out_path.exists():
        return set()
    out = set()
    for line in out_path.read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            out.add((r["task"], r["cond"], r["class"], r.get("catalog", "small")))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", required=True)
    ap.add_argument("--provider", help="OpenRouter provider to pin (no fallbacks)")
    ap.add_argument("--quantization")
    ap.add_argument("--max-tokens", type=int)
    ap.add_argument("--cap", type=float, help="per-run spend cap in USD (passed to the budget check)")
    ap.add_argument("--limit", type=int, help="pilot: run only the first N episodes, to *.pilot.jsonl")
    args = ap.parse_args(argv)
    if args.max_tokens is None:
        args.max_tokens = 1024 if is_gemini(args.model) else 700
    run(args)


if __name__ == "__main__":
    main()
