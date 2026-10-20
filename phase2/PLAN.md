# Phase 2 Implementation Plan: generality (new families, calling style, real validators, luna direct)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Test whether the September and Phase-1 findings hold beyond the two Gemini models, luna and Qwen.
Specifically: does diff-following break along the Gemini-vs-rest line (HANDOFF §4.6, the family confound),
does Qwen's placement effect generalize to another open-weight family, is "fill every optional parameter"
causal for survival on required and default_change drift, do real validators behave like the mock executor's
strict or lenient profile, and is luna's null an artifact of the OpenRouter route?

**Architecture:** Reuse the Phase-1 machinery. A `phase2_grid.py` defines the arms and job keys. The OpenRouter
runner gains an OpenAI-direct endpoint and a quantization pin. The log checker is generalized from Phase 1. A
pure `analyze_phase2.py` is wired into `analyze.py` under its own RNG, so `analysis.json`'s September and
Phase-1 blocks stay byte-identical. The validator replay is a separate $0 script.

**Tech Stack:** Python 3.13, numpy, pytest + pytest-cov, urllib (OpenRouter, OpenAI, Gemini REST),
pydantic v2, FastAPI + httpx (TestClient), jsonschema.

**Spec:** `HANDOFF.md` §5 "Phase 2 — Generality" and §6 (rules for adding experiments);
`MILESTONES.md` → "Phase 1 results — 2026-10-20" and "Phase 2 setup — 2026-10-20" (user decisions);
`phase1/PLAN.md` → "After Phase 1".

---

## State on 2026-10-20 (verified in this session)

- Branch `giangdo/phase2` (from `giangdo/phase1` at `e29c0bf`, plus `fbc27ba`). Nothing pushed; the user has no
  push rights on `origin` and no fork yet.
- Spend $11.76; `HARD_STOP_USD` $50 (raised today); $38.24 left.
- 136 tests pass; `analyze.py` reproduces `analysis.json` (sha1 `586e314b…`).
- `.env` has `GEMINI_API_KEY` and `OPENROUTER_API_KEY`; `OPENAI_API_KEY` is still to be added by the user.
- OpenRouter endpoints today (per M tokens, in/out):
  - Claude Haiku 5.5: `anthropic` $0.10/$0.50.
  - Claude Sonnet 5.5: `anthropic` $2.00/$10.00.
  - Llama 3.3 70B: `novita/bf16` $0.135/$0.40 (tools, bf16); `deepinfra/turbo` fp8 $0.10/$0.32;
    `coreweave/fp16` $0.71/$0.71.
- Measured per-call means (`cost_log.jsonl`): about 450 tokens in, 50–110 out (Gemini Pro: 320 out);
  1.1–1.3 calls per episode. Modal A10G cost $1.10 per GPU-hour.

## Open decisions (the user answers before Task 1; the recommendation is listed first)

- **D1. 70B open-weight route.** The handoff says Modal, but a 70B model needs an 80 GB GPU. A Modal run of
  1,470 episodes is several GPU-hours (≈ $15–30, to be verified), well over half of what is left.
  - **Recommended:** Llama 3.3 70B Instruct via OpenRouter, pinned to `novita` with
    `quantizations: ["bf16"]` and no fallbacks (≈ $0.30). This is a different family from Qwen, so it tests the
    family confound and the placement finding. The cost is that weights and serving are not under our control.
    The pin and quantization go in every record, and the decoding probe (Task 6) checks the route.
  - Alternative: Qwen2.5-72B on Modal (H100 or A100-80, AWQ or bf16). This tests size within Qwen's family,
    not the family confound.
- **D2. Compound drift.** "After Phase 1" says compound drift needs a new testbed with its own hash, never mixed
  with SchemaDrift-120.
  - **Recommended:** move it to its own plan after this one.
  - Alternative: include it here (adds a testbed builder task and about two days).
- **D3. Label audit for the new families.**
  - **Recommended:** the Phase-1 method, pre-registered this time: a blind Codex pass on a stratified sample,
    and the user reads only the disagreements.
  - Alternative: hand audit.

## Global Constraints

- Testbed `experiments/testbed_frozen.json`, sha256
  `e8bbd71c63b1311c76b87ceabe45456217f9054f2d5f010517e3930209d08475`, is never edited.
- Phase-2 records: `results/phase2/runs_<model>.jsonl`; pilots `*.pilot.jsonl` are never analysed.
  `analyze.load_runs()` keeps globbing only `results/runs_*.jsonl`. Phase 1 keeps `results/phase1/`.
- Conditions are assembled in `harness.py` only; runners supply `call_model`.
- `HARD_STOP_USD = 50.00`; every OpenRouter or OpenAI run passes `--cap`; the Phase-2 projection is ≈ $10.
- Temperature 0; `max_tokens` 700 (OpenRouter, OpenAI), 1024 (Gemini); no `reasoning` field sent
  (Claude extended thinking off, luna default); Flash thinking `MINIMAL`.
- Every OpenRouter call pins one provider with `allow_fallbacks: false`. The pin, `strict` and quantization are
  written into each record's `pin` and checked on resume.
- Seeds: job order `SEED = 42`. September `RNG` and Phase-1 `RNG_P1` are untouched. Phase-2 analysis uses
  `RNG_P2 = default_rng(<lock date as YYYYMMDD>)`. `N_BOOT = 10_000`, `N_PERM = 20_000`.
- One BH family: 194 + the Phase-2 tests fixed in the addendum (Task 1); the threshold is stated in
  `analysis.json`.
- Every prediction and rule is dated in `MILESTONES.md` and committed before the data it concerns.
- No drifted call goes to a real third-party API. The validator replay runs in-process, never over a network.
  `.env` is never staged.
- Commits `<type>: <description>` with no attribution trailer (user setting).
- New modules: functions < 50 lines, files < 400 lines, inputs never mutated, ≥ 80% line coverage.

## Review Focus

1. **Claude replies with text before (or instead of) the tool call.** Expected: `parse_or_response` keeps the
   tool call and the text; an episode with text and no call ends like any other no-call episode. A pilot
   transcript is read by eye. (Task 3)
2. **Llama's provider ignores the quantization pin or routes elsewhere.** Expected: `allow_fallbacks: false`
   plus `quantizations` makes the request fail rather than reroute; the checker fails a cell served by more
   than one provider. (Tasks 3 and 5)
3. **OpenAI direct returns a different response shape than OpenRouter** (no `provider` field, a different
   usage layout). Expected: the parser fills `meta.provider = "openai-direct"` and the same usage keys; the
   checker's completeness rule accepts it. (Task 3)
4. **The fill instruction changes the system prompt's default-omission sentence.** Expected: `A_fill` and
   `B_fill` replace exactly that sentence and nothing else, which a byte-level test pins. (Task 2)
5. **The validators accept or reject for a different reason than the mock does.** Expected: agreement is
   reported per error type (unknown parameter, missing required, type, enum), not only in total. (Task 4)

---

## Budget, streams and order

| Stream | Arms (episodes) | Estimate |
|---|---|---|
| Claude Sonnet 5.5, OpenRouter | probe, core 720, phrasing 240, noise 150, infoform 240, placement 120 | ≈ $5–8 |
| Claude Haiku 5.5, OpenRouter | same 1,470 | ≈ $0.4 |
| Llama 3.3 70B, OpenRouter (D1) | same 1,470 | ≈ $0.3 |
| Flash fill-style, Gemini | A_fill 120, B_fill 120 | ≈ $0.15 |
| luna, OpenAI direct | probe; contingent arm 480 | ≈ $0.3 |
| Validator replay | all drift-step calls in the logs | $0 |
| **Total** | **≈ 5,200** | **≈ $7–10**, cumulative ≈ $19–22 of $50 |

The Sonnet estimate assumes 650 tokens in and 150–250 out per call; the pilot rechecks it before the full run.

```
T0 preflight → T1 addendum (lock) → T2 conditions + grid → T3 runners → T5 checker → T6 probes + pilots → T7 full runs
                                  └→ T4 validator replay ($0, any time after T1)
T7 → T8 analysis → T9 audit → T10 results
```

---

### Task 0: Pre-flight (needs the user; no code)

- [ ] The user answers D1–D3 and adds `OPENAI_API_KEY` to `.env`. The agent checks only that the name is
      present (`cut -d= -f1 .env`), never the value.
- [ ] Prices: OpenAI's own price for luna matches `PRICE["openai/gpt-5.6-luna"]` ($0.20/$1.20), or a separate
      entry is added with a dated comment. Add the Llama 3.3 70B price for the chosen endpoint.
- [ ] Deps: `pip install pydantic fastapi httpx jsonschema` into `.venv` (company mirror first; public PyPI
      only with the user's say-so, as in Phase 1); add them to `requirements.txt`.
- [ ] Done when: a dated "Phase 2 run log" line in `MILESTONES.md` lists the decisions, prices and deps.

### Task 1: Pre-registration addendum (the lock; committed before any Phase-2 model call)

**Files:** Modify `MILESTONES.md`: new section "Phase 2 pre-registration — LOCKED <date>".

- [ ] **Scope.** New families: Claude Haiku 5.5, Claude Sonnet 5.5, and the D1 model, each on the primary 120
      pairs. Arms:
      - `core`: A, B_strict, B_lenient, C, D, E — September's grid, 720 episodes;
      - `phrasing`: A and B_strict on phrasing 1, 240;
      - `noise`: B_strict, 30 stratified tasks × 5, 150;
      - `infoform`: CD, Dprime, 240;
      - `placement`: `C:user:prose:apply`, Qwen's best Phase-1 cell, 120.

      Flash: `fill` arm (`A_fill`, `B_fill`) on the primary 120 pairs. luna: decoding probe on OpenAI direct,
      then the contingent `direct` arm.
- [ ] **Predictions** (draft below; the user edits them before the lock):
      - **P10.** Claude Haiku 5.5 and Claude Sonnet 5.5 each recover ≥ 0.5 under C (diff in the system prompt).
        If both do, diff-following is not a Gemini trait.
      - **P11.** The D1 model: C recovers < 0.5, and `C:user:prose:apply` recovers at least 0.30 more than C.
        This would show Qwen's placement effect in a second open-weight family.
      - **P12.** D′ − D on newly-required ≥ 0.30 in each new family (P5 extended).
      - **P13.** C+D ≥ max(C, D) in each new family (P7 extended; luna was the exception).
      - **P14.** Flash with the fill instruction: B_fill − B_strict ≥ +0.30 on required + default_change, and
        |B_fill − B_strict| < 0.10 on rename, enum and type. Filling protects only the classes it can protect,
        so calling style is causal.
      - **P15** (contingent). If an OpenAI-direct route lifts the decoding constraint (compliance ≥ 7/9), luna's
        `C:user:prose:apply` recovers ≥ 0.5 on the 72-pair contrast set: the Phase-1 null came from the route.
      - **P16.** Replayed drift-step calls: pydantic v2 defaults (extra ignored, lax types) and FastAPI agree
        with the lenient profile on ≥ 95% of calls; JSON Schema with `additionalProperties: false` agrees with
        the strict profile on ≥ 95%.
- [ ] **Decision rules.** "Recovers" and "unlocks" as in Phase 1: recovery ≥ 0.5 AND paired 95% CI excludes 0
      AND the test survives BH. Each new family's noise floor (its own B_strict flip rate) applies as in Phase 1.
      P16 is descriptive (no BH test).
- [ ] **Fill instruction (exact text).** In `harness.SYSTEM`, the sentence "Use parameter defaults by omitting
      a parameter when the user does not specify it." becomes "Pass every parameter explicitly, including
      optional ones; when the user does not specify a value, pass the documented default." Nothing else changes.
- [ ] **Decoding probe on every new route** (Phase-1 `probe_decoding` cases), `strict` unset and `false`:
      Claude Haiku and Sonnet (`anthropic`), the D1 route, luna on OpenAI direct. Recorded descriptively.
      For luna direct, a route lifts at ≥ 7/9 compliance. The `direct` arm (A, B_strict, `C:sys:json:none`,
      `C:user:prose:apply` on the primary 120, 480 episodes) runs on the lifting route with the highest k;
      no lift → P15 untested and luna's diff question is reported as not testable on either route.
- [ ] **BH family.** Fixed now, counted in code (Task 8):
      - per new family: September's 27 core tests, 2 phrasing tests, 4 information-vs-form tests, and
        2 placement tests (`C:user:prose:apply` − B_strict, `C:user:prose:apply` − C), so 35 × 3 = 105;
      - Flash fill: 2 tests;
      - total 194 + 107 = 301, plus 2 if the `direct` arm runs (`C:sys:json:none` − B_strict and
        `C:user:prose:apply` − B_strict on the contrast set).
- [ ] **Audit method** (D3) and **seed** `RNG_P2` stated.
- [ ] Commit `docs: lock Phase-2 pre-registration` before Task 6.

### Task 2: Phase-2 conditions and grid

**Files:** Modify `experiments/harness.py`; create `experiments/phase2_grid.py`; test `experiments/test_phase2.py`.

**Interfaces:**
- Produces:
  - `harness.FILL_SYSTEM: str`;
  - `harness.build_condition(task, "A_fill" | "B_fill", cls)`;
  - `phase2_grid.ARMS = ("core", "phrasing", "noise", "infoform", "placement", "fill", "direct")`;
  - `phase2_grid.jobs(arm) -> list[(task, cond, class, phrasing, rep)]`;
  - `phase2_grid.out_path(model, pilot=False) -> Path` (under `results/phase2/`);
  - `phase2_grid.run_episode(job, call_model, model, arm, reasoning, max_tokens, pin) -> dict`
    (Phase-1 record fields plus `"phase": "phase2"` and `"pin"`).

- [ ] Tests first:
      - `test_fill_system_changes_one_sentence`: `FILL_SYSTEM` differs from `SYSTEM` only by the sentence above.
      - `test_fill_conditions_match_A_and_B_strict`: same declarations, executor profile and retry as A and
        B_strict; only the system prompt differs.
      - `test_jobs_sizes`: core 720, phrasing 240, noise 150, infoform 240, placement 120, fill 240, direct 480.
      - `test_core_jobs_match_september`: equal to `run_gemini.jobs_for_grid("core", "primary")` as a set.
      - `test_out_path_under_phase2`.
- [ ] Implement; September and Phase-1 conditions are untouched. `test_mechanics.py` and `test_phase1.py` still pass.

### Task 3: Runners (OpenRouter pins, OpenAI direct, Gemini fill arm)

**Files:** Modify `experiments/run_openrouter.py`, `experiments/run_gemini.py`, `experiments/cost_tracker.py`,
`.env.example`; tests in `experiments/test_phase2.py`.

- [ ] Tests first (fake responses, no network):
      - `test_or_body_quantization_pin`: `provider = {"order": [p], "allow_fallbacks": false,
        "quantizations": ["bf16"]}` when given.
      - `test_openai_direct_body_has_no_provider_field`.
      - `test_parse_claude_text_plus_tool_call`: the tool call is kept and the text logged.
      - `test_parse_openai_direct_meta`: `meta.provider == "openai-direct"`, usage keys `in`, `out`, `reasoning`.
      - `test_resume_refuses_pin_mismatch` (pin includes `endpoint` and `quantization`).
- [ ] `run_openrouter.py --phase 2 --arm <arm> --model <id> --provider <p> [--quantization bf16]
      [--endpoint openai] --cap <usd>`. `--endpoint openai` reads `OPENAI_API_KEY` lazily, posts to
      `https://api.openai.com/v1/chat/completions` and logs cost under the model id. Phase 1 calls are unchanged.
- [ ] `run_gemini.py --phase 2 --arm fill` for Flash.
- [ ] `.env.example` gains `OPENAI_API_KEY=`.

### Task 4: Real-validator replay ($0)

**Files:** Create `experiments/replay_validators.py`; test `experiments/test_replay_validators.py`;
output `results/phase2/validator_replay.json`.

**Interfaces:**
- Produces:
  - `drift_calls(records) -> list[dict]`: model, cond, class, task, args sent, active v2 params, mock outcome;
  - `validators() -> dict[name, fn(params, args) -> (accepted: bool, error_type | None)]` for:
    - `pydantic_default`: extra ignored, lax types;
    - `pydantic_strict`: extra forbidden, strict types;
    - `fastapi_default`: a POST endpoint with the pydantic default model, through `TestClient`;
    - `jsonschema_closed`: Draft 2020-12, `additionalProperties: false`;
  - `agreement(rows) -> {validator: {"vs_strict", "vs_lenient", "by_error_type"}}`.

- [ ] Tests first, one per executor rule, each pinned against what that validator documents:
      - unknown parameter: strict profile rejects; `pydantic_default` drops (accepts); `jsonschema_closed` rejects;
      - missing required: everyone rejects;
      - `"3"` sent for an integer: `pydantic_default` coerces; `pydantic_strict` and `jsonschema_closed` reject;
      - enum violation: everyone rejects.
- [ ] Input: the drift-step call of every September `B_strict`/`B_lenient` record and every Phase-1 record
      (args from the transcript; rejected calls included).
- [ ] Output and commit `feat: real-validator replay of drift-step calls`. P16 is read from this file in Task 8.

### Task 5: Log checker for Phase 2

**Files:** Modify `experiments/check_phase1_logs.py`, generalized by a `--phase {1,2}` flag (default 1, so
Phase-1 behaviour is unchanged); tests in `experiments/test_check_phase1_logs.py`.

- [ ] Tests first: expected keys come from `phase2_grid.jobs`; the one-provider-per-cell rule includes the
      quantization; the truncation, version and duplicate rules are unchanged.
- [ ] Gate command: `python3 check_phase1_logs.py <file> --phase 2 --arm <arm> [--pilot]` → `PASS`.

### Task 6: Probes and pilots (spends cents; needs the user's go-ahead)

- [ ] Decoding probe on the new routes (Task 1 list); write `results/phase2/probe_decoding.json`; record the
      verdict for luna direct before reading anything else.
- [ ] Pilots: `--limit 5` per new model and arm (core and placement), Flash fill and, if luna direct lifts, the
      `direct` arm. Gate each with `--pilot`; read two transcripts per model by eye (Review Focus 1).
- [ ] Re-estimate the Sonnet cost from pilot usage. If the projection exceeds $15, stop and ask.
- [ ] Commit the probe result, pilots and a run-log line.

### Task 7: Full runs (one process per model file)

- [ ] Streams run in parallel; arms within a stream run one after another: Sonnet, Haiku, D1 model, Flash fill,
      luna direct (if it lifts).
- [ ] Gate every arm; commit per stream: `chore: Phase-2 runs for <model>`.

### Task 8: Phase-2 analysis

**Files:** Create `experiments/analyze_phase2.py` (never imports `analyze`, like `analyze_phase1`); modify
`experiments/analyze.py` (`RNG_P2`, `--phase2-dir`, `phase2_ctx()`); tests `experiments/test_analyze_phase2.py`.

- [ ] Refactor `analyze.analyze_model` to accept a `ctx` (rng and register), defaulting to the September
      stream. `test_no_phase1_data_reproduces_september` and the Phase-1 tests stay green.
- [ ] Blocks under `analysis.json → phase2`:
      - `models` (September blocks per new family, labels prefixed `p2:`);
      - `infoform`, `placement`, `fill`, `noise_floor`, `direct`, `probe`, `validator_replay`, `mechanism`;
      - `predictions` (P10–P16);
      - `family` (`n_tests`, `expected`, `complete`).
- [ ] An incomplete arm adds no tests; a partial family never overwrites `results/analysis.json` without
      `--allow-partial`. This is the Phase-1 rule.
- [ ] Tests: fake records for each new arm; BH count 301 (303 with `direct`); September and Phase-1 blocks
      unchanged.

### Task 9: Label audit for the new families

- [ ] `audit_sample.py` gains a `--phase 2` source: same strata rule (model × label, floor 2), seed `RNG_P2`.
- [ ] Audit by the D3 method; agreement ≥ 0.9 goes into `phase2.mechanism.audit_agreement`; below that, fix
      `drift_labels.classify` before Task 10 and re-run Phase-1's analysis to confirm its blocks do not move.

### Task 10: Results and records

- [ ] `analyze.py` twice, identical hash; `models`, `token_costs` and `phase1` unchanged against `e29c0bf`.
- [ ] `MILESTONES.md` "Phase 2 results — <date>": P10–P16 copied from `analysis.json`, reversals stated
      plainly, deviations, spend. `HANDOFF.md` progress row and family size; `viz/README.md` family size.
- [ ] Full test suite; commit `feat: Phase-2 results`; report to the user in the Phase-1 format.
