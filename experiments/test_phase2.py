#!/usr/bin/env python3
"""Tests for the Phase 2 conditions, job grid and runner plumbing. No API calls: fake models only.

Run: python3 -m pytest test_phase2.py -q
"""

import json
import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402
import phase2_grid as p2  # noqa: E402
from test_phase1 import oracle  # noqa: E402

PAIRS = p1.primary_pairs()


# ---------------- fill conditions (MILESTONES.md "Phase 2 pre-registration") ----------------

def test_fill_system_changes_one_sentence():
    old = "Use parameter defaults by omitting a parameter when the user does not specify it."
    new = ("Pass every parameter explicitly, including optional ones; when the user does not "
           "specify a value, pass the documented default.")
    assert old in harness.SYSTEM and new not in harness.SYSTEM
    assert harness.FILL_SYSTEM == harness.SYSTEM.replace(old, new)


@pytest.mark.parametrize("fill,base", [("A_fill", "A"), ("B_fill", "B_strict")])
def test_fill_conditions_differ_from_their_base_only_in_the_system_prompt(fill, base):
    for task, cls in PAIRS:
        got, ref = harness.build_condition(task, fill, cls), harness.build_condition(task, base, cls)
        assert got["system"] == harness.FILL_SYSTEM
        assert {k: v for k, v in got.items() if k != "system"} == {k: v for k, v in ref.items() if k != "system"}


def test_a_fill_is_scored_like_a():
    for task, cls in PAIRS[:20]:
        rec = harness.run_episode(task, "A_fill", cls, oracle("v1")(task, cls))
        assert rec["success"] and rec["drift_outcome"] is None


def test_b_fill_is_scored_like_b_strict():
    for task, cls in PAIRS[:20]:
        fill = harness.run_episode(task, "B_fill", cls, oracle("v1")(task, cls))
        base = harness.run_episode(task, "B_strict", cls, oracle("v1")(task, cls))
        assert (fill["success"], fill["drift_outcome"]) == (base["success"], base["drift_outcome"])
        assert harness.run_episode(task, "B_fill", cls, oracle("v2")(task, cls))["success"]


def test_model_text_beside_a_tool_call_is_logged():
    task, cls = PAIRS[0]
    v2 = oracle("v2")(task, cls)

    def chatty(system, user, decls, transcript):
        out = v2(system, user, decls, transcript)
        return {**out, "text": "Sure, calling it now."} if "name" in out else out

    rec = harness.run_episode(task, "B_strict", cls, chatty)
    calls = [t for t in rec["transcript"] if t["role"] == "assistant_tool_call"]
    assert calls[0]["text"] == "Sure, calling it now."
    plain = harness.run_episode(task, "B_strict", cls, v2)
    assert all("text" not in t for t in plain["transcript"])


# ---------------- grid ----------------

def test_jobs_sizes_and_unique_keys():
    sizes = {"core": 720, "phrasing": 240, "noise": 150, "infoform": 240, "placement": 120,
             "fill": 360, "direct": 480}
    assert set(sizes) == set(p2.ARMS)
    for arm, n in sizes.items():
        js = p2.jobs(arm)
        assert len(js) == n, arm
        assert len({(t["id"], c, cls, ph, rep) for t, c, cls, ph, rep in js}) == n, arm
    assert {c for _, c, _, _, _ in p2.jobs("fill")} == {"A_fill", "B_fill", "B_strict"}
    assert {c for _, c, _, _, _ in p2.jobs("direct")} == {"A", "B_strict", "C:sys:json:none", "C:user:prose:apply"}
    assert {c for _, c, _, _, _ in p2.jobs("placement")} == {"C:user:prose:apply"}
    assert {ph for _, _, _, ph, _ in p2.jobs("phrasing")} == {1}


def test_core_jobs_match_september():
    from run_gemini import jobs_for_grid
    sept = {(t["id"], c, cls, ph) for t, c, cls, ph in jobs_for_grid("core", "primary")}
    assert {(t["id"], c, cls, ph) for t, c, cls, ph, _ in p2.jobs("core")} == sept


def test_noise_jobs_match_september():
    from run_gemini import jobs_for_grid
    sept = {(t["id"], c, cls, ph, rep) for t, c, cls, ph, rep in jobs_for_grid("noise", "primary")}
    assert {(t["id"], c, cls, ph, rep) for t, c, cls, ph, rep in p2.jobs("noise")} == sept


def test_jobs_are_deterministic_and_unknown_arm_fails():
    assert [(t["id"], c) for t, c, *_ in p2.jobs("core")] == [(t["id"], c) for t, c, *_ in p2.jobs("core")]
    with pytest.raises(SystemExit):
        p2.jobs("ablation")


def test_out_path_under_phase2():
    assert p2.out_path("m/x").parent == p1.ROOT / "results" / "phase2"
    assert p2.out_path("m/x", pilot=True).name == "runs_m_x.pilot.jsonl"
    assert p2.out_path("openai/gpt-5.6-luna", endpoint="openai").name == "runs_openai_gpt-5.6-luna.openai.jsonl"
    assert p2.out_path("m/x", endpoint="openrouter").name == "runs_m_x.jsonl"
    with pytest.raises(SystemExit):
        p2.out_path("m/x", endpoint="../evil")


def test_run_episode_record_and_tag():
    job = p2.jobs("fill")[0]
    pin = {"provider": "google", "endpoint": "gemini", "strict": "unset"}
    rec = p2.run_episode(job, lambda *a: {"final": "x"}, "m/x", "fill", "MINIMAL", 1024, pin)
    assert rec["phase"] == "phase2" and rec["pin"] == pin and rec["arm"] == "fill"
    assert p1.rec_key(rec) == p1.key(job[0]["id"], job[1], job[2], 0, 0, "MINIMAL")
    assert p2.tag(job, "MINIMAL").startswith("p2-")


def test_phase2_logs_are_invisible_to_the_original_analysis():
    import analyze
    assert all("phase2" not in str(f) for f in analyze.RESULTS.glob("runs_*.jsonl"))


def test_token_costs_ignore_later_phases(tmp_path, monkeypatch):
    import analyze
    before = analyze.token_costs()
    log = tmp_path / "cost_log.jsonl"
    log.write_text((HERE / "cost_log.jsonl").read_text() + json.dumps(
        {"phase": "phase2", "model": "anthropic/claude-haiku-5.5", "tag": "p2-x01-B_strict-rename-p0-r0-default",
         "tokens_in": 9999, "tokens_out": 1}) + "\n")
    monkeypatch.setattr(analyze, "HERE", tmp_path)
    assert analyze.token_costs() == before


# ---------------- runner plumbing ----------------

MSGS = [{"role": "user", "content": "hi"}]
DECLS = [{"name": "t1", "parameters": {}}]


def test_or_body_quantization_pin():
    import run_openrouter as ro
    body = ro.or_body("m/x", MSGS, DECLS, 700, provider="novita", quantization="bf16")
    assert body["provider"] == {"order": ["novita"], "allow_fallbacks": False, "quantizations": ["bf16"]}
    assert ro.or_body("m/x", MSGS, DECLS, 700, provider="openai")["provider"] == {
        "order": ["openai"], "allow_fallbacks": False}
    assert body["max_tokens"] == 700 and body["temperature"] == 0
    assert ro.or_body("m/x", MSGS, DECLS, 700, reasoning="high")["reasoning"] == {"effort": "high"}


def _responses_reply():
    return {"model": "gpt-5.6-luna-2026-09-01", "status": "completed", "output": [
        {"type": "function_call", "call_id": "x", "name": "t1", "arguments": "{}"}],
        "usage": {"input_tokens": 10, "output_tokens": 20, "output_tokens_details": {"reasoning_tokens": 15}}}


def test_openai_direct_posts_to_the_responses_api(monkeypatch):
    """Addendum 2026-10-28: luna's chat completions refuse function tools at its default
    reasoning, so the OpenAI direct endpoint is /v1/responses (no temperature sent)."""
    import openai_responses as oa
    import run_openrouter as ro
    sent, logged = {}, []
    monkeypatch.setattr(ro, "or_call", lambda model, body, endpoint: sent.update(body=body, endpoint=endpoint)
                        or _responses_reply())
    monkeypatch.setattr(ro, "log_cost", lambda model, tag, usage, phase: logged.append((model, usage, phase)) or 0.0)
    monkeypatch.setattr(ro, "check_budget", lambda: 0.0)
    call = ro.make_call_model("openai/gpt-5.6-luna", ["t"], phase="phase2", strict=False, endpoint="openai")
    out = call("SYS", "hi", DECLS, [])
    assert sent == {"endpoint": "openai",
                    "body": oa.body("openai/gpt-5.6-luna", ro.or_messages("SYS", "hi", []), DECLS, 700, strict=False)}
    assert out["name"] == "t1" and out["meta"]["provider"] == "openai-direct"
    assert logged == [("openai/gpt-5.6-luna", {"prompt_tokens": 10, "completion_tokens": 20}, "phase2")]
    with pytest.raises(SystemExit, match="no --provider"):
        ro.make_call_model("openai/gpt-5.6-luna", ["t"], provider="openai", endpoint="openai")


def test_or_call_keeps_the_error_body(monkeypatch):
    import io
    import urllib.error
    import run_openrouter as ro

    def reject(req, timeout):
        raise urllib.error.HTTPError(req.full_url, 400, "Bad Request", {}, io.BytesIO(b'{"error": "no temperature"}'))
    monkeypatch.setattr(ro.urllib.request, "urlopen", reject)
    monkeypatch.setattr(ro, "_env_value", lambda name: "k")
    with pytest.raises(RuntimeError, match='HTTP 400 from openai: {"error": "no temperature"}'):
        ro.or_call("m", {}, endpoint="openai")


def test_endpoints_and_keys(tmp_path):
    import run_openrouter as ro
    assert ro.ENDPOINTS["openrouter"]["url"].startswith("https://openrouter.ai/")
    assert ro.ENDPOINTS["openai"]["url"] == "https://api.openai.com/v1/responses"
    env = tmp_path / ".env"
    env.write_text("OPENROUTER_API_KEY=a\nOPENAI_API_KEY= b \n")
    assert ro._env_value("OPENAI_API_KEY", env) == "b"
    empty = tmp_path / "empty.env"  # a new path: values are cached per (name, path)
    empty.write_text("OPENAI_API_KEY=\n")
    with pytest.raises(SystemExit, match="OPENAI_API_KEY"):
        ro._env_value("OPENAI_API_KEY", empty)


def test_parse_claude_text_plus_tool_call():
    import run_openrouter as ro
    resp = {"provider": "Anthropic", "model": "anthropic/claude-haiku-5.5", "usage": {},
            "choices": [{"finish_reason": "tool_calls", "message": {
                "content": "I'll book that.", "tool_calls": [{"function": {"name": "f", "arguments": "{}"}}]}}]}
    out = ro.parse_or_response(resp)
    assert out["name"] == "f" and out["text"] == "I'll book that."
    resp["choices"][0]["message"]["content"] = ""
    assert "text" not in ro.parse_or_response(resp)


def test_phase2_pin_records_endpoint_and_quantization():
    import run_openrouter as ro
    args = type("A", (), {"provider": "novita", "strict": "unset", "endpoint": "openrouter",
                          "quantization": "bf16"})()
    args.max_tokens = 0
    assert ro.phase2_pin(args) == {"provider": "novita", "strict": "unset", "endpoint": "openrouter",
                                   "quantization": "bf16", "max_tokens": 700}
    args.endpoint, args.provider, args.quantization, args.max_tokens = "openai", None, None, 900
    assert ro.phase2_pin(args) == {"provider": "openai-direct", "strict": "unset", "endpoint": "openai",
                                   "quantization": None, "max_tokens": 900}


def test_runner_arm_validation():
    import run_openrouter as ro
    with pytest.raises(SystemExit, match="Phase 2 arm"):
        ro.check_phase_arm(2, "ablation")
    with pytest.raises(SystemExit, match="Phase 1 arm"):
        ro.check_phase_arm(1, "fill")
    with pytest.raises(SystemExit, match="Phase 2 arm"):
        ro.check_phase_arm(2, "fill")  # Gemini only
    ro.check_phase_arm(2, "core")
    ro.check_phase_arm(1, "ablation")


def test_gemini_phase2_runs_only_the_fill_arm(tmp_path, monkeypatch):
    import run_gemini as rg
    assert rg.phase2_pin() == {"provider": "google", "strict": "unset", "endpoint": "gemini", "quantization": None}
    args = type("A", (), {"model": "gemini-3.6-flash", "arm": "core", "limit": 0, "phase": 2})()
    with pytest.raises(SystemExit, match="fill"):
        rg.run_phase2(args)


def test_gemini_phase2_writes_pinned_records(tmp_path, monkeypatch):
    import run_gemini as rg
    monkeypatch.setattr(p2, "OUT_DIR", tmp_path)
    task_by_id = {t["id"]: t for t, _ in PAIRS}

    def fake_make_call_model(model, tag_holder, phase="experiments"):
        assert phase == "phase2"
        oracles = {}

        def call_model(system, user, decls, transcript):
            assert system == harness.FILL_SYSTEM or system == harness.SYSTEM
            t_id, cls = tag_holder[0].split("-")[1], tag_holder[0].split("-")[3]
            key = (t_id, cls)
            oracles.setdefault(key, oracle("v2")(task_by_id[t_id], cls))
            return oracles[key](system, user, decls, transcript)
        return call_model
    monkeypatch.setattr(rg, "make_call_model", fake_make_call_model)
    args = type("A", (), {"model": "gemini-3.6-flash", "arm": "fill", "limit": 4, "phase": 2})()
    rg.run_phase2(args)
    rows = [json.loads(l) for l in (tmp_path / "runs_gemini-3.6-flash.pilot.jsonl").read_text().splitlines()]
    assert len(rows) == 4 and all(r["pin"] == rg.phase2_pin() and r["phase"] == "phase2" for r in rows)
    assert all(r["reasoning"] == "MINIMAL" and r["max_tokens"] == 1024 for r in rows)
    rg.run_phase2(args)  # resume: nothing new
    assert len((tmp_path / "runs_gemini-3.6-flash.pilot.jsonl").read_text().splitlines()) == 4


def _or_args(**kw):
    base = {"model": "anthropic/claude-haiku-5.5", "arm": "placement", "limit": 3, "phase": 2,
            "provider": "anthropic", "strict": "unset", "endpoint": "openrouter", "quantization": None,
            "reasoning": "default", "cap": 1.0, "max_tokens": 0}
    return type("A", (), {**base, **kw})()


def test_openrouter_phase2_run_resume_and_pin_refusal(tmp_path, monkeypatch):
    import run_openrouter as ro
    monkeypatch.setattr(p2, "OUT_DIR", tmp_path)
    task_by_id = {t["id"]: t for t, _ in PAIRS}
    seen = {}

    def fake_make_call_model(model, tag_holder, reasoning, max_tokens, provider, phase, strict,
                             quantization, endpoint):
        seen.update(phase=phase, provider=provider, endpoint=endpoint, quantization=quantization)

        def call_model(system, user, decls, transcript):
            t_id, cls = tag_holder[0].split("-")[1], tag_holder[0].split("-")[3]
            return oracle("v2")(task_by_id[t_id], cls)(system, user, decls, transcript)
        return call_model
    monkeypatch.setattr(ro, "make_call_model", fake_make_call_model)
    ro.run_phase2(_or_args())
    path = tmp_path / "runs_anthropic_claude-haiku-5.5.pilot.jsonl"
    rows = [json.loads(l) for l in path.read_text().splitlines()]
    assert len(rows) == 3 and all(r["success"] and r["arm"] == "placement" for r in rows)
    assert rows[0]["pin"] == ro.phase2_pin(_or_args()) and seen["phase"] == "phase2"
    ro.run_phase2(_or_args())  # resume: nothing new
    assert len(path.read_text().splitlines()) == 3
    with pytest.raises(SystemExit, match="other request settings"):
        ro.run_phase2(_or_args(strict="false"))
    with pytest.raises(SystemExit, match="other request settings"):
        ro.run_phase2(_or_args(max_tokens=900))
    with pytest.raises(SystemExit, match="--provider"):
        ro.run_phase2(_or_args(provider=None))
    ro.run_phase2(_or_args(model="openai/gpt-5.6-luna", arm="direct", endpoint="openai", provider=None, limit=2))
    assert (tmp_path / "runs_openai_gpt-5.6-luna.openai.pilot.jsonl").exists() and seen["endpoint"] == "openai"
