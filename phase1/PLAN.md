# Phase 1 Implementation Plan: diff-following ablation and information vs form

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Carry the locked Phase-1 pre-registration from instrument to verdicts: decoding probe, pilots,
4,470 episodes, one extended `results/analysis.json` with P1–P7 judged by code, and an answer to
HANDOFF §4.1 (why two families ignore the diff) and §4.2 (is "diff beats full schema" information or form).

**Architecture:** Conditions, logging and runners already exist (uncommitted) in `harness.py`,
`phase1_grid.py` and the three runners. This plan adds a pre-data addendum, a decoding-constraint probe, a
log checker that gates every run, a pure statistics module wired into `analyze.py` under its own RNG (so the
September numbers stay byte-identical while the BH family grows 112 → 194), tokenizer counts, and an audit.

**Tech Stack:** Python 3.13, numpy, pytest + pytest-cov, urllib (OpenRouter, Gemini REST), Modal + vLLM
(Qwen2.5-7B, A10G), tiktoken + tokenizers.

**Spec:** `MILESTONES.md` → "Phase 1 pre-registration — LOCKED 2026-10-19" (the contract);
`HANDOFF.md` §5 Phase 1 and §6 (rules for adding experiments). Gates borrowed from
`output/pdf/tool-schema-drift-plan-vi.pdf` (Day 1 and Day 2 gates).

---

## State on 2026-10-19 (verified in this session)

- Reproduction holds: `test_mechanics.py` 12 + `test_phase1.py` 27 + `viz` 16 tests pass; testbed hash
  matches; `analyze.py` regenerates `analysis.json` byte-identical.
- Phase-1 code and the locked pre-registration are **uncommitted**; the pre-registration says to commit
  before the first pilot call. No `.env`, no `results/phase1/`, no Phase-1 spend ($7.64 of $25, all September).
- OpenRouter lists `openai/gpt-5.6-luna` today on 7 endpoints: OpenAI (`flex` $0.10/M in, standard $0.20,
  `fast` $0.40), Azure ×3 (one down), Amazon Bedrock. September records do not say which endpoint served them.
- `notebooks/` and `output/` are untracked and unrelated to the study: never stage them.
- `origin` is the original author's public repository: do not push without the user's say-so.

### A finding in the September logs that changes how Phase 1 reads (no new data)

| September logs, all conditions | luna | Flash | Pro | Qwen |
|---|---|---|---|---|
| Accepted arguments outside the **declared** schema (undeclared name + off-enum + off-type) | **0** of 4,050 | 157 | 74 | 87 |
| Optional parameters filled in baseline A | **704/704** | 646/1408 | 322/704 | 988/1393 |

Under E, where the executor's error names the problem and luna gets one retry: renamed parameter, old name
resent 24/24; type change, integer resent 24/24; enum, old value resent 14/24 and a *different v1 value*
chosen 10/24, never the new value (which is never in the v1 enum).

**Hypothesis H-dec:** luna's serving route constrains tool-call arguments to the declared schema
(strict/structured-output decoding). If H-dec holds: (a) every ablation cell and `C_decl` keeps the v1
declaration, so all are null on the contrast set *by construction*; (b) luna's 100% optional fill, the
"calling style immunity" finding, is a decoding artifact rather than a model trait; (c) "the diff does nothing
for luna" becomes "luna could not express the diff". Qwen is not constrained (87 off-declaration
arguments), so its null needs a different explanation. A ~$0.05 probe (Task 4, run in Task 10) decides it.

## Global Constraints

- Testbed `experiments/testbed_frozen.json`, sha256
  `e8bbd71c63b1311c76b87ceabe45456217f9054f2d5f010517e3930209d08475`, is never edited.
- Phase-1 records: `results/phase1/runs_<model>.jsonl`; pilots `*.pilot.jsonl` are never analysed;
  `analyze.load_runs()` keeps globbing only `results/runs_*.jsonl`.
- Conditions are assembled in `harness.py` only; runners supply `call_model`.
- `HARD_STOP_USD = 25.00` stays; OpenRouter runs pass `--cap 6`; Phase-1 projection is about $5.
- Temperature 0; `max_tokens` 700 (OpenRouter, Qwen), 1024 (Gemini), 4000 at reasoning `high`; Gemini
  thinking Flash `MINIMAL`, Pro `LOW`; luna default = no `reasoning` field sent.
- Every luna Phase-1 call pins one OpenRouter provider with `allow_fallbacks: false` (default `openai`,
  confirmed in Task 10).
- Seeds: job order `SEED = 42`; September analysis `RNG = default_rng(20260909)` untouched; Phase-1
  analysis `RNG_P1 = default_rng(20261019)`; `N_BOOT = 10_000`, `N_PERM = 20_000`.
- One BH family: 112 + 82 = 194 (196 if the conditional route arm runs); threshold stated in `analysis.json`.
- Numbers flow raw logs → `analysis.json` → figures → text. Figures, site and film are Phase 4, not here.
- Any new rule or prediction is dated in `MILESTONES.md` and committed before the data it concerns.
- No drifted call ever goes to a real third-party API; `.env` is never staged.
- Commits `<type>: <description>` with no attribution trailer (user setting).
- New modules: functions < 50 lines, files < 400 lines, inputs never mutated, ≥ 80% line coverage.

## Review Focus

1. **Resume after a killed run.** A kill mid-write leaves a final line with no `\n`; `p1.load_done`
   `json.loads` every line and would crash, and the next append would glue a record onto the fragment.
   Expected: runners trim a trailing partial line before appending and redo that job. (Task 3)
2. **Two processes appending to one model file.** Expected: never done (one process per file, Task 11), and
   the checker reports unparsable lines by line number instead of crashing. (Task 5)
3. **Provider fallback inside a cell.** Expected: pinned without fallback, so requests fail loudly; the
   checker lists providers per cell and fails the gate on more than one. (Task 5)
4. **Truncated outputs** (`finish_reason == "length"`), likeliest at reasoning `high`. Expected: counted per
   cell as censoring; the gate fails a cell above 5%. (Task 5)
5. **A model version that moved since September** (Gemini `modelVersion`, OpenRouter `model`). Expected:
   the checker lists distinct versions per file and fails on more than one; analysis reports them beside the
   C re-run drift check. (Task 5)

---

## Budget, streams and order

| Stream | Arms (episodes) | Estimate | Wall time |
|---|---|---|---|
| luna, OpenRouter | probe (~90 calls), ablation 1,560, noise 150, infoform 240, thinking 240, route 360 (conditional) | ≈ $1.5 | ≈ 4 h |
| Gemini | infoform Flash 240, Pro 240 | ≈ $1.8 | ≈ 1 h |
| Qwen, Modal A10G | ablation 1,560, infoform 240 | ≈ 1.8 GPU-h ≈ $2.0 | ≈ 2 h |
| **Total** | **4,470** (+360) | **≈ $5**, cumulative ≈ $13 of $25 | |

Per-call costs from `cost_log.jsonl` (Flash $0.00037, Pro $0.0049, luna $0.00018; Qwen 1,830 episodes in
1.69 GPU-h); rechecked in Task 0. The three streams run in parallel; arms inside a stream run one after another.

```
T0 preflight → T1 commit → T2 addendum → T3 runner fixes → T4 probe code → T5 checker → T10 probe + pilots → T11 full runs → T12 thinking (+route)
                                       └→ T6 labeler → T7 stats → T8 analyze wiring → T9 token counts (alongside T10–T11; T7 is needed by T12)
T12 + T8 + T9 → T13 audit → T14 results
```

---

### Task 0: Pre-flight (needs the user; no code)

- [ ] User: `cp .env.example .env`, fill `GEMINI_API_KEY` and `OPENROUTER_API_KEY`; `python3 -m modal token set …`;
      `python3 -m modal profile current` prints a profile.
- [ ] Gemini models exist: `curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY&pageSize=1000" | grep -E 'models/gemini-3\.(6-flash|1-pro-preview)"'` → two lines.
      If one is missing, stop and record the substitution in `MILESTONES.md` before any call (HANDOFF §8).
- [ ] Prices: luna standard `openai` endpoint is $0.20/$1.20 per M (matches `cost_tracker.PRICE`); check Gemini
      prices against `PRICE`. Change `PRICE` only with a dated comment; never edit past `cost_log.jsonl` lines.
- [ ] Credits: OpenRouter ≥ $4 (`run_openrouter.py` prints it at start); Gemini billing active.
- [ ] Done when: one dated line under a new "Phase 1 run log" subsection of `MILESTONES.md` lists the four results.

### Task 1: Commit the existing instrument and the locked pre-registration

- [ ] Run `python3 -m pytest experiments/test_mechanics.py experiments/test_phase1.py viz/test_explorer_data.py -q` → `55 passed`.
- [ ] Commit A: `git add phase1/step1_diag_diff_following.py phase1/step1_diag_diff_following.json viz docs/explorer README.md`
      → `feat: step-1 diff-following diagnostic and data explorer` (viz imports the step-1 labeler, so they ship together).
- [ ] Commit B: `git add MILESTONES.md HANDOFF.md experiments/harness.py experiments/phase1_grid.py experiments/test_phase1.py experiments/run_gemini.py experiments/run_openrouter.py experiments/modal_qwen.py`
      → `feat: lock Phase-1 pre-registration; Phase-1 conditions, logging and runners`.
- [ ] `git status --short` → only `?? notebooks/` and `?? output/` remain (and `phase1/PLAN.md` until Task 2).

### Task 2: Pre-data addendum in `MILESTONES.md`

**Files:** Modify `MILESTONES.md`: new subsection "Phase 1 addendum — <date>, before any Phase-1 model call",
after "Logging required before the run". P1–P7 are not touched.

- [ ] **Disclosure 2.** The H-dec evidence above, numbers verbatim, marked as a post-lock look at September logs.
- [ ] **Probe (instrument check, not in BH).** Tool `probe_tool` rendered with `harness.declaration`:
      `mode` string enum `["alpha","beta"]` required; `count` integer required; `label` string optional, default
      `"none"`. System prompt `harness.SYSTEM`. Four user prompts, 3 reps each, temperature 0:
      `off_enum` "Call probe_tool with mode "gamma" and count 3. The service now accepts "gamma"; send exactly that value.";
      `off_type` "Call probe_tool with mode "alpha" and count set to the string "3 items" (a string, not a number).";
      `undeclared` "Call probe_tool with mode "alpha", count 3, and an extra argument named note with the value "hi".";
      `optional_fill` "Call probe_tool with mode "alpha" and count 3."
      Routes: luna × provider {`openai`, `azure`, `amazon-bedrock`} × `strict` {unset, `false`}; controls Flash
      and Pro at their study settings. Qwen is not probed (87 off-declaration arguments in September).
- [ ] **Probe decision rule.** On a route, *compliance* = off_enum + off_type + undeclared calls that carry the
      requested argument (out of 9). H-dec holds on a route when luna complies 0/9 and each Gemini control
      complies ≥ 7/9. A route *lifts* the constraint when luna complies ≥ 7/9. Anything between: report and treat
      as not lifted. Pre-registered luna arms always run on the pinned route with `strict` unset (the September request shape).
- [ ] **Conditional route arm**, run only if H-dec holds on the pinned route and some route lifts it: luna on
      that route, conditions `A`, `B_strict`, `C:sys:json:none`, primary 120 pairs (360 episodes). Predictions:
      **P8** on the lifting route luna's C "unlocks recovery" on the contrast set;
      **P9** on the lifting route luna's optional fill rate in A is < 0.90 and its B_strict success on
      required + default_change is ≥ 0.20 lower than September's. Two tests join BH (→ 196): route C − route
      B_strict on the contrast set; route B_strict − September B_strict on required + default_change.
      If H-dec holds and nothing lifts it, luna's diff question is reported as not testable on this route and the
      OpenAI direct API moves to Phase 2. If H-dec fails, the ablation is read as behaviour.
- [ ] **Analysis pins** (fills gaps the lock leaves open):
      A1 pair sets: luna tests on the 72-pair contrast set; Qwen on 120; information-vs-form on the 48
      required + default_change pairs; P5 on the 24 required pairs.
      A2 interactions with a 3-level factor: per pair *i* and place *p*, e_ip = the factor's effect at *p*
      averaged over the third factor; T = variance over *p* of mean_i e_ip; null permutes the three place labels
      within each pair; 20,000 permutations. format × instruction: per-pair 2×2 contrast averaged over place, sign-flip.
      A3 main effects: per-pair contrast averaged over the other two factors' cells (4 cells for place
      contrasts, 6 for format and instruction), sign-flip.
      A4 P2 holds when max(user−sys, tool−sys) exceeds both prose−json and apply−none (signed point
      estimates) and is not within noise.
      A5 noise floors: luna = Phase-1 noise-arm flip rate; Qwen 0.0, Flash 0.133 (September); Pro uses Flash's
      as a stated proxy. |mean difference| below the floor is "within noise" whatever its p.
      A6 thinking cell = highest luna recovery point on the contrast set among the 12 non-replicate cells
      (11 ablation + `C_decl`); ties → higher success on all 120 pairs → earlier in `harness.PHASE1_CONDS`.
      Written to `results/phase1/thinking_cell_selection.json` and committed before the thinking run.
      A7 P3 metric: Qwen type_change, per pair the share of prose cells labelled `V2_CORRECT` minus the share
      of JSON cells; holds when the mean > 0 and its bootstrap CI excludes 0 (descriptive, not in BH);
      `V2_PARTIAL` reported beside it. P7 fails in a family when the CI of C+D − C or of C+D − D lies wholly below 0.
      A8 drift-over-time: C re-run vs September C, paired difference with bootstrap CI plus call-identity
      rate per class; not tested.
      A9 if any `C:tool:*` cell unlocks recovery, a control `C:toolctrl` (changelog turn returns "No changes
      recorded." and the diff sits in the system prompt) runs for that model before a placement claim is made;
      reported descriptively.
- [ ] Commit: `git add MILESTONES.md phase1/PLAN.md` → `docs: Phase-1 pre-data addendum and execution plan`.

### Task 3: Runner logging and resume fixes

**Files:** Modify `experiments/run_openrouter.py`, `experiments/run_gemini.py`, `experiments/harness.py`,
`experiments/phase1_grid.py`, `experiments/modal_qwen.py`; Test `experiments/test_phase1.py`.

**Interfaces (produced):**
- `run_openrouter._key(env_path=ENV_PATH) -> str` and `run_gemini._key(env_path=ENV_PATH) -> str`: lazy, cached;
  importing either module no longer reads `.env`. `SystemExit` naming the missing variable.
- `run_openrouter.or_body(model, messages, declarations, max_tokens, reasoning="default", provider=None, strict=None) -> dict`
- `run_openrouter.parse_or_response(resp: dict) -> dict`: `{"name","args"}` or `{"final"}`, plus
  `"usage": {"in","out","reasoning"}` (reasoning from `usage.completion_tokens_details.reasoning_tokens`, else 0) and
  `"meta": {"provider","model","finish_reason"}`.
- `run_openrouter.make_call_model(..., strict=None)`; CLI `--strict {unset,false}`, `--route <label>`
  (`--arm route` without `--route` exits with a message).
- `run_gemini.parse_gemini_response(resp: dict, thinking: str) -> dict`: same shape; `out` = candidates + thoughts
  (as now), `reasoning` = `thoughtsTokenCount`.
- `harness.run_episode` sums `in`, `out`, `reasoning`.
- `phase1_grid.repair_tail(path) -> int` (bytes removed), called by every runner (Qwen: the `phase1` local
  entrypoint) before opening the file for append.
- `phase1_grid.ARMS` gains `"route"`; `jobs("route")` → `A`, `B_strict`, `C:sys:json:none` × primary pairs;
  `out_path(model, pilot=False, route=None)` → `runs_<model>[.<route>][.pilot].jsonl`; records carry `"route"`.

- [ ] **Step 1: Write the failing tests** in `test_phase1.py`:
  `test_or_body_strict_and_provider` — `strict=False` puts `"strict": False` in every `tools[i]["function"]`;
  `strict=None` leaves the key out; `provider="openai"` → `body["provider"] == {"order": ["openai"], "allow_fallbacks": False}`.
  `test_parse_or_response_logs_reasoning_and_provider` — `usage={"prompt_tokens":100,"completion_tokens":50,"completion_tokens_details":{"reasoning_tokens":30}}`,
  `provider="OpenAI"`, `finish_reason="tool_calls"` → `usage == {"in":100,"out":50,"reasoning":30}`, `meta["provider"] == "OpenAI"`;
  malformed `arguments` → `args == {}`.
  `test_parse_gemini_response_counts_thoughts` — `{promptTokenCount:10,candidatesTokenCount:5,thoughtsTokenCount:7}` → `{"in":10,"out":12,"reasoning":7}`.
  `test_runners_import_without_env` — both modules import; `_key(tmp_path / ".env")` raises `SystemExit`.
  `test_episode_usage_sums_reasoning` — fake model returning `{"in":10,"out":2,"reasoning":1}` on two calls → `{"in":20,"out":4,"reasoning":2}`.
  `test_repair_tail_drops_partial_line` — `'{"a":1}\n{"b":'` → file becomes `'{"a":1}\n'`, returns 5; a clean file returns 0
  unchanged; a missing file returns 0; `load_done` then succeeds.
  `test_route_jobs_and_paths` — `len(jobs("route")) == 360`; conditions `{"A","B_strict","C:sys:json:none"}`;
  `out_path("openai/gpt-5.6-luna", route="nostrict").name == "runs_openai_gpt-5.6-luna.nostrict.jsonl"`.
- [ ] **Step 2:** `cd experiments && python3 -m pytest test_phase1.py -q` → the new tests FAIL, old ones pass.
- [ ] **Step 3:** Implement the interfaces; `call_model` in both runners becomes `body → call → parse`.
- [ ] **Step 4:** `python3 -m pytest test_mechanics.py test_phase1.py -q` → all pass; then `python3 analyze.py && git status --short ../results` → empty.
- [ ] **Step 5:** Commit `fix: log reasoning tokens, optional strict flag and safe resume in Phase-1 runners`.

### Task 4: Decoding-constraint probe (code only; it runs in Task 10)

**Files:** Create `experiments/probe_decoding.py`, `experiments/test_probe.py`. Output (Task 10):
`results/phase1/probe_decoding.json`.

**Interfaces:**
- Consumes `run_openrouter.make_call_model(..., provider, strict, phase="phase1")`, `run_gemini.make_call_model`, `harness.declaration`, `harness.SYSTEM`.
- `PROBE_TOOL: dict`, `CASES: dict[str, str]` (the four prompts from Task 2, verbatim).
- `complied(case: str, call: dict | None) -> bool`: off_enum `args.get("mode") == "gamma"`; off_type
  `isinstance(args.get("count"), str)`; undeclared `"note" in args`; optional_fill `"label" in args`.
- `summarize(results: list[dict]) -> dict`: per route, per case `{"n","complied"}`, plus `{"h_dec": bool, "lifts": bool}` by the Task 2 rule.
- CLI `python3 probe_decoding.py --reps 3`; cost tags `p1-probe-<route>-<case>-r<k>`.

- [ ] **Step 1: Failing tests:** `test_complied_rules` (one true and one false example per case, including `None` call → False);
  `test_summarize_verdicts` (luna 0/9 with controls 9/9 → `h_dec` True and `lifts` False; luna 8/9 → `lifts` True;
  controls 5/9 → `h_dec` False); `test_probe_tool_rendering` (`PROBE_TOOL == harness.declaration(...)`, required == `["mode","count"]`);
  `test_probe_tags_are_phase1` (tag starts with `p1-probe`, so `analyze.token_costs()` ignores it).
- [ ] **Step 2:** `python3 -m pytest test_probe.py -q` → FAIL.
- [ ] **Step 3:** Implement.
- [ ] **Step 4:** `python3 -m pytest test_probe.py --cov=probe_decoding --cov-report=term-missing -q` → pass, ≥ 80% (network loop excluded with `# pragma: no cover`).
- [ ] **Step 5:** Commit `feat: decoding-constraint probe for tool-call arguments`.

### Task 5: Phase-1 log checker (the run gate)

**Files:** Create `experiments/check_phase1_logs.py`, `experiments/test_check_phase1_logs.py`.

**Interfaces:**
- `read_records(path) -> tuple[list[dict], list[int]]` (records, unparsable line numbers).
- `expected_keys(arm: str, reasoning: str, cells: list[str] | None = None) -> set[tuple]` from `phase1_grid.jobs` and `phase1_grid.key`.
- `coverage(records, arm, reasoning, cells=None) -> {"expected","present","missing"}`, matched **by key, not by
  the `arm` field**: a noise rep-0 key is the same request as the ablation `C:sys:json:none` record and is
  satisfied by it (the runner skips it on resume).
- `completeness(records) -> list[str]`: missing `transcript`/`usage`/`meta`/`reasoning`/`arm`/`phase`; `usage.in == 0`;
  a `C:tool:*` record whose transcript does not start with the two synthetic turns.
- `cell_report(records) -> dict[cond, {"n","length_rate","providers","versions","changelog_recall_rate"}]`.
- `gate(path, arm, reasoning, cells=None, pilot=False) -> tuple[bool, dict]`: fails on unparsable lines,
  completeness problems, > 1 provider in a cell, `length_rate > 0.05` in a cell, > 1 model version in the file,
  and (unless `pilot`) coverage < 100%. The report includes cost per episode from `cost_log.jsonl` (`p1-` tags) and episodes per minute.
- CLI `python3 check_phase1_logs.py <file> --arm <arm> [--reasoning R] [--cells a,b] [--pilot]`: prints the report, exits 1 on failure.

- [ ] **Step 1: Failing tests:** `test_unparsable_line_reported_with_line_number`; `test_two_providers_in_one_cell_fail_gate`;
  `test_length_rate_above_5pct_fails_gate`; `test_two_model_versions_fail_gate`;
  `test_coverage_lists_missing_keys` (1,559 of 1,560 ablation keys → exactly one missing);
  `test_noise_rep0_satisfied_by_ablation_record`; `test_complete_fake_run_passes` (records from
  `harness.run_episode` with the v2 oracle of `test_phase1.py` over `jobs("infoform")[:10]` plus provider/model meta → gate ok with `pilot=True`).
- [ ] **Step 2:** run → FAIL. **Step 3:** implement. **Step 4:** pass with ≥ 80% coverage.
- [ ] **Step 5:** Commit `feat: Phase-1 log checker gating pilots and full runs`.

### Task 6: Shared drift-call labeler

**Files:** Create `experiments/drift_labels.py` with `LABELS, drift_change, drift_call_args, error_param, classify, signature`
moved verbatim from `phase1/step1_diag_diff_following.py`; modify that script and the viz module that imports
them to import from `drift_labels`; Test `experiments/test_drift_labels.py`.

- [ ] **Step 1: Failing tests:** `test_rename_error_is_v1_form`; `test_type_string_with_old_unit_is_v2_partial`
  (accepted string arg, wrong value); `test_required_filled_is_v1_safe_when_b_succeeded`;
  `test_classify_accepts_phase1_records` (v2-oracle record → `V2_CORRECT`).
- [ ] **Step 2:** FAIL. **Step 3:** move the code.
- [ ] **Step 4:** `python3 phase1/step1_diag_diff_following.py && git diff --exit-code phase1/step1_diag_diff_following.json` → no diff;
  `python3 viz/build_explorer_data.py && git diff --exit-code docs/explorer/data.js` → no diff; `python3 -m pytest viz experiments -q` → all pass.
- [ ] **Step 5:** Commit `refactor: move the drift-call labeler into experiments/drift_labels.py`.

### Task 7: Phase-1 statistics (pure functions)

**Files:** Create `experiments/phase1_stats.py`, `experiments/test_phase1_stats.py`. No file I/O; every
random function takes `rng`; returns new objects.

**Interfaces:**
- `CONTRAST = ("rename","enum_tighten","type_change")`, `INFO = ("required","default_change")`.
- `pairs_in(pairs, classes=None) -> list[tuple]`; `cell_vector(tab, cond, pairs) -> np.ndarray` (raises `KeyError` naming missing pairs; no silent drops).
  `tab` is `dict[cond_or_(cond, reasoning) -> dict[(task, cls) -> 0|1]]`.
- `recovery(a, b, x, rng, n_boot=10_000) -> {"point","ci95"}`: same formula as `analyze_model`.
- `main_effect(tab, pairs, factor, level, ref) -> np.ndarray` (pin A3); `factor` ∈ `{"place","fmt","instr"}`.
- `effect_by_place(tab, pairs, factor) -> np.ndarray` shape `(n_pairs, 3)`; `perm_within_pairs(E, rng, n_perm=20_000) -> float` (pin A2).
- `fmt_instr_contrast(tab, pairs) -> np.ndarray`.
- `flip_rate(reps: dict[pair, list[bool]]) -> float`; `within_noise(mean, floor) -> bool`.
- `unlocks(recovery_point, ci_low, survives_bh, mean, floor) -> bool`: ≥ 0.5, CI excludes 0, BH, not within noise.
- `select_best_cell(recoveries, success_all, order) -> str` (pin A6; never returns `C:sys:json:none`).
- `verdicts(stats: dict) -> dict[str, {"holds": bool | None, "basis": str}]` for P1–P9 (`None` = arm not run).

- [ ] **Step 1: Failing tests** (synthetic tables with planted effects):
  `test_main_effect_recovers_planted_placement` (user cells 1, rest 0 → user−sys 1.0, prose−json 0.0, apply−none 0.0);
  `test_place_interaction_null_and_planted` (no interaction → p > 0.2; format effect only at `tool`, 72 pairs → p < 0.01);
  `test_fmt_instr_contrast_planted` (mean 1.0); `test_recovery_formula` (point equals (x−b).mean()/(a−b).mean(); CI contains it);
  `test_cell_vector_missing_pair_raises`; `test_flip_rate` (`{p1:[1]*5, p2:[1,0,1,1,1]}` → 0.5);
  `test_select_best_cell_tiebreak_excludes_replicate`; `test_unlocks_needs_all_four` (each condition failing alone → False);
  `test_verdict_P6_equivalence` (CI [−0.08, 0.09] holds; [−0.12, 0.0] fails); `test_verdict_P2_within_noise_fails`.
- [ ] **Step 2:** FAIL. **Step 3:** implement. **Step 4:** pass, ≥ 80% coverage.
- [ ] **Step 5:** Commit `feat: Phase-1 statistics (main effects, within-pair interactions, decision rules)`.

### Task 8: Wire Phase 1 into `analyze.py`

**Files:** Modify `experiments/analyze.py`; Create `experiments/select_thinking_cell.py`, `experiments/test_analyze_phase1.py`.

**Interfaces:**
- Consumes Task 6 `classify`, Task 7 everything, Task 9 `results/phase1/artifact_tokens.json` (optional).
- `boot_ci(diffs, rng=RNG)`, `signflip_p(diffs, rng=RNG)`, `paired_stats(diffs, label, rng=RNG)`: defaults keep September bytes.
- `RNG_P1 = np.random.default_rng(20261019)`; `PHASE1 = RESULTS / "phase1"`.
- `load_phase1_runs(path=PHASE1) -> list[dict]`: `runs_*.jsonl` minus `*.pilot.jsonl`, deduped by `(route, *phase1_grid.rec_key(r))`, last wins.
- `analyze_phase1(runs, p1runs) -> dict | None` (None when no Phase-1 records) with blocks `ablation`, `main_effects`,
  `interactions`, `thinking`, `infoform`, `noise_floor`, `drift_over_time`, `mechanism`, `instrument`, `accounting`,
  `route` (if present), `predictions`. References: September A, B_strict, C, D from `load_runs()` on primary pairs.
  Phase-1 test labels start with `p1:`. `mechanism` = `classify` label counts per model × cell × class (September
  B_strict record as `b_rec`); `instrument` = `check_phase1_logs.cell_report` per model file (reused, not re-implemented)
  plus reasoning tokens per cell; `accounting` = artifact tokens (Task 9) and mean prompt tokens per call per cell.
- `main(out=RESULTS/"analysis.json", phase1_dir=PHASE1)` with CLI `--out`, `--phase1-dir`. Phase 1 runs after
  `token_costs()` and before `bh()`. `out["phase1"]` and `out["bh_original_family"]` (BH over the 112 September labels)
  appear only when Phase-1 records exist.
- `select_thinking_cell.py` writes `results/phase1/thinking_cell_selection.json` = `{"selected", "recoveries", "success_all", "rule": "A6"}`;
  `analyze_phase1` reads it and re-derives it, failing loudly if they disagree.

- [ ] **Step 1: Failing tests** (analysis runs in a subprocess so module-level RNG and `ALL_P` start fresh):
  `test_no_phase1_data_is_byte_identical` (empty `--phase1-dir` → output bytes equal committed `results/analysis.json`);
  `test_phase1_leaves_september_blocks_unchanged` (synthetic Phase-1 dir from fake-model runs of every arm → `models` and
  `token_costs` equal committed; `bh.n_tests == 194`; `bh_original_family == committed bh`);
  `test_phase1_test_count` (82 `p1:` labels; 84 with a route fixture); `test_pilot_files_ignored`;
  `test_thinking_selection_mismatch_fails`.
- [ ] **Step 2:** FAIL. **Step 3:** implement (each block its own function < 50 lines).
- [ ] **Step 4:** `python3 -m pytest experiments -q` → all pass; `python3 analyze.py && git status --short ../results` → empty (no Phase-1 data yet).
- [ ] **Step 5:** Commit `feat: Phase-1 analysis in analyze.py; BH family 112 -> 194`.

### Task 9: Tokenizer-measured artifact sizes (HANDOFF accounting fix)

**Files:** Create `experiments/count_artifact_tokens.py`, `experiments/test_count_artifact_tokens.py`; Modify
`requirements.txt` (+ `tiktoken`, `tokenizers`, `pytest-cov`). Output `results/phase1/artifact_tokens.json` (committed).

**Interfaces:**
- `artifacts(key: str) -> dict[str, str]` per `tool::class`: `diff_json`, `diff_prose`, `v2_declaration`, `c_decl_suffix`,
  `dprime_suffix`, `cd_note`, all built with the `harness` functions the conditions use.
- `count(texts: dict[str, str], encode: Callable[[str], list]) -> dict[str, int]`.
- Encoders: `tiktoken.get_encoding("o200k_base")`; `tokenizers.Tokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")`;
  Gemini `models/<m>:countTokens` when `GEMINI_API_KEY` is set, else `null`. Output per encoder: mean per artifact and
  `diff_json / v2_declaration` (September chars/4 ratio was 0.137).
- `analyze.py` copies it to `phase1.accounting.artifact_tokens`; top-level `token_costs` is left untouched.

- [ ] **Step 1: Failing tests:** `test_diff_json_matches_condition_C_text` (equals the JSON block inside `build_condition(..., "C", ...)["system"]`);
  `test_count_with_fake_encoder` (`str.split` encoder → word counts).
- [ ] **Step 2–4:** FAIL → implement → pass; run the script once, commit the JSON.
- [ ] **Step 5:** Commit `feat: tokenizer-measured artifact sizes`.

### Task 10: Probe, pilots, gate (spends cents; needs the user's go-ahead)

- [ ] `cd experiments && python3 probe_decoding.py --reps 3` → `results/phase1/probe_decoding.json`; prints a verdict per route.
- [ ] Dated `MILESTONES.md` line: H-dec per route, route arm on/off with its setting, pinned provider. Commit with the JSON:
      `data: decoding-constraint probe`.
- [ ] Choose pilot sizes that cover every cell: `python3 -c "import phase1_grid as p; js=p.jobs('ablation'); print(next(n for n in range(13, len(js)) if len({j[1] for j in js[:n]}) == 13))"` → N.
- [ ] Pilots (write `*.pilot.jsonl`):
```bash
python3 run_openrouter.py --arm ablation --provider openai --cap 6 --limit N
python3 run_openrouter.py --arm noise    --provider openai --cap 6 --limit 5
python3 run_openrouter.py --arm infoform --provider openai --cap 6 --limit 5
python3 run_gemini.py --model gemini-3.6-flash       --arm infoform --limit 5
python3 run_gemini.py --model gemini-3.1-pro-preview --arm infoform --limit 5
caffeinate -i python3 -m modal run modal_qwen.py::phase1 --arm ablation --limit N
caffeinate -i python3 -m modal run modal_qwen.py::phase1 --arm infoform --limit 5
```
- [ ] Gate: `python3 check_phase1_logs.py ../results/phase1/<file>.pilot.jsonl --arm <arm> [--reasoning MINIMAL|LOW] --pilot`
      exits 0 for every pilot file. Read one full transcript each of `C:sys`, `C:user`, `C:tool`, `C_decl`, `CD`, `Dprime` and
      confirm the note or description is where Task 2 says.
- [ ] Record cost per episode, episodes per minute and the projected total in the run log. Full runs start only if every
      pilot passes and the projection keeps cumulative spend under $20.

### Task 11: Full runs (three streams in parallel; never two processes on one model file)

- [ ] luna, sequentially: `--arm ablation`, then `--arm noise`, then `--arm infoform`, each with `--provider openai --cap 6`.
- [ ] Gemini, sequentially: Flash `--arm infoform`, then Pro `--arm infoform`.
- [ ] Qwen: `caffeinate -i python3 -m modal run modal_qwen.py::phase1 --arm ablation`, then `--arm infoform`.
- [ ] After each arm: `check_phase1_logs.py <file> --arm <arm> [--reasoning …]` → coverage 100%, exit 0. A stopped run is resumed by
      rerunning the same command; records are never edited by hand. Add one row per arm to the `MILESTONES.md` spend log.
- [ ] Commit the logs and pilot files: `data: Phase-1 ablation, noise and information-vs-form runs`.

### Task 12: Thinking arm and conditional arms

- [ ] `python3 select_thinking_cell.py` → selection JSON; commit `data: thinking-cell selection (pin A6)` **before** the run.
- [ ] `python3 run_openrouter.py --arm thinking --reasoning high --cells C:sys:json:none,<selected> --provider openai --cap 6`;
      gate with `--reasoning high --cells …`. If `length_rate > 0.05`, record it as censoring; `max_tokens` stays 4000 (locked).
- [ ] Route arm only if Task 10 triggered it: `python3 run_openrouter.py --arm route --route <label> --provider <p> --strict false --cap 6`; gate.
- [ ] `C:toolctrl` only if pin A9 triggers: add the condition in `harness.py` with a test in `test_phase1.py` first (Task 3 pattern).
- [ ] Commit `data: Phase-1 thinking (and route) runs`.

### Task 13: Hand audit of the new coding (the user reads; an agent only draws the sample)

**Files:** Create `experiments/audit_sample.py`; output `results/phase1/audit_labels_sample.json`.

- [ ] `draw(p1runs, n=24, seed=20261019) -> list[dict]`: stratified by model × label, at least 2 per non-empty
      stratum, then filled to 24; each item carries the key, auto label, drift change and transcript.
- [ ] The user reads every item and fills `human_label` and `note`. Agreement goes into `phase1.mechanism.audit_agreement`.
      Below 90%: fix `drift_labels.classify`, re-run Task 6 step 4, then continue.
- [ ] Commit `data: hand audit of Phase-1 drift-call labels`.

### Task 14: Final analysis, verdicts, records

- [ ] `python3 analyze.py` twice; `shasum results/analysis.json` identical both times.
- [ ] `models` and `token_costs` unchanged against the September commit; `bh.n_tests` 194 (196 with route arm);
      `bh_original_family.n_survive == 74`.
- [ ] `MILESTONES.md`: "Phase 1 results — <date>" with each of P1–P9 copied from `analysis.json → phase1.predictions`
      (reversals stated plainly), the H-dec verdict, spend, and any deviation from the lock or addendum.
- [ ] `HANDOFF.md`: progress-log row; the family size at `HANDOFF.md:89` and `:188` and `viz/README.md:26`.
- [ ] `python3 -m pytest experiments viz -q`; README reproduction checks (hash; regenerate analysis → no diff).
- [ ] Commit `feat: Phase-1 results`; report to the user: what (if anything) unlocked luna and Qwen, the
      information-vs-form verdict, H-dec, spend.

---

## After Phase 1 (each phase gets its own plan when it starts)

- **Before Phase 2 (user decision):** Phase 2 alone is $15–25, so cumulative spend would pass the $25 hard
  stop. Raise `HARD_STOP_USD` with a dated line in `MILESTONES.md`, or cut scope.
- **Real-validator replay** (Phase 2, $0) does not depend on Phase-1 results and can start any time:
  B_lenient records log the arguments the model sent, and B_lenient shows the same prompt as B_strict.
  Phase-1 transcripts add rejected-call arguments under strict v2.
- **Two new families:** run the decoding probe on each candidate route first and record the decoding mode.
  Include the Phase-1 best cell, `CD` and `Dprime` in their grid. A 70B model needs an 80 GB-class GPU
  (A100-80/H100, AWQ or two GPUs), not the A10G script.
- **Within-model calling style:** if the route arm ran, luna on the lifted route is already a within-model
  test of filling behaviour; the instructed-Flash arm is still needed for the "told to fill" version.
- **Compound drift, changelog corpus, 100+ tool catalog, longer multi-turn:** each is a new testbed with
  its own hash; never mixed with SchemaDrift-120.
- **Phase 4:** `figures/build_figures.py` hard-codes the four models (lines 21, 58, 142). Rebuild figures,
  then the site, then the film, only after `analysis.json`.
