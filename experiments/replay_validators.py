#!/usr/bin/env python3
"""Real-validator replay of drift-step calls (phase2/PLAN.md Task 4; P16 in MILESTONES.md).

Every logged drift-step call is re-validated against the active (v2) schema by four real
validators and by the mock executor under both profiles:
  pydantic_default   pydantic v2 model, extra="ignore", lax types (the library default)
  pydantic_strict    pydantic v2 model, extra="forbid", strict=True
  fastapi_default    the pydantic_default model as a FastAPI POST body, called via TestClient
  jsonschema_closed  JSON Schema Draft 2020-12 with additionalProperties: false

Everything runs in-process; no call leaves the machine.

Sources:
  september  B_strict and B_lenient records in results/runs_*.jsonl. These logs keep only
             accepted calls, so rejected drift-step calls cannot be replayed from them.
  phase1     every record in results/phase1/ (pilots excluded). Transcripts keep rejected calls.
  phase2     every record in results/phase2/ once it exists (same loader).

Error types follow the executor's check order: unknown > missing > type > enum. A validator
that reports several violations is labelled with the first in that order.

Run: ../.venv/bin/python replay_validators.py   -> results/phase2/validator_replay.json
"""

import argparse
import json
import pathlib
from collections import Counter
from functools import lru_cache
from importlib import metadata
from typing import Literal

import jsonschema
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import ConfigDict, Field, ValidationError, create_model

import analyze
import analyze_phase1
import executor as ex
import harness

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "results" / "phase2" / "validator_replay.json"
PRIORITY = ("unknown", "missing", "type", "enum")
PY_TYPES = {"string": str, "integer": int, "boolean": bool}
SEPT_CONDS = ("B_strict", "B_lenient")
# The profile each validator is compared with in P16 (pydantic_strict is reported, not predicted).
P16_PROFILE = {"pydantic_default": "lenient", "fastapi_default": "lenient",
               "pydantic_strict": "strict", "jsonschema_closed": "strict"}
MOCK_ERRORS = {"Received unknown parameter": "unknown", "Missing required parameter": "missing",
               "Invalid type": "type", "Invalid value": "enum"}
PYDANTIC_ERRORS = {"extra_forbidden": "unknown", "missing": "missing", "literal_error": "enum", "enum": "enum"}
JSONSCHEMA_ERRORS = {"additionalProperties": "unknown", "required": "missing", "type": "type", "enum": "enum"}


def _first(types):
    """The executor-order first error type, or None when there are none."""
    found = [t for t in PRIORITY if t in set(types)]
    return found[0] if found else None


def _outcome(error_types):
    first = _first(error_types)
    return (first is None, first)


# ---------------- the mock executor ----------------

def mock(params, args, profile):
    status, payload = ex.execute(params, args, profile, {})
    if status == "accepted":
        return {"accepted": True, "error_type": None}
    etype = next((v for k, v in MOCK_ERRORS.items() if payload.startswith(k)), None)
    if etype is None:
        raise SystemExit(f"unrecognised executor error {payload!r}")
    return {"accepted": False, "error_type": etype}


# ---------------- real validators ----------------

def _schema_key(params):
    return json.dumps(params, sort_keys=True)


def _annotation(p):
    return Literal[tuple(p["enum"])] if "enum" in p else PY_TYPES[p["type"]]


@lru_cache(maxsize=None)
def _model(schema_key, strict):
    """A pydantic model for one parameter schema. Fields are f0, f1, ... aliased to the
    parameter names, so a parameter called e.g. `schema` cannot shadow a BaseModel attribute."""
    params = json.loads(schema_key)
    fields = {f"f{i}": (_annotation(p), Field(... if p.get("required") else p["default"], alias=name))
              for i, (name, p) in enumerate(params.items())}
    config = ConfigDict(extra="forbid", strict=True) if strict else ConfigDict(extra="ignore")
    return create_model("ToolArgs", __config__=config, **fields)


def _pydantic_types(errors):
    return [PYDANTIC_ERRORS.get(e["type"], "type") for e in errors]


def _pydantic(strict):
    def validate(params, args):
        try:
            _model(_schema_key(params), strict).model_validate_json(json.dumps(args))
        except ValidationError as err:
            return _outcome(_pydantic_types(err.errors()))
        return (True, None)
    return validate


@lru_cache(maxsize=None)
def _client(schema_key):
    model = _model(schema_key, False)
    app = FastAPI()

    @app.post("/call")
    def call(body: model):  # noqa: ARG001  (validation is the point)
        return {"ok": True}

    return TestClient(app)


def _fastapi(params, args):
    resp = _client(_schema_key(params)).post("/call", json=args)
    if resp.status_code == 200:
        return (True, None)
    if resp.status_code != 422:
        raise SystemExit(f"FastAPI returned {resp.status_code}: {resp.text[:200]}")
    return _outcome(_pydantic_types(resp.json()["detail"]))


def json_schema(params):
    props = {name: {"type": p["type"], **({"enum": p["enum"]} if "enum" in p else {})}
             for name, p in params.items()}
    return {"$schema": "https://json-schema.org/draft/2020-12/schema", "type": "object",
            "properties": props, "required": [n for n, p in params.items() if p.get("required")],
            "additionalProperties": False}


@lru_cache(maxsize=None)
def _jsonschema_validator(schema_key):
    schema = json_schema(json.loads(schema_key))
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema)


def _jsonschema(params, args):
    errors = _jsonschema_validator(_schema_key(params)).iter_errors(args)
    return _outcome([JSONSCHEMA_ERRORS.get(e.validator, "type") for e in errors])


def validators():
    """name -> fn(params, args) -> (accepted, error_type | None)."""
    return {"pydantic_default": _pydantic(False), "pydantic_strict": _pydantic(True),
            "fastapi_default": _fastapi, "jsonschema_closed": _jsonschema}


# ---------------- drift-step calls from the logs ----------------

def _tasks():
    return {t["id"]: t for t in harness.frozen()["tasks"]}


def _from_transcript(turns, task, pseudo):
    """Args of the first call to the drift tool made at the drift step (the harness's rule)."""
    dt, didx, ptr = task["drift_tool"], task["drift_step_index"], 0
    for i, turn in enumerate(turns):
        if turn["role"] != "assistant_tool_call" or turn.get("synthetic") or turn["name"] in pseudo:
            continue
        if turn["name"] == dt and ptr == didx:
            return turn["args"]
        result = turns[i + 1] if i + 1 < len(turns) else {}
        if result.get("role") == "tool_result" and not str(result.get("content", "")).startswith("Error:"):
            ptr += 1
    return None


def _from_executed(executed, task):
    """Accepted calls only: the drift-step call is there only if it was accepted."""
    didx = task["drift_step_index"]
    if len(executed) > didx and executed[didx]["tool"] == task["drift_tool"]:
        return executed[didx]["args"]
    return None


def _drift_args(r, task, setup):
    if "transcript" in r:
        return _from_transcript(r["transcript"], task, setup.get("pseudo", {}))
    return None if setup["retry"] else _from_executed(r["executed"], task)


def _drift_row(r, task, source):
    if harness.FILL_BASE.get(r["cond"], r["cond"]) == "A":
        return None
    setup = harness.build_condition(task, r["cond"], r["class"])
    args = _drift_args(r, task, setup)
    if args is None:
        return None
    params = setup["active"][task["drift_tool"]]
    replayed = mock(params, args, setup["profile"])["accepted"]
    if replayed != str(r["drift_outcome"]).startswith("ACCEPTED"):
        raise SystemExit(f"mock replay disagrees with the log: {r['model']} {r['task']} {r['cond']} "
                         f"{r['class']} logged {r['drift_outcome']}")
    return {"source": source, "model": r["model"], "cond": r["cond"], "class": r["class"],
            "task": r["task"], "phrasing": r["phrasing"], "rep": r.get("rep", 0),
            "tool": task["drift_tool"], "args": args, "params": params,
            "mock_strict": mock(params, args, "strict"), "mock_lenient": mock(params, args, "lenient")}


def drift_calls(records, source):
    """One row per record whose drift-step call is recoverable from the log."""
    tasks = _tasks()
    rows = (_drift_row(r, tasks[r["task"]], source) for r in records)
    return [row for row in rows if row is not None]


def replay(rows, vals=None):
    vals = vals or validators()
    return [{**row, "validators": {name: dict(zip(("accepted", "error_type"), fn(row["params"], row["args"])))
                                   for name, fn in vals.items()}} for row in rows]


# ---------------- agreement ----------------

def _rate(agree, n):
    return {"n": n, "agree": agree, "rate": round(agree / n, 4) if n else None}


def _agrees(row, name, profile):
    return row["validators"][name]["accepted"] == row[f"mock_{profile}"]["accepted"]


def _by_error_type(rows, name):
    out = {}
    for etype in dict.fromkeys(r["mock_strict"]["error_type"] or "none" for r in rows):
        sub = [r for r in rows if (r["mock_strict"]["error_type"] or "none") == etype]
        out[etype] = {"n": len(sub), "agree_strict": sum(_agrees(r, name, "strict") for r in sub),
                      "agree_lenient": sum(_agrees(r, name, "lenient") for r in sub)}
    return out


def agreement(rows):
    """validator -> accept/reject agreement with each mock profile, overall and by the strict
    profile's error type ("none" = the strict profile accepts)."""
    if not rows:
        return {}
    out = {}
    for name in rows[0]["validators"]:
        out[name] = {"vs_strict": _rate(sum(_agrees(r, name, "strict") for r in rows), len(rows)),
                     "vs_lenient": _rate(sum(_agrees(r, name, "lenient") for r in rows), len(rows)),
                     "by_error_type": _by_error_type(rows, name)}
    return out


# ---------------- output ----------------

def load_sources(phase1_dir, phase2_dir):
    sept = [r for r in analyze.load_runs() if r["cond"] in SEPT_CONDS]
    out = {"september": sept, "phase1": analyze_phase1.load_phase1_runs(phase1_dir)}
    if phase2_dir.exists():
        out["phase2"] = analyze_phase1.load_phase1_runs(phase2_dir)
    return out


def _compact(row, name):
    keep = ("source", "model", "cond", "class", "task", "phrasing", "rep", "tool", "args",
            "mock_strict", "mock_lenient")
    return {**{k: row[k] for k in keep}, "validator": name, "outcome": row["validators"][name]}


def disagreements(rows):
    """Calls on which a validator disagrees with the profile P16 compares it with."""
    return [_compact(r, name) for r in rows for name, profile in P16_PROFILE.items()
            if not _agrees(r, name, profile)]


def summary(rows):
    sources = list(dict.fromkeys(r["source"] for r in rows))
    return {
        "note": __doc__.split("\n\n")[0],
        "versions": {p: metadata.version(p) for p in ("pydantic", "fastapi", "jsonschema")},
        "p16_profile": P16_PROFILE,
        "n_calls": len(rows),
        "n_by_source": dict(Counter(r["source"] for r in rows)),
        "n_by_strict_error_type": dict(Counter(r["mock_strict"]["error_type"] or "none" for r in rows)),
        "agreement": agreement(rows),
        "agreement_by_source": {s: agreement([r for r in rows if r["source"] == s]) for s in sources},
        "disagreements": disagreements(rows),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", type=pathlib.Path, default=OUT)
    args = ap.parse_args()
    sources = load_sources(ROOT / "results" / "phase1", ROOT / "results" / "phase2")
    rows = replay([row for src, recs in sources.items() for row in drift_calls(recs, src)])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    result = summary(rows)
    args.out.write_text(json.dumps(result, indent=1) + "\n")
    for name, a in result["agreement"].items():
        print(f"{name:18s} vs strict {a['vs_strict']['rate']:.3f}  vs lenient {a['vs_lenient']['rate']:.3f}")
    print(f"{len(rows)} calls -> {args.out}")


if __name__ == "__main__":
    main()
