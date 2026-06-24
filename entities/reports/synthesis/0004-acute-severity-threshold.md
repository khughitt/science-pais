---
type: synthesis
title: "Synthesis: 0004-acute-severity-threshold"
report_kind: hypothesis-synthesis
id: synthesis:0004-acute-severity-threshold
hypothesis: hypothesis:0004-acute-severity-threshold
generated_at: 2026-06-24T03:28:17Z
source_commit: eb1a5ca60ed1cd69451e2a3d9d6fa16da31fbfec
provenance_coverage: high
---

## State

The hypothesis (hypothesis:0004-acute-severity-threshold) holds that the magnitude of the acute-phase insult sets a homeostatic recovery threshold: below it the system self-resolves, above it the system settles into durable dysregulation. The graph records this as `well_supported` with four support signals and zero disputes at the proposition level, drawing on eight source references.

Primary empirical support comes from qualitatively divergent multi-year trajectories in a large VA cohort, where hospitalized PASC remains elevated through year three while non-hospitalized patients approach baseline — a trajectory structure more consistent with threshold-crossing than with a pure dose-response gradient (question:0003-acute-severity-threshold-for-self-sustaining-pais). A meta-analytic literature review corroborates ICU/ventilation status as the dominant predictor of three-year PASC persistence (question:0003-acute-severity-threshold-for-self-sustaining-pais). Cross-pathogen support comes from a ~20% chronic fraction observed after Q-fever and from dengue hemorrhagic fever (severe dengue) selectively predicting post-dengue fatigue (question:0003-acute-severity-threshold-for-self-sustaining-pais).

A materially important qualification comes from interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment, which records that the male-biased vascular hard-endpoint signal is present *below* the hospitalization threshold (ambulatory VTE, aHR 1.69 from evidence-line:0029-xie2022-ambulatory-male-vte-excess-survives-low-severity-stratum), meaning the vascular sex-reversal is not gated by acute severity — a partial dispute for that specific domain recorded as background context rather than a formal refutation of the broader threshold hypothesis. A large mild-acute-infection fraction of ME/CFS and long COVID also sits in tension with a severity-only gate (question:0003-acute-severity-threshold-for-self-sustaining-pais).

## Arc

Investigation opened with the threshold framing as an organizing conjecture grounded in cross-pathogen severity-outcome associations (hospitalized COVID-19/influenza multi-organ burden, dengue DHF, Q-fever chronic fraction) and the qualitatively divergent hospitalized-vs-non-hospitalized trajectory in the VA cohort. The hypothesis was minted as `proposed` at project launch (2026-06-11) and immediately linked to question:0003-acute-severity-threshold-for-self-sustaining-pais as the required formal test — change-point or bistability modeling across pathogens — which remains unanswered.

The main investigative move since launch was task:t042 (Kopp2024, Xie2022, Abubasheer2025, Ambrosino2021 ingestion), which asked whether the male-biased vascular PAIS signal is explained by severity confounding. interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment resolved that sub-question: the male vascular hard-endpoint direction survives both the low-severity stratum (ambulatory Xie2022) and the high-severity stratum (within-hospitalized Kopp2024), establishing proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment. The implication for hypothesis:0004 is bounded: the vascular-thromboinflammatory domain operates below the hospitalization threshold and does not require severity-crossing to express — which is a domain-level qualification, not a global refutation. The FMD/endothelial leg (evidence-line:0032-ambrosino2021-fmd-male-endothelial-direction-only-severity-confounded) remains severity-confounded and was deliberately excluded from discriminating evidence by interpretation:0005.

Current epistemic position: the severity-threshold frame remains the best available cross-pathogen organizing principle for predicting chronicity risk, but the primary formal test (question:0003) is still open, and host-reserve modulation (sex, age, comorbidity) is acknowledged as shifting the effective threshold.

## Research Fronts

**Live questions.** question:0003-acute-severity-threshold-for-self-sustaining-pais — whether a quantifiable change-point exists in chronicity probability as a function of acute severity, shared across pathogens — is the central unanswered question and would most efficiently shift confidence in either direction. question:0012-prevention-vaccination-antiviral-reduces-pais asks whether acute-phase interventions (vaccination, antivirals, metformin) reduce PAIS incidence, which is mechanistically consistent with the threshold frame: early intervention should prevent threshold-crossing. question:0019-male-biased-vascular-signal-pasc-persistence and question:0020-male-vte-excess-post-acute-persistence remain partially open: post-acute CV mortality male excess is established (interpretation:0005), but late ambulatory VTE persistence is not.

**Open tasks.** task:t010 (literature search on reinfection and vaccination effects on PAIS risk and recovery, P3 proposed) is the most relevant active work, bearing on question:0012.

**Residual gaps.** The "for vs with" ascertainment confound in administrative cohorts inflates apparent severity effects. Formal change-point/bistability modeling has not been performed. Mild-onset PAIS cases need host-reserve enrichment data to reconcile with the threshold model. The male vascular reversal's COVID-specificity vs baseline-rate carryover (per interpretation:0005) is unresolved and could affect how severity and sex covariates should be jointly modeled.
