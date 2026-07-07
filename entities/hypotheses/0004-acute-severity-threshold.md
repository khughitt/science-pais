---
id: hypothesis:0004-acute-severity-threshold
kind: hypothesis
title: Acute-illness severity sets a homeostatic recovery threshold above which the
  post-infectious state becomes self-sustaining rather than self-resolving
status: proposed
phase: active
source_refs:
- cite:Rahmati2025
- cite:Cai2024
- cite:Morroy2016
- cite:Xie2024
- cite:Ambrosino2021
- cite:Xie2022
- paper:Spetz2025
- paper:Green2025
- paper:Carazo2025
- paper:ZhangRECOVEREHR2026
- paper:Truong2025
related:
- topic:shared-failure-mode-across-pais
- topic:innate-immune-memory-trained-immunity-in-pais
- question:0003-acute-severity-threshold-for-self-sustaining-pais
- question:0012-prevention-vaccination-antiviral-reduces-pais
- hypothesis:0001-shared-dysregulated-attractor
- immunity:research-question:immune-homeostasis-and-dysregulation
- proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
- proposition:0021-acute-antigen-burden-determines-pais-incidence
- interpretation:0018-t048-vascular-sex-baseline-carryover-audit
- interpretation:0022-t010-reinfection-vaccination-risk-recovery
- interpretation:0025-t009-pediatric-long-covid-and-misc
- topic:pediatric-long-covid-and-misc
- task:t048
- task:t010
created: '2026-06-11'
updated: '2026-07-07'
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
- The prevention/modification evidence (pre-infection vaccination/prior immunity lowers long-COVID risk; acute-phase metformin lowers clinician/provider-diagnosed long-COVID incidence; established-disease agents mostly fail) is consistent with a phase transition that, once crossed, is hard to reverse. This remains mechanism-mixed rather than a direct threshold test.

## Current Uncertainty

- Severity-outcome associations come largely from administrative/observational cohorts subject to "for vs with" ascertainment bias (Gandhi2023), which can inflate apparent severity effects.
- A large share of ME/CFS and long COVID follows *mild* acute infection (Oronsky2021), which a naive severity-threshold model does not explain — implying severity is one axis among several, not the sole gate.
- "Threshold/phase transition" vs "continuous dose-response" has not been formally tested with change-point or bistability statistics (see `question:0003`).
- **Vaccination/reinfection evidence is compatible but non-specific (t010, 2026-06-25).**
  Pre-infection vaccination and hybrid immunity reduce long-COVID risk in SARS-CoV-2 cohorts
  (`interpretation:0022`), but they are mixed proxies: they can prevent infection, lower acute severity,
  reduce viral burden, alter inflammatory priming, and change healthcare utilization. Therefore they
  support prevention/modification and host-reserve framing, but they do not by themselves prove a
  severity threshold or identify the acute mediator.
- **Vascular sex×severity interaction remains a modeling caution (t048, 2026-06-25).** Spetz2025 shows
  that mild/non-hospitalized COVID-19 has elevated DVT/PE risk and that COVID-associated
  thromboembolic risk appears larger in men than women against an uninfected baseline. This means sex
  should not be treated as only a baseline covariate or only an acute-severity proxy in vascular analyses;
  the needed estimand is sex×infection×time-window, stratified by non-hospitalized vs hospitalized
  severity.
- **Pediatric MIS-C constrains a severity-only reading (t009, 2026-06-26).** MIS-C can involve severe
  post-infectious hyperinflammation, vasoactive support, and cardiac dysfunction, yet MUSIC reports
  generally strong recovery by 6 months (Truong2025). This does not refute h0004, but it narrows the
  threshold model: the relevant threshold is not simply "severe inflammation occurred"; it is whether the
  host exits or remains trapped in a chronic dysregulated state.
- **Trained-immunity substrate offers a candidate — but severity-bounded — threshold mechanism (t095, 2026-07-07).**
  Central HSPC epigenetic imprinting (Cheong2023) is a molecular candidate for *how* a severity threshold
  could operate: severe acute IL-6 peaks reprogram bone-marrow progenitors into durable (months-long)
  myeloid hyperreactivity, plausibly gating attractor entry. But Cheong2023 demonstrated this only in
  *severe/hospitalized* COVID-19, so if HSPC central training is the substrate it would gate specifically
  the imprinting-dependent component and would *not* explain the common mild-onset PAIS case — reinforcing
  the "severity is one axis among several" reading above rather than a severity-only gate. See
  `topic:innate-immune-memory-trained-immunity-in-pais`.

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
- **Ambrosino2021 (empirical-data, case-control):** In post-severe/critical COVID-19 convalescents, FMD (endothelial function) directly correlates with pulmonary-impairment severity markers (rho 0.247–0.436); FMD thus tracks rather than dissociates from acute-severity sequelae. Load-bearing for the severity-confounded interpretation of male-biased vascular PAIS signals.
- **Spetz2025 (literature/registry cohort):** Swedish total-population cohort showing mild/non-hospitalized COVID-19 still carries elevated DVT/PE risk and that DVT/PE remain elevated in the 91-180 day window overall. It also suggests a larger COVID-associated thromboembolic increment in men than women, so future severity-threshold tests should model sex jointly with infection and severity rather than treating male vascular risk as pure baseline carryover.
- **Green2025 / Brannock2023 / LundbergMorris2023 / Malden2024 (literature/observational):**
  pre-infection vaccination is associated with lower long-COVID/PCC risk across systematic-review,
  EHR, and register designs. Compatible with the acute-threshold frame, but not mechanism-specific.
- **Carazo2025 (literature/observational):** booster and hybrid immunity reduce long-COVID risk in
  Quebec healthcare workers, with waning and strong dependence on prior infection/immunity state.
- **ZhangRECOVEREHR2026 (literature/EHR cohort):** RECOVER-EHR pediatric Omicron-era reinfection study shows
  second infection is associated with higher PASC diagnosis and PASC-related symptom/condition risk than
  first infection. Compatible with repeated acute-exposure burden increasing PAIS risk, but EHR coding and
  mechanism-mixing prevent a direct threshold claim.

## Disputing Evidence

- **Oronsky2021:** the SIRS→CARS→PICS severe-illness arc may not apply to mild-acute-infection PAIS, the predominant ME/CFS/long-COVID phenotype — a direct challenge to a severity-only gate.
- **Gandhi2023:** "for vs with" ascertainment bias inflates severity-outcome associations in administrative data.
- Mild-infection-onset ME/CFS and long COVID are common, arguing host factors can dominate over insult magnitude.
- **Truong2025/MUSIC:** severe MIS-C often resolves by 6 months, so acute/subacute inflammatory severity
  alone is not sufficient for chronic PAIS.

## Evidence Needed To Shift Belief

- **Most efficient upward:** change-point/bistability modeling across multiple pathogen cohorts showing a recurrent threshold, with host-reserve-adjusted threshold shifts (answers `question:0003`).
- **Most efficient downward:** ascertainment-corrected analysis showing continuous dose-response or no severity effect after reserve adjustment.
- **Also useful:** demonstration that mild-onset cases are low-reserve hosts (reconciling the counterexample) vs not (refuting the model).

## Related Work

- `topic:shared-failure-mode-across-pais` — the cross-pathogen severity/threshold synthesis.
- `question:0003-acute-severity-threshold-for-self-sustaining-pais` — the formal test.
- `hypothesis:0001-shared-dysregulated-attractor` — this threshold is the proposed *gate* for attractor entry.
- `immunity:research-question:immune-homeostasis-and-dysregulation` — host-reserve/homeostatic-margin biology.
- `topic:innate-immune-memory-trained-immunity-in-pais` — HSPC central-training as a candidate (severity-bounded) molecular substrate for the threshold.
