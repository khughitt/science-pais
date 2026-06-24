---
id: hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
type: hypothesis
title: Measurement-channel and ascertainment bias predictably shapes apparent PAIS
  group differences
status: proposed
phase: candidate
source_refs:
- cite:Walitt2024
- cite:Novak2026
related:
- topic:measurement-ascertainment-artifacts-in-pais
- topic:pais-case-definition-heterogeneity
- proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified
- proposition:0010-cognitive-female-excess-is-self-report-only-absent-in-objective-testing
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
- proposition:0013-immune-domain-partial-hormone-mediated-objective-exception
- question:0014-which-pais-case-definition-is-most-biologically-coherent
- question:0015-does-pem-requirement-improve-cross-study-comparability
- question:0018-objective-vs-subjective-cognition-dissociation-in
- interpretation:0003-t018-subphenotype-sex-reproductive-stage
- interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
- interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences
created: '2026-06-24'
updated: '2026-06-24'
---
# Hypothesis: Measurement-channel and ascertainment bias predictably shapes apparent PAIS group differences

## Organizing Conjecture

A substantial fraction of reported PAIS group and cross-trigger **phenotype differences are artifacts of
how a phenotype is measured and who is ascertained**, biased in a **predictable direction**: differences
inflate in self-report and selection/referral-enriched channels, and **attenuate toward null or reverse**
under objective, trigger-matched, ascertainment-controlled measurement.

This is a **methodological meta-hypothesis**, distinct in kind from the project's other hypotheses. It
makes **no pathophysiology claim** — it does not assert that PAIS lacks biology. It is a claim *about the
evidence*: it predicts **where** an apparent PAIS difference will survive objective re-measurement and
where it will dissolve, and it asserts the bias has a consistent enough direction to be useful as a prior.
It is the falsifiable promotion of the standing methodological check housed in
`topic:measurement-ascertainment-artifacts-in-pais`. Its claim layer is an **empirical regularity** over
the project's own corpus of group-difference findings, not a causal-effect or mechanistic claim.

The conjecture earns its keep only if it is **bounded**: genuine objective, trigger-matched group
differences exist and must be admitted (see the bounding proposition). Without that bound the hypothesis
degenerates into unfalsifiable "everything is artifact"; with it, the hypothesis is the specific, testable
claim that *the direction and locus of artifact are predictable*.

## Proposition Bundle

### Core Propositions

- **M1 — Channel-direction regularity** *(empirical_regularity)*. For a given PAIS construct, the apparent
  group difference is **systematically larger in — or confined to — the self-report channel** and is
  null, attenuated, or reversed when the *same construct* is measured objectively. Existing instances:
  `proposition:0010` (female cognitive excess present in subjective complaint, absent in objective
  neuropsychological testing); `proposition:0009` (dysautonomia female skew is baseline-carried, tracking
  the ~5:1 POTS baseline, not PAIS-amplified); and the mirror case `proposition:0012` (the *objective*
  vascular hard-endpoint signal runs male-biased — the opposite direction to the self-report female
  excess), via `interpretation:0003-t018-subphenotype-sex-reproductive-stage`.

- **M2 — Ascertainment and scoring inflation** *(empirical_regularity)*. Cross-study heterogeneity in PAIS
  prevalence/effect estimates is **substantially explained by ascertainment choices** — case definition,
  referral/selection enrichment, and endpoint/scoring breadth — rather than by biology. The decisive
  instance is `interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`: an apparent 0%→91%
  skin-biopsy SFN prevalence range across four studies decomposes into modality breadth, trigger, and
  referral enrichment, with within-trigger referral cohorts in fact concordant. The case-definition
  variants of this claim are `question:0014` and `question:0015`.

- **M3 — Endpoint/construct instability** *(structural_claim)*. A single named PAIS phenotype's objective
  correlate is **endpoint- and trigger-specific**, so the *choice* of objective endpoint can itself
  manufacture or hide a "shared mechanism." Instance: `proposition:0011` (the ME/CFS whole-body two-day
  CPET PEM decrement does not transfer to long COVID at that endpoint, even where a long-COVID muscle
  OXPHOS lesion exists), via `interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation`.

### Supporting Or Auxiliary Propositions

- **B — Bounded-exception clause** *(structural_claim; the falsifiability anchor)*. The bias is directional
  and predictable but **not total**: real objective, trigger-matched PAIS group differences exist and
  survive ascertainment control. Current admitted exceptions (the audited set, n=3 as of
  `interpretation:0015`): `proposition:0013` (a testosterone-conditioned objective female-biased
  immune-activation signal), `proposition:0012` (the male vascular hard-endpoint reversal is itself a
  robust objective signal, not an artifact), and `proposition:0025` (long-COVID persistent inflammatory
  activation — IL-6/JAK-STAT/type-II-IFN + CD8 exhaustion, two cohorts, >180d, no circulating virus — a
  robust objective case-vs-control difference). This clause is **load-bearing**: it both keeps the
  hypothesis falsifiable and defines the rate at which accumulating objective signals would weaken it. The
  `task:t055` audit (`interpretation:0015`) enlarged this set from 2→3, the first reading of the
  falsification meter: still bounded, not proliferating.

## Current Uncertainty

The hypothesis was assembled from instances discovered **piecemeal** across four other hypotheses
(h0001 PEM, h0005 sex, h0006 PEM-muscle, h0007 SFN). The `task:t055` audit
(`interpretation:0015`) has now tested it **as a regularity** for the first time: across 11 corpus
group-difference claims (9 determinate), 6/9 are artifact-consistent and the directional sub-structure is
8/8 (every self-report-channel difference attenuates; every objective-origin difference survives). So the
regularity is now a **rate estimated, not only a pattern noticed** — but the audit is retrospective,
project-internal, small-n (11), and coded by the same agent that built the hypothesis, so its support
remains **anecdotal-aggregate** pending the prospective same-cohort test (criterion #2). Two further uncertainties: (1) the hypothesis is at risk of unfalsifiability if stated
without the bounding clause; (2) the **mechanism** of the channel bias is unspecified and may differ by
instance — interoception/illness-behavior (self-report inflation), referral funnels (selection
enrichment), or definitional drift (scoring) are distinct causes the current evidence cannot separate
(an open sub-question, see `topic:measurement-ascertainment-artifacts-in-pais`).

## Predictions

- **Strong / discriminating.** Take a PAIS group difference established in a self-report channel and
  measure the *same construct* objectively in a trigger-matched, ascertainment-controlled design → the
  effect **attenuates toward null or reverses** (predicted for the female cognitive excess and the
  dysautonomia sex-skew; already observed retrospectively for cognition, `proposition:0010`).
- **Prevalence harmonization.** Harmonizing case definition + scoring breadth + referral stream across
  studies of one phenotype **collapses apparent cross-study heterogeneity** (demonstrated for SFN in
  `interpretation:0014`; predicted to generalize to other PAIS prevalence scatters).
- **Reporting corollary (weak).** Studies that do not report measurement channel / ascertainment will show
  **larger and more heterogeneous** PAIS effects than studies that do.

## Falsifiability

The hypothesis is materially weakened or refuted if:

- A **systematic audit** of PAIS group-difference claims (≥~10, coded by channel and ascertainment control)
  finds that the **majority survive objective, trigger-matched re-measurement unchanged** — i.e., robust
  objective biological differences are the rule, not the bounded exception.
- A well-powered, trigger-matched, ascertainment-controlled study finds a PAIS group difference that is
  **equally strong or stronger objectively than by self-report** for the same construct, with no
  attenuation, in a domain currently assumed self-report-channeled.
- Admitted objective exceptions (`proposition:0013`, `proposition:0012`) **proliferate** to the point that
  "predictable bias" weakens to "sometimes-artifact" — a non-useful claim. The accumulation rate of robust
  objective signals is the running falsification meter.

## Promotion criteria

Promote `candidate → active` when:

1. **A systematic within-corpus audit** codes ≥~10 PAIS group-difference claims by (a) measurement channel
   (self-report vs objective), (b) ascertainment control (case definition, referral, scoring), and
   (c) whether the effect attenuates/reverses under objective trigger-matched measurement — and shows a
   **directional majority** consistent with M1–M3. This converts the anecdotal instance-collection into a
   quantified regularity with an estimated rate and an explicit exception set.
   **✓ MET** by `interpretation:0015` (`task:t055`): 11 claims coded, 6/9 determinate claims
   artifact-consistent, directional sub-structure 8/8 by channel, exception set enumerated and bounded at 3.
2. **At least one prospective or individual-patient-data test** re-measures a self-report-established PAIS
   difference objectively in the *same* trigger-matched cohort and observes the predicted attenuation —
   moving beyond the current retrospective, cross-study instances.

## Supporting Evidence

- **`proposition:0010`** (literature; `interpretation:0003-t018-subphenotype-sex-reproductive-stage`) —
  female cognitive excess is self-report-only, absent in objective neuropsychological testing. The
  cleanest M1 instance. Walitt2024 independently reports increased subjective cognitive complaints across
  five domains with **no** group difference on 15 objective neuropsychological tests.
- **`proposition:0009`** — the dysautonomia female skew tracks the baseline POTS sex ratio rather than a
  PAIS-specific amplification (baseline-carried, not PAIS-amplified): M1 via an ascertainment/baseline
  route.
- **`proposition:0011`** (`interpretation:0004-t025-...`) — PEM's objective correlate is trigger- and
  endpoint-specific: the M3 anchor.
- **`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`** — the M2 anchor: SFN biopsy
  prevalence 0→91% decomposes into modality/trigger/referral, not biology; within-trigger concordant.
- **`interpretation:0003-t018-subphenotype-sex-reproductive-stage`** — the measurement-channel axis as the
  organizing structure of the female PAIS excess; Shah2025's within-age-band menopause null is a further
  ascertainment-control instance.
- **`interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test`** — an ascertainment audit that
  reclassified the entire HRT→PAIS literature as ascertainment context (no admissible causal estimate),
  an M2-adjacent instance.

## Disputing Evidence

These are **bounding** evidence, not refutations — they instantiate clause B and define the falsification
meter:

- **`proposition:0013`** — a testosterone-conditioned, objective, female-biased immune-activation signal
  in within-sex case-control designs. A genuine objective group difference that does **not** dissolve: the
  project's clearest current counter-instance to a strong channel-bias reading.
- **`proposition:0012`** — the male vascular hard-endpoint reversal survives severity adjustment across
  ambulatory and hospitalized strata: a robust objective signal. (It supports M1's *direction-reversal*
  prediction, but as a real objective effect it simultaneously bounds the "objective channels show
  nothing" caricature.) Provisional: its infection-attributable fraction is unresolved (no uninfected
  comparator; `question:0021`).
- **`proposition:0025`** — long-COVID persistent inflammatory activation survives as a robust objective
  case-vs-control difference (two cohorts, >180 days, no circulating virus). Added to clause B by the
  `task:t055` audit (`interpretation:0015`): an objective-origin difference that does not attenuate, the
  third member of the bounded exception set.

## Evidence Needed To Shift Belief

- **Most efficient (uses existing corpus): the systematic audit** in promotion criterion #1 — it requires
  no new data, only disciplined coding of claims already in the graph, and would convert belief from
  "pattern noticed" to "rate estimated."
- **Most discriminating: a same-cohort objective re-measurement** of a self-report-established difference
  (promotion criterion #2) — the only design that controls trigger, cohort, and ascertainment
  simultaneously and so isolates channel from biology.
- A counting discipline on accumulating objective exceptions (clause B) is the cheapest continuous
  belief-update signal.

## Related Work

- `topic:measurement-ascertainment-artifacts-in-pais` (the standing methodological check this hypothesis
  promotes to falsifiable form) and `topic:pais-case-definition-heterogeneity`.
- The four hypotheses whose evidence bases this meta-constraint spans:
  `hypothesis:0001-shared-dysregulated-attractor` (PEM endpoint-specificity, shared-mechanism inference),
  `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` (the female-excess decomposition),
  `hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem` (PEM endpoint dissociation), and
  `hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` (SFN prevalence harmonization).
- Open questions it would discipline: `question:0014`, `question:0015` (case-definition coherence and PEM
  comparability), `question:0018` (objective-vs-subjective cognition dissociation).
- Methodological adjacency: this hypothesis is the project's internal analogue of the
  measurement-invariance / ascertainment-bias literature in psychometrics and epidemiology; a future
  specify-model pass should decide whether M1–M3 become first-class graph propositions or remain an
  organizing umbrella over the existing `proposition:0009`–`0013` set.
