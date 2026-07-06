---
id: paper:Kharraziha2020
kind: paper
title: Serum Activity Against G Protein-Coupled Receptors and Severity of Orthostatic
  Symptoms in Postural Orthostatic Tachycardia Syndrome
status: active
paper_kind: ''
ontology_terms:
- GPCR autoantibody
- functional bioassay
- postural orthostatic tachycardia syndrome
- dysautonomia
- adrenergic receptor
- muscarinic receptor
- orthostatic intolerance
dataset_usage: []
source_refs:
- cite:Kharraziha2020
related:
- question:0009-functional-autoantibodies-drive-dysautonomia
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- topic:post-infectious-dysautonomia-and-autoimmunity
created: '2026-06-24'
updated: '2026-06-24'
---

# Serum Activity Against G Protein-Coupled Receptors and Severity of Orthostatic Symptoms in Postural Orthostatic Tachycardia Syndrome

<!--
- **Authors:** Isabella Kharraziha, Jonas Axelsson, Fabrizio Ricci, Giuseppe Di Martino, Margaretha Persson, Richard Sutton, Artur Fedorowski, Viktor Hamrefors
- **Year:** 2020
- **Journal:** Journal of the American Heart Association (JAHA), Vol. 9, Issue 15, e015989
- **DOI/URL:** https://doi.org/10.1161/JAHA.120.015989
- **PMID:** 32750291 / PMCID: PMC7792263
- **BibTeX key:** Kharraziha2020
- **Source:** Full text (Europe PMC XML)

**Author-attribution note:** The user anticipated "Gunning WT et al. ~2019" as first author. That is a *different* paper (Gunning et al. 2019, DOI 10.1161/JAHA.119.013602, binding-ELISA method) cited as reference 9 in this paper. The paper retrieved here is Kharraziha et al. 2020, which uses the FRET-based functional cell assay. Both papers study GPCR autoantibodies in POTS, but they are distinct works with distinct methods. The correct paper for the functional-assay / titer-severity correlational question is Kharraziha et al. 2020.
-->

## Key Contribution

This study is the first to use a functional, cell-based FRET (fluorescence resonance energy transfer) beta-arrestin reporter assay — rather than binding ELISA — to quantify serum-mediated activation of four GPCRs (ADRA1, ADRB2, CHRM2, OPRL1) in POTS patients versus healthy controls. The principal finding is that serum GPCR activity is highly predictive of POTS diagnosis (AUC 0.88 for all four receptors combined), and that alpha-1 adrenergic receptor (ADRA1) activity specifically correlates with orthostatic symptom severity (OHQ composite score) independently of the hemodynamic response during orthostasis. This is the correlational arm of the functional-autoantibody hypothesis: higher circulating serum activity against ADRA1 tracks worse self-reported orthostatic burden within the POTS population.

## Methods

**Design:** Cross-sectional, single-centre case-control study at a tertiary syncope/autonomic referral unit (Skåne University Hospital, Malmö, Sweden). Recruitment: January–December 2018.

**Cohort:**
- n = 48 POTS patients (mean age 28.6 ± 10.5 years; 44/48 women, 91.7%)
- n = 25 healthy controls (mean age 30.7 ± 8.6 years; 21/25 women, 84%)
- POTS diagnosed by expert clinician (A. Fedorowski); all POTS patients had a previously confirmed positive tilt test (criteria: sustained heart-rate rise ≥ 30 bpm on tilt, in the absence of orthostatic hypotension).
- OHQ was completed by 33/48 POTS patients and all 25 controls at the time of blood sampling; the remaining 15 POTS patients submitted blood from remote sites and did not complete the OHQ.
- 36/48 POTS patients were on heart-rate-regulating or vasoactive medications at blood draw.

**Functional assay (key methodological axis):**
Tango GeneBLAzer FRET-based beta-arrestin reporter system (Thermo Fisher Scientific). HEK293 cells overexpressing one of four GPCRs (ADRA1 = alpha-1 adrenergic; ADRB2 = beta-2 adrenergic; CHRM2 = muscarinic M2; OPRL1 = opioid receptor-like 1) were treated with 10% patient serum for 5 hours. Beta-arrestin recruitment (receptor activation) drives beta-lactamase transcription; GPCR activity is measured as the FRET emission ratio of cleaved:uncleaved substrate. This is a **whole-cell functional bioassay detecting receptor-conformation change**, not a binding ELISA detecting isolated epitopes — a methodologically critical distinction. The assay does not directly identify autoantibodies as the activating moiety; conformational changes could in principle arise from other serum factors, but the authors consider autoantibodies the most likely explanation given prior ELISA literature.

Note: ADRB1 (beta-1 adrenergic receptor) was **not** included; ADRB2 was prioritized based on prior work showing the ADRA1 + ADRB2 combination provides ~94% discriminative efficacy for POTS.

**Symptom assessment:** 10-item Orthostatic Hypotension Questionnaire (OHQ), validated for orthostatic hypotension and used off-label for POTS; translated and validated into Swedish. Subscales: OHSA (6 symptom items) and OHDAS (4 daily-activity impact items). Composite score = mean of OHSA and OHDAS items (0–10 scale). Recall period: past week.

**Statistics:** GPCR activity log-transformed; independent-samples t-tests for group comparisons; ROC curves with combined logistic model for POTS prediction; age-adjusted linear regression of log-GPCR activity vs. OHQ scores; additional models adjusting for ΔHR and ΔSBP at 3-minute active standing.

## Key Findings

**POTS vs. controls — GPCR activity:**
- Serum from POTS patients activated all four receptors significantly more than controls (P < 0.01 for each receptor individually).
- 87.5% of POTS patients (42/48) had at least one receptor activity value above the 75th percentile of controls.
- ROC AUC = 0.88 (95% CI 0.80–0.97, P < 0.001) for the four-receptor logistic model; individual AUCs: ADRA1 0.72, ADRB2 0.76, CHRM2 0.73, OPRL1 0.75.
- Some GPCR activity was detectable in all controls (no zero-activity floor; there is no clean healthy-control negative baseline).

**Symptom severity correlation (primary correlational result):**
- ADRA1 activity above the within-POTS median was associated with higher OHQ composite score (median-split: 6.94 ± 1.18 vs. 5.74 ± 1.95, P = 0.043; n = 33).
- Continuous: ADRA1 activation β = 0.77 OHQ points per SD of activity (P = 0.009) in age-adjusted linear regression in POTS patients; no significant association in controls (P = 0.953).
- ADRA1 association with OHQ remained significant after adjusting for ΔHR and ΔSBP at 3 minutes (P = 0.031), meaning the activity-symptom relationship is **partly independent of the orthostatic hemodynamic response itself**.
- ADRA1 activity specifically correlated with reduced tolerability for prolonged standing (P = 0.037) and walking for short (P = 0.042) or long periods (P = 0.001).
- ADRB2, CHRM2, and OPRL1 activity did NOT show significant associations with OHQ composite score in POTS patients (P = 0.638, 0.260, 0.904 respectively).
- All four receptors were associated with worse visual-symptom scores (ADRA1 P < 0.001; ADRB2 P = 0.011; CHRM2 P = 0.014; OPRL1 P = 0.003).
- OPRL1 additionally associated with walking symptoms (P = 0.035).

**POTS case definition and diagnostic criterion used:** Previous positive head-up tilt test showing ≥ 30 bpm heart-rate increase sustained on orthostasis without orthostatic hypotension, per Heart Rhythm Society 2015 consensus.

**Contrast with Gunning et al. 2019 (ref 9 in this paper, binding-ELISA method):**
Gunning et al. used ELISA against isolated receptor epitopes (not whole-cell assay) and tested 9 receptor subtypes (ADRA1/2, ADRB1/2, CHRM1–5); they found a weak correlation between antibody concentration and orthostatic symptom severity across all 9 receptors in POTS/OH combined cohort, and 89% of POTS had ADRA1 antibodies by ELISA. The Kharraziha paper's functional FRET assay complements this by showing that serum *activity* (not just binding levels) tracks severity, and that ADRA1 is the most symptoms-specific receptor by the functional readout.

## Relevance

This paper is load-bearing for `question:0009-functional-autoantibodies-drive-dysautonomia` because it directly tests the correlational arm of the functional-autoantibody hypothesis: does GPCR serum *activity* (functional, receptor-activation readout) track orthostatic symptom severity in POTS? The answer is yes for ADRA1: β = 0.77 OHQ/SD activity, P = 0.009, surviving adjustment for the hemodynamic response. This partial independence from ΔHR is particularly important — it suggests the autoantibody-like activity is contributing to symptom burden through mechanisms beyond simply driving tachycardia.

For `hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` (`proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity`), this paper provides the symptom-correlation support but does not test the structural endpoint (IENFD or autonomic nerve fiber density). It is consistent with proposition:0018 but does not distinguish functional autoantibody activity from downstream fiber damage.

The ADRA1-specific correlational finding is more directly relevant to the question of **which receptor subtype** drives POTS severity: the alpha-1 adrenergic receptor, not the beta-2 or muscarinic-2 subtypes, correlates with global orthostatic burden. This is mechanistically coherent with the literature model in which ADRA1 antagonism impairs vasoconstriction and secondary sympathetic activation drives tachycardia.

For `hypothesis:0007` promotion criterion #2 (correlational arm): this study offers partial fulfillment — a functional assay shows titer-like ADRA1 activity correlating with orthostatic symptom severity. However the cohort is POTS (not specifically post-infectious), and GPCR activity is not normalized to a clean healthy-control floor (activity is present in all controls). The study is strengthened by (a) using a whole-cell functional assay rather than binding ELISA and (b) adjusting for the hemodynamic response.

The OPRL1 finding (elevated activity in POTS, correlation with vision/walking symptoms) is novel but unexplored; nociceptin receptor involvement in POTS autonomic signalling has no prior literature at the time of publication.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Serum GPCR activity (FRET β-arrestin assay) | Functional autoantibody bioassay | Key methodological axis: functional (whole-cell receptor activation) vs. binding ELISA |
| ADRA1 activity correlates with OHQ | Titer↔symptom-severity correlation (h0007 promotion criterion #2) | Partial fulfillment: functional readout, but POTS cohort not restricted to post-infectious; effect size β = 0.77 OHQ/SD |
| POTS diagnosis (tilt ≥ 30 bpm, no OH) | Dysautonomia / orthostatic intolerance subphenotype | Heart Rhythm Society 2015 criteria; tertiary referral cohort |
| OHQ composite and subscales | Orthostatic symptom burden | Validated for OH; used off-label for POTS; captures both symptoms and daily-activity impact |
| ADRB1 excluded, ADRB2 included | Receptor coverage gap | Beta-1 AR (most cardiac-relevant) not tested; prior work justified ADRB2 choice |
| OPRL1 (nociceptin receptor) | Novel GPCR target in POTS | No prior POTS literature; possibly relevant to chronic pain and visual symptoms |
| Adjustment for ΔHR / ΔSBP | Hemodynamic confound adjustment | Symptom-ADRA1 association survives, supporting mechanism beyond simple tachycardia |

## Limitations

1. **Small sample size:** n = 48 POTS patients, with OHQ available for only 33; results require external validation in larger cohorts.
2. **OHQ validated for orthostatic hypotension, not POTS:** The questionnaire does not capture cognitive symptoms, GI problems, or chronic pain well, all common in POTS; this may underestimate associations with non-orthostatic symptom domains.
3. **ADRB1 not tested:** Beta-1 adrenergic receptor, arguably the most directly cardiac-relevant receptor subtype, was excluded based on earlier pilot data; the absence means the most clinically prominent adrenergic receptor in tachycardia is not characterized.
4. **Most POTS patients on medications at sampling (n = 36/48):** HR-regulating and vasoactive agents could modulate receptor expression or GPCR signalling, potentially dampening both the activity signal and the symptom-GPCR correlation.
5. **Assay does not directly identify autoantibodies:** The FRET reporter detects *any* serum factor causing receptor-conformation change; the authors assume autoantibodies are responsible (consistent with prior ELISA findings) but this is not directly demonstrated. Non-antibody serum components (e.g., catecholamines, other proteins) could theoretically contribute.
6. **Controls not tilt-tested formally:** Controls had negative active standing (not formal tilt); subclinical POTS might be present in some controls, which would deflate group differences.
7. **GPCR activity present in all controls:** There is no clean healthy-control zero floor; specificity depends on relative elevation, not presence/absence. Optimal cutoffs for diagnostic use have not been established.
8. **Causation not established:** The cross-sectional design cannot distinguish whether GPCR-activating factors cause symptoms vs. are an epiphenomenon of the same process driving POTS. Passive-transfer or antibody-depletion experiments are needed.
9. **No post-infectious POTS subgroup analysis:** Post-infectious onset is mentioned as a known POTS subtype motivating the autoimmune hypothesis, but the cohort is not stratified by trigger; PAIS-specific relevance is inferred rather than directly tested.
10. **ADRA1-symptom severity correlation is modest:** β = 0.77 OHQ points per SD activity in an already high-burden population (mean OHQ 6.36/10); while statistically significant, the explained variance is not reported and the clinical magnitude is uncertain given the restricted range.
11. **Multiple testing not corrected:** P values are unadjusted for multiple comparisons across four receptors × ten OHQ items; the authors acknowledge this and note results should be interpreted accounting for multiplicity, but no Bonferroni or FDR correction is applied.

## Model / Tool Availability

No model, software, or dataset is released. Data available from corresponding author (I. Kharraziha) upon reasonable request. The assay platform (Tango GeneBLAzer, Thermo Fisher Scientific) is a commercial FRET kit; Karolinska University Hospital Center for Apheresis and Stem Cell Handling performed the assays. No public repository or analytical code available.

## Follow-up

**Papers to read next:**
- Gunning WT et al. 2019 (DOI 10.1161/JAHA.119.013602): the binding-ELISA study cited as reference 9 here, which found weak correlations between GPCR antibody levels and orthostatic symptoms using a different methodology — a direct methodological contrast.
- Fedorowski et al. 2017, Europace (ref 7): antiadrenergic autoimmunity in POTS from the same group; establishes ADRA1 partial-antagonist / ADRB1-2 agonist functional model that mechanistically contextualizes the ADRA1-symptom correlation.
- Yu et al. 2018 (ref 8): angiotensin AT1R autoantibodies in POTS from the same Fedorowski/Kem collaboration.
- Stein2025 (already in corpus): beta-2 AR-autoantibody-selected immunoadsorption improves POTS symptoms — represents the interventional arm that would complement this correlational evidence.

**Questions this raises:**
- Does ADRA1-activity severity correlation replicate in a post-infectious POTS subgroup (long COVID onset), versus primary/adolescent POTS onset?
- Does ADRA1 activity correlate with structural small-fiber outcomes (IENFD) in the same patients? (connects to `hypothesis:0007` promotion criterion #1)
- Why does ADRA1 but not ADRB2 track symptom severity? Is the mechanistic model (ADRA1 antagonism → vasoconstriction failure → reflex tachycardia driven through ADRB2 sensitization) testable with this assay by using antagonist pre-treatment controls?
- What is the test-retest reproducibility of the FRET assay within POTS patients over time? Intra-individual stability would determine whether GPCR activity could serve as a treatment-response biomarker.
- Can OPRL1 activity's association with visual and walking symptoms be replicated and mechanistically explained (e.g., nociceptin effects on iris, intraocular pressure)?
