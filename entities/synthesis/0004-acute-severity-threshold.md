---
id: synthesis:0004-acute-severity-threshold
kind: synthesis
title: "Synthesis: 0004-acute-severity-threshold"
status: "active"
report_kind: hypothesis-synthesis
hypothesis: hypothesis:0004-acute-severity-threshold
generated_at: 2026-06-24T19:16:12Z
source_commit: 05a785bf71096ea8cc4d486b93f3f920a481cd74
created: "2026-06-24"
updated: "2026-06-25"
provenance_coverage: high
---

## State

`hypothesis:0004-acute-severity-threshold` holds that the magnitude of the acute-phase insult sets a homeostatic recovery threshold: below it the system self-resolves; above it the system settles into durable dysregulation. Eight source references underpin the claim, and `interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment` records the most recent bearing on this hypothesis.

Primary empirical support rests on qualitatively divergent multi-year trajectories in which hospitalized PASC remains elevated through year three while non-hospitalized patients approach baseline — a trajectory structure more consistent with threshold-crossing than a smooth dose-response gradient, and the organizing question for `question:0003-acute-severity-threshold-for-self-sustaining-pais`. Cross-pathogen breadth comes from a roughly 20% chronic fraction after Q-fever and from severe dengue (DHF) selectively predicting post-dengue fatigue, both cited in the proposition bundle of `hypothesis:0004-acute-severity-threshold` [@Morroy2016; @Hertanti2025; @Conde2026]. Host reserve modulates the effective threshold: sex, age, and cardiometabolic comorbidity shift recovery trajectories per the auxiliary propositions.

A materially important qualification comes from `interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment`: the male-biased vascular hard-endpoint signal is present *below* the hospitalization threshold (ambulatory VTE, `evidence-line:0029-xie2022-ambulatory-male-vte-excess-survives-low-severity-stratum`; aHR 1.69 [@Xie2022]), establishing that the vascular sex-reversal is not gated by acute severity. This is recorded as a domain-level partial dispute rather than a global refutation. The FMD/endothelial leg (`evidence-line:0032-ambrosino2021-fmd-male-endothelial-direction-only-severity-confounded`) remains severity-confounded and was deliberately excluded from discriminating evidence. A large mild-acute-infection fraction of ME/CFS and long COVID also sits in tension with a severity-only gate (`question:0003-acute-severity-threshold-for-self-sustaining-pais`).

## Arc

The threshold framing was minted at project launch (2026-06-11) as an organizing conjecture anchored in cross-pathogen severity-outcome associations and the qualitatively divergent hospitalized-vs-non-hospitalized VA cohort trajectories. `hypothesis:0004-acute-severity-threshold` linked immediately to `question:0003-acute-severity-threshold-for-self-sustaining-pais` as the required formal test — change-point or bistability modeling across pathogens — which remains open.

The main investigative move was `task:t042`, a targeted literature sweep asking whether the male-biased vascular PAIS signal is explained by severity confounding. `interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment` resolved that sub-question by bracketing the severity range: the male hard-endpoint direction survives both the low-severity stratum (ambulatory outpatients, `evidence-line:0029`) and the high-severity stratum (within-hospitalized pneumonia cohort, `evidence-line:0030-kopp2024-male-cv-mortality-excess-within-hospitalized-stratum`; HR 1.68 at 18 months [@Kopp2024]). This established `proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment` and amended `interpretation:0003-t018-subphenotype-sex-reproductive-stage`. The implication for `hypothesis:0004-acute-severity-threshold` is bounded: the vascular-thromboinflammatory domain does not require severity-crossing to express, qualifying the threshold frame for that domain without refuting the broader conjecture.

Current epistemic position: the severity-threshold frame remains the best available cross-pathogen organizing principle for predicting chronicity, but the primary formal test (`question:0003-acute-severity-threshold-for-self-sustaining-pais`) is still open, and the male vascular reversal thread — specifically its COVID-specificity vs baseline-rate carryover — is the active investigative front.

## Research Fronts

**Live questions.** `question:0003-acute-severity-threshold-for-self-sustaining-pais` (change-point vs continuous dose-response across pathogens) is the central unanswered question. `question:0019-male-biased-vascular-signal-pasc-persistence` and `question:0020-male-vte-excess-post-acute-persistence` are partially resolved: post-acute CV-mortality male excess is established (`interpretation:0005`), but late ambulatory VTE persistence beyond 30 days is not. `question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover` — COVID-amplified vs baseline-carried male risk — is unresolved. `question:0012-prevention-vaccination-antiviral-reduces-pais` bears on the threshold frame mechanistically.

**Open tasks.** `task:t048` is the live front (P2, proposed): find a sex-stratified COVID-vs-uninfected ambulatory cohort with post-acute (31–180 day) vascular endpoint follow-up to estimate the infection-attributable male excess as a ratio-of-ratios for `question:0020` and `question:0021`. Candidate designs named in `task:t048` include the VA Million Veteran / Al-Aly test-negative cohort, OpenSAFELY, and N3C. `task:t010` (reinfection and vaccination effects on PAIS risk, P3 proposed) is secondary, bearing on `question:0012`.

**Residual gaps.** Formal change-point modeling has not been performed. "For vs with" ascertainment confound inflates apparent severity effects in administrative cohorts. Mild-onset PAIS cases require host-reserve enrichment data to reconcile with the threshold model. Baseline-rate confounding for male vascular risk (older-age male VTE predominance independent of COVID) is the leading caveat on `proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment` and would require a formal infection × sex interaction term against an age-stratified uninfected comparator to resolve.
