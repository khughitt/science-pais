---
id: paper:Nilforoshan2026
kind: paper
title: 'Revised estimates of the types and durations of long Covid symptoms based on
  claims records from 245 million US patients'
status: active
paper_kind: ""
ontology_terms:
- long COVID
- PASC
- selection bias
- collider bias
- insurance claims
- electronic health records
- test-based prospective design
- negative control outcomes
- synthetic control
- epidemiology methods
dataset_usage: []
source_refs:
- cite:Nilforoshan2026
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a
- hypothesis:0004-acute-severity-threshold
- question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization
- question:0042-is-the-cross-trigger-1020-chronic-fraction-an-artifact-of-shared-case
created: '2026-07-10'
updated: '2026-07-10'
---
# Revised estimates of the types and durations of long Covid symptoms based on claims records from 245 million US patients

- **Authors:** Hamed Nilforoshan, Julia Reisler, Erfan Jahanparast, Michael Moor, Steven N. Goodman, Stefan Wager, Jure Leskovec
- **Year:** 2026
- **Journal:** medRxiv preprint (not peer-reviewed)
- **DOI:** 10.64898/2026.02.17.26346448
- **BibTeX key:** Nilforoshan2026
- **Source:** Full-text PDF (~/d/health/processes/post-acute-infection/papers/pdfs/2026_Nilforoshan_revised-estimates-of-long-covid-symptoms-from-245m-us-patients.pdf), read 2026-07-10. Metadata cross-checked via `science paper-fetch --doi 10.64898/2026.02.17.26346448` (status: ok, source: unpaywall_pdf).

## Key Contribution

Using 14.4 billion health insurance claims from 244.7 million US patients (Komodo Health), this study introduces a **test-based prospective study design** that compares individuals whose first COVID-19 PCR test came back positive to those who tested negative — rather than to untested uninfected controls — thereby correcting the **selective-testing selection bias** that inflates conventional long COVID estimates. The corrected design finds the number of attributable long COVID outcomes to be an order of magnitude smaller than conventional analyses of the same data, and finds that population-level health returns to baseline within approximately one year of infection. The result is the largest empirical quantification to date of the degree to which conventional retrospective EHR/claims designs overstate long COVID burden.

## Methods

**Dataset.** Komodo Health de-identified US health insurance claims database. The Pandemic dataset contains 48,812,613,382 claims from 228,010,550 patients covering all COVID-related encounters; the Control dataset contains 5,759,362,767 claims from 33,749,570 randomly sampled never-COVID-diagnosed patients (who may have received testing or vaccination). Observation window ends April 4, 2023. Restricted to individuals with at least one claim in 2019 (n = 18,084,992 Pandemic; n = 158,213,552 Control). Patients linked longitudinally via a hash of first name, last name (Soundex-coded), gender, and date of birth.

**Test-based prospective design.** Cases are individuals enrolled at the time of their **first COVID-19 PCR test** with a positive result; controls are individuals enrolled at the same moment with a negative result. Enrollment is prospective relative to test outcome — no future information is used to select controls — which eliminates immortal time bias and controls for the fact that all PCR-tested individuals visited a healthcare center with an underlying reason for the visit. This directly addresses the core confound in conventional designs: that COVID-19 cases are all healthcare-visit-triggered, while controls are often randomly sampled from the general population.

**Matching / weighting.** A synthetic control approach re-weights the control group so that its full medical history (longitudinal claims prior to enrollment) matches the COVID-19 case group, further reducing residual confounding and collider bias.

**Outcomes.** 614 health outcomes derived from ICD-10-CM codes aggregated via the Clinical Classification Software Refined (CCSR): 565 plausibly COVID-19-caused and 49 **negative control outcomes** (e.g., firearm injuries, congenital malformations in adults, lightning/drowning events) that COVID-19 could not plausibly cause and are used to empirically benchmark bias.

**Time windows.** Early post-acute: 30–120 days; middle post-acute: 120–360 days; late: 360–720 days.

**Statistical significance threshold.** Risk ratio (RR) ≥ 1.1 with p < 0.05 (two-sided bootstrap, Bonferroni correction for multiple comparisons). This RR ≥ 1.1 threshold means the study may miss small but real effects.

**Bias benchmark.** A parallel conventional analysis on the same dataset (COVID-19 diagnosis vs matched never-diagnosed controls) is run as a head-to-head comparison. False positive rate on negative control outcomes is used as the primary bias metric.

**Sample representativeness.** Supplementary geographic analysis confirms approximate representation across US zip codes; Extended Data Tables show balance on age, race, income, and education.

## Key Findings

**Dramatic reduction in attributable symptom count under the test-based design.**

| Time window | Test-based design | Conventional design |
|---|---|---|
| 30–120 days | 43 outcomes | 262 outcomes |
| 120–360 days | 5 outcomes | 286 outcomes |
| 360–720 days | 0 outcomes | 369 outcomes |

The test-based design attributes 83.5% fewer outcomes at 30–120 days and 98.2% fewer at 120–360 days vs the conventional design on the same data.

**False positive rates on negative control outcomes.**
- Conventional design: 53.1% of 49 negative-control outcomes are falsely detected as significant (RR ≥ 1.1 and p < 0.05; unadjusted for multiple comparisons). For example, it attributes a 76% higher likelihood of lightning/drowning/electrocution injury, and 18.6% higher congenital malformations of the eye/ear/face/neck in adults, to COVID-19 infection.
- Test-based design: 4.1% false positive rate on the same negative-control outcomes. Only mild negative bias (4.1% of negative controls detected as protective, RR ≤ 0.9) remains, estimated at ~10–20% conservative.

**Top attributable outcomes at 30–120 days (test-based, all RR ≥ 1.1 with Bonferroni-corrected p < 0.05).**
Leading by relative risk: myopathy (RR 3.1), pneumonia except TB, respiratory failure/insufficiency/arrest, pneumothorax, shock, hypoxemia, pulmonary embolism, acute pulmonary embolism, postprocedural respiratory complications, cardiogenic shock, viral infection, deep vein thrombosis, shortness of breath, septicemia, pleuritic chest pain, phlebitis/thrombophlebitis, malnutrition (RR 1.20), palpitations (RR 1.21), nonspecific and general chest pain, renal failure, circulatory signs and symptoms, hair loss (RR 1.89), fatigue (RR 1.12). The leading burden (by absolute risk difference) comes from respiratory (pneumonia, respiratory failure, shortness of breath), immune (viral infection, septicemia), and circulatory conditions (chest pain, circulatory symptoms).

**Outcomes persisting to 120–360 days.** Only five outcomes retain RR > 1.1 with Bonferroni-corrected significance: myopathy, hair loss, pulmonary embolism, acute pulmonary embolism, and respiratory failure/insufficiency/arrest. High-baseline-prevalence conditions (pneumonia, shortness of breath, chest pain, fatigue) continue to contribute measurable excess risk difference (public health burden) even with risk ratios between 1.0 and 1.1.

**No attributable outcomes at 360–720 days.** Average population-level health returns to baseline within approximately one year. This contrasts with conventional analyses of the same data finding 369 persistent significant effects. The authors note that symptoms still occurring at >1 year in COVID-19 patients are not demonstrably specific to COVID-19 — they may reflect non-COVID conditions that originally prompted the healthcare visit and PCR test.

**Selection bias mechanism confirmed.** A negative-control-exposure analysis shows that PCR-negative individuals (vs untested matched individuals) themselves have elevated long-term health risk at 360–720 days (82.5% of outcomes with RR ≥ 1.1), and that these elevated risks correlate positively with those attributed to COVID-19 by conventional analysis (Spearman r = 0.48, p < 10⁻⁴). This demonstrates that the shared non-COVID risk factors of tested individuals — not COVID infection itself — drive the conventional design's apparent long-term effects.

**Validation on acute COVID-19 symptoms.** Applying the test-based design to the first 30 days correctly detects established acute COVID-19 symptoms across multiple organ systems (with only one exception: anorexia, which may be coded due to COVID-19 appetite decrease), confirming the design's ability to detect genuine COVID-19 effects when they exist.

**Multi-system character confirmed.** Even under the conservative test-based design, long COVID in the 30–120 day window involves respiratory, cardiovascular, renal, immune, musculoskeletal, gastrointestinal, neurologic, and dermatological systems, confirming the multi-systemic nature of the disease while narrowing its scope compared to prior estimates.

## Relevance

**Strongest connection: hypothesis:0008 (measurement-channel and ascertainment bias predictably shapes apparent PAIS group differences).** This paper is a direct large-scale quantitative demonstration of the core claim of h0008-M2 (ascertainment and scoring inflation). The drop from 53.1% to 4.1% false positive rate on negative controls, achieved purely by changing which control group is used (tested-negative vs never-tested), confirms that *testing selection bias* — one specific form of ascertainment confounding — accounts for a dominant share of long COVID effect estimates in conventional studies. This adds a major new data point to the bounded-exception register: the ascertainment collapse seen here is as large as or larger than any single instance previously catalogued in the h0008 M2 cut.

The paper also demonstrates the negative-control-outcome methodology (the empirical tool described in question:0039) at massive scale: 49 negative controls, 14.4 billion claims. This directly addresses the standing open question about whether healthcare-utilization confounding can be bounded numerically rather than only qualitatively, and provides a concrete answer: yes, and the conventional design's ~50% false positive rate on biologically implausible outcomes is the bound.

**Relevance to hypothesis:0010 (slow recovery gradient, not a stable chronic state).** The population-level return to baseline by one year under the corrected design supports h0010's claim that the "chronic state" in many PAIS studies is a measurement artifact of insufficient follow-up and control-group mismatch. However, the design's RR ≥ 1.1 threshold is conservative: the authors explicitly note that mild effects (RR < 1.1) may persist undetected. The five outcomes persisting to 120–360 days (myopathy, hair loss, pulmonary embolism, acute PE, respiratory failure) are consistent with a true subset of longer-duration effects, consistent with h0010's prediction of trajectory heterogeneity around a population mean that recovers.

**Relevance to hypothesis:0004 (acute severity threshold).** The paper does not stratify results by acute illness severity, so it cannot directly test h0004. However, the 30–120 day outcomes dominated by acute respiratory and cardiovascular sequelae (pneumonia, pulmonary embolism, respiratory failure, shock) are consistent with the view that patients who crossed an acute severity threshold drive the detected signal disproportionately. The population mean returning to baseline by 1 year is also consistent with most patients *not* crossing h0004's threshold into a self-sustaining state.

**Relevance to question:0042 (is the 10–20% chronic fraction an artifact?).** The findings provide substantial methodological support for the view that a large fraction of claimed 2-year PAIS burden is ascertainment artifact: 369 conventional-design associations at 360–720 days collapse to zero under the corrected design on the same data. However, it does not settle whether the residual (missed by RR < 1.1 threshold) chronic fraction is real or artifactual for specific subpopulations.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Test-based prospective design (PCR+ vs PCR−) | Ascertainment-controlled design | Addresses h0008-M2: removes the selective-testing form of ascertainment inflation |
| Negative control outcomes (49 biologically implausible outcomes) | Negative-control-exposure approach | The empirical tool proposed in question:0039; provides the false-positive benchmark |
| Selective testing selection bias | Ascertainment bias / collider bias | The specific mechanism: tested individuals share non-COVID health vulnerabilities |
| RR ≥ 1.1 with Bonferroni correction | Conservative detection threshold | Intentionally conservative; may miss small real effects below RR 1.1 |
| Population-level return to baseline at ~1 year | Slow recovery gradient (h0010) | Compatible with h0010; does not distinguish subgroup heterogeneity |
| Multi-system involvement at 30–120 days | Shared dysregulated attractor (h0001) | Validates multi-system nature under corrected design |
| 10–20% conservative/negative bias | Collider bias from test-negative controls | Test-negative controls may have other conditions → effect estimates conservative |
| Komodo Health claims database | Administrative EHR/claims data type | Billing-coded; advantage is scale; limitation is clinical resolution |

## Limitations

1. **Preprint status.** This paper has not been peer-reviewed as of the summary date (2026-07-10). Results should be treated as preliminary.

2. **Insurance claims data quality.** Claims are billing-coded, not designed for clinical research. Clinical accuracy and granularity are limited; misclassification of outcomes is possible. The study shows it can detect established acute COVID-19 symptoms, providing partial validation.

3. **Cannot capture at-home testers.** Individuals who took only home antigen tests are excluded, biasing toward those with healthcare access and potentially more severe illness. The design cannot be applied to the large fraction of COVID-19 cases identified only by home testing.

4. **Collider bias from test-negative controls.** Patients who test negative at their first PCR test may be seeking care for other serious conditions (e.g., cancer) that produce long-term health effects. This induces mild negative bias estimated at ~10–20%: true long COVID effects are conservatively estimated. The authors acknowledge and measure this but cannot fully eliminate it.

5. **RR ≥ 1.1 threshold.** Effects with RR between 1.0 and 1.1 (potentially including fatigue, cognitive symptoms, and other subjective outcomes) are not detected as significant after Bonferroni correction. Clinically meaningful small-RR population effects may be missed.

6. **Patient linkage via probabilistic hash.** Longitudinal linkage uses a hash of name (Soundex), DOB, and gender — risk of misidentification and improper merging across providers. Robustness checks show results are stable after filtering overlapping patients.

7. **No stratification by acute severity, variant era, vaccination status, or subgroup.** Population-average recovery to baseline by 1 year does not exclude persistent long COVID in severely ill, immunocompromised, or specific demographic subgroups. This is the most important inferential gap: the zero-outcome finding at 360–720 days is a population mean, not a statement about every patient.

8. **Observation window ends April 2023.** Covers predominantly pre-Omicron and early-Omicron waves; effects may differ for later variants or with widespread vaccination.

9. **Claims-level outcomes may not map cleanly to biological phenotypes.** ICD-coded "myopathy" or "fatigue" in claims captures billing events, not validated clinical assessments or objective measurements. The degree to which these codes reflect the mechanistic PAIS phenotypes under study in this project is uncertain.

10. **Control group contamination.** A small minority (<1.1% per month) of PCR-negative controls later tested positive for COVID-19, which would attenuate effect estimates further. This is acknowledged and shown to be small.

## Model / Tool Availability

No model or tool released. Data analysis was performed on the proprietary Komodo Health database; analysis code is not indicated as publicly available in the preprint. [UNVERIFIED: whether code or processed datasets will be shared upon peer review.]

## Follow-up

- **Stratified analysis by acute severity and vaccination status.** The most important gap: do the 360–720 day null results hold for hospitalized, unvaccinated, or immunocompromised subgroups? If a small subgroup (e.g., ~5%) retains attributable effects, it is invisible in the population mean but clinically significant. Relates to hypothesis:0004.
- **Apply test-based design to non-COVID PAIS triggers.** The test-based design relies on PCR testing infrastructure unique to COVID-19 during the pandemic era. How should ascertainment-controlled designs be constructed for EBV, Lyme disease, dengue, Q fever, or post-influenza fatigue, where systematic PCR testing of matched healthcare visitors was not performed? This is now the primary methodological extension question (see new question reserved from this paper).
- **Update question:0039.** This paper provides the most concrete empirical answer yet to the negative-control-outcome design question; the question's Current Evidence section should now cite Nilforoshan2026.
- **Reconcile with clinical cohort studies.** How do these estimates compare to RECOVER, Thaweethai2023, and other prospective clinical cohorts that used different ascertainment methods and found higher long-COVID fractions? A head-to-head design-sensitivity analysis across datasets is needed.
- **Interpretation of 120–360 day persisting outcomes.** The five persisting outcomes (myopathy, hair loss, pulmonary embolism, acute PE, respiratory failure) represent a biologically plausible residual. Follow-up papers examining mechanistic evidence for these specific outcomes (e.g., myopathy as a signature of skeletal muscle injury from hypothesis:0006) would be valuable.
- **Relation to hypothesis:0008 promotion criterion #2.** The paper is not a same-cohort objective re-measurement of a self-report-established difference, so it does not meet criterion #2 for h0008 promotion. But it demonstrates the complementary "whole-design" ascertainment correction, which has different scope and validity.
