#!/usr/bin/env python3
"""Tests for the Phase 1 conditions and job grid. No API calls: fake models only.

Run: python3 -m pytest test_phase1.py -q
"""

import json
import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402

PAIRS = p1.primary_pairs()


def drift_change(task, cls):
    return harness.frozen()["diffs"][f"{task['drift_tool']}::{cls}"]["changes"][0]


def drift_decl(setup, task):
    return next(d for d in setup["declarations"] if d["name"] == task["drift_tool"])


# ---------------- fake models ----------------

def oracle(gt_key):
    """Calls the ground-truth tools in order with ground-truth args (v1 or v2)."""
    def make(task, cls):
        steps = task["gt_v1"] if gt_key == "v1" else task["gt_v2"][cls]
        tools = [s["tool"] for s in task["steps"]]

        def call_model(system, user, decls, transcript):
            real = [t for t in transcript if t["role"] == "assistant_tool_call" and not t.get("synthetic")
                    and t["name"] != harness.CHANGELOG_TOOL]
            i = len(real)
            if i >= len(steps):
                return {"final": "DONE"}
            args = dict(steps[i])
            if i > 0:
                first = json.loads(next(t for t in transcript if t["role"] == "tool_result"
                                        and t["name"] == tools[0])["content"])
                args = {k: first.get(v[3:], v) if isinstance(v, str) and v.startswith("$1.") else v
                        for k, v in args.items()}
            return {"name": tools[i], "args": args, "usage": {"in": 10, "out": 2},
                    "meta": {"provider": "fake"}}
        return call_model
    return make


# ---------------- condition construction ----------------

def test_replicate_cell_is_byte_identical_to_condition_C():
    for task, cls in PAIRS:
        a = harness.build_condition(task, "C", cls)
        b = harness.build_condition(task, p1.REPLICATE_C, cls)
        for k in ("system", "declarations", "active", "profile", "retry"):
            assert a[k] == b[k], (task["id"], k)
        assert b["user_suffix"] == "" and b["preamble"] == []


def test_every_phase1_condition_builds_strict_v2_for_every_pair():
    v2 = harness.frozen()["v2_schemas"]
    for task, cls in PAIRS:
        for cond in harness.PHASE1_CONDS:
            s = harness.build_condition(task, cond, cls)
            assert s["profile"] == "strict" and s["retry"] is False
            assert s["active"][task["drift_tool"]] == v2[f"{task['drift_tool']}::{cls}"]


def test_placements_put_the_note_in_exactly_one_place():
    task, cls = PAIRS[0]
    for fmt in harness.FORMATS:
        for instr in harness.INSTRS:
            sys_ = harness.build_condition(task, f"C:sys:{fmt}:{instr}", cls)
            usr = harness.build_condition(task, f"C:user:{fmt}:{instr}", cls)
            tool = harness.build_condition(task, f"C:tool:{fmt}:{instr}", cls)
            assert sys_["system"] != harness.SYSTEM and not sys_["user_suffix"] and not sys_["preamble"]
            assert usr["system"] == harness.SYSTEM and "change log" in usr["user_suffix"] and not usr["preamble"]
            assert tool["system"] == harness.SYSTEM and not tool["user_suffix"]
            assert [t["role"] for t in tool["preamble"]] == ["assistant_tool_call", "tool_result"]
            assert any(d["name"] == harness.CHANGELOG_TOOL for d in tool["declarations"])
            note = {"sys": sys_["system"], "user": usr["user_suffix"], "tool": tool["preamble"][1]["content"]}
            for place, text in note.items():
                assert ("step by step" in text) == (instr == "apply"), (place, instr)
                assert (('"change"' in text) if fmt == "json" else ("Plain-language" in text)), (place, fmt)


def test_prose_templates_cover_every_diff():
    for diff in harness.frozen()["diffs"].values():
        for ch in diff["changes"]:
            s = harness.prose_change(ch)
            assert ch["param"] in s or ch.get("old", "") in s
            assert harness.old_contract(ch).startswith(" (previous")


def test_c_decl_keeps_v1_names_and_writes_the_change_into_the_parameter():
    for task, cls in PAIRS:
        s = harness.build_condition(task, "C_decl", cls)
        d = drift_decl(s, task)
        ch = drift_change(task, cls)
        v1 = harness.frozen()["tools_v1"][task["drift_tool"]]["params"]
        assert set(d["parameters"]["properties"]) == set(v1)
        assert "CHANGED:" in d["parameters"]["properties"][ch["param"]]["description"]
        assert s["system"] == harness.SYSTEM


def test_cd_and_dprime_show_v2():
    for task, cls in PAIRS:
        ch = drift_change(task, cls)
        v2 = harness.frozen()["v2_schemas"][f"{task['drift_tool']}::{cls}"]
        cd = harness.build_condition(task, "CD", cls)
        dp = harness.build_condition(task, "Dprime", cls)
        assert set(drift_decl(cd, task)["parameters"]["properties"]) == set(v2)
        assert "current version" in cd["system"]
        props = drift_decl(dp, task)["parameters"]["properties"]
        assert set(props) == set(v2) and dp["system"] == harness.SYSTEM
        pname = ch["new"] if ch["change"] == "renamed" else ch["param"]
        assert "(previous" in props[pname]["description"]


# ---------------- episodes with fake models ----------------

@pytest.mark.parametrize("cond", harness.PHASE1_CONDS)
def test_v2_oracle_succeeds_in_every_condition(cond):
    for task, cls in PAIRS:
        rec = harness.run_episode(task, cond, cls, oracle("v2")(task, cls))
        assert rec["success"], (cond, task["id"], cls, rec["error_seen"])
        assert rec["usage"]["in"] > 0 and rec["meta"] == {"provider": "fake"}


def test_rejected_calls_are_logged_with_their_arguments():
    n = 0
    for task, cls in PAIRS:
        if cls != "rename":
            continue
        rec = harness.run_episode(task, p1.REPLICATE_C, cls, oracle("v1")(task, cls))
        assert rec["drift_outcome"] == "ERROR_SURFACED"
        calls = [t for t in rec["transcript"] if t["role"] == "assistant_tool_call"]
        old = drift_change(task, cls)["old"]
        assert any(old in c["args"] for c in calls if c["name"] == task["drift_tool"])
        assert rec["transcript"][-1]["content"].startswith("Error:")
        n += 1
    assert n == 24


def test_tool_placement_preamble_is_logged_and_a_changelog_call_is_answered():
    task, cls = PAIRS[0]
    asked = []

    def model(system, user, decls, transcript):
        if not asked:
            asked.append(1)
            return {"name": harness.CHANGELOG_TOOL, "args": {"tool": task["drift_tool"]}}
        return {"final": "DONE"}
    rec = harness.run_episode(task, "C:tool:prose:none", cls, model)
    roles = [(t["role"], t.get("synthetic", False)) for t in rec["transcript"]]
    assert roles[:2] == [("assistant_tool_call", True), ("tool_result", True)]
    assert rec["transcript"][3]["content"] == rec["transcript"][1]["content"]  # same note handed over
    assert rec["final_text"] == "DONE" and rec["calls_made"] == 1


# ---------------- grid ----------------

def test_grid_sizes_and_unique_keys():
    sizes = {"ablation": 13 * 120, "infoform": 2 * 120, "noise": 30 * 5}
    for arm, n in sizes.items():
        js = p1.jobs(arm)
        assert len(js) == n
        assert len({p1.key(t["id"], c, cls, ph, rep, "default") for t, c, cls, ph, rep in js}) == n
    js = p1.jobs("thinking", ["C:sys:json:none", "C_decl"])
    assert len(js) == 240
    with pytest.raises(SystemExit):
        p1.jobs("thinking", ["C"])  # original C is not a Phase-1 condition


def test_jobs_are_deterministic():
    a = [(t["id"], c, cls, rep) for t, c, cls, ph, rep in p1.jobs("ablation")]
    b = [(t["id"], c, cls, rep) for t, c, cls, ph, rep in p1.jobs("ablation")]
    assert a == b


def test_phase1_logs_are_invisible_to_the_original_analysis():
    import analyze
    assert p1.OUT_DIR.parent == analyze.RESULTS
    assert not list(analyze.RESULTS.glob("runs_*.jsonl")) or all(
        f.parent == analyze.RESULTS for f in analyze.RESULTS.glob("runs_*.jsonl"))
    assert "phase1" not in {f.parent.name for f in analyze.RESULTS.glob("runs_*.jsonl")}
    assert p1.tag(p1.jobs("noise")[0], "default").startswith("p1-")


def test_pilot_runs_go_to_a_separate_file():
    assert p1.out_path("m/x", pilot=True).name == "runs_m_x.pilot.jsonl"
    assert p1.out_path("m/x").name == "runs_m_x.jsonl"


# ---------------- runner logging and resume (Task 3) ----------------

def test_or_body_strict_and_provider():
    import run_openrouter as ro
    decls = [{"name": "t1", "parameters": {}}, {"name": "t2", "parameters": {}}]
    msgs = [{"role": "user", "content": "hi"}]
    body = ro.or_body("m/x", msgs, decls, 700, strict=False, provider="openai")
    assert all(t["function"]["strict"] is False for t in body["tools"])
    assert body["provider"] == {"order": ["openai"], "allow_fallbacks": False}
    assert "strict" not in decls[0]  # declarations are not mutated
    plain = ro.or_body("m/x", msgs, decls, 700)
    assert all("strict" not in t["function"] for t in plain["tools"])
    assert "provider" not in plain and "reasoning" not in plain
    assert ro.or_body("m/x", msgs, decls, 4000, reasoning="high")["reasoning"] == {"effort": "high"}


def test_parse_or_response_logs_reasoning_and_provider():
    import run_openrouter as ro
    resp = {"provider": "OpenAI", "model": "openai/gpt-5.6-luna",
            "usage": {"prompt_tokens": 100, "completion_tokens": 50,
                      "completion_tokens_details": {"reasoning_tokens": 30}},
            "choices": [{"finish_reason": "tool_calls", "message": {"tool_calls": [
                {"function": {"name": "f", "arguments": '{"a": 1}'}}]}}]}
    out = ro.parse_or_response(resp)
    assert out["name"] == "f" and out["args"] == {"a": 1}
    assert out["usage"] == {"in": 100, "out": 50, "reasoning": 30}
    assert out["meta"] == {"provider": "OpenAI", "model": "openai/gpt-5.6-luna", "finish_reason": "tool_calls"}
    resp["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"] = "{not json"
    assert ro.parse_or_response(resp)["args"] == {}
    final = ro.parse_or_response({"usage": {}, "choices": [{"finish_reason": "stop", "message": {"content": "done"}}]})
    assert final["final"] == "done" and final["usage"] == {"in": 0, "out": 0, "reasoning": 0}


def test_parse_gemini_response_counts_thoughts():
    import run_gemini as rg
    resp = {"modelVersion": "v1", "usageMetadata": {"promptTokenCount": 10, "candidatesTokenCount": 5,
                                                   "thoughtsTokenCount": 7},
            "candidates": [{"finishReason": "STOP", "content": {"parts": [{"functionCall": {"name": "f", "args": {"a": 1}}}]}}]}
    out = rg.parse_gemini_response(resp, "MINIMAL")
    assert out["usage"] == {"in": 10, "out": 12, "reasoning": 7}
    assert out["name"] == "f" and out["args"] == {"a": 1}
    assert out["meta"] == {"model": "v1", "thinking": "MINIMAL", "finish_reason": "STOP"}
    assert rg.parse_gemini_response({"usageMetadata": {}}, "LOW")["final"] == "(empty)"


def test_runners_import_without_env(tmp_path):
    import subprocess
    guard = ("import pathlib, sys\n"
             "real = pathlib.Path.read_text\n"
             "def guard(self, *a, **k):\n"
             "    if self.name == '.env':\n"
             "        raise AssertionError('.env read at import')\n"
             "    return real(self, *a, **k)\n"
             "pathlib.Path.read_text = guard\n"
             f"sys.path.insert(0, {str(HERE)!r})\n"
             "import run_openrouter, run_gemini\n")
    res = subprocess.run([sys.executable, "-c", guard], capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    import run_gemini as rg
    import run_openrouter as ro
    with pytest.raises(SystemExit, match="OPENROUTER_API_KEY"):
        ro._key(tmp_path / ".env")
    env = tmp_path / ".env"
    env.write_text("GEMINI_API_KEY=\nOPENROUTER_API_KEY= abc \n")
    assert ro._key(env) == "abc"
    with pytest.raises(SystemExit, match="GEMINI_API_KEY"):
        rg._key(env)  # present but empty


def test_episode_usage_sums_reasoning():
    t, cls = PAIRS[0]

    def two_calls(system, user, decls, transcript):
        u = {"in": 10, "out": 2, "reasoning": 1}
        if not transcript:
            return {"name": "no_such_tool", "args": {}, "usage": u}
        return {"final": "done", "usage": u}

    rec = harness.run_episode(t, "B_strict", cls, two_calls)
    assert rec["usage"] == {"in": 20, "out": 4, "reasoning": 2}


def test_repair_tail_drops_partial_line(tmp_path):
    f = tmp_path / "runs.jsonl"
    assert p1.repair_tail(f) == 0  # missing file
    good = json.dumps({"task": "T", "cond": "A", "class": "rename", "phrasing": 0}) + "\n"
    f.write_text(good + '{"b":')
    assert p1.repair_tail(f) == 5
    assert f.read_text() == good
    assert p1.repair_tail(f) == 0 and f.read_text() == good  # clean file unchanged
    assert len(p1.load_done(f)) == 1
    f.write_text('{"b":')
    assert p1.repair_tail(f) == 5 and f.read_text() == ""


def test_route_jobs_and_paths():
    js = p1.jobs("route")
    assert len(js) == 360
    assert {c for _, c, _, _, _ in js} == {"A", "B_strict", "C:sys:json:none"}
    assert p1.out_path("openai/gpt-5.6-luna", route="nostrict").name == "runs_openai_gpt-5.6-luna.nostrict.jsonl"
    assert p1.out_path("m/x", pilot=True, route="az").name == "runs_m_x.az.pilot.jsonl"
    with pytest.raises(SystemExit):
        p1.out_path("m/x", route="../evil")
    t, c, cls, ph, rep = js[0]
    rec = p1.run_episode(js[0], lambda *a: {"final": "x"}, "m/x", "route", "default", 700, route="az")
    assert rec["route"] == "az"


def test_load_pins_reads_the_request_settings_a_file_was_written_with(tmp_path):
    f = tmp_path / "runs.jsonl"
    assert p1.load_pins(f) == set()
    rows = [{"task": "T", "pin": {"provider": "openai", "strict": "unset"}},
            {"task": "U", "pin": {"strict": "unset", "provider": "openai"}},
            {"task": "V"}]
    f.write_text("".join(json.dumps(r) + "\n" for r in rows))
    assert p1.load_pins(f) == {p1.pin_id({"provider": "openai", "strict": "unset"})}
