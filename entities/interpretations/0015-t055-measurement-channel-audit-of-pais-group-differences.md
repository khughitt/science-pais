---
id: interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences
type: interpretation
title: "Systematic measurement-channel audit of PAIS group-difference claims (h0008 promotion criterion #1) — coding 11 corpus claims by channel × ascertainment-control × behaviour-under-objective-re-measurement: 6/9 determinate claims artifact-consistent (M1/M2/M3) against a bounded 3-member objective-exception set; self-report-/mixed-origin claims attenuate 4/4 and weak-ascertainment claims collapse 3/3, but objective-origin claims are mixed (3 survive, 2 artifact-consistent) — so criterion #1 is met without a clean 'objective ⇒ survives' rule; two cross-trigger SAMENESS claims remain untested under a standardized protocol"
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

It is, at the level of the headline count — **6 of 9 determinate claims are artifact-consistent
(M1/M2/M3), against a fully enumerated 3-member bounded-exception set.** The directional sub-structure is
real but **weaker than a clean "channel predicts survival"** rule, and the honest cuts are:

- **Self-report- and mixed-origin claims attenuate or decompose — 4 of 4** (`proposition:0010` cognition
  [self-report], `proposition:0009` dysautonomia [mixed], `proposition:0001` menopause threshold [mixed],
  and the crude female-excess parent `proposition:0008` [mixed]). None survived as stated — the cleanest
  cut, and the one most directly confirming M1.
- **Weak-ascertainment determinate claims collapse or attenuate — 3 of 3** (`proposition:0001`,
  `proposition:0014` SFN prevalence, `proposition:0008`). This is the M2 cut: where ascertainment control
  is weak, the difference does not survive harmonization.
- **Objective-origin determinate claims are MIXED, not uniformly surviving — 3 survive, 2 do not.**
  Three survive and form bounded-exception set B (`proposition:0012` vascular male reversal,
  `proposition:0013` immune female exception, `proposition:0025` LC inflammatory activation); but two
  objective-origin claims are themselves artifact-consistent — `proposition:0014` (SFN prevalence,
  COLLAPSES/M2) and `proposition:0011` (cross-trigger PEM, ENDPOINT-CONTINGENT/M3). So "objective channel
  ⇒ survives" is **false as a rule**: an objective measurement can still be ascertainment-inflated (M2) or
  endpoint-contingent (M3). The bias is bounded in the objective channel, but the objective channel is not
  uniformly clean.
- **The third mode (M3, endpoint/construct instability) is instantiated once** (`proposition:0011`
  cross-trigger PEM): the cross-trigger *sameness* claim is contingent on which objective endpoint is
  chosen.
- **Two cross-trigger SAMENESS claims remain untestable** without a standardized head-to-head protocol
  (`proposition:0015` non-length-dependent SFN pattern, `proposition:0017` SFN cross-trigger
  convergence). They are coded `UNTESTED`, not counted toward the majority, and are precisely what
  `pre-registration:0003` is designed to resolve.

So the regularity that held is the **establishment-channel and ascertainment-control cuts** (self-report/
mixed-origin attenuate 4/4; weak-ascertainment collapse 3/3), **not** a clean "objective ⇒ survives" rule
— two objective-origin claims are artifact-consistent. That is enough to satisfy criterion #1 (a
directional majority with a bounded exception set) without overclaiming an M1 channel substructure the
table does not support; it is still *not* the unfalsifiable "everything is artifact" caricature the
bounding clause was written to prevent.

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

**Directional sub-structure (the cuts that actually hold — and the one that does not):**

- **By establishment channel** (claims 1–9 split on axis (a)):
  - self-report / mixed-origin → attenuate/decompose: **4/4** (claims 1 [self-report], 2, 3, 5 [mixed]).
    No survivors. *This is the M1 cut and it holds cleanly.*
  - objective-origin → **mixed: 3 survive (claims 7, 8, 9), 2 are artifact-consistent** (claim 4
    COLLAPSES/M2, claim 6 ENDPOINT-CONTINGENT/M3). **"Objective ⇒ survives" is false** — an objective
    measurement can still be ascertainment-inflated or endpoint-contingent.
- **By ascertainment control** (claims 1–9 split on axis (b)):
  - weak-ascertainment determinate claims → collapse/attenuate: **3/3** (claims 3, 4, 5). *This is the M2
    cut and it holds.*
  - strong/partial-ascertainment determinate claims → 5 of 6 are the surviving objective exceptions plus
    the two attenuating sex claims; no clean rule.

There is **no** "channel predicts survival 8/8" rule: that count was an artifact of placing objective-but-
weak claim 4 on the attenuation side and dropping objective claim 6. The defensible regularities are the
**self-report/mixed-origin → attenuate (4/4)** and **weak-ascertainment → collapse (3/3)** cuts, which
together carry M1 and M2; the objective channel is bounded but not uniformly clean.

**Untested (n = 2; claims 10, 11):** both are cross-trigger/anatomical *sameness* claims that require a
standardized protocol that does not yet exist. Reported, excluded from the majority denominator. Their
resolution is the job of `pre-registration:0003` (cross-syndrome paired-site biopsy with
primary-dysautonomia controls).

**Corroborating sub-audit (not double-counted):** `interpretation:0006` is itself a four-domain objective
sweep that returned 3 nulls/gaps + 1 surviving exception (the immune signal, claim 8) — an
independently-constructed mini-replication of this audit's attenuate-dominant-with-bounded-exception shape
within a single deliberate objective-domain search.

## What this does and does not establish

**Establishes (criterion #1 met):**
- A directional majority (6/9 determinate) is artifact-consistent, against a bounded enumerable exception
  set — the decision rule for criterion #1.
- The M1 cut holds in the establishment-channel and ascertainment-control directions: self-report/mixed-
  origin claims attenuate or decompose (4/4) and weak-ascertainment claims collapse (3/3). It does **not**
  hold as a clean "objective ⇒ survives" rule (two objective-origin claims are artifact-consistent), so M1
  is supported as a channel/ascertainment regularity, not as a property of the objective channel per se.
- M2 (ascertainment/scoring inflation) and M3 (endpoint instability) each have ≥1 clean determinate
  instance — and both are instantiated by *objective-origin* claims (4 and 6), which is why the objective
  channel is not uniformly clean.
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
   (criterion #2 + resolves claims 10–11 simultaneously), not more retrospective coding — the
   self-report/mixed-origin attenuation cut is near-saturated (4/4) and further within-corpus coding will
   mostly re-confirm it.
4. **Continue the exception-set count** as the cheap continuous signal: a fourth, fifth, … robust
   objective trigger-matched survivor each nudges "predictable bias" toward "sometimes-artifact." Three is
   bounded; track the rate.
