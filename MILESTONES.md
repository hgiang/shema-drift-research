# Schema-Drift Audit · Milestones & Checkpoints

Budget cap: **$30 total** (hard stop $25). Update this file at
every checkpoint. RULE: at each CP, STOP and report to the user; wait for approval.

## Pre-registered directions (recorded BEFORE any testbed generation or data collection)
- [x] Direction 1: Newly-required arguments cause the largest silent-failure rate;
      renames the most recoverable.  Recorded: 2026-09-09
- [x] Direction 2: Diff-conditioning recovers >50% of the dropped success at <10% of the
      token cost of full-schema re-injection.  Recorded: 2026-09-09
- [x] Direction 3: Failure rates differ by model family at matched task difficulty.
      Recorded: 2026-09-09
- [x] Direction 4: A nontrivial fraction of drifted calls SUCCEED with wrong semantics;
      quantify it.  Recorded: 2026-09-09
- Note at registration: executor mechanics may force REQUIRED drift to surface errors
  rather than fail silently; if D1 reverses for that mechanical reason we report exactly
  that (reversal-reporting discipline per the voice paper).

## Phase 1 pre-registration — LOCKED 2026-10-19
Drafted and locked 2026-10-19, before any Phase-1 model call; the owner accepted the
recommended choices for every former [DECIDE] item in chat on 2026-10-19. Pilot
`--limit 5` runs are excluded and not analysed.
- Locked: 2026-10-19 (commit this file before the first pilot call)

**Disclosure.** Before writing this, step 1 re-read the EXISTING logs
(`phase1/step1_diag_diff_following.py`, no new data). It showed that under C, GPT-5.6-luna
sent the v1-form call on 71/72 rename/enum/type pairs, identical argument-for-argument to
its B_strict call in 71/72 (114/120 overall); Qwen was identical in 196/240 and
half-applied 7/48 type changes (string sent, old unit kept); D on newly-required fell to
.17 (luna, Qwen) and .40/.42 (Flash/Pro) because v2 drops the old default. The
predictions below are informed by that look; they are directional bets on NEW runs.

**Scope (new data only; testbed unchanged, sha256 e8bbd71c...).**
- Ablation: placement {system, user turn, tool result} x format {JSON, prose} x
  instruction {none, "apply this change log step by step"} = 12 cells, on luna and
  Qwen2.5-7B, primary 120 pairs each (2,880 episodes). Cell system/JSON/none re-runs C.
- Extra cell C_decl (INCLUDED): v1 declaration, with the change written in plain
  language into the drifted parameter's description; no system-prompt note (luna and
  Qwen, 240 episodes). Step 1 suggests declarations are the channel luna follows.
- Thinking (luna only; Qwen2.5 has none): reasoning effort {provider default, high} x
  {C re-run, best ablation cell} (default level already run in the ablation, so 240 new
  episodes at high, max_tokens 4000). "Best cell" = highest luna recovery on the
  contrast set in the ablation; it is reported as selected. The default level is
  "no reasoning parameter sent", exactly as in the original luna arm.
- Information vs form: C+D (v2 schema + diff, note reworded so it is true when v2 is
  shown) and D' (v2 schema; the drifted parameter's description states the old contract,
  e.g. "previous default: X") on all four families, primary 120 pairs (960 episodes).
- Noise floor: luna, C re-run, 30 stratified tasks x 5 identical calls (150 episodes).
- Budget: about $8-12 + about 1.5 A10G GPU-h; stays under the $25 hard stop
  ($7.64 spent). OpenRouter per-run cap: $6 (`--cap 6`).
- Silent-drift and baseline references (A, B_strict) are the existing September logs
  for the same model and pairs; the C re-run (C:sys:json:none) is compared with the
  original C as a drift-over-time check and reported, not tested.

**Primary contrasts (fixed now).**
- luna: recovery on the contrast set = rename + enum_tighten + type_change (72 pairs).
  Newly-required and default-change are excluded: luna passes every optional parameter,
  so it already survives them without any diff (B_strict 1.00 and .92).
- Qwen: recovery on all five classes (120 pairs).
- Information vs form: C vs D', D' vs D, C+D vs C, C+D vs D, on newly-required +
  default-change (48 pairs per family), per family.
- Recovery = (success(X) - success(B_strict)) / (success(A) - success(B_strict)), paired
  per task-drift pair, as in analyze.py.

**Predictions.**
- P1. No cell that keeps the diff in the system prompt (format or instruction changes
  only) brings luna to recovery >= 0.5 on the contrast set.
- P2. For luna, moving the diff out of the system prompt (user turn or tool result)
  raises recovery more than changing format or adding the instruction (placement main
  effect > format and instruction main effects).
- P3. Qwen: prose format raises correct application on type_change (fewer
  string-with-old-unit calls) relative to JSON.
- P4. More thinking does not unlock luna (recovery stays < 0.5 at high effort).
- P5. D' beats D on newly-required by >= 0.30 in every family.
- P6. On Gemini Flash and Pro, D' is equivalent to C on newly-required + default-change:
  95% CI of the paired difference inside [-0.10, +0.10]. If so, the diff's advantage over
  the full schema is the information it carries (old contract), not its form.
- P7. C+D >= max(C, D) in every family (no family is hurt by having both).

**Decision rules.**
- "Unlocks recovery" = recovery >= 0.5 AND paired 95% bootstrap CI of
  success(X) - success(B_strict) excludes 0 AND the test survives BH.
- A cell difference smaller than luna's measured flip rate (noise floor) is not read as
  an effect, whatever its p-value.
- Main effects (placement, format, instruction) are paired contrasts averaged over the
  other two factors; interactions are tested directly, not inferred from differing
  significance.
- One BH family: the existing 112 tests + 82 Phase-1 tests = 194. The 82 are:
  each of the 13 ablation cells vs B_strict (13 x 2 models = 26); each non-replicate
  cell vs the C re-run (12 x 2 = 24); main effects user-vs-sys, tool-vs-sys,
  prose-vs-json, apply-vs-none (4 x 2 = 8); two-way interactions place x format,
  place x instruction, format x instruction (3 x 2 = 6); high vs default reasoning on
  the two thinking cells (2); C vs D', D' vs D, C+D vs C, C+D vs D (4 x 4 families =
  16). State the effective threshold in analysis.json.
- Any reversal is reported plainly. In particular, if P6 fails because D' still loses to
  C, we say the form of the diff matters beyond its information.

**Logging required before the run** (otherwise no full run): variant ID, full
transcript including rejected calls and their arguments, usage tokens, reasoning
setting, model/version string, OpenRouter provider; Phase-1 records written to
`results/phase1/runs_<model>.jsonl` (outside analyze.py's glob, so analysis.json stays
reproducible), keyed by (task, cond, class, phrasing, rep, reasoning). Implemented in
experiments/harness.py (build_phase1), experiments/phase1_grid.py and the three
runners; tests in experiments/test_phase1.py.

## Phase 1 addendum — 2026-10-19, before any Phase-1 model call
Adds rules the lock leaves open. P1–P7, the scope and the unlock rule above are not
changed. Execution plan: `phase1/PLAN.md`.

**Disclosure 2 (post-lock look at the September logs, no new data).**

| September logs, all conditions | luna | Flash | Pro | Qwen |
|---|---|---|---|---|
| Accepted arguments outside the declared schema (undeclared name + off-enum + off-type) | 0 of 4,050 | 157 | 74 | 87 |
| Optional parameters filled in baseline A | 704/704 | 646/1408 | 322/704 | 988/1393 |

Under E (error names the problem, one retry) luna resent the old parameter name 24/24 on
rename and the integer 24/24 on type change; on enum it resent the old value 14/24 and
chose a different v1 value 10/24, never the new value. September records do not say which
OpenRouter endpoint served luna (7 endpoints list it on 2026-10-19).

**Hypothesis H-dec.** luna's serving route constrains tool-call arguments to the declared
schema. If it holds, every ablation cell and C_decl (all keep the v1 declaration) is null on
the contrast set by construction, and luna's 100% optional fill is a decoding artifact.

**Route pin.** Every luna Phase-1 call pins one OpenRouter provider with
`allow_fallbacks: false` (default `openai`, confirmed by the probe). Pre-registered luna
arms run on that route with `strict` unset (the September request shape).

**Probe (instrument check, not in BH).** Tool `probe_tool`, rendered with
`harness.declaration`: `mode` string enum ["alpha","beta"], required; `count` integer,
required; `label` string, optional, default "none". System prompt `harness.SYSTEM`,
temperature 0, 3 reps per prompt:
- `off_enum`: `Call probe_tool with mode "gamma" and count 3. The service now accepts "gamma"; send exactly that value.`
- `off_type`: `Call probe_tool with mode "alpha" and count set to the string "3 items" (a string, not a number).`
- `undeclared`: `Call probe_tool with mode "alpha", count 3, and an extra argument named note with the value "hi".`
- `optional_fill`: `Call probe_tool with mode "alpha" and count 3.`

Routes: luna × provider {openai, azure, amazon-bedrock} × `strict` {unset, false};
controls Flash and Pro at their study settings. Qwen is not probed (87 off-declaration
arguments in September).

**Probe decision rule.** Compliance on a route = off_enum + off_type + undeclared calls
that carry the requested argument (out of 9). H-dec holds on a route when luna complies
0/9 and each Gemini control complies ≥ 7/9. A route lifts the constraint when luna
complies ≥ 7/9. Anything between is reported and treated as not lifted.

**Conditional route arm.** Runs only if H-dec holds on the pinned route and some route
lifts it: luna on that route, conditions A, B_strict, C:sys:json:none, primary 120 pairs
(360 episodes).
- P8. On the lifting route, luna's C unlocks recovery (rule above) on the contrast set.
- P9. On the lifting route, luna's optional-fill rate in A is < 0.90, and its B_strict
  success on required + default_change is ≥ 0.20 lower than September's.
- Two tests join the BH family (194 → 196): route C − route B_strict on the contrast
  set; route B_strict − September B_strict on required + default_change.
- If H-dec holds and no route lifts it, luna's diff question is reported as not testable
  on this route, and the OpenAI direct API moves to Phase 2. If H-dec fails, the luna
  ablation is read as behaviour.

**Analysis pins.**
- A1. Pair sets: luna tests on the 72-pair contrast set; Qwen on all 120; information vs
  form on the 48 required + default_change pairs; P5 on the 24 required pairs.
- A2. Interactions with the 3-level place factor: per pair i and place p, e_ip = the other
  factor's effect at p, averaged over the third factor; T = variance over p of mean_i
  e_ip; the null permutes the three place labels within each pair; 20,000 permutations.
  Format × instruction: per-pair 2×2 contrast averaged over place, sign-flip test.
- A3. Main effects: per-pair contrast averaged over the other two factors' cells (4 cells
  for place contrasts, 6 for format and instruction), sign-flip test.
- A4. P2 holds when max(user − sys, tool − sys) exceeds both prose − json and
  apply − none (signed point estimates) and is not within noise.
- A5. Noise floors: luna = Phase-1 noise-arm flip rate; Qwen 0.0 and Flash 0.133
  (September); Pro uses Flash's as a stated proxy. |mean difference| below the floor is
  "within noise" whatever its p.
- A6. Thinking cell = highest luna recovery point on the contrast set among the 12
  non-replicate cells (11 ablation + C_decl); ties → higher success on all 120 pairs →
  earlier in `harness.PHASE1_CONDS`. Written to
  `results/phase1/thinking_cell_selection.json` and committed before the thinking run.
- A7. P3 metric: Qwen type_change, per pair the share of prose cells labelled V2_CORRECT
  minus the share of JSON cells; holds when the mean > 0 and its bootstrap CI excludes 0
  (descriptive, not in BH); V2_PARTIAL reported beside it. P7 fails in a family when the
  CI of C+D − C or of C+D − D lies wholly below 0.
- A8. Drift over time: C re-run vs September C, paired difference with bootstrap CI plus
  call-identity rate per class; not tested.
- A9. If any C:tool:* cell unlocks recovery, a control C:toolctrl (the changelog turn
  returns "No changes recorded." and the diff sits in the system prompt) runs for that
  model before a placement claim is made; reported descriptively.

## Phase 1 amendment 1 — 2026-10-19, after the 8-call probe pilot, before the full probe
Replaces the "Probe decision rule" and the trigger of the "Conditional route arm" above.
Written after seeing the pilot (`results/phase1/probe_decoding.pilot.json`, 1 rep,
routes luna-openai-unset and flash) and before any full-probe call.

**Why.** In the pilot, Flash sent the off-enum value but sent `count` as the integer 3
and dropped `note`: the Gemini API itself appears to coerce types and strip undeclared
arguments, so Gemini is not an unconstrained control for off_type and undeclared. Under
the old rule (each control ≥ 7/9) the controls would likely fail and H-dec would be
rejected whatever luna does. luna on the pinned route sent
`{"mode":"alpha","count":3,"label":"none"}` on all four prompts.

**New rule.** Per luna route, compliance k of 9 as before; incomplete routes get no verdict.
- A route is *constrained* when k = 0 and *lifts* when k ≥ 7.
- H-dec holds when the pinned route (luna-openai-unset) is constrained and at least one
  other luna route lifts. The within-model contrast (same model, different route) is the
  control.
- H-dec is undecided when the pinned route is constrained and no luna route lifts; luna's
  diff question is then reported as not testable on OpenRouter and the OpenAI direct API
  moves to Phase 2.
- H-dec does not hold when the pinned route has k ≥ 1; the luna ablation is read as
  behaviour, and partial compliance is reported.
- Gemini Flash and Pro are descriptive: per-case compliance, reported beside luna.

**Route-arm trigger.** The conditional route arm runs if and only if H-dec holds, on the
lifting route with the highest k; ties go to the earlier route in
`probe_decoding.ROUTES`. P8, P9 and the two added BH tests are unchanged.

## Phase 1 run log
- 2026-10-19 pre-flight (no model calls): Gemini `gemini-3.6-flash` (version
  `3.6-flash-07-2026`) and `gemini-3.1-pro-preview` (version `3.1-pro-preview-01-2026`)
  listed; the September logs recorded no version string, so sameness cannot be shown.
  Prices: luna `openai` endpoint $0.20/$1.20 and Pro $2.00/$12.00 per M match
  `cost_tracker.PRICE`; Flash rose to $0.75/$3.75 (was $0.50/$3.00), PRICE updated.
  Credits: OpenRouter $30.00 unused; Gemini billing on the paid tier. Logged spend
  $7.64 of the $25 hard stop.
- 2026-10-19 probe pilot (8 calls, $0.0014; `results/phase1/probe_decoding.pilot.json`)
  led to amendment 1 (committed before the full probe).
- 2026-10-19 full probe (`results/phase1/probe_decoding.json`, 3 reps, $0.06; spend now
  $7.70). Compliance with off-enum + off-type + undeclared (of 9) and optional fill (of 3):
  luna-openai-unset 0/9, fill 3/3; luna-openai-false 1/9, fill 0/3; luna-azure-unset 0/9,
  fill 3/3; luna-azure-false 0/9, fill 0/3; both amazon-bedrock routes HTTP 404 on every
  call (no verdict); Flash 3/9 (off_enum 3/3, off_type 0/3, undeclared 0/3), fill 0/3;
  Pro 6/8 (off_enum 3/3, off_type 1/3, undeclared 2/2), fill 0/2, two calls timed out.
  **Amendment-1 decision: H-dec undecided (pinned route constrained, no luna route
  lifts); the conditional route arm does not run.** Descriptive, not a verdict: (a) with
  `strict` unset luna filled the optional `label` 6/6 and with `strict: false` 0/6, so the
  September 704/704 optional fill is consistent with strict-mode decoding on the September
  request shape rather than a model trait; (b) with `strict: false` luna still kept to the
  declared schema (1/18 off-declaration) and often answered in text that the schema does
  not allow the value, i.e. the declaration-over-instruction preference shows without a
  decoding constraint. Gemini Pro calls took up to ~14 min each (timeouts and retries):
  re-measure before the Pro infoform arm.
- 2026-10-19 pilots (`*.pilot.jsonl`, not analysed), all passing `check_phase1_logs.py
  --pilot`: luna ablation 30 (13 cells), Flash infoform 8, Qwen ablation 30, Pro infoform
  1 of 4 (then timed out; 2 more on retry at 17:59, 10 s each).
- 2026-10-19 full runs, each passing the full gate (100% coverage, one provider per cell,
  no truncation, one model version per file): luna (provider `openai` pinned, `strict`
  unset) ablation 1,560, noise 150 (rep 0 shared with the ablation), infoform 240;
  Qwen ablation 1,560 + infoform 240 (1.65 A10G GPU-h); Flash infoform 240.
- 2026-10-19 thinking selection (pin A6, committed before the run): all 12 candidates have
  luna recovery 0.000 on the contrast set (0/72 in every cell, as in September's B_strict
  and C); ties went to success on all 120 pairs, then PHASE1_CONDS order:
  `C:user:prose:none`. Thinking arm (reasoning `high`, max_tokens 4000): 240/240, gate
  passes; mean reasoning tokens per episode 63 at default vs 83 at high (max 389), no
  truncation.
- 2026-10-19 Pro infoform stopped at 182/240: HTTP 429, quota
  `GenerateRequestsPerDayPerProjectPerModel` = 250 for `gemini-3.1-pro-preview` on this
  project; resumes after the daily reset. Logged spend $11.41 of the $25 hard stop.
- 2026-10-20 Hand-audit sample drawn (Task 13, `audit_sample.py`, seed 20261019) from the
  main records with Pro at 182/240: 23 model x label strata, floor 2 each, so 44 items
  (the floor overrides the target of 24).
- 2026-10-20 Pro infoform resumed after the quota reset (15:30 +08): 58 new, 240/240, gate
  passes. Pro infoform cost $1.49. Logged spend $11.76 of the $25 hard stop.
- 2026-10-20 Label audit (Task 13). Deviation: the 44 items were labelled by Codex (model
  version not recorded), not by hand, because the user had no time. Codex read only the
  blind reading copy (`audit_labels_sample.md`), with the automatic labels and the labeler
  code off limits; `git diff` confirmed it changed only the answer lines. Agreement 42/44
  = 0.955 (threshold 0.9), so `drift_labels.classify` is unchanged. Both disagreements
  were marked unsure by Codex and are recorded as labeler limits, not fixed after seeing
  the audit: item 24 (Qwen, required) sent a correct v2 `send_message` before creating the
  channel, so it was never scored as the drift step; `NO_DRIFT_CALL` therefore also
  covers out-of-order drift calls. Item 44 (Flash, type_change) omitted `chunk_mb`
  entirely; the labeler counts a missing type-changed parameter as `V1_FORM` (Codex:
  `OTHER_WRONG`). Neither touches P3 (Qwen type_change `V2_CORRECT` share).

## Phase 1 results — 2026-10-20

Source: `results/analysis.json → phase1` (regenerated twice, identical hash). Every arm is
complete; the BH family is the locked 194 tests (effective threshold p ≤ 0.0225, 108
survive). The September blocks are unchanged; the 112-test family alone is kept as
`bh_original_family` (74 survive). In the joint family, 72 of those 74 survive; two drop
out: `gemini-3.1-pro-preview:E-B:enum_tighten` and `modal-qwen2.5-7b:drop:default_change`.

**Verdicts (copied from `phase1.predictions`).**
- P1 **holds.** No system-prompt cell unlocks luna: all 4 present, recovery 0.
- P2 **fails.** Nothing moves luna: placement, format and instruction main effects are all
  +0.000 on the 72 contrast pairs (noise floor 0.033), so placement cannot exceed the others.
- P3 **holds.** Qwen type_change: prose − JSON share of `V2_CORRECT` +0.222, CI [0.111, 0.340].
- P4 **holds.** luna recovery at high effort is 0.0 on both thinking cells
  (`C:sys:json:none`, `C:user:prose:none`).
- P5 **holds.** D' − D on newly-required: luna 0.625, Qwen 0.625, Flash 0.500, Pro 0.542.
- P6 **fails (Flash).** Pro: D' − C is 0.000, CI [0, 0], equivalent. Flash: −0.062, CI
  [−0.146, 0.000]; the CI leaves the ±0.10 band, so equivalence is not shown, though D' is
  not significantly worse than C either.
- P7 **fails (luna).** C+D − C for luna is −0.188, CI [−0.312, −0.062]: adding the v2
  schema to the diff lowers luna's success. C+D ≥ max(C, D) holds in the other three
  families.
- P8, P9 not tested: the route arm did not run (amendment 1).
- H-dec: undecided (no luna route lifted compliance to 7/9). Descriptive: with `strict`
  unset luna filled the optional parameter 6/6, with `strict: false` 0/6, so the September
  704/704 fill reflects the route's strict mode.

**Beyond the predictions.**
- Qwen's September C failure was about placement, not about ignoring the diff. Main effects
  (120 pairs): user − sys +0.388, tool − sys +0.260, prose − JSON +0.189, apply − none
  +0.028. Best cell `C:user:prose:apply`, recovery 0.896 (September C: 0.06).
- luna: 0/72 recovered pairs in all 13 ablation cells and at high effort; mean reasoning
  tokens 63 (default) vs 83 (high).
- Tokenizer-measured diff / v2 declaration is 0.20–0.25 (o200k 0.204, Qwen 0.202, Gemini
  0.249), not the September chars/4 figure of 0.137.

**Deviations from the lock and addendum.** Hand-audit sample 44 items, not 24 (stratum
floor); the audit was labelled by Codex, blind, not by hand (agreement 0.955). The explorer
(`docs/explorer/data.js`), figures, site and film still show the September analysis; they
are rebuilt in Phase 4. Phase-1 spend: logged total $11.76 of the $25 hard stop.

## Phase 2 setup — 2026-10-20 (user decisions, before any Phase-2 call)

- Budget: `HARD_STOP_USD` raised from $25 to $50 (`TOTAL_CAP_USD` $30 → $55) with $11.76
  already spent; Phase 2 was estimated at $15–25 plus GPU hours.
- New families: both Claude Haiku 5.5 and Claude Sonnet 5.5 via OpenRouter (list prices
  checked 2026-10-20: $0.10/$0.50 and $2.00/$10.00 per M tokens), plus one open-weight
  70B-class model (choice made in the Phase-2 plan).
- luna on the OpenAI direct API joins Phase 2 (amendment 1: H-dec undecided on OpenRouter);
  the user adds `OPENAI_API_KEY` to `.env`.
- Phase-2 predictions are written and committed in this file before the first Phase-2 run.

### Phase 2 run log

- 2026-10-20 Pre-flight (`phase2/PLAN.md` Task 0). Decisions D1–D3 as recommended in the plan:
  D1 the open-weight family is Llama 3.3 70B Instruct via OpenRouter, pinned to `novita`
  with `quantizations: ["bf16"]` and no fallbacks (listed $0.135/$0.40 per M, priced
  $0.14/$0.40 in `cost_tracker.py`); D2 compound drift moves to its own plan with a new
  testbed; D3 the label audit for the new families is a blind Codex pass, and the user
  reads only the disagreements. `OPENAI_API_KEY` is in `.env` (name checked, value not
  read). luna on OpenAI direct is priced as OpenRouter's `openai` endpoint ($0.20/$1.20);
  the OpenAI billing page is the check after the probe. Validator deps installed from
  public PyPI with the user's approval (the company mirror has no pydantic-core v2 wheel
  for Python 3.13 on arm64): pydantic 2.14.1, pydantic-core 2.50.1, fastapi 0.151.0,
  starlette 1.9.0, httpx 0.28.1, jsonschema 4.26.0.
- 2026-10-21 Real-validator replay (Task 4, $0, in-process): `experiments/replay_validators.py`
  → `results/phase2/validator_replay.json`. 5,208 drift-step calls: 793 from September
  B_strict/B_lenient (those logs keep accepted calls only, so rejected September calls are
  absent) and 4,415 from Phase 1 (transcripts, rejected calls included). Accept/reject
  agreement: pydantic default and FastAPI 0.868 with the strict profile and 0.877 with the
  lenient one; pydantic strict and JSON Schema (`additionalProperties: false`) 1.000 with strict.
  Every lenient-side disagreement (639 calls, all `type_change`) is an integer sent to a
  parameter that became a string: the mock's lenient profile coerces it, pydantic v2 lax mode
  does not. P16 is scored from this file in Task 8. The Phase-2 log checker now takes
  `--phase 2` (Task 5); Phase-1 gates are unchanged and still pass.
- 2026-10-28 Decoding probe (Task 6, after Phase 2 amendment 1):
  `results/phase2/probe_decoding.json`, 8 routes x 4 cases x 3 reps = 96 calls, $0.095.
  The two pilots are kept and not analysed: `probe_decoding.pilot-chat-completions.json`
  (all routes, 1 rep; luna's 400s) and `probe_decoding.pilot.json` (luna direct on the
  Responses API, 1 rep). Every call was served by its pinned provider (Anthropic, Novita,
  openai-direct), with no errors and no truncation. Comply k of 9 (off_enum, off_type,
  undeclared), strict unset / false: Haiku 4 / 4, Sonnet 4 / 4, Llama 9 / 9, luna direct
  0 / 2. optional_fill: luna direct unset 3/3, every other route 0/3.
  **Decision (pre-registered rule): no luna direct route lifts, so the `direct` arm does
  not run; P15 is untested and luna's diff question is reported as not testable on
  OpenRouter or the OpenAI direct API.** Descriptive: with `strict` absent, luna direct
  behaves as luna on OpenRouter did in Phase 1: every call carries `label`, requested
  values move into it (`label: "3 items"`, `label: "hi"`), or luna declines in text. With
  `strict: false` it sent `"gamma"` once and `count: "3 items"` once, so decoding on that
  route does not hold it to the schema; the other 7 were text refusals (4) and a dropped
  `note` (3). Logged spend $11.88.
- 2026-10-28 Run pilots (Task 6): `--limit 5` per arm on Sonnet, Haiku and Llama (core,
  placement) and Flash (fill), 35 episodes, $0.065, files `results/phase2/*.pilot.jsonl`
  (never analysed). All 7 gates PASS with `--pilot` (Flash with `--reasoning MINIMAL`);
  every episode on its pinned provider (Anthropic, Novita@bf16, Google), no truncation.
  Projection from pilot usage: Sonnet $8.2 (1,440 episodes x $0.0057, under the $15 stop),
  Haiku $0.6, Llama $0.2, Flash fill $0.25; total $9.2, cumulative about $21 of $50.
  Claude thinks by default and Llama on Novita sends numbers as strings: see Phase 2
  amendment 2. Logged spend $11.95.
- 2026-10-28/29 Full runs (Task 7): four streams in parallel, arms one after another,
  every arm gated (Flash with `--reasoning MINIMAL`). All arms PASS with 100% coverage and
  one provider per file (Anthropic, Novita@bf16, Google); truncation at most 1.7% per cell
  (Haiku), 0.8% (Sonnet, Llama). Episodes and spend: Sonnet 1,440, $7.01; Haiku 1,440,
  $0.39; Llama 1,440, $0.17; Flash fill 360, $0.23. The luna `direct` arm did not run (no
  lift in the probe). Interruptions, each resumed with the same command (resume-safe, no
  partial records): Novita rate-limited Llama (HTTP 429) three times; Sonnet (685/720 core)
  and Haiku (infoform 58/240) stopped within 20 s of each other on HTTP 502 "forbidden:
  Request not allowed" from Anthropic via OpenRouter and ran on without further errors.
  **Deviation from "records are never edited by hand" (user's decision, 2026-10-29).** One
  Llama core record (zip03 / B_strict / type_change, rep 0) failed the gate: Novita returned
  `finish_reason` null on a call whose arguments parsed to `{}` (the raw response is not
  kept). The record was moved verbatim to `results/phase2/removed_records.jsonl` and the job
  re-run: `finish_reason` tool_calls, full arguments (numbers and booleans as strings, as in
  Llama's other calls), ERROR_SURFACED, the same outcome as the removed record. All five
  Llama arms then PASS. Logged spend $19.69.

## Phase 2 pre-registration — LOCKED 2026-10-20

Written before any Phase-2 model call. Execution plan: `phase2/PLAN.md`. Testbed unchanged
(sha256 e8bbd71c...). Phase-1 rules (recovery, "unlocks", noise floors, BH) carry over
unless restated here.

**Families and arms.** New families: Claude Haiku 5.5 and Claude Sonnet 5.5
(`anthropic/...` on OpenRouter, provider `anthropic`), and Llama 3.3 70B Instruct
(`meta-llama/llama-3.3-70b-instruct`, provider `novita`, `quantizations: ["bf16"]`). Every
call pins one provider with no fallbacks; temperature 0; `max_tokens` 700; no `reasoning`
field. Each new family runs on the primary 120 pairs (24 per class):
- `core`: A, B_strict, B_lenient, C, D, E (September's grid, 720 episodes);
- `phrasing`: A and B_strict on phrasing 1 (240);
- `noise`: B_strict on the 30 stratified tasks × 5 reps (150);
- `infoform`: CD and Dprime (240);
- `placement`: `C:user:prose:apply`, Qwen's best Phase-1 cell (120).

Gemini Flash (`MINIMAL` thinking): `fill` arm, A_fill, B_fill and a B_strict re-run on the
primary 120 (360). luna: decoding probe on the OpenAI direct API, then the contingent
`direct` arm below.

**Fill instruction (exact).** In `harness.SYSTEM` the sentence "Use parameter defaults by
omitting a parameter when the user does not specify it." is replaced by "Pass every
parameter explicitly, including optional ones; when the user does not specify a value,
pass the documented default." A_fill and B_fill are A and B_strict with that system
prompt; nothing else differs.

**Decoding probe (instrument check, not in BH).** Phase-1 `probe_decoding` cases and
rule, on: Claude Haiku and Sonnet (`anthropic`), Llama (`novita`, bf16), and luna on the
OpenAI direct API, each with `strict` unset and `false` (8 routes, 96 calls). New-family
results are descriptive and are read before their runs. luna: a direct route *lifts* at
compliance ≥ 7/9. The `direct` arm runs only on a lifting route (highest k; ties go to
`strict` unset): A, B_strict, `C:sys:json:none`, `C:user:prose:apply` on the primary 120
(480). No lift: P15 is untested and luna's diff question is reported as not testable on
OpenRouter or the OpenAI direct API.

**Predictions.**
- P10. Claude Haiku 5.5 and Claude Sonnet 5.5 each: C unlocks recovery (diff in the system
  prompt), on all 120 pairs.
- P11. Llama 3.3 70B: C recovery < 0.5, and `C:user:prose:apply` − C ≥ 0.30 in recovery
  units with the paired test `C:user:prose:apply − C` surviving BH.
- P12. D' − D on newly-required (24 pairs) ≥ 0.30 in each new family (P5 extended).
- P13. C+D ≥ max(C, D) in each new family; fails in a family when the CI of C+D − C or of
  C+D − D lies wholly below 0 (pin A7, P7 extended).
- P14. Flash: B_fill − B_strict (re-run) ≥ +0.30 on required + default_change (48 pairs)
  with the CI excluding 0 and the test surviving BH; and the CI of B_fill − B_strict on
  rename + enum_tighten + type_change (72 pairs) lies inside [−0.10, +0.10].
- P15 (contingent). On the lifting direct route, luna's `C:user:prose:apply` unlocks
  recovery on the 72-pair contrast set, with A and B_strict from the same arm.
- P16 (descriptive, not in BH). Over the replayed drift-step calls, pydantic v2 defaults
  and FastAPI agree with the lenient profile on ≥ 95% of calls, and JSON Schema with
  `additionalProperties: false` agrees with the strict profile on ≥ 95%.

**Decision rules.**
- Recovery = (success(X) − success(B_strict)) / (success(A) − success(B_strict)), paired
  per pair; "unlocks" = recovery ≥ 0.5 AND paired 95% CI of X − B_strict excludes 0 AND
  the test survives BH.
- Noise floor per new family = its own `noise` arm flip rate; Flash keeps 0.133. A
  difference below the floor is "within noise" whatever its p.
- Pair sets: new families on all 120; information vs form on the 48 required +
  default_change pairs; P12 on the 24 required pairs; luna direct on the 72 contrast pairs.
- A new-family arm with missing jobs adds no tests and its predictions are reported as
  pending.
- Any reversal is reported plainly. A Sonnet projection above $15 after the pilot stops
  the run until the user decides.

**BH family.** One family: the 194 existing tests plus 107 = 301 (303 if the `direct` arm
runs). Per new family (35 × 3 = 105): September's 27 core tests (drop, C/D/E − B_strict
per class and overall, three interactions), 2 phrasing tests (A, B_strict), 4
information-vs-form tests (C vs D', D' vs D, C+D vs C, C+D vs D), 2 placement tests
(`C:user:prose:apply` − B_strict, `C:user:prose:apply` − C). Flash fill: 2 tests (B_fill −
B_strict on the 48 and on the 72). `direct`: `C:sys:json:none` − B_strict and
`C:user:prose:apply` − B_strict on the contrast set. Labels carry the prefix `p2:`.
Analysis RNG: `RNG_P2 = default_rng(20261020)`; `N_BOOT = 10_000`, `N_PERM = 20_000`.

**Label audit.** Stratified sample of Phase-2 main records (model × automatic label, at
least 2 per non-empty stratum, seed 20261020), labelled blind by Codex; the user reads the
disagreements. Agreement ≥ 0.9 keeps `drift_labels.classify`; below that, it is fixed
before the final analysis.

**Logging required before the run.** Every record carries model, provider, endpoint,
quantization (when pinned), `strict`, `meta.model` and `finish_reason`; the gate fails a
file with more than one provider, version or quantization, or with > 5% truncation in a
cell.

## Phase 2 amendment 1 — 2026-10-28, after the 32-call probe pilot, before the full probe
Changes how the luna direct route is called; the probe rule, the `direct` arm, P15 and the
BH count are unchanged. Written after seeing the pilot (`probe_decoding.py --phase 2
--reps 1`, $0.03) and before any full-probe call.

**Why.** All 8 luna direct calls failed with HTTP 400: "Function tools with reasoning_effort
are not supported for gpt-5.6-luna in /v1/chat/completions. To use function tools, use
/v1/responses or set reasoning_effort to 'none'." The pre-registered request (no reasoning
field, so luna's default effort) cannot reach luna through chat completions.

**New request (user's decision, 2026-10-28).** The OpenAI direct endpoint posts to the
Responses API (`/v1/responses`, `experiments/openai_responses.py`): the same system
prompt, user message, transcript (as `function_call` / `function_call_output` items with
the same call ids) and declarations; the per-tool `strict` flag unset or `false` as
pre-registered (with the flag absent the API applies its own default, which the probe
measures); `max_output_tokens` 700; no reasoning field (the API's default; the response
reports effort `medium`); `store: false`. **No temperature is sent on this route only**:
the Responses API rejects it for luna ("Unsupported parameter: 'temperature' is not
supported with this model"). Every other route keeps temperature 0.

**Rejected alternative.** Chat completions with `reasoning_effort: "none"` keeps
temperature 0 but turns reasoning off, which Phase-1 luna on OpenRouter had (mean 63
reasoning tokens); a lift there could not be told apart from switching reasoning off.

**Seen before this amendment (disclosed; not data).** Pilot, 1 rep, comply k of 3:
Haiku unset 0, false 2; Sonnet unset 2, false 1; Llama unset 3, false 3 (Llama sends
`count` as the string "3" in every case); optional_fill 0 of 1 on every route. Two
diagnostic off_enum calls to luna ($0.0003, tagged `p2-diag-*` in the cost log): chat
completions with `reasoning_effort: "none"` sent `"gamma"`; the Responses API at default
reasoning made no tool call.

## Phase 2 amendment 2 — 2026-10-28, after the 35-episode run pilot, before any full run
Corrects the parenthetical "(Claude extended thinking off)" in `phase2/PLAN.md` Global
Constraints; the request, arms, predictions and rules are unchanged.

**Why.** With no reasoning field, as pre-registered, Claude Haiku 5.5 and Sonnet 5.5 on
OpenRouter (`anthropic`) think by default: pilot episodes report reasoning tokens (Haiku up
to 495, Sonnet up to 299) and the responses carry `reasoning.text` blocks. A replay of one
Haiku pilot episode with `reasoning: {"enabled": false}` was accepted and used 0 reasoning
tokens (both replays ended ERROR_SURFACED, like the pilot record).

**Decision (user, 2026-10-28).** Keep the pre-registered request: no reasoning field, so
Claude runs at the provider default (thinking on), as luna does. Records keep
`reasoning: "default"`; reasoning tokens are in `usage.reasoning`.

**Known limitation, reported with the results.** The runner sends earlier turns back as
tool calls and tool results only. Claude's thinking blocks are not returned, so each turn
of a multi-step episode thinks afresh.

**Seen before this amendment (disclosed; not data).** Pilot successes: Haiku 9/10,
Sonnet 8/10, Llama 1/10, Flash fill 3/5. Llama on the pinned route (`novita`, bf16) sends
integers and booleans as strings (`"weight_grams": "500"`, `"visible": "true"`) in 10 of
13 pilot calls; the strict executor rejects them, so 8 of 10 episodes end on a type error,
condition A included. One `optional_fill` probe call per Llama provider ($0.0005, tagged
`p2-diag-llama-types-*`): Novita and CoreWeave sent `count: "3"`, DeepInfra sent
`count: 3` and also filled the optional `label`.

## CP1 · Lit review + pre-emption — DONE 2026-09-08, awaiting approval
- [x] Angle agents (4) + recency sweep -> lit_review/lit_review.csv (55 ids, all verified
      against export.arxiv.org on 2026-09-08)
- [x] Full-text pre-emption reads: MCPEvol-Bench (2607.14642 — EXISTS), ToolBench-X
      (2606.25819, paper+code), ToolMisuseBench (2604.01508, paper+code)
- [x] LIT_REVIEW.md with novelty-delineation table
- [x] Verdict: ALIVE-BUT-CROWDED -> GO with reframing. Headline = C3 (diff-conditioning
      recovery comparison) + C2 (drift-class-conditioned silent/wrong-semantics ledger);
      C1 (deterministic minimal-pair drift taxonomy) demoted to instrument; C4 table stakes.
      "First drift benchmark" framing is dead (MCPEvol-Bench, ToolBench-X own it).
- [ ] **REPORTED TO USER, APPROVAL RECEIVED: ____**

Key sanity checks (2026-09-08): Gemini key OK; Modal profile OK;
OpenRouter key has ~$0.83 remaining of its $5 cap (4.17 used) — GPT arm must be scoped
tightly or key topped up before CP3.

## CP2 · Experiment plan frozen — DONE 2026-09-09, awaiting approval
- [x] EXPERIMENT_PLAN.md + site/plan.html; budget table totals ~$17.4 of $30 cap
- [x] Pre-registered directions recorded above, dated 2026-09-09
- [x] experiments/cost_tracker.py armed with the $25 hard stop (+ Modal GPU logging)
- [x] Design: SchemaDrift-120 (30 tools / 120 tasks / 2 phrasings), 5 deterministic
      minimal-pair drift classes (48 pairs/class doubled, 24/class primary), conditions
      A/B-strict/B-lenient/C-diff/D-fullschema/E-retry, 4 families, outcome ledger with
      ACCEPTED_WRONG cell + n>=20 manual audit, noise floor 30x5, interaction tests + BH
- [ ] **REPORTED TO USER, APPROVAL RECEIVED: ____**

## CP3 · Experiments + analysis — IN PROGRESS
- [x] Frozen testbed/corpus: SchemaDrift-120 (30 tools, 120 tasks, 30 two-step,
      48 task-drift pairs/class, primary 24/class); executor+harness 12/12 tests green.
      First freeze b009f779... (2026-09-09) was amended ONCE during pre-drift baseline
      calibration (Flash condition-A 114/120): 3 phrasing ambiguities fixed (rem01,
      log04, ride03) + case-insensitive free-string canonicalization; no drifted arm
      had run. Final frozen sha256:
      e8bbd71c63b1311c76b87ceabe45456217f9054f2d5f010517e3930209d08475
- [x] All arms run 2026-09-09 (4,800 records): Flash full grid (core doubled + noise
      30x5 + phrasing), Pro primary, gpt-5.6-luna primary (OpenRouter, $0.10),
      Qwen2.5-7B full grid on Modal A10G (+noise+phrasing)
- [x] Noise floor (Flash flip 13.3%, Qwen 0.0%), phrasing battery null (p .27-1.0),
      class x condition interactions tested directly, BH over 112 tests -> 74 survive
      (threshold .0316)
- [x] analyze.py -> results/analysis.json; hand audit
      results/audit_accepted_wrong_sample.json (24/24 confirmed)
- [x] Spend: $7.64 of $25 hard stop
- [ ] **REPORTED TO USER (headline numbers), APPROVAL RECEIVED: ____**

Headline: B_strict success 11-38% vs baselines 87-99%. Diff recovery: Gemini 0.96-0.98
(beats full-schema 0.82-0.83), Qwen 0.06, luna -0.06 (CI<0). Luna fills 100% of optional
params (Flash 53%) -> immune to required+default drift by calling style. default_change
is the only universally silent class; type/rename silent only under lenient executor.
D1 partially reversed as pre-noted; D2 holds for Gemini only (diff=13.7% of schema
tokens, not <10%); D3 strongly confirmed; D4 confirmed (audited).

## CP4 · Paper — DONE 2026-09-09, awaiting approval
- [x] ICLR dual build compiles (tectonic): paper_iclr_preprint.pdf (named) +
      paper_iclr_submission.pdf (anonymous), 15 pages, 0 unresolved cites
- [x] Title: "The Schema Changed and Nobody Told the Agent: Silent Failure and
      Diff-Conditioned Recovery under Tool-Schema Drift"
- [x] 4 figures (HTML->Chrome teaser + 3 matplotlib house-style, all traced to
      analysis.json via figures/build_figures.py)
- [x] 41 references, ALL verified by 3 batch agents (41/41 OK; venues checked)
- [x] Appendix: freeze provenance + amendment note, verbatim prompts/diff/errors,
      per-class tables, full ledger, audit sample table, batteries, BH detail
- [x] Register check: no em/en dashes, no banned words; BH survivors bolded
- [ ] **DELIVERED TO USER, APPROVAL RECEIVED: ____**

## CP5 · Publish — DONE 2026-09-09, awaiting approval
- [x] Public repo (public repository) (.env verified absent from
      index at every commit; repo was private, flipped public for Pages)
- [x] Pages site rebuilt in the
      script-bias aesthetic (Georgia serif, numbered narrative sections, TOC, stat
      cards, GIF figure cards); both paper PDFs served from the site
- [x] Film: 3:25, 1080p60, Matilda narration phrase-anchored via ElevenLabs timestamps,
      ElevenLabs music bed ducked under narration, two-pass loudnorm (-14.8 LUFS,
      -1.2 dBTP), continuous motion (bars grow on spoken numbers, counters count);
      embedded at the top of the site (9.9 MB)
- [x] 3 concept GIFs (840x840, flat charts, monospace numerals, script-bias card look):
      the-drop, the-call-that-never-errors, the-28-token-fix; embedded in the site
- [ ] **LINKS DELIVERED, APPROVAL RECEIVED: ____**

## CP6 · Self-review + handoff — DONE 2026-09-23
- [x] Simulated A* review done (kept with the paper materials, outside this repo)
- [x] Paper source and PDFs moved out of this repository; the repo now carries the
      testbed, logs, analysis, figures, website and film
- [x] HANDOFF.md (reproduce first, then roadmap), README.md (setup + reproduction),
      requirements.txt, .env.example

## Spend log
| Date | Item | Amount | Running total |
|---|---|---|---|
