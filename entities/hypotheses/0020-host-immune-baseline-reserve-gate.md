---
id: hypothesis:0020-host-immune-baseline-reserve-gate
kind: hypothesis
title: Pre-infection host immune-baseline reserve gates PAIS risk across host strata
status: draft
source_refs:
- cite:Vinson2024
- cite:Peluso2022a
- cite:Chavatza2025
origins:
- type: user
  date: '2026-07-10'
- type: assistant
related:
- question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts
- question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse
- question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
- question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a
- question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory
- hypothesis:0004-acute-severity-threshold
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
created: "2026-07-10"
updated: "2026-07-10"
added_by: user
---
# Hypothesis: Pre-infection host immune-baseline reserve gates PAIS risk across host strata

## Organizing Conjecture

A patient's **pre-infection immune homeostatic reserve** — not just the acute insult magnitude — sets the probability that recovery fails after infection. The conjecture is that several apparently unrelated host conditions (chronic immunosuppression, frailty / inflammaging, atopic / mast-cell hyperreactivity, pregnancy-phase immune remodelling, and ancestral / LMIC immune-architecture and exposure history) are **instances of one shared mechanism**: each perturbs the baseline immune set-point so that a smaller perturbation suffices to lock the system into the failed-recovery state. This reframes the project's scattered "host-modifier" questions as a single **vulnerability gate** that operates *upstream of and orthogonal to* the acute-severity threshold (`hypothesis:0004`) and specializes the reproductive-stage-margin idea (`hypothesis:0005`) into a general baseline-reserve claim. Its central testable payoff is a **rank-ordering prediction**: PAIS incidence and phenotype should track a measurable pre-infection reserve axis across host strata, in a direction the individual conditions share.

## Proposition Bundle

### Core Propositions

- **P1 (reserve gates risk).** Reduced pre-infection immune homeostatic reserve raises the probability of failed post-infectious recovery independent of acute-illness severity. (`causal_effect`.)
- **P2 (shared mechanism across strata).** Chronic immunosuppression, frailty/inflammaging, atopy/MCAS, pregnancy remodelling, and ancestral/LMIC immune context modify PAIS risk through the *same* lowered-threshold-for-lock-in mechanism rather than five unrelated pathways. (`structural_claim`.)
- **P3 (rank-ordering).** A measurable baseline-reserve axis rank-orders PAIS incidence/severity across these host strata in a consistent direction. (`empirical_regularity`.)

### Supporting Or Auxiliary Propositions

- **P4 (bidirectional coupling).** For frailty specifically, reserve and PAIS are bidirectionally coupled — low reserve raises PAIS risk and PAIS accelerates reserve loss (`question:0033`).
- **P5 (phenotype shift, not just incidence).** Some strata (atopy/MCAS, pregnancy) shift the PAIS *phenotype* (e.g., toward Th2/mast-cell-dependent presentations), not merely its incidence (`question:0034`, `question:0040`).
- **P6 (mechanistic distinctness of immunosuppression).** In chronically immunosuppressed hosts the antigen-clearance vs immune-activation balance is altered, so this stratum also probes `hypothesis:0002` and `hypothesis:0003` directly (`question:0031`).

## Current Uncertainty

The frame is a **synthesis conjecture with thin direct grounding**: only `question:0031` currently carries sourced evidence (Vinson2024, Peluso2022a, Chavatza2025 on immunosuppressed hosts), while the frailty, atopy/MCAS, pregnancy, and ancestry/LMIC strata are literature-motivated but not yet evidence-backed in the project. The unifying claim (P2) is the fragile core: it is entirely possible these strata modify PAIS through *distinct* mechanisms and share only the descriptive label "reduced reserve." No operational, pre-infection measurement of "immune homeostatic reserve" is agreed on, so P3's rank-ordering test is not yet specifiable without first defining the axis. Confounding by healthcare access, ascertainment, and baseline comorbidity burden is severe, especially for the LMIC/ancestry and frailty strata.

## Predictions

**Strong / discriminating:**
- Across host strata, PAIS incidence/severity rank-orders with a pre-infection reserve proxy (e.g., baseline inflammatory tone, thymic output / naïve-T fraction, vaccine-response competence) **after** adjusting for acute severity (P1, P3).
- The strata share directionality (all reduced-reserve conditions push the *same way*), rather than some raising and some lowering risk once severity and ascertainment are controlled (P2).

**Weaker / corollaries:**
- Frailty and PAIS show bidirectional longitudinal coupling (P4).
- Atopy/MCAS and pregnancy strata show a phenotype shift (Th2 / mast-cell features), not just an incidence change (P5).
- Immunosuppressed hosts dissociate antigen persistence from immune-activation readouts relative to immunocompetent PAIS (P6).

## Falsifiability

Confidence would be materially reduced if:
- Host-stratum effects on PAIS are fully explained by acute-severity differences, healthcare-access/ascertainment, or baseline comorbidity — with no residual reserve effect (against P1).
- The strata modify risk in *inconsistent directions* or via demonstrably distinct mechanisms, defeating the shared-gate claim (against P2).
- No pre-infection reserve proxy rank-orders PAIS risk across strata (against P3).

## Promotion criteria

Promote from `candidate` to `active` when: (1) at least one operational pre-infection reserve proxy is defined and shown to predict PAIS risk *independent of acute severity* in ≥1 stratum (P1); **and** (2) ≥2 of the five host strata show the same-direction effect under ascertainment/severity adjustment, giving initial support to the shared-mechanism claim (P2). Until then the frame stays a candidate that organizes the host-modifier questions (`question:0031`–`question:0034`, `question:0040`) and the `topic:population-boundary-conditions-and-effect-modifiers-in-pais` under one testable umbrella.

## Supporting Evidence

- **Vinson2024 / Peluso2022a / Chavatza2025 (literature, via `question:0031`):** evidence on PAIS incidence and mechanism in chronically immunosuppressed hosts — the one stratum with current grounding, supporting P1/P6 in that subgroup.
- **`hypothesis:0004` (project frame):** the acute-severity-threshold line already posits a homeostatic recovery threshold; this hypothesis supplies the *baseline-reserve* term that moves the threshold, a compatible extension.
- **`hypothesis:0005` (project frame):** the reproductive-stage-margin work is a worked example of a reserve-modifying host state, generalized here.

## Disputing Evidence

- Most strata (frailty, atopy/MCAS, pregnancy, LMIC/ancestry) currently lack project-level evidence, so the shared-mechanism claim is asserted more than demonstrated.
- Ascertainment and healthcare-access confounding plausibly generate stratum differences with no reserve mechanism at all — the leading deflationary account, adjacent to `hypothesis:0008`.

## Evidence Needed To Shift Belief

- **Most efficient upward:** a cohort with a pre-infection reserve proxy and post-infection PAIS outcomes across ≥2 host strata, showing same-direction, severity-adjusted effects (P1–P3).
- **Most efficient downward:** stratum effects vanish under severity + ascertainment adjustment, or resolve into distinct mechanisms.
- **Most discriminating next test:** define and validate one operational pre-infection reserve axis, then test rank-ordering of PAIS incidence across immunosuppressed, frail, atopic, and pregnant strata within a single harmonized framework.

## Related Work

- `question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts`, `question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse`, `question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with`, `question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a`, `question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory` — the five host-modifier questions this hypothesis homes.
- `hypothesis:0004-acute-severity-threshold` — the acute-insult term; this hypothesis adds the orthogonal baseline-reserve term. `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` — a worked instance generalized here.
- `hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent` — the deflationary rival: stratum effects as ascertainment artifacts.
- `topic:population-boundary-conditions-and-effect-modifiers-in-pais` — the organizing topic for this cluster.
