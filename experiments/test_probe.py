#!/usr/bin/env python3
"""Tests for the decoding-constraint probe. No API calls: fake call_model only.

Run: python3 -m pytest test_probe.py -q
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402
import phase2_grid as p2  # noqa: E402
import probe_decoding as pd  # noqa: E402


def call(**args):
    return {"name": "probe_tool", "args": {"mode": "alpha", "count": 3, **args}}


def test_complied_rules():
    assert pd.complied("off_enum", call(mode="gamma"))
    assert not pd.complied("off_enum", call(mode="beta"))
    assert pd.complied("off_type", call(count="3 items"))
    assert not pd.complied("off_type", call(count=3))
    assert pd.complied("undeclared", call(note="hi"))
    assert not pd.complied("undeclared", call())
    assert pd.complied("optional_fill", call(label="none"))
    assert not pd.complied("optional_fill", call())
    for case in pd.CASES:
        assert not pd.complied(case, None)
    assert not pd.complied("off_enum", {"name": "other_tool", "args": {"mode": "gamma"}})


def test_cases_are_the_addendum_prompts_verbatim():
    assert set(pd.CASES) == {"off_enum", "off_type", "undeclared", "optional_fill"}
    assert pd.CASES["off_enum"] == ('Call probe_tool with mode "gamma" and count 3. '
                                    'The service now accepts "gamma"; send exactly that value.')
    assert pd.CASES["optional_fill"] == 'Call probe_tool with mode "alpha" and count 3.'


def rows(route, n_comply, reps=3, errors=0):
    """reps per case; n_comply of the 3*reps comply-case calls carry the requested argument."""
    out, left = [], n_comply
    for case in pd.COMPLY_CASES:
        for rep in range(reps):
            ok, left = left > 0, left - 1
            out.append({"route": route, "case": case, "rep": rep, "complied": ok, "error": None})
    for i in range(errors):
        out[i] = {**out[i], "complied": False, "error": "HTTP 400"}
    out += [{"route": route, "case": "optional_fill", "rep": r, "complied": True, "error": None}
            for r in range(reps)]
    return out


def decision(**k):
    luna = {r["label"]: 0 for r in pd.ROUTES if r["family"] == "luna"}
    rows_ = [row for lb, n in {**luna, **k}.items() for row in rows(lb, n)]
    return pd.summarize(rows_ + rows("flash", 3) + rows("pro", 2), reps=3)


def test_summarize_verdicts_amendment_1():
    s = decision(**{"luna-azure-false": 8})
    assert s["decision"] == {"h_dec": True, "status": "holds", "route_arm": "luna-azure-false"}
    assert s["routes"][pd.PINNED]["constrained"] is True and s["routes"]["luna-azure-false"]["lifts"] is True
    assert "constrained" not in s["routes"]["flash"]  # Gemini is descriptive only
    assert s["routes"]["luna-azure-false"]["cases"]["optional_fill"] == {"n": 3, "complied": 3, "errors": 0}

    assert decision()["decision"]["h_dec"] is None
    assert decision()["decision"]["status"].startswith("undecided")
    assert decision(**{pd.PINNED: 2, "luna-azure-false": 9})["decision"]["h_dec"] is False
    assert decision(**{"luna-azure-unset": 6})["decision"]["h_dec"] is None  # 6/9 does not lift
    tie = decision(**{"luna-azure-unset": 9, "luna-openai-false": 9, "luna-amazon-bedrock-false": 8})
    assert tie["decision"]["route_arm"] == "luna-openai-false"  # earlier in ROUTES


def test_summarize_withholds_verdicts_on_incomplete_routes():
    s = pd.summarize(rows(pd.PINNED, 0, errors=2) + rows("luna-azure-false", 9), reps=3)
    r = s["routes"][pd.PINNED]
    assert r["comply"] == {"n": 7, "complied": 0} and r["errors"] == 2
    assert r["constrained"] is None and r["lifts"] is None
    assert s["decision"]["h_dec"] is None and s["decision"]["status"] == "pinned route incomplete"


def test_probe_tool_rendering():
    assert pd.PROBE_TOOL == harness.declaration("probe_tool", pd.PROBE_TOOL_V1, pd.PROBE_PARAMS)
    params = pd.PROBE_TOOL["parameters"]
    assert params["required"] == ["mode", "count"]
    assert params["properties"]["mode"]["enum"] == ["alpha", "beta"]
    assert params["properties"]["count"]["type"] == "integer"
    assert '(optional; default: "none")' in params["properties"]["label"]["description"]


def test_routes_cover_the_addendum_grid():
    luna = [r for r in pd.ROUTES if r["family"] == "luna"]
    assert {(r["provider"], r["strict"]) for r in luna} == {
        (p, s) for p in ("openai", "azure", "amazon-bedrock") for s in ("unset", "false")}
    assert {r["label"] for r in pd.ROUTES if r["family"] != "luna"} == set(pd.CONTROLS)
    assert len({r["label"] for r in pd.ROUTES}) == len(pd.ROUTES)


def test_probe_tags_are_phase1():
    tag = pd.tag("luna-openai-unset", "off_enum", 2)
    assert tag == "p1-probe-luna-openai-unset-off_enum-r2"
    assert tag.startswith("p1-")


def test_probe_route_records_each_call_and_survives_errors():
    route = {"label": "luna-openai-unset", "family": "luna"}

    def fake(system, user, decls, transcript):
        assert system == harness.SYSTEM and decls == [pd.PROBE_TOOL] and transcript == []
        if "extra argument" in user:
            raise RuntimeError("HTTP 400: bad request")
        return {"name": "probe_tool", "args": {"mode": "alpha", "count": 3, "label": "none"},
                "usage": {"in": 5, "out": 2, "reasoning": 0}, "meta": {"provider": "OpenAI"}}

    out = pd.probe_route(route, fake, reps=2, tag_holder=[""])
    assert len(out) == 8
    bad = [r for r in out if r["case"] == "undeclared"]
    assert all(r["error"].startswith("RuntimeError") and r["complied"] is False for r in bad)
    fill = [r for r in out if r["case"] == "optional_fill"]
    assert all(r["complied"] and r["meta"] == {"provider": "OpenAI"} for r in fill)


def test_output_path_keeps_partial_runs_out_of_the_data_file():
    assert pd.output_path(all_routes=True, reps=3).name == "probe_decoding.json"
    assert pd.output_path(all_routes=False, reps=3).name == "probe_decoding.pilot.json"
    assert pd.output_path(all_routes=True, reps=1).name == "probe_decoding.pilot.json"


def test_truncated_reply_and_odd_args_are_not_observations():
    route = {"label": "luna-openai-unset"}

    def cut(system, user, decls, transcript):
        return {"final": "", "meta": {"finish_reason": "length"}}

    def listy(system, user, decls, transcript):
        return {"name": "probe_tool", "args": ["gamma"], "meta": {"finish_reason": "tool_calls"}}

    row = pd.probe_once(route, "off_enum", 0, cut)
    assert row["error"].startswith("truncated") and row["complied"] is False
    row = pd.probe_once(route, "off_enum", 0, listy)
    assert row["error"] is None and row["call"]["args"] == {} and row["complied"] is False
    refusal = pd.probe_once(route, "off_enum", 0, lambda *a: {"final": "gamma is not allowed",
                                                             "meta": {"finish_reason": "stop"}})
    assert refusal["error"] is None and refusal["complied"] is False  # a refusal is an observation


def test_full_grid_needs_every_route_exactly_once():
    assert pd.is_full_grid(pd.ROUTES)
    assert not pd.is_full_grid(pd.ROUTES[:-1])
    assert not pd.is_full_grid(pd.ROUTES[:-1] + [pd.ROUTES[0]])  # same count, one missing


# Phase 2 (MILESTONES.md "Phase 2 pre-registration", decoding probe): 4 routes x strict {unset, false}

def test_phase2_routes_are_the_locked_grid():
    bases = [("anthropic/claude-haiku-5.5", "anthropic", None, "openrouter"),
             ("anthropic/claude-sonnet-5.5", "anthropic", None, "openrouter"),
             ("meta-llama/llama-3.3-70b-instruct", "novita", "bf16", "openrouter"),
             (pd.LUNA, None, None, "openai")]
    got = {(r["model"], r["provider"], r["quantization"], r["endpoint"], r["strict"]) for r in pd.P2_ROUTES}
    assert got == {(*b, s) for b in bases for s in ("unset", "false")}
    assert len(pd.P2_ROUTES) == 8 == len({r["label"] for r in pd.P2_ROUTES})
    assert [r["label"] for r in pd.P2_ROUTES if r["family"] == "luna"] == ["luna-direct-unset", "luna-direct-false"]
    assert pd.routes(1) is pd.ROUTES and pd.routes(2) is pd.P2_ROUTES


def test_phase2_tags_paths_and_grid():
    assert pd.tag("luna-direct-unset", "off_enum", 2, phase=2) == "p2-probe-luna-direct-unset-off_enum-r2"
    assert pd.output_path(all_routes=True, reps=3, phase=2) == p2.OUT_DIR / "probe_decoding.json"
    assert pd.output_path(all_routes=False, reps=3, phase=2) == p2.OUT_DIR / "probe_decoding.pilot.json"
    assert pd.output_path(all_routes=True, reps=3).parent == p1.OUT_DIR  # Phase 1 unchanged
    assert pd.is_full_grid(pd.P2_ROUTES, phase=2) and not pd.is_full_grid(pd.ROUTES, phase=2)
    assert not pd.is_full_grid(pd.P2_ROUTES[:-1], phase=2)


def test_phase2_probe_route_tags_each_call():
    seen, holder = [], [""]

    def fake(system, user, decls, transcript):
        seen.append(holder[0])
        return {"name": "probe_tool", "args": {"mode": "alpha", "count": 3}}

    pd.probe_route(pd.P2_ROUTES[0], fake, reps=1, tag_holder=holder, phase=2)
    assert seen == [f"p2-probe-{pd.P2_ROUTES[0]['label']}-{c}-r0" for c in pd.CASES]


def p2_summary(**k):
    """Every Phase-2 route complete at 3 reps; k sets comply counts (default 0)."""
    counts = {r["label"]: 0 for r in pd.P2_ROUTES}
    return pd.summarize([row for lb, n in {**counts, **k}.items() for row in rows(lb, n)], reps=3, phase=2)


def test_phase2_decision_picks_the_lifting_direct_route():
    s = p2_summary(**{"luna-direct-false": 7, "sonnet-anthropic-unset": 9})
    assert s["decision"] == {"lifts": True, "status": "lifts", "direct_arm": "luna-direct-false"}
    assert s["routes"]["luna-direct-unset"]["constrained"] is True
    assert "lifts" not in s["routes"]["sonnet-anthropic-unset"]  # new families are descriptive
    assert s["routes"]["sonnet-anthropic-unset"]["comply"] == {"n": 9, "complied": 9}
    tie = p2_summary(**{"luna-direct-unset": 8, "luna-direct-false": 8})
    assert tie["decision"]["direct_arm"] == "luna-direct-unset"  # ties go to strict unset
    best = p2_summary(**{"luna-direct-unset": 7, "luna-direct-false": 9})
    assert best["decision"]["direct_arm"] == "luna-direct-false"  # highest k
    none = p2_summary(**{"luna-direct-unset": 6, "haiku-anthropic-false": 9})
    assert none["decision"] == {"lifts": False, "status": "no lift: P15 untested", "direct_arm": None}


def test_phase2_decision_waits_for_both_direct_routes():
    gap = pd.summarize(rows("luna-direct-unset", 9) + rows("luna-direct-false", 9, errors=1), reps=3, phase=2)
    assert gap["decision"] == {"lifts": None, "status": "luna direct route incomplete", "direct_arm": None}
    assert gap["routes"]["luna-direct-false"]["lifts"] is None
    one = pd.summarize(rows("luna-direct-unset", 9), reps=3, phase=2)
    assert one["decision"]["lifts"] is None
