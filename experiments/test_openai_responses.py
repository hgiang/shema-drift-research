#!/usr/bin/env python3
"""Tests for the OpenAI Responses API adapter (luna direct, Phase 2). No network.

Run: python3 -m pytest test_openai_responses.py -q
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import openai_responses as oa  # noqa: E402
import run_openrouter as ro  # noqa: E402

MSGS = ro.or_messages("SYS", "do it", [
    {"role": "assistant_tool_call", "name": "get_changelog", "args": {"tool": "t1"}},
    {"role": "tool_result", "name": "get_changelog", "content": "t1 changed"}])
PARAMS = {"type": "object", "properties": {"a": {"type": "integer"}}, "required": ["a"]}
DECLS = [{"name": "t1", "description": "d", "parameters": PARAMS}]


def test_input_mirrors_the_chat_messages():
    assert oa.to_input(MSGS) == [
        {"role": "system", "content": "SYS"},
        {"role": "user", "content": "do it"},
        {"type": "function_call", "call_id": "c1", "name": "get_changelog", "arguments": '{"tool": "t1"}'},
        {"type": "function_call_output", "call_id": "c1", "output": "t1 changed"}]


def test_body_sends_no_temperature_and_no_reasoning_by_default():
    body = oa.body("openai/gpt-5.6-luna", MSGS, DECLS, 700)
    assert body["model"] == "gpt-5.6-luna"
    assert body["max_output_tokens"] == 700 and body["store"] is False
    assert not {"temperature", "reasoning", "provider", "max_tokens", "messages"} & set(body)
    assert body["tools"] == [{"type": "function", "name": "t1", "description": "d", "parameters": PARAMS}]
    assert body["input"] == oa.to_input(MSGS)


def test_body_strict_flag_and_reasoning_effort():
    assert oa.body("gpt-5.6-luna", MSGS, DECLS, 700, strict=False)["tools"][0]["strict"] is False
    assert oa.body("gpt-5.6-luna", MSGS, DECLS, 700, reasoning="high")["reasoning"] == {"effort": "high"}
    assert DECLS == [{"name": "t1", "description": "d", "parameters": PARAMS}]  # inputs not mutated


REASONING = {"type": "reasoning", "summary": []}
CALL = {"type": "function_call", "call_id": "x", "name": "t1", "arguments": '{"a": 1}'}
MSG = {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "Done."}]}


def resp(output, status="completed", reason=None):
    return {"model": "gpt-5.6-luna-2026-09-01", "status": status,
            "incomplete_details": {"reason": reason} if reason else None, "output": output,
            "usage": {"input_tokens": 50, "output_tokens": 120, "output_tokens_details": {"reasoning_tokens": 100}}}


def test_parse_tool_call():
    assert oa.parse(resp([REASONING, CALL])) == {
        "name": "t1", "args": {"a": 1}, "usage": {"in": 50, "out": 120, "reasoning": 100},
        "meta": {"provider": "openai-direct", "model": "gpt-5.6-luna-2026-09-01", "finish_reason": "tool_calls"}}


def test_parse_text_beside_a_call_and_a_final_answer():
    assert oa.parse(resp([MSG, CALL]))["text"] == "Done."
    final = oa.parse(resp([REASONING, MSG]))
    assert final["final"] == "Done." and final["meta"]["finish_reason"] == "stop" and "name" not in final


def test_parse_truncation_filters_and_bad_arguments():
    cut = oa.parse(resp([REASONING], status="incomplete", reason="max_output_tokens"))
    assert cut["final"] == "" and cut["meta"]["finish_reason"] == "length"  # the checker's truncation word
    assert oa.parse(resp([], status="incomplete", reason="content_filter"))["meta"]["finish_reason"] == "content_filter"
    assert oa.parse(resp([{**CALL, "arguments": "{oops"}]))["args"] == {}
    assert oa.parse({"output": None})["usage"] == {"in": 0, "out": 0, "reasoning": 0}


def test_cost_usage_feeds_log_cost():
    assert oa.cost_usage({"in": 50, "out": 120, "reasoning": 100}) == {"prompt_tokens": 50, "completion_tokens": 120}
