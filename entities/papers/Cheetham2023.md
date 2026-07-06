---
id: paper:Cheetham2023
kind: paper
title: 'The effects of COVID-19 on cognitive performance in a community-based cohort:
  a COVID symptom study biobank prospective cohort study'
status: active
ontology_terms:
- long COVID
- brain fog
- cognitive impairment
- post-acute sequelae
- working memory
- attention
- post-COVID-19 condition
- prospective cohort
dataset_usage: []
source_refs:
- cite:Cheetham2023
related:
- question:0007-mechanism-of-female-predominance-in-pais
- task:t018
created: '2026-06-22'
updated: '2026-06-22'
---
# The effects of COVID-19 on cognitive performance in a community-based cohort: a COVID symptom study biobank prospective cohort study

- **Authors:** Nathan J. Cheetham, Rose Penfold, Valentina Giunchiglia, Vicky Bowyer, Carole H. Sudre, Liane S. Canas, Jie Deng, Benjamin Murray, Eric Kerfoot, Michela Antonelli, Khaled Rjoob, Erika Molteni, Marc F. Osterdahl, Nicholas R. Harvey, William R. Trender, Michael H. Malim, Katie J. Doores, Peter J. Hellyer, Marc Modat, Alexander Hammers, Sebastien Ourselin, Emma L. Duncan, Adam Hampshire, Claire J. Steves
- **Year:** 2023
- **Journal:** eClinicalMedicine, 62, 102086
- **DOI:** 10.1016/j.eclinm.2023.102086
- **PMID:** 37654669
- **PMCID:** PMC10466229
- **BibTeX key:** Cheetham2023
- **Source:** Europe PMC full text (XML)

## Key Contribution

This prospective, controlled, two-round cohort study (COVID Symptom Study Biobank, UK) provides the strongest controlled-longitudinal evidence to date that SARS-CoV-2 infection causes objective, persistent cognitive accuracy deficits in community-based (non-hospitalised) individuals. The central finding is that deficits track **ongoing symptom status**, not merely past infection: positive individuals who reported full recovery showed no detectable deficit, whereas those with ongoing symptoms — largest for ≥12 weeks duration — showed deficits comparable in magnitude to a 10-year age difference or hospital presentation during acute illness. Deficits persisted without improvement over ~9 months of follow-up (nearly two years post-infection). Sex is treated as a statistical **adjustment covariate** throughout; the study reports no sex-stratified cognitive outcomes and no sex × COVID-status interaction, meaning the objective deficit is not framed as sex-differentiated.

## Methods

- **Design:** Prospective, two-round observational cohort with controls. Round 1: July–August 2021; Round 2: April–June 2022 (~9-month interval).
- **Cohort:** COVID Symptom Study Biobank (CSSB), UK. Volunteers from the ZOE COVID Symptom Study app; CSSB invited five pre-specified groups stratified by SARS-CoV-2 test result and symptom duration as of October–November 2020 / May 2021.
- **Sample sizes:** 3,335 completed Round 1; 2,435 completed Round 2; 1,768 completed both rounds.
- **Cohort composition:** Median age ~57 years (IQR 50–64); 81% female; 96% white ethnicity; skewed toward lower deprivation. Substantially over-represents female sex relative to the UK general population (reflecting CSSB composition).
- **Exposure variable:** Eight-category "COVID-19 group" combining SARS-CoV-2 test result (positive/negative) × symptom duration (asymptomatic / <4 weeks / 4–12 weeks / ≥12 weeks). Symptom duration derived from prospective app logging.
- **Cognitive assessment:** Validated "Cognitron" online battery — 12 tasks assessing working memory, attention, reasoning, motor control. Primary outcome: first principal component of composite accuracy across all tasks (PCA-derived, standardised z-score). Secondary outcomes: reaction time and reaction time variation composites.
- **Statistical approach:** Multivariable ordinary least squares (OLS) regression weighted by inverse probability of participation (to address response bias). Separate models per exposure, each with a DAG-derived minimal adjustment set. Adjustment variables for the main COVID-19 group model: age, BMI, area deprivation, ethnicity, frailty, mental health condition count, physical health condition count, hospital presentation, region, **sex** (covariate, not interaction term). Education added in Round 2 models only (not collected at Round 1).
- **Self-perceived recovery analysis:** 84% (N = 1,455/1,737) of SARS-CoV-2 positive Round 1 participants answered a CSSB survey question ("have you now recovered and are back to normal?") administered shortly before Round 1.
- **Longitudinal analysis:** Models testing Round 2 accuracy ~ COVID-19 group + Round 1 accuracy (as mediator) + covariates, on the 1,768 who completed both rounds. Isolates cognitive *change* between rounds.
- **Case definition used:** NICE guidelines: asymptomatic / acute COVID-19 (<4 weeks) / ongoing symptomatic COVID-19 (4–12 weeks) / post-COVID-19 syndrome (≥12 weeks).

## Key Findings

**Cross-sectional cognitive accuracy (Round 1)**

- SARS-CoV-2 positive vs. negative (controlling for symptom duration): β = −0.14 SDs (95% CI: −0.21, −0.07; adjusted p = 0.00026).
- Positive, ≥12 weeks symptoms vs. negative, asymptomatic reference: β = −0.22 SDs (95% CI: −0.35, −0.09; adjusted p = 0.0045). This is the largest deficit observed.
- Hospital presentation during illness: β = −0.31 SDs (95% CI: −0.44, −0.18; p < 0.0001).
- Age difference 10 years (60–70 vs. 50–60): β = −0.21 SDs (95% CI: −0.30, −0.13). The ≥12-week symptom deficit is comparable in scale to this 10-year age gap.
- Positive, asymptomatic or <4 weeks symptoms: no statistically significant deficit.
- Negative test groups (all symptom durations): no significant deficit.

**Self-perceived recovery stratification**

- SARS-CoV-2 positive individuals who reported full recovery ("yes, back to normal"; N = 769): **no detectable deficit** — ≥12-week symptom subgroup β = +0.05 SDs (95% CI: −0.21, 0.30; adjusted p = 0.86); overall (controlling for duration) β = −0.03 SDs (95% CI: −0.12, 0.05; adjusted p = 0.72).
- SARS-CoV-2 positive individuals who had not recovered ("still have some or all symptoms"; N = 686): deficit increased relative to unstratified sample, β = −0.18 SDs (95% CI: −0.28, −0.08; adjusted p = 0.0032).
- Recovery was highly correlated with symptom duration (Spearman r = −0.83; p < 0.0001). Only 17% (77/455) with ≥12 weeks symptoms had recovered at median 38 weeks post-infection.

**Longitudinal analysis (Round 1 → Round 2, ~9 months)**

- No evidence of cognitive improvement or decline for positive individuals not recovered at Round 1 (93% pre-vaccination). Deficits persisted at nearly two years post-infection (median ~84 weeks, IQR 74–108).
- No detectable change for positive individuals who recovered before Round 1.
- New infections between rounds (post-vaccination, >99% vaccinated): less convincing evidence of cognitive sequelae; infections skewed shorter duration. This was an opportunistic subgroup, not a primary analysis.

**Reaction time**

- No significant effect of SARS-CoV-2 infection on mean reaction time (in contrast to critical care COVID-19 patients). Weak effect on reaction time variation. Accuracy deficit is the primary signal.

**Mediators**

- Presence of ongoing fatigue, psychological distress, and functional impairment at time of testing partially mediated the cognitive deficit, but did not fully account for it. These are downstream correlates of the same underlying state, not alternative explanations.

**Sex in this study**

- Cohort is ~81% female (CSSB over-represents female sex; not population-representative in this dimension).
- Sex is included as a **confounder/adjustment covariate** in all primary regression models. It is not an exposure variable and is not stratified on.
- The paper reports **no sex-stratified cognitive outcomes** and **no sex × COVID-status interaction**. The deficit is reported across the predominantly female cohort without characterising it as female-specific or testing whether effect sizes differ by sex.
- Implication for project: the objective cognitive accuracy deficit does not emerge from the literature as sex-differentiated in this study. The cohort's female-predominance means the deficit is observed predominantly in women, but no claim is made — nor can be made from this paper's analyses — that women carry a larger or different objective deficit than men.

## Relevance

This paper is the strongest single controlled-longitudinal study of **objective** (not self-reported) cognition in long COVID at community level, and is directly load-bearing for several project claims:

1. **Cognitive subphenotype of PAIS is real and persistent.** The PCA-accuracy deficit is detected by an objective validated battery, survives adjustment for age/sex/frailty/education/mental health/deprivation, and persists for nearly two years without change in non-recovered individuals. This anchors the cognitive subphenotype as biologically genuine, not a self-report artifact.

2. **Ongoing symptom status is the key stratifier, not infection history.** The clean dissociation — no deficit in fully recovered individuals regardless of symptom duration, persistent deficit in not-recovered individuals — establishes that the cognitive impairment tracks the *active PAIS state*, not merely COVID-19 history. This is consistent with the project's attractor-state framing: exit from the dysregulated state restores the phenotype; remaining in it does not spontaneously improve.

3. **Link to `question:0007` (sex and cognitive brain fog):** The project needs to distinguish whether the female excess in self-reported "brain fog" in long COVID reflects a genuine sex-differentiated *objective* cognitive deficit or is a self-report / symptom-expression difference. Cheetham2023 provides a critical data point: in a cohort that is ~81% female and uses objective cognitive measurement, the authors make no claim of a sex-specific deficit. Sex is only a covariate. The absence of any sex-stratified analysis or sex × deficit interaction means this paper neither confirms nor refutes a sex difference in objective deficit, but it is notable that no such difference was reported, despite the ideal opportunity (large female-skewed sample with objective measures). This is consistent with the interpretation that the female excess in "brain fog" is a **subjective / self-report phenomenon** rather than an objective sex-differentiated deficit — though confirmation would require an explicit sex-stratified analysis, which Cheetham2023 does not perform.

4. **Link to `task:t018`:** When t018 compares female and reproductive-stage excess across PAIS subphenotypes, the cognitive subphenotype should be coded using Cheetham2023's finding: the objective cognitive deficit tracks ongoing symptom status and severity (not sex), while self-reported brain fog is female-predominant. This dissociation is the critical evidence for distinguishing the objective and subjective cognitive subphenotypes by sex.

5. **Vaccination and temporal context:** The apparent attenuation for post-vaccination infections provides context for how the long-COVID cognitive risk landscape has evolved — relevant for project decisions about which cohorts are most informative for modeling PAIS pathophysiology.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Ongoing-symptom / not-recovered status | Active PAIS state | Recovery from PAIS state = no cognitive deficit; active state = persistent deficit |
| ≥12 weeks symptom duration | Post-COVID-19 syndrome (NICE); PAIS case criterion | Largest objective deficit group; matches PAIS temporal threshold |
| No deficit in fully recovered | Homeostatic recovery restores function | Supports that cognitive impairment is state-dependent, not fixed damage |
| Persistence with no change at ~9 months | Attractor-state stability; absence of spontaneous recovery | Consistent with self-sustaining dysregulated state |
| Sex as confounder (not exposure) | Sex as adjustment covariate | Objective cognitive deficit not characterised as sex-differentiated |
| Partially mediated by fatigue / distress | Symptom co-clustering in PAIS | Cognitive, fatigue, and distress are correlated components of the PAIS state |
| Post-vaccination attenuation | PAIS risk modifiers | Vaccination and later variants reduce ≥4-week symptom rate, reducing PAIS-cognitive risk |

## Limitations

- **No pre-infection cognitive baseline for most participants.** The UK Biobank longitudinal imaging study (Douaud et al. 2022, ref 8 in the paper) had pre/post data; this study does not, making it impossible to distinguish pre-existing differences from infection-caused change in the cross-sectional models. Longitudinal within-person analysis (Round 1 → Round 2) partially addresses this.
- **Female-skewed cohort (~81% female); low ethnic diversity (~96% white).** Limits generalisability. No sex-stratified results reported — a gap, though the study was not powered for sex-interaction tests.
- **Self-report symptom logging for infection status and duration.** Misclassification of COVID-19 group is possible. Some participants may have had COVID-19 before app-based tracking began; symptom duration estimates may be imprecise.
- **Volunteer cohort (CSSB) with differential participation predictors.** Women and older age groups more likely to participate; inverse probability weighting attempts to address this but cannot fully adjust for unmeasured selection factors.
- **No SARS-CoV-2 variant or vaccination history for most Round 1 participants.** Pre-vaccination infections (93% of not-recovered Round 1 participants) dominate the longitudinal analysis; results most applicable to earlier, unvaccinated pandemic.
- **Mediation confounding.** Fatigue, distress, and functional impairment are partial mediators but also correlates of the same underlying state; the causal direction between cognitive deficit and concurrent symptom burden cannot be determined.
- **Online unsupervised testing.** Environmental variation in test conditions may add noise, though prior work showed consistency between supervised and unsupervised Cognitron testing.
- **No data on prior neurovascular/neurodegenerative comorbidities** that could confound cognitive performance.

## Model / Tool Availability

- Analysis code: GitHub, https://github.com/nathan-cheetham/CSSBiobank_CognitiveAssessment (open access).
- CSS Biobank data access: application to CSS Biobank Management Group (https://cssbiobank.com/information-for-researchers); not directly open.
- Anonymised ZOE/CSS app data: Health Data Research UK / SAIL consortium (UK Secure Research Platform): https://web.www.healthdatagateway.org/dataset/fddcb382-3051-4394-8436-b92295f14259.

## Follow-up

- Seek a study explicitly testing sex × COVID-status interaction on objective cognitive performance, or sex-stratified objective cognitive outcomes in long COVID (Cheetham2023 does not provide this; it is a gap).
- Compare with Douaud et al. (2022; UK Biobank pre/post MRI + cognitive data) which has pre-infection baselines — complementary design for ruling out pre-existing differences.
- Compare the magnitude of objective cognitive deficit (β ≈ −0.22 SDs) with effect sizes for sex-stratified self-reported brain fog in large long COVID registries (e.g., RECOVER) to quantify the subjective/objective gap by sex.
- When executing `task:t018` (subphenotype sex-excess comparison), code the cognitive row as: objective deficit tracks ongoing-symptom status (sex not a significant driver per Cheetham2023); self-reported brain fog female-predominant (other sources). Flag the gap — no published sex-interaction analysis of objective cognition in the CSSB or similar large battery study.
- Update `question:0007` evidence section with the Cheetham2023 finding: the study's sex-as-covariate design and absence of sex-stratified results is consistent with (but does not prove) the hypothesis that the female brain-fog excess is a subjective reporting phenomenon. The finding needs a dedicated sex-stratified Cognitron / objective-battery analysis to resolve.
