#!/usr/bin/env python3
"""Gemini arm runner (Flash + Pro). One episode per record, randomized order,
resume-safe JSONL, temperature 0, cost-tracked with the $25 hard stop.

Usage:
  python3 run_gemini.py --model gemini-3.6-flash --grid core --limit 5      # dry run
  python3 run_gemini.py --model gemini-3.6-flash --grid core
  python3 run_gemini.py --model gemini-3.6-flash --grid noise
  python3 run_gemini.py --model gemini-3.6-flash --grid phrasing
  python3 run_gemini.py --model gemini-3.1-pro-preview --grid core --set primary

Phase 1 (writes results/phase1/runs_<model>.jsonl; see phase1_grid.py):
  python3 run_gemini.py --model gemini-3.6-flash --arm infoform --limit 5    # pilot
  python3 run_gemini.py --model gemini-3.6-flash --arm infoform
  python3 run_gemini.py --model gemini-3.1-pro-preview --arm infoform

Phase 2 (writes results/phase2/runs_<model>.jsonl; see phase2_grid.py):
  python3 run_gemini.py --phase 2 --model gemini-3.6-flash --arm fill --limit 5    # pilot
  python3 run_gemini.py --phase 2 --model gemini-3.6-flash --arm fill
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
RESULTS.mkdir(exist_ok=True)

CONDS = ["A", "B_strict", "B_lenient", "C", "D", "E"]
THINKING = {"gemini-3.6-flash": "MINIMAL", "gemini-3.1-pro-preview": "LOW"}


ENV_PATH = HERE.parent / ".env"


@functools.lru_cache(maxsize=None)
def _key(env_path=ENV_PATH):
    """Read lazily so importing this module (tests, run_openrouter) needs no .env."""
    lines = env_path.read_text().splitlines() if env_path.exists() else []
    for line in lines:
        if line.startswith("GEMINI_API_KEY="):
            value = line.split("=", 1)[1].strip()
            if value:
                return value
    raise SystemExit(f"GEMINI_API_KEY missing or empty in {env_path}")


def gemini_call(model, body, tries=6):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    data = json.dumps(body).encode()
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers={
                "Content-Type": "application/json", "x-goog-api-key": _key()})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:400]
            if e.code == 429 and "prepayment" in msg.lower():
                raise SystemExit(f"GEMINI CREDITS DEPLETED — top up at ai.studio/projects. {msg}")
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


def make_call_model(model, tag_holder, phase="experiments"):
    def call_model(system, user, declarations, transcript):
        contents = [{"role": "user", "parts": [{"text": user}]}]
        last_call_id = None
        for turn in transcript:
            if turn["role"] == "assistant_tool_call":
                part = turn.get("raw") or {"functionCall": {"name": turn["name"], "args": turn["args"]}}
                last_call_id = part.get("functionCall", {}).get("id")
                contents.append({"role": "model", "parts": [part]})
            else:
                fr = {"name": turn["name"], "response": {"content": turn["content"]}}
                if last_call_id:
                    fr["id"] = last_call_id
                contents.append({"role": "user", "parts": [{"functionResponse": fr}]})
        body = {
            "contents": contents,
            "systemInstruction": {"parts": [{"text": system}]},
            "tools": [{"functionDeclarations": declarations}],
            "generationConfig": {"temperature": 0, "maxOutputTokens": 1024,
                                 "thinkingConfig": {"thinkingLevel": THINKING[model]}},
        }
        resp = gemini_call(model, body)
        log_cost(model, tag_holder[0], resp.get("usageMetadata", {}), phase=phase)
        check_budget()
        return parse_gemini_response(resp, THINKING[model])
    return call_model


def parse_gemini_response(resp, thinking):
    """{"name","args","raw"} or {"final"}, plus usage (out includes thoughts) and meta."""
    usage = resp.get("usageMetadata") or {}
    candidate = (resp.get("candidates") or [{}])[0]
    thoughts = usage.get("thoughtsTokenCount", 0)
    extra = {"usage": {"in": usage.get("promptTokenCount", 0),
                       "out": usage.get("candidatesTokenCount", 0) + thoughts, "reasoning": thoughts},
             "meta": {"model": resp.get("modelVersion"), "thinking": thinking,
                      "finish_reason": candidate.get("finishReason")}}
    parts = (candidate.get("content") or {}).get("parts")
    if not parts:
        return {"final": "(empty)", **extra}
    for part in parts:
        if "functionCall" in part:
            fc = part["functionCall"]
            return {"name": fc["name"], "args": fc.get("args", {}), "raw": part, **extra}
    return {"final": " ".join(p.get("text", "") for p in parts), **extra}


def jobs_for_grid(grid, subset):
    tasks = harness.frozen()["tasks"]
    jobs = []
    if grid == "core":
        for t in tasks:
            classes = t["assigned"][:1] if subset == "primary" else t["assigned"]
            jobs.append((t, "A", t["assigned"][0], 0))
            for cls in classes:
                for cond in ["B_strict", "B_lenient", "C", "D", "E"]:
                    jobs.append((t, cond, cls, 0))
    elif grid == "noise":  # 30 stratified tasks x 5 identical B_strict calls
        strat = [t for i, t in enumerate(sorted(tasks, key=lambda x: x["id"])) if i % 4 == 0]
        for t in strat[:30]:
            for rep in range(5):
                jobs.append((t, "B_strict", t["assigned"][0], 0, rep))
    elif grid == "phrasing":  # A + B_strict on phrasing 2
        for t in tasks:
            jobs.append((t, "A", t["assigned"][0], 1))
            jobs.append((t, "B_strict", t["assigned"][0], 1))
    else:
        raise SystemExit(f"unknown grid {grid}")
    return jobs


PHASE2_ARMS = ("fill",)  # MILESTONES.md "Phase 2 pre-registration": Flash runs the fill arm only


def phase2_pin():
    return {"provider": "google", "strict": "unset", "endpoint": "gemini", "quantization": None}


def _run_arm(args, grid, out_path, jobs, phase, pin=None):
    """Resume-safe loop shared by Phase 1 and Phase 2; records carry the model's fixed thinking level."""
    trimmed = p1.repair_tail(out_path)
    if trimmed:
        print(f"repaired {out_path.name}: dropped a {trimmed}-byte partial last line")
    if pin is not None and p1.load_pins(out_path) - {p1.pin_id(pin)}:
        raise SystemExit(f"{out_path.name} was written with other request settings than {pin}")
    done = p1.load_done(out_path)
    if args.limit:
        jobs = jobs[:args.limit]
    tag_holder = [""]
    call_model = make_call_model(args.model, tag_holder, phase=phase)
    reasoning = THINKING[args.model]  # Gemini thinking level is fixed per model, as in the original arms
    n_done = n_skip = 0
    with out_path.open("a") as f:
        for job in jobs:
            t, cond, cls, ph, rep = job
            if p1.key(t["id"], cond, cls, ph, rep, reasoning) in done:
                n_skip += 1
                continue
            tag_holder[0] = grid.tag(job, reasoning)
            extra = (pin,) if pin is not None else ()
            rec = grid.run_episode(job, call_model, args.model, args.arm, reasoning, 1024, *extra)
            f.write(json.dumps(rec) + "\n")
            f.flush()
            n_done += 1
            if n_done % 50 == 0:
                print(f"...{n_done} done (skipped {n_skip}), spend ${check_budget():.2f}")
    shown = out_path.relative_to(HERE.parent) if out_path.is_relative_to(HERE.parent) else out_path
    print(f"DONE {args.arm}: {n_done} new, {n_skip} skipped, total spend ${check_budget():.2f} -> {shown}")


def run_phase1(args):
    """Phase 1 arms for Gemini (pre-registered: infoform). Resume-safe."""
    _run_arm(args, p1, p1.out_path(args.model, pilot=bool(args.limit)), p1.jobs(args.arm), "phase1")


def run_phase2(args):
    """Phase 2 arms for Gemini (pre-registered: fill, Flash). Resume-safe, pinned."""
    if args.arm not in PHASE2_ARMS:
        raise SystemExit(f"Gemini runs only the Phase-2 arms {PHASE2_ARMS}, not {args.arm!r}")
    _run_arm(args, p2, p2.out_path(args.model, pilot=bool(args.limit)), p2.jobs(args.arm), "phase2",
             pin=phase2_pin())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--grid", default="core")
    ap.add_argument("--set", dest="subset", default="doubled", choices=["primary", "doubled"])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--phase", type=int, choices=(1, 2), default=1)
    ap.add_argument("--arm", choices=sorted(set(p1.ARMS) | set(p2.ARMS)),
                    help="Phase 1 or 2 arm (omit for the original grids)")
    args = ap.parse_args()
    if args.arm:
        return run_phase2(args) if args.phase == 2 else run_phase1(args)

    out_path = RESULTS / f"runs_{args.model.replace('/', '_')}_{args.grid}.jsonl"
    done = set()
    if out_path.exists():
        for line in out_path.read_text().splitlines():
            r = json.loads(line)
            done.add((r["task"], r["cond"], r["class"], r["phrasing"], r.get("rep", 0)))

    jobs = jobs_for_grid(args.grid, args.subset)
    rng = random.Random(42)
    rng.shuffle(jobs)
    if args.limit:
        jobs = jobs[:args.limit]

    tag_holder = [""]
    call_model = make_call_model(args.model, tag_holder)
    n_done = n_skip = 0
    with out_path.open("a") as f:
        for job in jobs:
            t, cond, cls, ph = job[0], job[1], job[2], job[3]
            rep = job[4] if len(job) > 4 else 0
            key = (t["id"], cond, cls, ph, rep)
            if key in done:
                n_skip += 1
                continue
            tag_holder[0] = f"{t['id']}-{cond}-{cls}-p{ph}-r{rep}"
            rec = harness.run_episode(t, cond, cls, call_model, phrasing_idx=ph)
            rec["rep"] = rep
            rec["model"] = args.model
            f.write(json.dumps(rec) + "\n")
            f.flush()
            n_done += 1
            if n_done % 50 == 0:
                print(f"...{n_done} done (skipped {n_skip}), spend ${check_budget():.2f}")
    print(f"DONE: {n_done} new episodes, {n_skip} skipped, total spend ${check_budget():.2f}")


if __name__ == "__main__":
    main()
