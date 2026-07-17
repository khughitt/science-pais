---
id: "synthesis:0020-host-immune-baseline-reserve-gate"
kind: "synthesis"
title: "Synthesis: 0020-host-immune-baseline-reserve-gate"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0020-host-immune-baseline-reserve-gate"
generated_at: "2026-07-17T10:26:49Z"
source_commit: "f6365a35a9baa2b2d02bb68e5ed53199312617bf"
created: "2026-07-17"
updated: "2026-07-17"
provenance_coverage: "partial"
---

## State

`hypothesis:0020-host-immune-baseline-reserve-gate` proposes that a patient's pre-infection immune homeostatic reserve — rather than the acute insult magnitude alone — sets the probability that post-infectious recovery fails. It organizes five host-modifier strata (chronic immunosuppression, frailty/inflammaging, atopy/MCAS, pregnancy-phase immune remodelling, and ancestral/LMIC immune context) as instances of one shared vulnerability gate operating upstream of the acute-severity threshold (`hypothesis:0004-acute-severity-threshold`) and generalizing the reproductive-stage-margin frame (`hypothesis:0005-reproductive-stage-immune-homeostatic-margin`).

The sole current causal-mediation result is `proposition:0043-host-reserve-dominates-acute-severity-gate`, grounded in a single EHR study: `evidence-line:0092-azhir2026-mediation-supports-reserve-over-severity` (paper:Azhir2026) reports that physiological reserve outweighs chronological age in post-infectious sequelae risk, providing one-source support for reserve dominance. `evidence-line:0093-russell2023-multimorbidity-tolerance-supports-reserve-gate` (paper:Russell2023) contributes mechanistic vocabulary — multimorbidity as a tolerance-reduction frame — but is not an independent effect estimate and does not corroborate the magnitude.

This is intentional fragility: the project has formally reviewed and accepted that `proposition:0043` is fragile-single-line pending a second cohort with a pre-infection biological-reserve measure. The rank-ordering prediction (P3) across host strata is untested, and no operational pre-infection reserve axis has been measured in any grounded source. `question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts` is the one stratum with project-level sourced evidence; `question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse`, `question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with`, `question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a`, and `question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory` remain grounded only in literature motivation.

## Arc

Arc reconstruction is limited because no interpretations with `prior_interpretations` chains exist for this hypothesis.

The hypothesis entered the project on 2026-07-10 as a user-originated conjecture, framing the project's scattered host-modifier questions as a single testable vulnerability gate. Its founding move was to bundle five existing questions — `question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts`, `question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse`, `question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with`, `question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a`, and `question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory` — under one shared-mechanism claim (P2) and to declare a rank-ordering prediction (P3) as the discriminating test.

A 2026-07-16 curation sweep backfilled outbound `related:` edges from the five primary questions to the hypothesis, making the bidirectional wiring explicit; the reciprocal hypothesis-to-question edges already existed. Separately, evidence integration deposited `proposition:0043-host-reserve-dominates-acute-severity-gate`, anchored by paper:Azhir2026 as the single causal-mediation grounding line, with paper:Russell2023 attached as a mechanistic-frame anchor only. The project then formally accepted the fragility designation: the reserve-dominance magnitude rests on one published EHR mediation result; the strata-level shared-mechanism claim and P3's rank-ordering test remain uninitiated.

Current epistemic position: one suggestive EHR causal-mediation result (paper:Azhir2026), no independent second cohort, no operational reserve axis defined, and four of five host strata without project-level grounded evidence.

## Research Fronts

**Live questions.** The five primary questions are `question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts`, `question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse`, `question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with`, `question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a`, and `question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory`. Back-inverse questions probing the reserve frame include `question:0074-age-65-pasc-resilience-threshold-phenotype`, `question:0083-serial-pasc-episodes-reserve-depletion`, `question:0084-mrna-vaccine-platform-long-covid-protection`, `question:0086-hybrid-immunity-type-pais-risk-modifier`, and `question:0087-vaccine-response-proxy-immune-baseline-reserve` — the last of these is the most proximate, asking whether vaccine-response competence can stand as a pre-infection reserve readout.

**Critical structural gap.** No operational pre-infection reserve axis has been defined or validated; without one, P3's rank-ordering test is not specifiable. The highest-priority next step is to define one reserve proxy and test rank-ordering of PAIS incidence across ≥2 host strata with severity adjustment.

**Replication need.** `proposition:0043-host-reserve-dominates-acute-severity-gate` rests entirely on paper:Azhir2026; a second independent cohort carrying a pre-infection biological-reserve measure is required before the reserve-dominance magnitude can be labeled as anything stronger than one-source. No new gated-EHR analyses are in scope under decision D-004.
