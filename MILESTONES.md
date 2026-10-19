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

## Phase 1 run log
- 2026-10-19 pre-flight (no model calls): Gemini `gemini-3.6-flash` (version
  `3.6-flash-07-2026`) and `gemini-3.1-pro-preview` (version `3.1-pro-preview-01-2026`)
  listed; the September logs recorded no version string, so sameness cannot be shown.
  Prices: luna `openai` endpoint $0.20/$1.20 and Pro $2.00/$12.00 per M match
  `cost_tracker.PRICE`; Flash rose to $0.75/$3.75 (was $0.50/$3.00), PRICE updated.
  Credits: OpenRouter $30.00 unused; Gemini billing on the paid tier. Logged spend
  $7.64 of the $25 hard stop.

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
