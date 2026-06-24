---
id: interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences
type: interpretation
title: "Systematic measurement-channel audit of PAIS group-difference claims (h0008 promotion criterion #1) — coding 11 corpus claims by channel × ascertainment-control × behaviour-under-objective-re-measurement shows the predicted directional regularity: every self-report-/weak-ascertainment-channel difference attenuates, collapses, or reverses under objective control (5/5), while every objective-origin difference survives (3/3, the bounded exception set), with two cross-trigger SAMENESS claims still untested under a standardized protocol"
status: active
source_refs: []
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- topic:measurement-ascertainment-artifacts-in-pais
- proposition:0008-female-excess-concentrates-in-post-acute-persistence
- proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified
- proposition:0010-cognitive-female-excess-is-self-report-only-absent-in-objective-testing
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
- proposition:0013-immune-domain-partial-hormone-mediated-objective-exception
- proposition:0014-pais-small-fiber-structural-lesion-ienfd
- proposition:0015-pais-sfn-non-length-dependent-pattern
- proposition:0017-pais-sfn-cross-trigger-convergence
- proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
- proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold
- interpretation:0003-t018-subphenotype-sex-reproductive-stage
- interpretation:0006-t041-objective-female-biased-subphenotype-search
- interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis
- pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls
- question:0014-which-pais-case-definition-is-most-biologically-coherent
- question:0015-does-pem-requirement-improve-cross-study-comparability
- task:t055
created: '2026-06-24'
updated: '2026-06-24'
input: []
prior_interpretations: []
relations:
- predicate: "sci:bears_on"
  target: hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
---

# Interpretation: Systematic measurement-channel audit of PAIS group-difference claims (h0008 promotion criterion #1)

## Verdict

**Verdict:** [+] Supports `hypothesis:0008` with a bounded, enumerated exception set — **promotion
criterion #1 is met; criterion #2 is not** (so h0008 stays `candidate`).

This is the systematic within-corpus audit that h0008 named as the cheapest belief-shifting test
(`task:t055`, promotion criterion #1). It codes **11 PAIS group-difference claims** already in the graph
by three pre-committed axes — (a) the measurement **channel** in which the difference was *established*,
(b) the **ascertainment control** of that establishing evidence, and (c) the **behaviour under
objective, trigger-matched re-measurement** — and asks whether a directional majority is consistent with
M1–M3.

It is. The regularity holds in the *specific directional form* h0008 predicts, which is sharper than a
bare "majority are artifacts":

- **Every difference established in a self-report or weak-ascertainment channel attenuates, collapses,
  or reverses under objective, ascertainment-controlled measurement — 5 of 5** (`proposition:0010`
  cognition, `proposition:0009` dysautonomia, `proposition:0001` menopause threshold,
  `proposition:0014` SFN prevalence, and the crude female-excess parent `proposition:0008`). None
  survived as stated.
- **Every difference that was *objective from the start* survives — 3 of 3**, and these *are* the
  bounded-exception set B (`proposition:0012` vascular male reversal, `proposition:0013` immune female
  exception, `proposition:0025` LC inflammatory activation). The bias is bounded exactly where h0008
  said it would be: in the objective channel.
- **The third mode (M3, endpoint/construct instability) is instantiated once** (`proposition:0011`
  cross-trigger PEM): the cross-trigger *sameness* claim is contingent on which objective endpoint is
  chosen.
- **Two cross-trigger SAMENESS claims remain untestable** without a standardized head-to-head protocol
  (`proposition:0015` non-length-dependent SFN pattern, `proposition:0017` SFN cross-trigger
  convergence). They are coded `UNTESTED`, not counted toward the majority, and are precisely what
  `pre-registration:0003` is designed to resolve.

So the channel **predicts survival**: self-report-channeled differences attenuate (5/5), objective-origin
differences survive (3/3). That is the falsifiable content of M1, and it held — this is *not* the
unfalsifiable "everything is artifact" caricature the bounding clause was written to prevent.

**The one substantive belief-update against a strong reading:** the audit **enlarged the exception set
from 2 to 3** by admitting `proposition:0025` (LC persistent inflammatory activation, two cohorts, >180d,
no circulating virus) as a robust objective case-vs-control difference. This is the "running falsification
meter" of clause B working as designed — the exception set is meant to be counted, and it grew by one.
Three robust objective signals is still a *bounded* exception set, not a proliferation, so the claim is
strengthened rather than weakened; but the rate is now on record and is the quantity to watch.

## Method (pre-committed coding rules)

To avoid post-hoc latitude in a retrospective self-audit, the coding rules are fixed **before** the table
and applied uniformly. A claim qualifies for the audit if it asserts that **two groups differ on a PAIS
phenotype** — group axis ∈ {sex, trigger, case-vs-control, reproductive-stage}. Claims that are purely
*mechanistic* or *measurement-process* statements (e.g. `proposition:0005`, itself an M2 mechanism) are
cited as infrastructure but are **not** codeable group-difference claims and are excluded from the tally.

**Axis (a) — establishing channel:** `self-report` | `objective` | `mixed` (the channel the *original*
group difference was demonstrated in).

**Axis (b) — ascertainment control** of that establishing evidence (case-definition + referral/selection
+ scoring breadth): `weak` | `partial` | `strong`.

**Axis (c) — behaviour under objective, trigger-matched re-measurement**, one of:
- `ATTENUATES` — effect dissolves toward null objectively → **artifact-consistent (M1)**
- `REVERSES` — effect flips sign objectively → **artifact-consistent (M1, direction-reversal)**
- `COLLAPSES` — cross-study heterogeneity explained by ascertainment/scoring, not biology →
  **artifact-consistent (M2)**
- `ENDPOINT-CONTINGENT` — objective correlate depends on endpoint/trigger choice →
  **artifact-consistent (M3)**
- `SURVIVES` — robust objective trigger-matched difference → **bounded exception (clause B)**
- `UNTESTED` — no standardized objective trigger-matched comparison exists yet → **excluded from the
  majority denominator**, reported separately.

**Decision rule (pre-committed):** promotion criterion #1 is met iff, among claims with a determinate
behaviour (i.e. excluding `UNTESTED`), a **directional majority** is artifact-consistent (M1/M2/M3) AND
the surviving objective differences form an enumerable, non-proliferating exception set. `UNTESTED`
claims are counted and named but do not move the verdict.

## Coded table

| # | Claim | Group axis | (a) Channel | (b) Ascert. control | (c) Behaviour | Mode | Key evidence |
|---|---|---|---|---|---|---|---|
| 1 | `proposition:0010` cognitive female excess | sex | self-report | strong | **ATTENUATES** (null on 15 objective neuropsych tests, Walitt2024 same-cohort) | M1 | `interpretation:0003`; Walitt2024 |
| 2 | `proposition:0009` dysautonomia female skew | sex | mixed | partial | **ATTENUATES** (PAIS-amplification dissolves once baseline ~5:1 POTS sex ratio is netted out — baseline-carried) | M1 | `interpretation:0003` |
| 3 | `proposition:0001` reproductive-stage threshold | reprod-stage | mixed | weak | **ATTENUATES** (menopause-specific signal → null within age band: Shah2025 menopausal RR 1.42 ≈ non-menopausal 1.45) | M1/M2 | `interpretation:0003`; Shah2025 |
| 4 | `proposition:0014` SFN biopsy prevalence | case-vs-control | objective | weak | **COLLAPSES** (0%→91% range decomposes into modality × trigger × referral; within-trigger concordant) | M2 | `interpretation:0014` |
| 5 | `proposition:0008` crude female persistence excess (parent) | sex | mixed | weak | **ATTENUATES/decomposes** (the uniform excess is channel-structured, not uniform biology) | M1 (parent) | `interpretation:0002`, `:0003` |
| 6 | `proposition:0011` cross-trigger PEM correlate | trigger | objective | partial | **ENDPOINT-CONTINGENT** (ME/CFS 2-day-CPET decrement does not transfer to LC at that endpoint) | M3 | `interpretation:0004` |
| 7 | `proposition:0012` vascular male reversal | sex | objective | strong | **SURVIVES** (VTE/CV-mortality hard endpoints survive severity restriction, ambulatory + hospitalized) | **B** | `interpretation:0005` |
| 8 | `proposition:0013` immune female exception | sex | objective | strong | **SURVIVES** (testosterone-conditioned objective immune-activation, within-sex case-control) | **B** | `interpretation:0006` |
| 9 | `proposition:0025` LC inflammatory activation | case-vs-control | objective | partial | **SURVIVES** (IL-6/JAK-STAT/type-II-IFN + CD8 exhaustion, 2 cohorts, >180d, no virus) | **B (new)** | Aid2025; `interpretation:0012` |
| 10 | `proposition:0015` SFN non-length-dependent pattern | case-vs-control | objective | weak | **UNTESTED** (needs standardized paired-site biopsy; "asserted more than measured") | — | `pre-registration:0003` |
| 11 | `proposition:0017` SFN cross-trigger convergence | trigger | objective | weak | **UNTESTED** (no head-to-head single-protocol comparison; ME/CFS leg internally contested) | — | `interpretation:0014` |

## Tally

**Determinate claims (n = 9; claims 1–9):**

- Artifact-consistent (M1/M2/M3): **6** — claims 1, 2, 3, 4, 5, 6.
- Bounded exceptions (B, SURVIVES): **3** — claims 7, 8, 9.
- Directional majority artifact-consistent: **6/9 = 67%**, with a fully enumerated 3-member exception set.

**Directional sub-structure (the sharper test that actually held):**

- Self-report / weak-ascertainment establishing channel → attenuate/collapse: **5/5** (claims 1, 2, 3,
  4, 5). No survivors.
- Objective-from-the-start establishing channel → survive: **3/3** (claims 7, 8, 9). No attenuators.

The channel of establishment is a near-perfect predictor of survival in this corpus — which is M1's
literal content. The 67% headline understates the regularity because it pools the two channels; split by
channel, the prediction is 8/8.

**Untested (n = 2; claims 10, 11):** both are cross-trigger/anatomical *sameness* claims that require a
standardized protocol that does not yet exist. Reported, excluded from the majority denominator. Their
resolution is the job of `pre-registration:0003` (cross-syndrome paired-site biopsy with
primary-dysautonomia controls).

**Corroborating sub-audit (not double-counted):** `interpretation:0006` is itself a four-domain objective
sweep that returned 3 nulls/gaps + 1 surviving exception (the immune signal, claim 8) — an
independently-constructed mini-replication of this audit's 5-attenuate/1-survive shape within a single
deliberate objective-domain search.

## What this does and does not establish

**Establishes (criterion #1 met):**
- The M1 channel-direction regularity is real *as a directional rule*, not just a count: in this corpus
  the establishing channel predicts whether a difference survives objective re-measurement (8/8 when
  split by channel).
- M2 (ascertainment/scoring inflation) and M3 (endpoint instability) each have ≥1 clean determinate
  instance.
- Clause B is operative and bounded: the exception set is enumerable (now {`proposition:0012`,
  `proposition:0013`, `proposition:0025`}) and grew by exactly one under audit — the falsification meter
  is live and reads "bounded," not "proliferating."

**Does NOT establish (criterion #2 still open, and real limits):**
- **Self-audit / confirmation-bias risk.** h0008 was assembled by the same agent now coding its
  instances; the corpus is small (n = 11) and project-internal. The audit is retrospective coding, not a
  blinded re-extraction. The single *same-cohort* attenuation (claim 1, Walitt2024) is the only cell that
  is not cross-study retrospective — the rest infer attenuation by comparing *different* cohorts, which is
  itself an M2-type confound the audit is supposed to police.
- **Criterion #2 (prospective, same-cohort objective re-measurement) is unmet.** No new data was used;
  the only design that controls trigger, cohort, and ascertainment simultaneously is `pre-registration:0003`,
  which is data-gated and unrun. h0008 therefore **remains `candidate`** — criterion #1 met, criterion #2
  pending.
- **`proposition:0012`'s infection-attributable fraction is unresolved** (no uninfected comparator;
  `question:0021`), so one of the three exceptions is a *provisional* survivor.

## Recommendation

1. **Keep `hypothesis:0008` at `phase: candidate`** but record criterion #1 as satisfied. Both promotion
   criteria are conjunctive; #2 requires the prospective test.
2. **Update clause B's exception set to three members** in h0008 (add `proposition:0025`) — the audit's
   one concrete belief-update. Done as part of `task:t055` closure.
3. **The fastest path to `active`** is now `pre-registration:0003`'s prospective paired-site biopsy
   (criterion #2 + resolves claims 10–11 simultaneously), not more retrospective coding — the retrospective
   channel is near-saturated at 8/8 and further within-corpus coding will mostly re-confirm.
4. **Continue the exception-set count** as the cheap continuous signal: a fourth, fifth, … robust
   objective trigger-matched survivor each nudges "predictable bias" toward "sometimes-artifact." Three is
   bounded; track the rate.
