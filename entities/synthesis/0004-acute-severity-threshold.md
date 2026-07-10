---
id: "synthesis:0004-acute-severity-threshold"
kind: "synthesis"
title: "Synthesis: 0004-acute-severity-threshold"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0004-acute-severity-threshold"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-06-24"
updated: "2026-07-10"
provenance_coverage: "high"
---

## State

`hypothesis:0004-acute-severity-threshold` proposes that acute insult magnitude sets a homeostatic recovery threshold: below it the system self-resolves; above it it settles into durable dysregulation. Status `proposed`, phase `active`.

Empirical backing is suggestive but unconfirmed. Hospitalized PASC shows qualitatively divergent multi-year trajectories from non-hospitalized patients — consistent with threshold-crossing rather than a smooth gradient (Cai2024) — and a ~20% chronic fraction recurs across Q-fever (Morroy2016) and severe dengue. `question:0003-acute-severity-threshold-for-self-sustaining-pais` — formal change-point or bistability modeling across pathogens — has not been executed.

Within the vascular domain, `proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment` is well-supported: male hard-endpoint excess holds in ambulatory patients (`evidence-line:0029-xie2022-ambulatory-male-vte-excess-survives-low-severity-stratum`, aHR 1.69) and within a hospitalized-restricted cohort (`evidence-line:0030-kopp2024-male-cv-mortality-excess-within-hospitalized-stratum`, HR 1.68). `evidence-line:0074-spetz2025-sex-stratified-covid-thromboembolic-amplification-supports-0012` narrows baseline-carryover as explanation; `evidence-line:0032-ambrosino2021-fmd-male-endothelial-direction-only-severity-confounded` is excluded as severity-confounded. The vascular signal is not severity-gated, a domain-level qualification of h0004 without refuting the broader conjecture.

Three constraints further narrow the model. `interpretation:0025-t009-pediatric-long-covid-and-misc` establishes that severe MIS-C inflammation typically resolves by 6 months (Truong2025), ruling out "severe inflammation" as the operative threshold criterion. `task:t113` found that the Hammel2023 frailty–PASC signal lacks an acute-severity covariate and fades beyond 6 months — materially weaker support for a durable reserve-independent effect than the raw aHR suggests. `interpretation:0022-t010-reinfection-vaccination-risk-recovery` finds pre-infection vaccination reduces long-COVID risk observationally but via mechanism-mixed pathways, compatible with but not a direct proof of the threshold frame.

## Arc

The threshold conjecture was minted at project launch (2026-06-11), anchored in cross-pathogen severity-outcome associations and the divergent VA hospitalized-vs-non-hospitalized trajectory (Cai2024). `question:0003-acute-severity-threshold-for-self-sustaining-pais` was registered immediately as the required formal test and remains open.

`task:t042` was the first investigative move: `interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment` bracketed the severity range for male vascular endpoints across ambulatory and hospitalized strata, establishing `proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment` and recording a domain-level qualification of h0004. `task:t048` then audited baseline carryover (`interpretation:0018-t048-vascular-sex-baseline-carryover-audit`): Spetz2025 narrows that alternative explanation but does not report the ambulatory 31–180 day sex interaction, leaving `question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover` partially open.

`task:t009` (`interpretation:0025-t009-pediatric-long-covid-and-misc`) and `task:t010` (`interpretation:0022-t010-reinfection-vaccination-risk-recovery`) added scope constraints via MIS-C recovery evidence and mechanism-mixed vaccination data respectively. Feasibility triage for a causal estimand (`task:t079`; `interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision`, `interpretation:0034-t079-bc6-acute-severity-dateability`) confirmed acute severity is dateable in N3C and OpenSAFELY, though the linked autoimmune-sex-PASC estimand was subsequently shelved under D-004.

Most recently, `task:t108` (`interpretation:0039-t108-cross-pais-il6-peak-vs-pais-risk`) refuted serum IL-6 magnitude as a cross-pathogen HSPC-imprinting proxy — severity survives as the cross-trigger ranking axis, consistent with h0004 but inferred via one-source desk compilation. `task:t107` (`interpretation:0040-t107-hspc-epigenomics-feasibility-banked-pbmc`) identified monocyte-progeny ATAC-seq on banked PBMC as the feasible direct test of the imprinting hypothesis, operationalized in `pre-registration:0006-monocyte-atac-hspc-imprint-pais-persistence`.

## Research Fronts

**Live questions.** `question:0003-acute-severity-threshold-for-self-sustaining-pais` — change-point or bistability modeling across pathogens — is the primary formal test. `question:0019-male-biased-vascular-signal-pasc-persistence`, `question:0020-male-vte-excess-post-acute-persistence`, and `question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover` address the vascular sex-severity interaction: post-acute CV-mortality male excess is established; late ambulatory VTE persistence (31–180 days) and COVID-specific attribution remain open. `question:0052-acute-clearance-rate-as-cross-pathogen-pais-trajectory-predictor` and `question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais` probe the modification structure of the threshold. `question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors` and `question:0055-hspc-epigenomic-imprinting-depth-predicts-pais-persistence` are redirected to direct HSPC epigenomics following `interpretation:0039-t108-cross-pais-il6-peak-vs-pais-risk`.

**Open tasks.** `task:t111` (proposed) — DAG for compound/co-occurring boundary conditions underpinning `question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais`. `task:t121` (proposed) — specimen-access query for RECOVER/LIINC/UK ME/CFS Biobank, gating `pre-registration:0006-monocyte-atac-hspc-imprint-pais-persistence`.

**Residual gaps.** Formal change-point modeling across pathogens has not been performed. "For vs with" ascertainment bias inflates apparent severity effects in administrative cohorts. Mild-onset PAIS cases still require host-reserve enrichment evidence to reconcile with the threshold model. Baseline male vascular predominance (older-age VTE) is the leading unresolved caveat on `proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment`.
