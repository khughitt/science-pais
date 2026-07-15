---
id: hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
kind: hypothesis
title: Post-infectious immune-set-point shift drives long-term autoimmune conversion
status: draft
source_refs:
- cite:Rojas2022
- cite:Sharma2023
- cite:Ciaffi2023
related:
- question:0005-latent-to-overt-autoimmunity-conversion
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- question:0044-chronic-gvhd-as-analogy-for-post-viral-tolerance-infrastructure-collapse
required_capabilities:
- analysis_role: mr_exposure
  trait: autoimmune-disease
created: "2026-07-01"
updated: "2026-07-10"
datasets:
- dataset:bentham-2015-sle-gwas
- dataset:covid19-hgi-longcovid-gwas
---
# Hypothesis: Post-infectious immune-set-point shift drives long-term autoimmune conversion

## Organizing Conjecture

In a **minority** post-infectious subset, the near-universal *latent* autoimmunity seen after
acute infection is not a transient molecular-mimicry response that resolves with convalescence,
but the visible marker of a **durable immune-set-point shift** — the same persistent
post-infectious immune-state displacement reframed in `hypothesis:0001`, viewed on a
**multi-year prognostic timescale** rather than a mechanistic one. The conjecture is that this
displaced state, in susceptible hosts, **progresses to clinically overt autoimmune disease over a
5–10-year horizon**, and that the **breadth of anti-cytokine / anti-IFN (and functional-GPCR)
autoantibody repertoire** measured early stratifies who converts.

This is deliberately the **forward arrow — PAIS → later overt autoimmunity** — and is *distinct
from* the reverse-arrow work in `plan:0005` / `task:t079` (pre-existing autoimmune **diathesis →
PAIS risk**, autoimmunity as an upstream effect-modifier). The two are complementary halves of the
same autoimmunity↔PAIS relationship and share the same sex-confounding trap; neither entails the
other. This hypothesis houses the previously orphaned `question:0005-latent-to-overt-autoimmunity-
conversion`.

## Proposition Bundle

### Core Propositions

- **[causal_effect]** In a minority subset, post-infectious latent autoimmunity **converts** to
  clinically overt autoimmune disease at a rate **above the age/sex-matched uninfected baseline**,
  over a 5–10-year horizon (subject: post-infectious latent autoimmunity; predicate: raises hazard
  of; object: incident overt autoimmune disease).
- **[causal_effect / predictive]** Early **anti-cytokine / anti-IFN autoantibody breadth** (and/or
  functional-GPCR autoantibody load) **predicts** which latent-autoimmune patients convert —
  i.e. conversion is stratifiable, not uniform.
- **[structural_claim]** Conversion reflects a **durable immune reprogramming** (a persisting
  set-point shift, continuous with `hypothesis:0001`'s displacement), **not** a transient
  post-infectious mimicry response that would resolve on its own.

### Supporting Or Auxiliary Propositions

- The 83%-latent / ~3%-overt gap at 7 months (Rojas2022) is a **staging snapshot of an unfinished
  trajectory**, not a stable endpoint — the overt fraction should rise with follow-up time.
- Converters concentrate among hosts with deeper basin / higher susceptibility (overlap with the
  `hypothesis:0001` predisposition axis and the `hypothesis:0005` homeostatic-margin axis).

## Current Uncertainty

- **Purely prognostic, longitudinal, and essentially untested at the conversion step.** The
  phenomenon (near-universal latent autoimmunity; elevated new-onset autoimmune-disease hazards) is
  established, but the **conversion trajectory itself** — what fraction of latent converts, over
  what horizon, and which autoantibodies mark the high-risk subset — is not demonstrated. Rojas2022
  is a single-cohort 7-month cross-section; Sharma2023 is retrospective EHR hazard estimation
  without the latent-autoantibody link.
- **Sex-confounding trap (load-bearing).** Both autoimmunity and long COVID are female-predominant,
  so any naive latent→overt or infection→autoimmunity association is sex-confounded — the project's
  standing measurement-channel / ascertainment meta-constraint (`hypothesis:0008`) applies directly.
  Ascertainment (autoimmune patients are seen more, tested more) can manufacture apparent conversion.
- **Mimicry-vs-durable-reprogramming is unresolved:** a transient-mimicry rival predicts most latent
  autoantibodies decay without conversion.

## Predictions

**Strong / discriminating:**

- In a prospective post-infectious cohort with baseline autoantibody profiling, **overt autoimmune-
  disease incidence exceeds an age/sex/ascertainment-matched uninfected comparator** over 5–10 years,
  and the excess **concentrates in the early-broad-autoantibody stratum** (dose-response on breadth).
- Latent autoantibody breadth measured early is **retained/consolidated** (not decayed) in converters
  and **decays** in non-converters — separating durable reprogramming from transient mimicry.

**Weaker / corollaries:**

- The overt fraction **rises monotonically with follow-up duration** beyond the Rojas2022 7-month
  ~3%.
- Converters over-represent the shared PAIS predisposition/comorbidity cluster and higher acute
  severity.

## Falsifiability

Confidence would be materially reduced if:

- A sex- and ascertainment-matched prospective cohort shows **no excess overt-autoimmune conversion**
  over the uninfected baseline once these confounders are controlled (the apparent signal was
  channelled through sex/ascertainment — a `hypothesis:0008` outcome).
- Early autoantibody breadth **does not stratify** conversion (conversion is uniform or driven by
  unrelated factors), refuting the prognostic-marker core.
- Latent autoantibodies **decay without conversion** in the great majority, supporting the transient-
  mimicry rival over durable reprogramming.

## Promotion criteria

Promote from `candidate` to `active` when **either**: (1) a longitudinal post-infectious cohort with
early autoantibody profiling and ≥3–5-year follow-up becomes identifiable/accessible as an
admissible vehicle for the conversion-rate + breadth-stratification test (analogous to the
vehicle-admissibility gates on `task:t028` / `task:t050`); **or** (2) a formalized decomposition
shows the elevated new-onset-autoimmune hazard (Sharma2023-type) survives sex- and
ascertainment-adjustment and links to a latent-autoantibody marker — i.e. the phenomenon clears the
`hypothesis:0008` confound bar. Until then it remains a candidate framing whose job is to give
`question:0005` a home and keep the forward-arrow prognostic claim distinct from the t079
reverse-arrow work.

## Supporting Evidence

- **Rojas2022 (literature):** ~83% of post-COVID patients carry latent autoantibodies at 7 months
  while only ~3% have overt autoimmune disease — establishes the latent reservoir and the
  latent↔overt gap this hypothesis interprets as an unfinished trajectory.
- **Sharma2023 (literature):** large retrospective cohorts show elevated new-onset autoimmune-disease
  hazards after COVID-19 — consistent with (but not proof of) an above-baseline conversion rate; does
  not yet carry the early-autoantibody stratifier or full sex/ascertainment adjustment.
- **Ciaffi2023 (literature):** post-COVID new-onset autoimmune/inflammatory rheumatic disease
  reports — corroborating incident-autoimmunity signal at the phenotype level.

## Disputing Evidence

- **Transient-mimicry reading (general immunology prior):** many post-infectious autoantibodies are
  short-lived and non-pathogenic; without demonstrated persistence + conversion, the latent reservoir
  may largely resolve — a live rival to durable reprogramming.
- **`hypothesis:0008` (measurement-channel/ascertainment):** the female predominance shared by
  autoimmunity and PAIS, plus differential testing/follow-up of autoimmune-prone patients, can
  generate an apparent conversion excess that is really an ascertainment artifact.

## Evidence Needed To Shift Belief

- **Most efficient upward:** a prospective post-infectious cohort with **baseline autoantibody
  breadth** and **≥3–5-year** overt-autoimmune outcomes, against a sex/ascertainment-matched
  uninfected comparator, showing above-baseline conversion concentrated in the broad-autoantibody
  stratum.
- **Most efficient downward:** the same design finding no adjusted excess, or no stratification by
  autoantibody breadth.
- **Also useful:** a sex- and ascertainment-adjusted re-analysis of existing large-cohort new-onset-
  autoimmune hazards (Sharma2023-type) with an autoantibody linkage.

## Related Work

- `question:0005-latent-to-overt-autoimmunity-conversion` — the open question this hypothesis houses.
- `hypothesis:0001-shared-dysregulated-attractor` — the immune-state-displacement frame this extends
  onto a longitudinal-prognostic timescale (via `patch-definition:immune-state-shift-causal-landscape`).
- `hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent` — the
  sex/ascertainment confound bar any conversion claim must clear.
- `plan:0005` / `task:t079` — the **reverse-arrow** counterpart (pre-existing autoimmune diathesis as
  a sex-conditioned effect-modifier of PAIS risk); complementary, not overlapping.
- `topic:post-infectious-dysautonomia-and-autoimmunity` — home topic (Rojas2022, Sharma2023,
  Ciaffi2023).
- `question:0009-functional-autoantibodies-drive-dysautonomia` — the functional-autoantibody
  mechanism that may supply the stratifying repertoire.

## Notes

- 2026-07-01: Created as `phase: candidate` to house the orphan `question:0005` (flagged in
  `synthesis:9000-emergent-threads` as the sole orphan question with a drafted-but-uncreated candidate
  hypothesis). Promotion of this candidate was ratified in the 2026-07-01 next-steps review
  (`meta:0001-next-steps-2026-07-01`). Kept explicitly distinct from the t079 reverse-arrow diathesis
  work.
