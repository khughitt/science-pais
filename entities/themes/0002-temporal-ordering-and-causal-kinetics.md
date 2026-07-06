---
id: theme:0002-temporal-ordering-and-causal-kinetics
kind: theme
title: Temporal ordering and causal kinetics of PAIS onset and resolution
status: active
theme_kind: methodological
theme_scope: project
related:
- question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute
- question:0052-acute-clearance-rate-as-cross-pathogen-pais-trajectory-predictor
- question:0053-gut-microbiome-normalization-kinetics-leading-vs-lagging
- question:0054-ebv-reactivation-autoantibody-emergence-temporal-ordering
- question:0036-critical-slowing-down-fingerprints-as-pre-chronification-early-warning
- question:0037-latent-homeostatic-fragility-after-pais-recovery-lower-re-entry
- question:0046-mechanistic-basis-of-the-time-limited-acute-phase-intervention-window
- hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a
source_refs: []
origins: []
evidence_refs: []
created: '2026-07-06'
updated: '2026-07-06'
---
# Theme: Temporal ordering and causal kinetics of PAIS onset and resolution

## Definition

The **temporal-ordering / causal-kinetics** frame organizes the project's use of *time structure* — the
rate, sequence, and lead/lag of events across the acute-to-chronic transition — as a lever for causal
inference. Many PAIS mechanisms are indistinguishable at a cross-sectional snapshot (a marker that
*drives* the illness and one that is a *consequence* look identical in a single blood draw); their
temporal signatures are not. This theme collects the questions and hypotheses whose discriminating power
comes from *when* things happen — acute clearance kinetics, normalization trajectories, event ordering,
and the dynamical-systems fingerprints (critical slowing, hysteresis, re-entry thresholds) of attractor
entry and exit.

## Why It Matters

- **Timing is often the only handle on driver-vs-consequence.** The same driver-vs-marker calls that the
  deflationary theme frames epistemically are frequently *decided* by ordering evidence: whether gut
  microbiome recovery leads or lags symptom resolution (`question:0053`), whether EBV reactivation
  precedes or parallels autoantibody emergence (`question:0054`), whether acute clearance rate predicts
  trajectory (`question:0052`).
- **It defines intervention windows.** If chronification is an attractor entry, the acute phase is a
  time-limited window where a small push changes the outcome (`question:0046`), and pre-chronification
  early-warning signals (`question:0036`) become actionable — a fundamentally different therapeutic
  posture from treating established chronic illness.
- **It disciplines the attractor claim.** The dynamical hallmarks of `hypothesis:0001` (bistability,
  hysteresis, critical slowing) are *temporal* predictions; without longitudinal data they stay
  qualitative. This theme is where those predictions get operationalized (and where the slow-gradient
  rival, `hypothesis:0010`, is tested against them).

## Boundaries

- **In-scope:** questions/hypotheses whose evidentiary value is temporal — clearance/normalization
  kinetics, event ordering, lead/lag, critical-transition fingerprints, re-entry thresholds, and
  intervention-window timing.
- **Out-of-scope (stays where it lives):** the biological *content* of each mechanism (its own
  hypothesis); the static formalization of the attractor model
  (`question:0008-formalize-vicious-cycle-attractor-model`) except where it makes a *temporal*
  prediction; and generic longitudinal-cohort cataloguing (a design/dataset concern, not this frame).

## Current Project Links

- **Ordering hub:** `question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute`.
- **Kinetics / lead-lag (2026-07-06 pass):**
  `question:0052-acute-clearance-rate-as-cross-pathogen-pais-trajectory-predictor`,
  `question:0053-gut-microbiome-normalization-kinetics-leading-vs-lagging`,
  `question:0054-ebv-reactivation-autoantibody-emergence-temporal-ordering`.
- **Dynamical-systems fingerprints & windows:**
  `question:0036-critical-slowing-down-fingerprints-as-pre-chronification-early-warning`,
  `question:0037-latent-homeostatic-fragility-after-pais-recovery-lower-re-entry`,
  `question:0046-mechanistic-basis-of-the-time-limited-acute-phase-intervention-window`.
- **Trajectory hypothesis under test:**
  `hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a` (monotonic
  gradient vs. bistable attractor is a *temporal* discriminator against `hypothesis:0001`).

## Guardrails

- **Association timing ≠ causation.** A marker preceding an outcome is necessary but not sufficient for
  causality (a common upstream cause can produce both with a lag); ordering evidence must still be read
  against confounding (e.g. acute severity co-varying with clearance rate in `question:0052`).
- **Snapshot studies cannot answer ordering questions.** Flag cross-sectional designs used to infer
  lead/lag; the discriminating designs here require dense, jointly-sampled longitudinal data from the
  acute phase onward, which the project largely does not yet hold.
- **Do not over-read dynamical fingerprints.** Critical-slowing / hysteresis signatures are suggestive of
  bistability but have alternative explanations; treat them as consistent-with, not proof-of, an attractor.

## Downstream Work

- Longitudinal / dense-sampling cohort designs that jointly measure the candidate ordered variables
  (microbiome + symptoms; EBV + autoantibodies; clearance rate + trajectory).
- Cross-lagged / mediation and critical-transition analyses on any available longitudinal PAIS data.
- See the `explore-followups` task group (temporal-dynamics batch) for enumerated follow-ups.

## Open Questions

- Which single design most efficiently yields ordering evidence across several mechanisms at once (a
  shared dense-sampled acute-to-chronic cohort) versus bespoke per-mechanism studies?
- Do the dynamical-systems fingerprints (critical slowing, hysteresis) actually appear in real PAIS
  trajectories, or is the transition better described as a slow heterogeneous gradient
  (`hypothesis:0010`)?

## Update Triggers

- Acquisition or identification of a dense longitudinal PAIS cohort spanning the acute phase.
- Any ordering result that resolves a lead/lag call (microbiome, EBV/autoantibody, clearance).
- A formalization advance in `question:0008` that makes new temporal predictions to test here.
