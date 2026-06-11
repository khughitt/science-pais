---
id: hypothesis:0004-acute-severity-threshold
type: hypothesis
title: Acute-illness severity sets a homeostatic recovery threshold above which the
  post-infectious state becomes self-sustaining rather than self-resolving
status: proposed
phase: active
source_refs:
- cite:Rahmati2025
- cite:Cai2024
- cite:Morroy2016
- cite:Xie2024
related:
- topic:shared-failure-mode-across-pais
- question:0003-acute-severity-threshold-for-self-sustaining-pais
- hypothesis:0001-shared-dysregulated-attractor
- immunity:research-question:immune-homeostasis-and-dysregulation
created: '2026-06-11'
updated: '2026-06-11'
---
# Hypothesis: Acute-illness severity sets a homeostatic recovery threshold above which the post-infectious state becomes self-sustaining rather than self-resolving

## Organizing Conjecture

The magnitude of the acute-phase insult sets a *threshold* in the host's recovery dynamics: below it, the system relaxes back to baseline (self-resolving); above it, recovery mechanisms are overwhelmed and the system settles into a durable dysregulated state (self-sustaining). The threshold is not pathogen-specific — it reflects how far the immune/physiological system is pushed relative to its host-determined reserve — which is why hospitalization-level acute illness predicts durable multi-organ sequelae after both SARS-CoV-2 and influenza, and why severe dengue (DHF) selectively predicts post-dengue fatigue. The threshold position is modulated by host reserve (sex, age, comorbidity, prior immunity), so the same insult crosses it for some hosts and not others. This is the *gating* mechanism for entry into the shared attractor of hypothesis 0001.

## Proposition Bundle

### Core Propositions

- Acute-illness severity predicts post-acute burden across pathogens (SARS-CoV-2 and influenza: Xie2024, Gandhi2023; dengue DHF: Hertanti2025, Conde2026; COVID-19 hospitalization: Rahmati2025, Cai2024).
- The hospitalized vs non-hospitalized split produces *qualitatively* different multi-year trajectories — hospitalized PASC stays elevated through year 3 while non-hospitalized approaches baseline (Cai2024) — consistent with crossing vs not crossing a threshold rather than a pure linear gradient.
- A consistent chronic fraction (~10-20%) recurs across triggers (Morroy2016, Kalimuddin2022, Bai2023), consistent with a host-reserve threshold interacting with insult magnitude.

### Supporting Or Auxiliary Propositions

- Host reserve modulates the threshold: female sex, age, and comorbidity shift recovery (Gusinow2026's ~4x recovery-time difference; cardiometabolic multimorbidity in Zheng2026).
- The intervention-window evidence (acute-phase metformin/antivirals work, established-disease agents mostly fail; Seo2025) is consistent with a phase transition that, once crossed, is hard to reverse.

## Current Uncertainty

- Severity-outcome associations come largely from administrative/observational cohorts subject to "for vs with" ascertainment bias (Gandhi2023), which can inflate apparent severity effects.
- A large share of ME/CFS and long COVID follows *mild* acute infection (Oronsky2021), which a naive severity-threshold model does not explain — implying severity is one axis among several, not the sole gate.
- "Threshold/phase transition" vs "continuous dose-response" has not been formally tested with change-point or bistability statistics (see `question:0003`).

## Predictions

**Strong / discriminating:**

- Longitudinal trajectory modeling will show a *discontinuity/change-point* in chronicity probability as a function of acute severity (a threshold), not a smooth monotonic gradient, and the discontinuity will recur across pathogens (COVID-19, influenza, dengue, Q-fever).
- After adjusting for host reserve (sex, age, comorbidity), the severity threshold position will shift predictably — lower reserve → lower severity needed to cross.
- Mild-acute-infection PAIS cases will be enriched for low-reserve hosts (so the *effective* insult relative to reserve still exceeds threshold), reconciling the mild-infection counterexample.

**Weaker / corollaries:**

- The severity-stratified DALY/IRR gradient seen in COVID-19 (Cai2024) will be mirrored in other PAIS-defining infections.

## Falsifiability

Confidence would be materially reduced if:

- Trajectory modeling shows a smooth continuous dose-response with no detectable change-point/bistability across cohorts and pathogens.
- A large, ascertainment-corrected analysis finds severity does not predict chronicity once host reserve is controlled.
- Mild-infection PAIS cases are *not* enriched for low host reserve, leaving the threshold model unable to explain the most common clinical scenario.

## Supporting Evidence

- **Cai2024 (empirical-data):** 3-year VA cohort — qualitatively divergent hospitalized vs non-hospitalized trajectories; severity as dominant predictor of multi-year recovery failure.
- **Rahmati2025 (literature/meta-analysis):** ICU/ventilation/severity predict 3-year PASC persistence.
- **Xie2024 / Gandhi2023 (empirical-data/commentary):** hospitalization-level COVID-19 and influenza both produce large post-acute multi-organ burden; post-acute phase dominates.
- **Morroy2016 (literature):** ~20% chronic fraction after Q-fever; severity-threshold framing across cohorts.
- Hertanti2025, Conde2026: DHF (severe dengue) selectively predicts post-dengue fatigue.

## Disputing Evidence

- **Oronsky2021:** the SIRS→CARS→PICS severe-illness arc may not apply to mild-acute-infection PAIS, the predominant ME/CFS/long-COVID phenotype — a direct challenge to a severity-only gate.
- **Gandhi2023:** "for vs with" ascertainment bias inflates severity-outcome associations in administrative data.
- Mild-infection-onset ME/CFS and long COVID are common, arguing host factors can dominate over insult magnitude.

## Evidence Needed To Shift Belief

- **Most efficient upward:** change-point/bistability modeling across multiple pathogen cohorts showing a recurrent threshold, with host-reserve-adjusted threshold shifts (answers `question:0003`).
- **Most efficient downward:** ascertainment-corrected analysis showing continuous dose-response or no severity effect after reserve adjustment.
- **Also useful:** demonstration that mild-onset cases are low-reserve hosts (reconciling the counterexample) vs not (refuting the model).

## Related Work

- `topic:shared-failure-mode-across-pais` — the cross-pathogen severity/threshold synthesis.
- `question:0003-acute-severity-threshold-for-self-sustaining-pais` — the formal test.
- `hypothesis:0001-shared-dysregulated-attractor` — this threshold is the proposed *gate* for attractor entry.
- `immunity:research-question:immune-homeostasis-and-dysregulation` — host-reserve/homeostatic-margin biology.
