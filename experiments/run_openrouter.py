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

Phase 2 (writes results/phase2/runs_<model>[.<endpoint>].jsonl; see phase2_grid.py):
  python3 run_openrouter.py --phase 2 --arm core --model anthropic/claude-haiku-5.5 --provider anthropic --cap 3 --limit 5
  python3 run_openrouter.py --phase 2 --arm core --model meta-llama/llama-3.3-70b-instruct --provider novita --quantization bf16 --cap 3
  python3 run_openrouter.py --phase 2 --arm direct --model openai/gpt-5.6-luna --endpoint openai [--strict false] --cap 3
  Arms: core, phrasing, noise, infoform, placement, direct (fill runs on Gemini).
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
import phase2_grid as p2  # noqa: E402
from cost_tracker import log_cost, check_budget  # noqa: E402

RESULTS = HERE.parent / "results"
ARM_CAP_USD = 0.78  # default per-run cap (original arm); Phase 1 passes --cap


ENV_PATH = HERE.parent / ".env"
STRICT = {"unset": None, "false": False}
ENDPOINTS = {  # Phase 2: luna also runs on the OpenAI API directly (MILESTONES.md)
    "openrouter": {"url": "https://openrouter.ai/api/v1/chat/completions", "key": "OPENROUTER_API_KEY"},
    "openai": {"url": "https://api.openai.com/v1/chat/completions", "key": "OPENAI_API_KEY"},
}


@functools.lru_cache(maxsize=None)
def _env_value(name, env_path=ENV_PATH):
    """Read lazily so importing this module (tests, run_probe) needs no .env."""
    lines = env_path.read_text().splitlines() if env_path.exists() else []
    for line in lines:
        if line.startswith(f"{name}="):
            value = line.split("=", 1)[1].strip()
            if value:
                return value
    raise SystemExit(f"{name} missing or empty in {env_path}")


def _key(env_path=ENV_PATH):
    return _env_value("OPENROUTER_API_KEY", env_path)


_arm_spend = [0.0]


def remaining_credits():
    req = urllib.request.Request("https://openrouter.ai/api/v1/credits",
                                 headers={"Authorization": f"Bearer {_key()}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.loads(r.read())["data"]
    return d["total_credits"] - d["total_usage"]


def or_call(model, body, tries=6, endpoint="openrouter"):
    data = json.dumps(body).encode()
    ep = ENDPOINTS[endpoint]
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                ep["url"], data=data,
                headers={"Authorization": f"Bearer {_env_value(ep['key'])}", "Content-Type": "application/json"})
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


def or_body(model, messages, declarations, max_tokens, reasoning="default", provider=None, strict=None,
            quantization=None, endpoint="openrouter"):
    """Request body; strict=None leaves the per-tool flag out (the September request shape).
    endpoint "openai" posts to OpenAI directly: bare model name, no provider block."""
    if endpoint == "openai":
        if provider or quantization:
            raise SystemExit("the OpenAI direct endpoint takes no --provider or --quantization")
        model = model.split("/", 1)[1] if model.startswith("openai/") else model
    functions = [d if strict is None else {**d, "strict": strict} for d in declarations]
    limit = "max_completion_tokens" if endpoint == "openai" else "max_tokens"  # OpenAI's current name
    body = {"model": model, "messages": messages, "temperature": 0, limit: max_tokens,
            "tools": [{"type": "function", "function": f} for f in functions]}
    if reasoning != "default":
        body.update({"reasoning_effort": reasoning} if endpoint == "openai" else {"reasoning": {"effort": reasoning}})
    if provider:
        body["provider"] = {"order": [provider], "allow_fallbacks": False,
                            **({"quantizations": [quantization]} if quantization else {})}
    return body


def parse_or_response(resp, endpoint="openrouter"):
    """{"name","args"[,"text"]} or {"final"}, plus usage (with reasoning tokens) and serving meta.
    "text" is prose the model wrote beside its tool call (Claude often does)."""
    usage = resp.get("usage") or {}
    details = usage.get("completion_tokens_details") or {}
    choice = (resp.get("choices") or [{}])[0]
    msg = choice.get("message") or {}
    extra = {"usage": {"in": usage.get("prompt_tokens", 0), "out": usage.get("completion_tokens", 0),
                       "reasoning": details.get("reasoning_tokens") or 0},
             "meta": {"provider": "openai-direct" if endpoint == "openai" else resp.get("provider"),
                      "model": resp.get("model"),
                      "finish_reason": choice.get("finish_reason")}}
    tcs = msg.get("tool_calls") or []
    if not tcs:
        return {"final": (msg.get("content") or ""), **extra}
    fn = tcs[0].get("function") or {}
    try:
        parsed = json.loads(fn.get("arguments") or "{}")
    except json.JSONDecodeError:
        parsed = {}
    text = msg.get("content")
    return {"name": fn.get("name", ""), "args": parsed, **({"text": text} if text else {}), **extra}


def make_call_model(model, tag_holder, reasoning="default", max_tokens=700,
                    provider=None, phase="experiments", strict=None, quantization=None, endpoint="openrouter"):
    def call_model(system, user, declarations, transcript):
        body = or_body(model, or_messages(system, user, transcript), declarations, max_tokens,
                       reasoning, provider, strict, quantization, endpoint)
        resp = or_call(model, body, endpoint=endpoint)
        _arm_spend[0] += log_cost(model, tag_holder[0], resp.get("usage", {}), phase=phase)
        check_budget()
        if _arm_spend[0] > ARM_CAP_USD:
            raise SystemExit(f"OpenRouter ARM CAP hit: ${_arm_spend[0]:.3f} > ${ARM_CAP_USD}")
        return parse_or_response(resp, endpoint)
    return call_model


def _shown(path):
    return path.relative_to(HERE.parent) if path.is_relative_to(HERE.parent) else path


def check_phase_arm(phase, arm):
    arms = tuple(a for a in p2.ARMS if a != "fill") if phase == 2 else p1.ARMS  # fill: Gemini only
    if arm not in arms:
        raise SystemExit(f"{arm!r} is not a Phase {phase} arm; choose from {arms}")


def phase2_pin(args):
    """Request settings every Phase-2 record carries; resume refuses a file written with others."""
    direct = args.endpoint == "openai"
    return {"provider": "openai-direct" if direct else args.provider, "strict": args.strict,
            "endpoint": args.endpoint, "quantization": args.quantization,
            "max_tokens": args.max_tokens or 700}


def _prepare(out_path, pin):
    trimmed = p1.repair_tail(out_path)
    if trimmed:
        print(f"repaired {out_path.name}: dropped a {trimmed}-byte partial last line")
    if p1.load_pins(out_path) - {p1.pin_id(pin)}:
        raise SystemExit(f"{out_path.name} was written with other request settings than {pin}")
    return p1.load_done(out_path)


def _run_jobs(out_path, jobs, done, reasoning, tag_holder, tag_fn, make_rec, endpoint="openrouter"):
    """Run the jobs not in `done`, appending one record per episode; returns (new, skipped, providers)."""
    n_done = n_skip = 0
    providers = {}
    with out_path.open("a") as f:
        for job in jobs:
            t, cond, cls, ph, rep = job
            if p1.key(t["id"], cond, cls, ph, rep, reasoning) in done:
                n_skip += 1
                continue
            tag_holder[0] = tag_fn(job, reasoning)
            rec = make_rec(job)
            prov = (rec.get("meta") or {}).get("provider")
            providers[prov] = providers.get(prov, 0) + 1
            f.write(json.dumps(rec) + "\n")
            f.flush()
            n_done += 1
            if n_done % 50 == 0:
                _progress(n_done, providers, endpoint)
    return n_done, n_skip, providers


def _progress(n_done, providers, endpoint):
    if endpoint != "openrouter":
        print(f"...{n_done} done, arm spend ${_arm_spend[0]:.3f}, providers {providers}")
        return
    rem = remaining_credits()
    print(f"...{n_done} done, arm spend ${_arm_spend[0]:.3f}, credits left ${rem:.3f}, providers {providers}")
    if rem < 0.05:
        raise SystemExit("Credits nearly exhausted — stopping cleanly (resume-safe).")


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
    pin = {"provider": args.provider, "strict": args.strict}
    done = _prepare(out_path, pin)
    jobs = p1.jobs(args.arm, args.cells.split(",") if args.cells else None)
    if args.limit:
        jobs = jobs[:args.limit]
    tag_holder = [""]
    call_model = make_call_model(args.model, tag_holder, args.reasoning, max_tokens,
                                 args.provider, phase="phase1", strict=strict)

    def make_rec(job):
        return {**p1.run_episode(job, call_model, args.model, args.arm, args.reasoning, max_tokens,
                                 route=args.route), "pin": pin}
    n_done, n_skip, providers = _run_jobs(out_path, jobs, done, args.reasoning, tag_holder, p1.tag, make_rec)
    print(f"DONE {args.arm}: {n_done} new, {n_skip} skipped, arm spend ${_arm_spend[0]:.3f}, "
          f"providers {providers} -> {_shown(out_path)}")


def run_phase2(args):
    """Phase 2 arms: results/phase2/runs_<model>[.<endpoint>].jsonl, resume-safe, own cap."""
    global ARM_CAP_USD
    if args.endpoint == "openrouter" and not args.provider:
        raise SystemExit("Phase 2 pins one OpenRouter provider: pass --provider")
    ARM_CAP_USD = args.cap
    max_tokens = args.max_tokens or 700
    out_path = p2.out_path(args.model, pilot=bool(args.limit), endpoint=args.endpoint)
    pin = phase2_pin(args)
    done = _prepare(out_path, pin)
    jobs = p2.jobs(args.arm)
    if args.limit:
        jobs = jobs[:args.limit]
    tag_holder = [""]
    call_model = make_call_model(args.model, tag_holder, args.reasoning, max_tokens, args.provider,
                                 phase="phase2", strict=STRICT[args.strict],
                                 quantization=args.quantization, endpoint=args.endpoint)

    def make_rec(job):
        return p2.run_episode(job, call_model, args.model, args.arm, args.reasoning, max_tokens, pin)
    n_done, n_skip, providers = _run_jobs(out_path, jobs, done, args.reasoning, tag_holder, p2.tag, make_rec,
                                          args.endpoint)
    print(f"DONE {args.arm}: {n_done} new, {n_skip} skipped, arm spend ${_arm_spend[0]:.3f}, "
          f"providers {providers} -> {_shown(out_path)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--phase", type=int, choices=(1, 2), default=1)
    ap.add_argument("--arm", choices=sorted(set(p1.ARMS) | set(p2.ARMS)),
                    help="Phase 1 or 2 arm (omit for the original core grid)")
    ap.add_argument("--reasoning", default="default", choices=["default", "minimal", "low", "medium", "high"])
    ap.add_argument("--cells", default="", help="comma list of Phase-1 conditions (arm thinking)")
    ap.add_argument("--provider", default=None, help="pin one OpenRouter provider, no fallbacks")
    ap.add_argument("--strict", default="unset", choices=sorted(STRICT),
                    help="per-tool strict flag: unset (September shape) or false")
    ap.add_argument("--route", default=None, help="route label for --arm route (output file suffix)")
    ap.add_argument("--cap", type=float, default=ARM_CAP_USD, help="per-run spend cap in USD")
    ap.add_argument("--max-tokens", dest="max_tokens", type=int, default=0)
    ap.add_argument("--endpoint", default="openrouter", choices=sorted(ENDPOINTS), help="Phase 2 only")
    ap.add_argument("--quantization", default=None, help="Phase 2: pin the provider's quantization (e.g. bf16)")
    args = ap.parse_args()
    if args.arm:
        check_phase_arm(args.phase, args.arm)
    if args.phase == 1 and (args.endpoint != "openrouter" or args.quantization):
        raise SystemExit("--endpoint and --quantization are Phase 2 options")

    if args.endpoint == "openrouter":
        rem = remaining_credits()
        print(f"OpenRouter credits remaining: ${rem:.3f}")
        if rem < 0.10:
            raise SystemExit("Under $0.10 remaining — stopping before the arm starts.")
    if args.arm:
        return run_phase2(args) if args.phase == 2 else run_phase1(args)
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
