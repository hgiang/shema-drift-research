#!/usr/bin/env python3
"""OpenRouter GPT-family arm (primary set only; key has hard $5 cap, ~$0.83 left).
Patterns copied from script-bias repo run_openrouter_judge.py: temperature 0,
None-safe parsing, exponential backoff on 429, per-battery spend cap.

Usage:
  python3 run_openrouter.py --model openai/gpt-5.6-mini --limit 5   # dry run
  python3 run_openrouter.py --model openai/gpt-5.6-mini

Phase 1 (writes results/phase1/runs_<model>.jsonl; see phase1_grid.py):
  python3 run_openrouter.py --arm ablation --provider openai --cap 6 --limit 5   # pilot
  python3 run_openrouter.py --arm ablation --provider openai --cap 6
  python3 run_openrouter.py --arm noise --provider openai --cap 6
  python3 run_openrouter.py --arm infoform --provider openai --cap 6
  python3 run_openrouter.py --arm thinking --provider openai --reasoning high --cells C:sys:json:none,<best> --cap 6
  python3 run_openrouter.py --arm route --route <label> --provider <name> [--strict false] --cap 6
  Phase 1 needs --provider <name>: one OpenRouter provider, no fallbacks
  (MILESTONES.md "Phase 1 addendum"); --strict false sends "strict": false per tool.
"""

import argparse
import functools
import json
import pathlib
import random
import sys
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402
from cost_tracker import log_cost, check_budget  # noqa: E402

RESULTS = HERE.parent / "results"
ARM_CAP_USD = 0.78  # default per-run cap (original arm); Phase 1 passes --cap


ENV_PATH = HERE.parent / ".env"
STRICT = {"unset": None, "false": False}


@functools.lru_cache(maxsize=None)
def _key(env_path=ENV_PATH):
    """Read lazily so importing this module (tests, run_probe) needs no .env."""
    lines = env_path.read_text().splitlines() if env_path.exists() else []
    for line in lines:
        if line.startswith("OPENROUTER_API_KEY="):
            value = line.split("=", 1)[1].strip()
            if value:
                return value
    raise SystemExit(f"OPENROUTER_API_KEY missing or empty in {env_path}")


_arm_spend = [0.0]


def remaining_credits():
    req = urllib.request.Request("https://openrouter.ai/api/v1/credits",
                                 headers={"Authorization": f"Bearer {_key()}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.loads(r.read())["data"]
    return d["total_credits"] - d["total_usage"]


def or_call(model, body, tries=6):
    data = json.dumps(body).encode()
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                "https://openrouter.ai/api/v1/chat/completions", data=data,
                headers={"Authorization": f"Bearer {_key()}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:300]
            if e.code == 402:
                raise SystemExit(f"OPENROUTER CREDITS EXHAUSTED: {msg}")
            if e.code in (429, 500, 503) and attempt < tries - 1:
                time.sleep(2 ** attempt + random.random())
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            if attempt < tries - 1:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("unreachable")


def or_messages(system, user, transcript):
    messages = [{"role": "system", "content": system},
                {"role": "user", "content": user}]
    pending_id = 0
    for turn in transcript:
        if turn["role"] == "assistant_tool_call":
            pending_id += 1
            messages.append({"role": "assistant", "content": None, "tool_calls": [
                {"id": f"c{pending_id}", "type": "function",
                 "function": {"name": turn["name"], "arguments": json.dumps(turn["args"])}}]})
        else:
            messages.append({"role": "tool", "tool_call_id": f"c{pending_id}",
                             "content": turn["content"]})
    return messages


def or_body(model, messages, declarations, max_tokens, reasoning="default", provider=None, strict=None):
    """Request body; strict=None leaves the per-tool flag out (the September request shape)."""
    functions = [d if strict is None else {**d, "strict": strict} for d in declarations]
    body = {"model": model, "messages": messages, "temperature": 0, "max_tokens": max_tokens,
            "tools": [{"type": "function", "function": f} for f in functions]}
    if reasoning != "default":
        body["reasoning"] = {"effort": reasoning}
    if provider:
        body["provider"] = {"order": [provider], "allow_fallbacks": False}
    return body


def parse_or_response(resp):
    """{"name","args"} or {"final"}, plus usage (with reasoning tokens) and serving meta."""
    usage = resp.get("usage") or {}
    details = usage.get("completion_tokens_details") or {}
    choice = (resp.get("choices") or [{}])[0]
    msg = choice.get("message") or {}
    extra = {"usage": {"in": usage.get("prompt_tokens", 0), "out": usage.get("completion_tokens", 0),
                       "reasoning": details.get("reasoning_tokens") or 0},
             "meta": {"provider": resp.get("provider"), "model": resp.get("model"),
                      "finish_reason": choice.get("finish_reason")}}
    tcs = msg.get("tool_calls") or []
    if not tcs:
        return {"final": (msg.get("content") or ""), **extra}
    fn = tcs[0].get("function") or {}
    try:
        parsed = json.loads(fn.get("arguments") or "{}")
    except json.JSONDecodeError:
        parsed = {}
    return {"name": fn.get("name", ""), "args": parsed, **extra}


def make_call_model(model, tag_holder, reasoning="default", max_tokens=700,
                    provider=None, phase="experiments", strict=None):
    def call_model(system, user, declarations, transcript):
        body = or_body(model, or_messages(system, user, transcript), declarations, max_tokens,
                       reasoning, provider, strict)
        resp = or_call(model, body)
        _arm_spend[0] += log_cost(model, tag_holder[0], resp.get("usage", {}), phase=phase)
        check_budget()
        if _arm_spend[0] > ARM_CAP_USD:
            raise SystemExit(f"OpenRouter ARM CAP hit: ${_arm_spend[0]:.3f} > ${ARM_CAP_USD}")
        return parse_or_response(resp)
    return call_model


def run_phase1(args):
    """Phase 1 arms: results/phase1/runs_<model>.jsonl, resume-safe, own cap."""
    global ARM_CAP_USD
    if not args.provider:
        raise SystemExit("Phase 1 pins one provider: pass --provider (default route is openai)")
    if args.arm == "route" and not args.route:
        raise SystemExit("--arm route needs --route <label> (names the output file)")
    ARM_CAP_USD = args.cap
    strict = STRICT[args.strict]
    max_tokens = args.max_tokens or (4000 if args.reasoning in ("medium", "high") else 700)
    out_path = p1.out_path(args.model, pilot=bool(args.limit), route=args.route)
    trimmed = p1.repair_tail(out_path)
    if trimmed:
        print(f"repaired {out_path.name}: dropped a {trimmed}-byte partial last line")
    pin = {"provider": args.provider, "strict": args.strict}
    if p1.load_pins(out_path) - {p1.pin_id(pin)}:
        raise SystemExit(f"{out_path.name} was written with other request settings than {pin}; "
                         "use another --route label")
    done = p1.load_done(out_path)
    jobs = p1.jobs(args.arm, args.cells.split(",") if args.cells else None)
    if args.limit:
        jobs = jobs[:args.limit]
    tag_holder = [""]
    call_model = make_call_model(args.model, tag_holder, args.reasoning, max_tokens,
                                 args.provider, phase="phase1", strict=strict)
    n_done = n_skip = 0
    providers = {}
    with out_path.open("a") as f:
        for job in jobs:
            t, cond, cls, ph, rep = job
            if p1.key(t["id"], cond, cls, ph, rep, args.reasoning) in done:
                n_skip += 1
                continue
            tag_holder[0] = p1.tag(job, args.reasoning)
            rec = {**p1.run_episode(job, call_model, args.model, args.arm, args.reasoning, max_tokens,
                                    route=args.route), "pin": pin}
            prov = (rec.get("meta") or {}).get("provider")
            providers[prov] = providers.get(prov, 0) + 1
            f.write(json.dumps(rec) + "\n")
            f.flush()
            n_done += 1
            if n_done % 50 == 0:
                rem = remaining_credits()
                print(f"...{n_done} done, arm spend ${_arm_spend[0]:.3f}, credits left ${rem:.3f}, providers {providers}")
                if rem < 0.05:
                    raise SystemExit("Credits nearly exhausted — stopping cleanly (resume-safe).")
    print(f"DONE {args.arm}: {n_done} new, {n_skip} skipped, arm spend ${_arm_spend[0]:.3f}, "
          f"providers {providers} -> {out_path.relative_to(HERE.parent)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--arm", choices=p1.ARMS, help="Phase 1 arm (omit for the original core grid)")
    ap.add_argument("--reasoning", default="default", choices=["default", "minimal", "low", "medium", "high"])
    ap.add_argument("--cells", default="", help="comma list of Phase-1 conditions (arm thinking)")
    ap.add_argument("--provider", default=None, help="pin one OpenRouter provider, no fallbacks")
    ap.add_argument("--strict", default="unset", choices=sorted(STRICT),
                    help="per-tool strict flag: unset (September shape) or false")
    ap.add_argument("--route", default=None, help="route label for --arm route (output file suffix)")
    ap.add_argument("--cap", type=float, default=ARM_CAP_USD, help="per-run spend cap in USD")
    ap.add_argument("--max-tokens", dest="max_tokens", type=int, default=0)
    args = ap.parse_args()

    rem = remaining_credits()
    print(f"OpenRouter credits remaining: ${rem:.3f}")
    if rem < 0.10:
        raise SystemExit("Under $0.10 remaining — stopping before the arm starts.")
    if args.arm:
        return run_phase1(args)
    from run_gemini import jobs_for_grid  # original grid only

    out_path = RESULTS / f"runs_{args.model.replace('/', '_')}_core.jsonl"
    done = set()
    if out_path.exists():
        for line in out_path.read_text().splitlines():
            r = json.loads(line)
            done.add((r["task"], r["cond"], r["class"], r["phrasing"], r.get("rep", 0)))

    jobs = jobs_for_grid("core", "primary")
    rng = random.Random(42)
    rng.shuffle(jobs)
    if args.limit:
        jobs = jobs[:args.limit]

    tag_holder = [""]
    call_model = make_call_model(args.model, tag_holder)
    n_done = n_skip = 0
    with out_path.open("a") as f:
        for t, cond, cls, ph in jobs:
            key = (t["id"], cond, cls, ph, 0)
            if key in done:
                n_skip += 1
                continue
            tag_holder[0] = f"{t['id']}-{cond}-{cls}-p{ph}"
            rec = harness.run_episode(t, cond, cls, call_model, phrasing_idx=ph)
            rec["rep"] = 0
            rec["model"] = args.model
            f.write(json.dumps(rec) + "\n")
            f.flush()
            n_done += 1
            if n_done % 50 == 0:
                rem = remaining_credits()
                print(f"...{n_done} done, arm spend ${_arm_spend[0]:.3f}, credits left ${rem:.3f}")
                if rem < 0.05:
                    raise SystemExit("Credits nearly exhausted — stopping cleanly (resume-safe).")
    print(f"DONE: {n_done} new, {n_skip} skipped, arm spend ${_arm_spend[0]:.3f}")


if __name__ == "__main__":
    main()
