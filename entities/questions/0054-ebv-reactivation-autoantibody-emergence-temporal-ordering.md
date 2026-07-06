---
id: question:0054-ebv-reactivation-autoantibody-emergence-temporal-ordering
kind: question
title: Causal temporal ordering of EBV reactivation and autoantibody emergence in
  PAIS
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Peluso2022
- cite:Jernbom2024
origins:
- type: assistant
  ref: explore-ideas-temporal
related:
- question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute
- hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais
- question:0009-functional-autoantibodies-drive-dysautonomia
- question:0051-prior-symptomatic-ebv-mononucleosis-as-pais-risk-amplifier
created: '2026-07-06'
updated: '2026-07-06'
added_by: explore-ideas:claude-opus-4-8:cand-temporal-ebv-reactivation-autoantibody-sequence
lens_views:
- lens: temporal
  rationale: EBV reactivation and de novo autoantibodies are each independently associated
    with PAIS severity, but the causal order between them is unknown because most
    studies measure each at a single post-acute time point. If EBV reactivation (EA-D
    IgG within weeks) consistently precedes and predicts autoantibody emergence (3-6
    months), this implies a cascade (immune suppression -> EBV reactivation -> molecular
    mimicry/bystander activation -> autoantibodies) with distinct therapeutic implications
    from a parallel-drivers model. This sharpens the project's general question:0045
    (temporal ordering of homeostatic domain failure) into a specific EBV->autoantibody
    sequencing test requiring dense serial serology.
  origin_ref: explore-ideas-temporal
---
# Causal temporal ordering of EBV reactivation and autoantibody emergence in PAIS

## Summary

In individuals who develop PAIS, does serological EBV reactivation during or immediately after the acute
infection phase **temporally precede and causally enable** new-onset autoantibody production — or do the
two occur as **independent parallel consequences** of initial immune dysregulation? This sharpens the
project's EBV and autoimmunity threads into a single ordering test: serial (EBV → autoimmunity, e.g. via
molecular mimicry) versus parallel (both downstream of the same immune disruption).

## Why It Matters

- **Decision it affects:** the causal architecture linking two candidate PAIS mechanisms, and therefore
  therapeutic sequencing — a serial EBV→autoimmunity chain argues for antiviral-first strategies, whereas
  parallel-consequence architecture argues for immunomodulation regardless of EBV.
- **Risk if unanswered:** EBV-reactivation and autoantibody findings keep being reported in isolation, so
  the field cannot tell whether targeting EBV would prevent autoimmunity or merely treat a co-traveler
  (directly relevant to `hypothesis:0015`, EBV-as-consequence).

## Current Evidence

- **Supporting:** Peluso2022 shows EBV EA-D IgG seropositivity at ~4 months associates with long-COVID
  fatigue — establishing an EBV signal in the right time window. Jernbom2024 (longitudinal proteome-wide
  autoantibody profiling over 16 months) shows new-onset autoantibodies emerge and persist after
  COVID-19 — establishing the autoantibody signal. The EBV→autoimmunity precedent from multiple
  sclerosis (EBNA1 mimicry) makes a serial ordering mechanistically plausible.
- **Conflicting / limiting:** neither study cross-references the *other's* timing — Peluso2022 is a
  snapshot at ~4 months and Jernbom2024 tracks autoantibodies without concurrent EBV-reactivation
  timing — so the ordering is entirely unresolved. Both signals could be parallel readouts of acute
  immune disruption.

## Thoughts

- **Best current interpretation:** ordering is genuinely open; molecular mimicry makes a serial chain
  plausible but it has not been tested in PAIS, and parallel-consequence remains equally consistent with
  present data.
- **Major uncertainty:** requires *joint* longitudinal sampling of EBV-reactivation markers and
  autoantibody repertoires in the same individuals from the acute phase onward — a design that does not
  yet exist for PAIS.

## Connections to Project

- Related hypotheses: `question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute`
  (the general ordering frame); `hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais` (the
  ordering test bears directly on whether EBV is causal); autoimmunity/functional-autoantibody threads
  (`question:0009`).
- Required datasets: joint longitudinal EBV-serology + proteome-wide autoantibody cohort sampled from the
  acute phase.
- Required analyses: cross-lagged temporal-ordering / mediation analysis of EBV reactivation vs.
  autoantibody emergence.
- Priority level: P3 — mechanistically decisive but needs a bespoke joint-sampling cohort.

## Related

- Topic notes: `topic:post-infectious-dysautonomia-and-autoimmunity`, `topic:antigen-pathogen-persistence`.
- Article notes: Peluso2022 (EBV EA-D IgG ↔ long-COVID fatigue), Jernbom2024 (persistent new-onset
  autoantibodies post-COVID).
- Methods/Datasets: none yet — requires joint EBV + autoantibody longitudinal cohort.
