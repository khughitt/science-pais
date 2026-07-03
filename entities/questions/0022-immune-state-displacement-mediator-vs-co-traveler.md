---
id: question:0022-immune-state-displacement-mediator-vs-co-traveler
type: question
title: Does persistent immune-state displacement mediate PAIS symptoms, or is it mainly
  a marker / co-traveler of another failed-recovery process?
status: active
ontology_terms:
- mediation
- immune dysregulation
- causal model
- biomarker vs driver
datasets:
- dataset:covid19-hgi-longcovid-gwas
source_refs: []
related:
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
- question:0006-jak-stat-il6-driver-vs-marker
- question:0008-formalize-vicious-cycle-attractor-model
- patch-definition:immune-state-shift-causal-landscape
- pre-registration:0004-jak1-inhibitor-driver-vs-marker
required_capabilities:
- analysis_role: mr_outcome
  trait: long-covid
created: '2026-06-30'
updated: '2026-07-03'
---

# Does persistent immune-state displacement mediate PAIS symptoms, or is it mainly a marker / co-traveler of another failed-recovery process?

## Summary

The reframed `hypothesis:0001` holds that PAIS share a **persistent post-infectious
immune-state displacement**. That reframe deliberately splits two claims: a
*descriptive* claim (immune state is persistently shifted — relatively well-supported)
and a *causal-hub* claim (immune state is the central **mediator** through which most
symptoms arise — much less settled). This question isolates the second. Is the displaced
immune state a **driver** of the symptom burden, or largely a **co-traveler / marker**
of some other failed-recovery process (e.g. an autonomic, vascular, metabolic, or
neural primary lesion) that the immune state merely indexes?

## Why It Matters

- It is the load-bearing assumption behind treating immune state as the *hub* node in
  `patch-definition:immune-state-shift-causal-landscape`; if immune state is a marker,
  the landscape's topology (and the case for immunomodulation) is wrong.
- It cleanly separates "immune signal correlates with PAIS" (abundant, cheap) from
  "moving immune state moves symptoms" (rare, decisive), and so guides whether
  immunomodulatory trials are mechanism tests or symptomatic shots in the dark.
- It guards against the project's recurring failure mode — reading a descriptive
  state-shift as a causal driver without an intervention or mediation design.

## Current Evidence

- **Live causal test:** the abrocitinib JAK1 trial (`hypothesis:0003`,
  `pre-registration:0004`, NCT06597396). The discriminating contrast is **symptom +
  pathway co-suppression** (immune state is a driver) vs **pathway suppression without
  symptom change** (immune state is a marker/co-traveler).
- **Adjacent question:** `question:0006` (JAK-STAT/IL-6 driver-vs-marker) already frames
  the driver/marker distinction for a specific pathway; this question generalizes it to
  immune *state* as a whole.
- **Caution:** most existing support for the descriptive claim is observational and
  cross-sectional; correlation of an immune signature with PAIS does not establish
  mediation. A formal mediation design needs the immune state measured *and*
  manipulated, with the downstream symptom and the candidate parallel lesions measured.

## Thoughts

- Best current interpretation: the descriptive displacement is plausible; the mediation
  claim is open and should not inherit the descriptive claim's support.
- Cleanest designs: (1) intervention — does immunomodulation that demonstrably moves
  immune state also move symptoms (target engagement required, per the h0002/h0003
  admissibility lessons)? (2) longitudinal mediation — does change in immune state
  *precede* and statistically mediate change in symptoms, vs. moving in parallel?
- Major uncertainty: immune ⇄ autonomic and immune ⇄ metabolic feedback means
  "mediator vs marker" may be ill-posed at a single timescale — a node can be both,
  depending on phase. This ties the question to the dynamical treatment in
  `question:0008`.

## Connections to Project

- Related hypotheses: `hypothesis:0001` (this question tests its causal-hub leg),
  `hypothesis:0003` (supplies the live intervention test).
- Required data or analyses: an immunomodulation trial with demonstrated target
  engagement and symptom + pathway co-readout; or a longitudinal multi-axis cohort
  permitting formal mediation with the parallel (vascular/metabolic/neural) lesions
  measured.
- Priority level: P2 — the decisive disambiguation of the reframe's strong leg, but
  data-gated on an admissible interventional or longitudinal design.

## Related

- Inquiry: `patch-definition:immune-state-shift-causal-landscape`.
- Sibling questions: `question:0006`, `question:0008`, `question:0009`.
