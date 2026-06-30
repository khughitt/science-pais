---
id: synthesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
type: synthesis
title: "Synthesis: 0007-autoimmune-sfn-peripheral-dysautonomia-substrate"
status: "active"
report_kind: hypothesis-synthesis
hypothesis: hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
generated_at: 2026-06-24T19:16:12Z
source_commit: 05a785bf71096ea8cc4d486b93f3f920a481cd74
created: "2026-06-24"
updated: "2026-06-25"
provenance_coverage: partial
---

## State

`hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` posits a non-length-dependent autoimmune small-fiber neuropathy (SFN) as the shared peripheral structural substrate of dysautonomia across PAIS triggers. The hypothesis carries four core propositions at varying evidence levels.

**P1 (structural lesion, `proposition:0014`)** is the best-evidenced leg and is rated contested due to one rigorous null. Skin-biopsy SFN is documented across long COVID (67% by biopsy, `interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat`), ME/CFS (31–53%, `interpretation:0009-t049-sfn-cross-syndrome-ingestion`), and PTLDS (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`), against 0% in healthy controls. The Walitt2024 adjudicated PI-ME/CFS cohort returned a null, preserved as a real counterexample to universality (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`). Metric-harmonization work shows the apparent 0–91% prevalence scatter is dominated by modality breadth, trigger, and referral-enrichment rather than the QASAT-vs-percentile cutoff rule, and that within-trigger referral cohorts are in fact concordant (`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`) [@Novak2026; @Oaklander2022; @Joseph2021; @Walitt2024].

**P4 (cross-trigger convergence, `proposition:0017`)** was quality-upgraded from "convergence of finding, not of protocol" by Novak2026's single-protocol, single-center comparison of long COVID and ME/CFS under one paired-site design (`interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat`). A real LC > ME/CFS sensory-ENFD gradient (p = 0.021) rides on top of the convergence signal, indicating "same substrate, trigger-graded severity" rather than identical rates (`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`) [@Novak2026].

**P2 (non-length-dependent pattern, `proposition:0015`)** is the thinnest leg. Group-level proximal SGNFD in Novak2026 is consistent with the NLD claim but no per-subject NLD classification has been reported in any infection-triggered cohort (`interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat`). P2 remains asserted more than measured.

**P3 (autoimmune causation, `proposition:0016`) and the anti-GPCR route (`proposition:0018`)** are contested. deSa2026 causally links long-COVID IgG to intraepidermal nerve-fiber loss in a passive-transfer mouse model, but the autoantigens were non-GPCR (MED20/USP5) and the autonomic axis was not recapitulated (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`). The anti-GPCR arm is one functional-assay correlation (Kharraziha2020 α1-AR activity vs orthostatic-symptom severity) against a binding-ELISA specificity null (Hall2022), with no study linking any anti-GPCR antibody to the small-fiber lesion (`interpretation:0010-t006-functional-gpcr-autoantibody-ingestion`). A new specificity caveat from Novak2026 shows hEDS (a non-infectious heritable dysautonomia, n=290) carries SFN comparable to or greater than the PAIS arms — the first corpus evidence that the substrate is not exclusive to post-infectious syndromes, pressuring `question:0004-convergent-small-fiber-neuropathy-substrate`'s "distinguishes from primary dysautonomia" clause (`interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat`) [@deSa2026; @Kharraziha2020; @Hall2022; @Novak2026].

The graph flags `proposition:0014`, `proposition:0016`, and `proposition:0018` as `evidential_fragility(contested)`.

## Arc

The hypothesis was assembled at project launch as a structural-lesion frame occupying a level no other h0007-era hypothesis addressed: the peripheral end-organ, downstream of system-level dysregulation hypotheses.

The first investigative move was the t049 cross-syndrome SFN ingestion, which coded seven papers into eleven evidence-lines and established the current proposition-level architecture (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`). That pass documented P1 and P4 across three triggers but left P2 as the "least-measured leg" (only the post-vaccine Limongelli2026 cohort supplied a clean paired-site NLD fraction), and P3 as causally anchored for long COVID (deSa2026 passive transfer) but null in the best ME/CFS cohort (Walitt2024). The primary-dysautonomia-control gap was called universal at that stage: no paper in the corpus included such a comparator.

The second move, task:t006, deepened the anti-GPCR route by ingesting the primary functional-autoantibody literature (`interpretation:0010-t006-functional-gpcr-autoantibody-ingestion`). This formally contested `proposition:0018`: one functional assay (Kharraziha2020) survives Hall2022's binding-ELISA specificity null, but the critical antibody-to-lesion bridge — functional anti-GPCR activity and IENFD measured in the same subjects — remains untested by any study.

The third move was the t050 vehicle hunt for `pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls`, which surfaced Novak2026 as the largest paired-site PAIS biopsy series to date (`interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat`). Novak2026 reinforced P1 (adding the largest independent cohort) and upgraded P4 to a single-protocol two-trigger demonstration — the methodological caveat that had weakened the convergence claim since t049. It also introduced the hEDS specificity signal, shifting the hypothesis's key open question from "does the lesion exist?" to "is its pattern specific relative to primary dysautonomia?" Novak2026 was screened as a promotion vehicle but ruled inadmissible: its comparators are healthy controls and hEDS, neither satisfying the locked G2 primary-dysautonomia arm requirement.

The fourth move, a metric-harmonization re-analysis of the four corpus biopsy studies, resolved `interpretation:0013`'s open question about QASAT-vs-percentile scoring (`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`). The cutoff rule contributes surprisingly little; modality breadth (48→67→91% on identical Novak2026 patients), trigger, and referral-enrichment are the dominant drivers of the apparent heterogeneity. This finding validated `pre-registration:0003`'s within-subject NLD-classification metric as structurally less vulnerable to the absolute-prevalence confound than between-study comparisons [@Novak2026].

The hypothesis now stands at candidate with a sharper account of what the discriminating study must show — not lesion existence (now well-evidenced) but pattern specificity against a clean primary-dysautonomia control arm — and with both promotion criteria blocked: criterion #1 on the missing G2 vehicle (`pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls`), criterion #2 on the untested antibody-to-lesion bridge (`interpretation:0010-t006-functional-gpcr-autoantibody-ingestion`).

## Research fronts

**Open questions.** `question:0004-convergent-small-fiber-neuropathy-substrate` is the primary driver of criterion #1: it asks whether PAIS SFN is a distinct, non-length-dependent substrate distinguishable from primary dysautonomia. The Novak2026 hEDS signal makes the specificity half harder to win than the lesion-existence half. `question:0009-functional-autoantibodies-drive-dysautonomia` is criterion #2's driver and remains contested after t006: the antibody-to-lesion bridge is the gap, not antibody existence.

**Open tasks.** `task:t050` is blocked on the G2 primary-dysautonomia vehicle, with no admissible study in the corpus as of the 2026-06-24 hunt. The Novak group is identified as the most realistic near-term source of a qualifying vehicle (one protocol amendment away: add an idiopathic-POTS arm, re-score to percentile cutoffs). `task:t006` is complete; the gap it exposed is now owned by `pre-registration:0003`'s G5 serology arm.

**Promotion criteria status (candidate frame).** Criterion #1 is data-gated at `pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls`; no admissible vehicle exists. Criterion #2 (titer↔IENFD/autonomic-severity correlation or immunomodulation response in a seropositive subset) is unmet on the strict lesion-linked reading; only Kharraziha2020's functional α1-AR↔OHQ correlation survives as partial and contested support at the autonomic-function level.

**Graph fragility flags.** `proposition:0014`, `proposition:0016`, and `proposition:0018` are flagged `evidential_fragility(contested)`. The Walitt2024 null and the Hall2022 binding-ELISA specificity null are the live competing signals. A well-powered null at the ≥80 lesion-positive/side floor on a future admissible vehicle would materially weaken P1 and the structural-lesion frame.

**Convention note.** All future SFN-prevalence claims must state trigger, biopsy modality (ENFD/SGNFD/functional), site protocol, and cutoff rule; absolute prevalence without these four axes is uninterpretable (`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`).
