---
title: 'Wave-1 hard checkpoint — coverage delta + design-premise correction'
status: active
created: '2026-07-03'
see_also:
- doc:2026-07-03-data-catalog-expansion-design
- doc:2026-07-03-gate0-triage
- doc:2026-07-03-wave1-gwas-mr-estimand
- doc:2026-07-03-gwas-mr-ingestion-handoff
- decision:D-004
---

<!-- Non-entity design/checkpoint doc under doc/plans/. No `type:` field, so
     `science validate` does not treat it as a mis-homed plan entity, consistent
     with the design doc's own convention. -->

# Wave-1 hard checkpoint (2026-07-03)

This is the design's §4 "Wave-1 hard checkpoint": after the Wave-1 handoffs land,
rerun `prioritize --coverage`, record the delta, and decide whether Waves 2/3
proceed as scoped or re-weight. It also records a design-premise correction
surfaced by Gate-0 triage that changes how §2c should be read going forward.

## 1. Coverage delta (recomputed and confirmed)

Recomputed via `uv run --frozen science graph build` then
`uv run --frozen science dataset prioritize --coverage --format json`, 2026-07-03,
against the current `data-catalog-wave1` branch state (Task 8's `related:` edges +
Wave-1 dataset entities committed).

```
BASELINE (pre-Gate-0, coverage-baseline-2026-07-03.json)
  31 targets: Counter({'no-candidate': 22, 'missing-required-capabilities': 9})

POST-GATE-0 (coverage-postgate0-2026-07-03.json)
  31 targets: Counter({'no-candidate': 22, 'covered-unstaged': 4,
                       'capability-mismatch': 3, 'covered-pointer': 1,
                       'covered-runnable': 1})

NOW (post-Task-8, recomputed 2026-07-03)
  31 targets: Counter({'no-candidate': 18, 'covered-reference': 4,
                       'covered-unstaged': 4, 'capability-mismatch': 3,
                       'covered-pointer': 1, 'covered-runnable': 1})
```

`missing-required-capabilities` is now `0` (was 9 at baseline) and has been `0`
since Gate-0. The Wave-1-specific movement is the `no-candidate` count: **22 → 18**,
a lift of exactly the 4 targets the Wave-1 GWAS/MR vehicle serves.

## 2. Which blocked clusters Wave 1 lifted

The open GWAS/MR vehicle (three candidates: `dataset:covid19-hgi-longcovid-gwas`,
`dataset:bentham-2015-sle-gwas`, `dataset:ruth-2020-shbg-testosterone-gwas`; see the
ingestion handoff, `doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md`) moved these 4
causal targets from `no-candidate` to `covered-reference`:

| Target | Lifted by | Estimand role |
|---|---|---|
| `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` | `dataset:ruth-2020-shbg-testosterone-gwas` | `mr_exposure` / `trait: sex-hormone-biomarker`, uniquely `stratification: sex` (truthful) |
| `hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` | `dataset:bentham-2015-sle-gwas` | `mr_exposure` / `trait: autoimmune-disease` |
| `hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune` | `dataset:bentham-2015-sle-gwas` | `mr_exposure` / `trait: autoimmune-disease` |
| `question:0022-immune-state-displacement-mediator-vs-co-traveler` | `dataset:covid19-hgi-longcovid-gwas` | `mr_outcome` / `trait: long-covid` (reverse-causation/mediation direction, estimand §b.1) |

`covered-reference` is the correct state, not `covered-runnable`: these are
candidate GWAS entities (`status: candidate`, sumstats not yet staged locally) whose
`provided_capabilities` satisfy the target's `required_capabilities` under the
capability vocabulary's exact-match rule
(`doc/plans/2026-07-03-capability-vocabulary.md`) — coverage is real but analysis
execution has not happened (see §4 below and the ingestion handoff).

Note that `hypothesis:0005` is covered here by the **causal-MR** route
(`ruth-2020-shbg-testosterone-gwas`), which is separate from — and additive to — the
plain **descriptive** `related:`-wiring the Gate-0 triage table flagged as
Gate-0-actionable-now (`dataset:uk-biobank-covid` / `dataset:my-lc-iwasaki-klein`
already carry `outcome: sex-hormone-level` + `stratification: sex`). The
capability-vocabulary rule that `analysis_role`/`trait` separate descriptive from
causal-MR coverage means these are two independent, non-collapsing routes to the
same hypothesis, both legitimate.

## 3. What remains blocked

**18 no-candidate targets** (genuine-discovery per the Gate-0 triage,
`doc/plans/2026-07-03-gate0-triage.md`), including:

- `question:0003-acute-severity-threshold-for-self-sustaining-pais` (sits alongside
  the 3 `capability-mismatch` targets below as a discovery gap — no dataset carries
  `stratification: severity`, used by zero of the 20 annotated datasets)
- `question:0015-does-pem-requirement-improve-cross-study-comparability` (no dataset
  carries `outcome: pem`)
- the antigen-persistence cluster: `hypothesis:0002`,
  `question:0002-antigen-clearance-rescues-symptoms`
- the immune-exhaustion/JAK-STAT cluster: `hypothesis:0003`,
  `question:0006-jak-stat-il6-driver-vs-marker`
- the muscle/mitochondrial-PEM cluster: `hypothesis:0006`,
  `question:0011-mitochondrial-basis-of-pem`
- the small-fiber-neuropathy/dysautonomia substrate cluster: `question:0004`,
  `question:0009-functional-autoantibodies-drive-dysautonomia` (t050-gated)
- the vascular/VTE-by-sex cluster: `question:0019`, `question:0020`,
  `question:0021`
- others with no corpus modality/outcome token at all: `question:0005`,
  `question:0008`, `question:0010`, `question:0012`, `question:0016`,
  `question:0018`

**3 capability-mismatch targets** (Gate-0-era discovery signals, unaffected by
Wave 1): `question:0003-acute-severity-threshold-for-self-sustaining-pais`,
`question:0014-which-pais-case-definition-is-most-biologically-coherent`,
`question:0015-does-pem-requirement-improve-cross-study-comparability` — each has
`required_capabilities` declared but zero dataset in the corpus provides a matching
set (0 `compatible_datasets`).

`hypothesis:0009` and `question:0005` were deliberately *not* lifted by wiring the
superficially-adjacent gated N3C/OpenSAFELY EHR capability (per D-004 and the Gate-0
triage's explicit anti-reopening rule); `hypothesis:0009` is lifted here instead
through the genuinely-open Bentham SLE GWAS route, which answers a narrower,
different estimand (see the estimand note, §c) — it does not retroactively validate
wiring the gated vehicle.

All 21 genuine-discovery targets from the Gate-0 triage remain open discovery gaps
for Waves 2/3 dataset discovery, **except** the 4 lifted above, which the triage had
also flagged as genuine-discovery under the *descriptive*-coverage reading but are
now separately reachable via the *causal-MR* route.

## 4. Design-premise correction (§2c terrain claim)

The design doc's §2c grounding scan (`doc/plans/2026-07-03-data-catalog-expansion-design.md`,
lines ~94 and its Gate-0 Step 1 worked example at line ~159) gives, as its
illustrative example of a *reconcilable* prose-only citation: **"RECOVER is
prose-cited by h0006 but its `related:` edge is not wired"** — i.e. it treats
`dataset:recover-adult` → `hypothesis:0006` as a case where a `science dataset link`
call would close the gap.

**This does not hold**, per the Task 2 grep (reused here, not re-litigated) recorded
in the Gate-0 triage: every occurrence of the string "recover" in `hypothesis:0006`'s
body is the plain-English word ("...continued exercise attempts without adequate
recovery...", etc.), not a citation to the RECOVER cohort. There is no prose
reference to reconcile. Independently, `dataset:recover-adult` has no
muscle-biopsy / mitochondrial-function assay in its `provided_capabilities` — even
if a `related:` edge were added, it would not satisfy h0006's actual evidentiary need
(a provoked muscle-biopsy time-course with mitochondrial and ionic measurement; see
the Gate-0 triage table). So the edge would be both unjustified (no real citation)
and, if added anyway, non-load-bearing (wrong capability).

**Correction for the record:** `hypothesis:0006` (and, by the same substrate-gap
reasoning, `hypothesis:0002` and `hypothesis:0003`) are **genuine-discovery gaps**,
not reconcilable prose-citation repairs. The design doc's §2c "RECOVER → h0006"
example should be read as **superseded by this correction** — it was a plausible-looking
illustration at design time that did not survive the literal grep once Task 2 ran.
This does not change §2c's larger structural claim (two coupled problems: capability-blind
reached targets vs. genuine-discovery no-candidate targets) — only its specific
worked example, which this document now corrects in place rather than editing the
original design doc (kept immutable as a dated design record).

## 5. Decision rule — do Waves 2/3 proceed as scoped, or re-weight?

Per the design's §4 hard checkpoint: **Waves 2/3 proceed largely as scoped, with one
re-weighting.**

**Reasoning:**

- The Wave-1 open-GWAS/MR vehicle worked as designed: it lifted exactly the causal
  targets it was built for (h0005, h0007, h0009, q0022) via a genuinely reproducible,
  third-party-verifiable route (GWAS Catalog public sumstats, `fullPvalueSet=true`,
  no gating) — validating the "open substitute for the gated arm" thesis in design
  §2(b) without reopening D-004.
- The `no-candidate` count (22 → 18) moved by exactly the targets Wave 1 targeted,
  with no unintended side effects on the `capability-mismatch` or other states —
  the capability-vocabulary role/trait separation (§4 of the vocabulary doc) held:
  causal-MR and descriptive coverage did not collapse into each other.
  This is evidence the Gate-0 machinery (capability vocabulary + coverage scan) is
  trustworthy enough to keep driving Waves 2/3 without new tooling.
- **Re-weighting:** the design-premise correction in §4 above means Wave 2's
  "thin-link repair" framing for h0006 (design §4, "h0006 (RECOVER only)") should be
  read as a **pure discovery task** (find an open muscle/exercise-physiology or PEM
  dataset from scratch), not a "repair an existing thin link" task — there was never
  a real link to repair. This does not change Wave 2's scope (open
  muscle/exercise-physiology / PEM datasets was already the stated discovery aim),
  only its framing and effort estimate (discovery-from-zero is typically higher
  effort than reconciling an existing citation).
- h0002/h0003 sit in the same corrected bucket (design §4's "h0002/h0003 (two
  datasets)" line already reads as discovery, not repair, and needs no correction).
- The 3 `capability-mismatch` targets (q0003, q0014, q0015) and the 18
  `no-candidate` targets remain live, unchanged-in-kind Wave 2/3 discovery input,
  exactly as scoped in the design's Wave 2/3 tables and the Gate-0 triage.
- The second Wave-1 open substitute named in the design (open
  epidemiology/surveillance for h0008/h0004) was **not** run in this pilot round
  (out of scope for Task 9 per the brief) and remains queued, either as "Wave-1
  round 2" or folded into Wave 2, per the design's own optionality.

**Rule stated plainly:** proceed with Waves 2/3 as scoped in the design doc, with
the h0006 (and by extension h0002/h0003) framing corrected from "repair" to
"discover", and with the epidemiology/surveillance open substitute still pending a
decision on whether it runs as a Wave-1 second round or inside Wave 2. No larger
re-plan is warranted — the coverage delta is a clean, additive win with no evidence
of capability-vocabulary drift or coverage-scan untrustworthiness.
