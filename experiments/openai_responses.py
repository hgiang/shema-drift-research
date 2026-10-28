#!/usr/bin/env python3
"""OpenAI Responses API adapter for luna on the OpenAI direct endpoint (Phase 2).

luna's /v1/chat/completions refuses function tools at its default reasoning effort, so the
direct route posts to /v1/responses (MILESTONES.md "Phase 2 addendum — 2026-10-28"). The
request mirrors the OpenRouter one except that no temperature is sent (the API rejects it
for luna) and the token limit is max_output_tokens. Replies are parsed into the shape
run_openrouter.parse_or_response returns, so the harness and the log checker see no
difference.
"""

import json

URL = "https://api.openai.com/v1/responses"
PROVIDER = "openai-direct"


def to_input(messages):
    """Chat messages from run_openrouter.or_messages -> Responses input items (same call ids)."""
    items = []
    for m in messages:
        if m["role"] == "assistant":
            items += [{"type": "function_call", "call_id": tc["id"], "name": tc["function"]["name"],
                       "arguments": tc["function"]["arguments"]} for tc in m["tool_calls"]]
        elif m["role"] == "tool":
            items.append({"type": "function_call_output", "call_id": m["tool_call_id"], "output": m["content"]})
        else:
            items.append({"role": m["role"], "content": m["content"]})
    return items


def body(model, messages, declarations, max_tokens, reasoning="default", strict=None):
    """Request body; strict=None leaves the per-tool flag out, reasoning "default" sends none."""
    tools = [{"type": "function", **d, **({} if strict is None else {"strict": strict})} for d in declarations]
    out = {"model": model.split("/", 1)[1] if model.startswith("openai/") else model,
           "input": to_input(messages), "tools": tools, "max_output_tokens": max_tokens, "store": False}
    return out if reasoning == "default" else {**out, "reasoning": {"effort": reasoning}}


def _finish_reason(resp, has_call):
    """Chat-style finish reason: "length" on a max_output_tokens cut, as the log checker expects."""
    reason = (resp.get("incomplete_details") or {}).get("reason")
    if reason:
        return "length" if reason == "max_output_tokens" else reason
    return "tool_calls" if has_call else "stop"


def parse(resp):
    """{"name","args"[,"text"]} or {"final"}, plus usage (with reasoning tokens) and serving meta."""
    output = resp.get("output") or []
    usage = resp.get("usage") or {}
    calls = [o for o in output if o.get("type") == "function_call"]
    text = "".join(c.get("text", "") for o in output if o.get("type") == "message"
                   for c in o.get("content") or [] if c.get("type") == "output_text")
    extra = {"usage": {"in": usage.get("input_tokens", 0), "out": usage.get("output_tokens", 0),
                       "reasoning": (usage.get("output_tokens_details") or {}).get("reasoning_tokens") or 0},
             "meta": {"provider": PROVIDER, "model": resp.get("model"),
                      "finish_reason": _finish_reason(resp, bool(calls))}}
    if not calls:
        return {"final": text, **extra}
    try:
        args = json.loads(calls[0].get("arguments") or "{}")
    except json.JSONDecodeError:
        args = {}
    return {"name": calls[0].get("name", ""), "args": args, **({"text": text} if text else {}), **extra}


def cost_usage(usage):
    """Parsed usage -> the keys cost_tracker.log_cost reads (output tokens include reasoning)."""
    return {"prompt_tokens": usage["in"], "completion_tokens": usage["out"]}
