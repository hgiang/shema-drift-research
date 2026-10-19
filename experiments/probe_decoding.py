#!/usr/bin/env python3
"""Decoding-constraint probe (H-dec), pre-registered in MILESTONES.md "Phase 1 addendum".

Asks each route to send an argument the declared schema does not allow (off-enum value,
string for an integer, undeclared name) and records whether the call carries it. luna runs
on three OpenRouter providers x strict {unset, false}; Gemini Flash and Pro are controls.
An instrument check: not part of the BH family.

Usage:
  python3 probe_decoding.py --reps 3                                   # full probe, ~90 calls
  python3 probe_decoding.py --reps 1 --routes luna-openai-unset,flash  # pilot (*.pilot.json)
"""

import argparse
import json
import pathlib
import sys
import time
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402

LUNA = "openai/gpt-5.6-luna"
PROBE_TOOL_V1 = {"description": "Diagnostic tool: records the mode, count and label it is called with."}
PROBE_PARAMS = {
    "mode": {"type": "string", "desc": "Processing mode.", "enum": ["alpha", "beta"], "required": True},
    "count": {"type": "integer", "desc": "Number of items.", "required": True},
    "label": {"type": "string", "desc": "Free-text label.", "required": False, "default": "none"},
}
PROBE_TOOL = harness.declaration("probe_tool", PROBE_TOOL_V1, PROBE_PARAMS)

CASES = {
    "off_enum": 'Call probe_tool with mode "gamma" and count 3. The service now accepts "gamma"; send exactly that value.',
    "off_type": 'Call probe_tool with mode "alpha" and count set to the string "3 items" (a string, not a number).',
    "undeclared": 'Call probe_tool with mode "alpha", count 3, and an extra argument named note with the value "hi".',
    "optional_fill": 'Call probe_tool with mode "alpha" and count 3.',
}
COMPLY_CASES = ("off_enum", "off_type", "undeclared")
CHECKS = {
    "off_enum": lambda a: a.get("mode") == "gamma",
    "off_type": lambda a: isinstance(a.get("count"), str),
    "undeclared": lambda a: "note" in a,
    "optional_fill": lambda a: "label" in a,
}
THRESHOLD = Fraction(7, 9)  # control works / route lifts: >= 7 of 9 at 3 reps

CONTROLS = ("flash", "pro")
ROUTES = [{"label": f"luna-{prov}-{strict}", "family": "luna", "model": LUNA,
           "provider": prov, "strict": strict}
          for prov in ("openai", "azure", "amazon-bedrock") for strict in ("unset", "false")] + [
    {"label": "flash", "family": "gemini", "model": "gemini-3.6-flash"},
    {"label": "pro", "family": "gemini", "model": "gemini-3.1-pro-preview"},
]


def complied(case, call):
    """True when the call is a probe_tool call carrying the argument the prompt asked for."""
    if not call or call.get("name") != "probe_tool":
        return False
    return CHECKS[case](call.get("args") or {})


def tag(route_label, case, rep):
    # "p1-" prefix keeps analyze.token_costs() (original study) blind to probe spend
    return f"p1-probe-{route_label}-{case}-r{rep}"


def probe_once(route, case, rep, call_model):
    base = {"route": route["label"], "case": case, "rep": rep}
    try:
        out = call_model(harness.SYSTEM, CASES[case], [PROBE_TOOL], [])
    except Exception as e:  # an unavailable route is a result, not a crash; SystemExit still stops
        return {**base, "call": None, "final": None, "usage": None, "meta": None,
                "complied": False, "error": f"{type(e).__name__}: {e}"[:300]}
    args = out.get("args") if isinstance(out.get("args"), dict) else {}
    call = {"name": out["name"], "args": args} if "name" in out else None
    truncated = call is None and (out.get("meta") or {}).get("finish_reason") == "length"
    return {**base, "call": call, "final": out.get("final"), "usage": out.get("usage"),
            "meta": out.get("meta"), "complied": complied(case, call),
            # a reply cut off by max_tokens is no observation, so it cannot count as 0/9
            "error": "truncated: finish_reason length, no call" if truncated else None}


def probe_route(route, call_model, reps, tag_holder):
    rows = []
    for case in CASES:
        for rep in range(reps):
            tag_holder[0] = tag(route["label"], case, rep)
            rows.append(probe_once(route, case, rep, call_model))
    return rows


def _case_counts(rows):
    ok = [r for r in rows if r["error"] is None]
    return {"n": len(ok), "complied": sum(r["complied"] for r in ok), "errors": len(rows) - len(ok)}


def _route_summary(rows, reps):
    cases = {c: _case_counts([r for r in rows if r["case"] == c]) for c in CASES}
    n = sum(cases[c]["n"] for c in COMPLY_CASES)
    k = sum(cases[c]["complied"] for c in COMPLY_CASES)
    errors = sum(cases[c]["errors"] for c in COMPLY_CASES)
    return {"cases": cases, "comply": {"n": n, "complied": k}, "errors": errors,
            "complete": n == len(COMPLY_CASES) * reps}


def summarize(results, reps):
    """Per-route counts and, for luna routes, the addendum verdicts:
    h_dec = luna complies 0/9 and every control >= 7/9; lifts = luna >= 7/9.
    Verdicts are None when a route is incomplete (errors) or a control is missing."""
    labels = list(dict.fromkeys(r["route"] for r in results))
    routes = {lb: _route_summary([r for r in results if r["route"] == lb], reps) for lb in labels}
    controls = [routes.get(c) for c in CONTROLS]
    controls_ok = all(c and c["complete"] and Fraction(c["comply"]["complied"], c["comply"]["n"]) >= THRESHOLD
                      for c in controls)
    controls_known = all(c and c["complete"] for c in controls)
    for lb, r in routes.items():
        if lb in CONTROLS:
            continue
        if not r["complete"]:
            routes[lb] = {**r, "h_dec": None, "lifts": None}
            continue
        rate = Fraction(r["comply"]["complied"], r["comply"]["n"])
        h_dec = (r["comply"]["complied"] == 0 and controls_ok) if controls_known else None
        routes[lb] = {**r, "h_dec": h_dec, "lifts": rate >= THRESHOLD}
    return {"routes": routes, "controls_ok": controls_ok, "reps": reps}


def is_full_grid(chosen):
    labels = [r["label"] for r in chosen]
    return len(labels) == len(set(labels)) and set(labels) == {r["label"] for r in ROUTES}


def output_path(all_routes, reps):
    name = "probe_decoding.json" if all_routes and reps == 3 else "probe_decoding.pilot.json"
    return p1.OUT_DIR / name


def make_caller(route, tag_holder):  # pragma: no cover - builds a networked call_model
    if route["family"] == "luna":
        import run_openrouter as ro
        return ro.make_call_model(route["model"], tag_holder, "default", 700, route["provider"],
                                  phase="phase1", strict=ro.STRICT[route["strict"]])
    import run_gemini as rg
    return rg.make_call_model(route["model"], tag_holder, phase="phase1")


def main():  # pragma: no cover - network loop
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--routes", default="", help="comma list of route labels (default: all)")
    args = ap.parse_args()
    known = {r["label"]: r for r in ROUTES}
    chosen = [known[x] for x in args.routes.split(",")] if args.routes else ROUTES
    from cost_tracker import check_budget
    print(f"logged spend before probe: ${check_budget():.4f}")
    tag_holder, results, finished = [""], [], False
    try:
        for route in chosen:
            rows = probe_route(route, make_caller(route, tag_holder), args.reps, tag_holder)
            results += rows
            s = _route_summary(rows, args.reps)
            print(f"{route['label']:<26} comply {s['comply']['complied']}/{s['comply']['n']} "
                  f"fill {s['cases']['optional_fill']['complied']}/{s['cases']['optional_fill']['n']} "
                  f"errors {s['errors']}")
        finished = True
    finally:  # a stop mid-run (spend cap) still saves what was paid for, as a pilot file
        out = output_path(finished and is_full_grid(chosen), args.reps)
        p1.OUT_DIR.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"date": time.strftime("%Y-%m-%d"), "spec": "MILESTONES.md Phase 1 addendum",
                                   "finished": finished, "probe_tool": PROBE_TOOL, "cases": CASES,
                                   "routes": chosen, "summary": summarize(results, args.reps),
                                   "results": results}, indent=1))
        print(f"wrote {out.relative_to(HERE.parent)}; logged spend now ${check_budget():.4f}")


if __name__ == "__main__":
    main()
