#!/usr/bin/env python3
"""Tokenizer-measured sizes of the artifacts the conditions show (HANDOFF accounting fix:
the September token_costs used chars/4; its diff/declaration ratio was 0.137).

Artifacts per drift (tool::class), built with the same harness functions the conditions use:
  diff_json, diff_prose, v2_declaration, c_decl_suffix, dprime_suffix, cd_note
Encoders: tiktoken o200k_base (luna family), the Qwen2.5 tokenizer, Gemini countTokens
(when GEMINI_API_KEY is in .env), and chars/4 for comparison. A missing encoder is
recorded as null with the reason, never silently skipped.

Writes results/phase1/artifact_tokens.json (analyze.py copies it into phase1.accounting).
Usage:  python3 count_artifact_tokens.py
"""

import json
import pathlib
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402

ARTIFACTS = ("diff_json", "diff_prose", "v2_declaration", "c_decl_suffix", "dprime_suffix", "cd_note")
OUT = p1.OUT_DIR / "artifact_tokens.json"
QWEN_TOKENIZER = "Qwen/Qwen2.5-7B-Instruct"
GEMINI_COUNT_MODEL = "gemini-3.6-flash"


def artifacts(key):
    """The six texts for one drift, exactly as the conditions render them."""
    fz = harness.frozen()
    tool = key.split("::")[0]
    changes = fz["diffs"][key]["changes"]
    diff_json = json.dumps(changes, indent=1)
    return {
        "diff_json": diff_json,
        "diff_prose": "\n".join(f"- {harness.prose_change(ch)}" for ch in changes),
        "v2_declaration": json.dumps(harness.declaration(tool, fz["tools_v1"][tool], fz["v2_schemas"][key])),
        "c_decl_suffix": " CHANGED: " + harness.prose_change(changes[0]),
        "dprime_suffix": harness.old_contract(changes[0]),
        "cd_note": harness.CD_NOTE.format(tool=tool, diff=diff_json),
    }


def count(texts, encode):
    return {name: len(encode(text)) for name, text in texts.items()}


def summarize(per_key):
    names = list(next(iter(per_key.values())))
    means = {n: sum(v[n] for v in per_key.values()) / len(per_key) for n in names}
    return {"means": means, "ratio_diff_json_to_v2_declaration": means["diff_json"] / means["v2_declaration"]}


def encoders():  # pragma: no cover - needs the tokenizer packages or the network
    """name -> (encode or None, note)."""
    out = {"chars_div_4": (lambda s: range(round(len(s) / 4)), "September convention")}
    try:
        import tiktoken
        out["o200k_base"] = (tiktoken.get_encoding("o200k_base").encode, "tiktoken")
    except Exception as e:
        out["o200k_base"] = (None, f"unavailable: {type(e).__name__}: {e}"[:200])
    try:
        from tokenizers import Tokenizer
        tok = Tokenizer.from_pretrained(QWEN_TOKENIZER)
        out["qwen2.5"] = (lambda s: tok.encode(s).ids, QWEN_TOKENIZER)
    except Exception as e:
        out["qwen2.5"] = (None, f"unavailable: {type(e).__name__}: {e}"[:200])
    out["gemini"] = _gemini_encoder()
    return out


def _gemini_encoder():  # pragma: no cover - network
    try:
        import run_gemini
        key = run_gemini._key()
    except SystemExit as e:
        return None, f"unavailable: {e}"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_COUNT_MODEL}:countTokens"

    def encode(text):
        body = json.dumps({"contents": [{"role": "user", "parts": [{"text": text}]}]}).encode()
        req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json",
                                                              "x-goog-api-key": key})
        with urllib.request.urlopen(req, timeout=60) as r:
            return range(json.loads(r.read())["totalTokens"])
    return encode, f"countTokens on {GEMINI_COUNT_MODEL} (free; no generation)"


def main():  # pragma: no cover - writes the committed result
    keys = sorted(harness.frozen()["diffs"])
    texts = {k: artifacts(k) for k in keys}
    result = {"n_drifts": len(keys), "artifacts": list(ARTIFACTS), "encoders": {}}
    for name, (encode, note) in encoders().items():
        if encode is None:
            result["encoders"][name] = {"note": note, "summary": None}
            print(f"{name}: {note}")
            continue
        per_key = {k: count(t, encode) for k, t in texts.items()}
        result["encoders"][name] = {"note": note, "summary": summarize(per_key), "per_drift": per_key}
        s = result["encoders"][name]["summary"]
        print(f"{name}: diff_json {s['means']['diff_json']:.1f}, v2_declaration {s['means']['v2_declaration']:.1f}, "
              f"ratio {s['ratio_diff_json_to_v2_declaration']:.3f}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=1))
    print(f"wrote {OUT.relative_to(HERE.parent)}")


if __name__ == "__main__":
    main()
