---
id: "paper:Wang2026c"
type: "paper"
title: "The prevalence of orthostatic intolerance, postural orthostatic tachycardia syndrome and orthostatic hypotension in post-acute sequelae of COVID-19"
status: active
ontology_terms:
  - orthostatic intolerance
  - postural orthostatic tachycardia syndrome
  - orthostatic hypotension
  - dysautonomia
  - post-acute sequelae of COVID-19
  - meta-analysis
  - meta-regression
  - sex differences
source_refs:
  - cite:Wang2026c
related:
  - question:0007-mechanism-of-female-predominance-in-pais
  - task:t018
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
created: "2026-06-22"
updated: "2026-06-22"
---

<!--
- **Authors:** Chunliang Wang, Yuzhu Fan, Chang Li, Bing Chang, Juan Wang, Xu Cao, Guiting Liang, Yan Liang, Kan Sun
- **Year:** 2026 (published online 2026-01-08; journal collection date 2025; DOI 10.3389/fcvm.2025.1679252)
- **Journal:** Frontiers in Cardiovascular Medicine, 12:1679252
- **DOI:** 10.3389/fcvm.2025.1679252
- **PMID:** 41584279
- **PMCID:** PMC12824017
- **BibTeX key:** Wang2026c
- **Source:** PDF (Europe PMC full-text XML)
-->

# The prevalence of orthostatic intolerance, postural orthostatic tachycardia syndrome and orthostatic hypotension in post-acute sequelae of COVID-19

## Key Contribution

This is the first global systematic review and meta-analysis to estimate pooled prevalence of orthostatic intolerance (OI), POTS, and orthostatic hypotension (OH) in PASC using a random-effects GLMM framework (21 observational studies, n = 2,916). Using univariate and multivariable meta-regression, the study shows that **younger age is a significant predictor of higher POTS and OH prevalence** (negative association, P < 0.001 for POTS; P = 0.038 for OH), while **female sex proportion does not predict pooled POTS prevalence** (P = 0.083) **or OH prevalence** (P = 0.959) across cohorts. This dissociates the female skew of PASC-POTS from a sex-amplification mechanism: being female does not increase the probability that a PASC cohort will have more POTS; being younger does.

## Methods

- **Study design:** Systematic review and meta-analysis (PRISMA 2020); PROSPERO CRD42024556546.
- **Databases searched:** PubMed, Embase, CENTRAL (inception through February 1, 2025), supplemented by grey literature (OpenGrey, ProQuest).
- **Inclusion criteria:** Observational studies of PASC patients (symptoms persisting ≥3 months post-SARS-CoV-2) reporting prevalence of OI, POTS, or OH. POTS diagnostic standard: heart rate increase ≥30 bpm in adults (≥40 bpm in children/adolescents) within 10 minutes of upright posture, without classical OH. OH standard: SBP drop ≥20 mmHg or DBP drop ≥10 mmHg within 3 minutes of standing or HUT ≥60°. PASC duration ≥12 weeks.
- **Studies included:** 21 total. OI: 3 studies (n = 1,641). POTS: 15 studies (n = 1,058). OH: 12 studies (n = 689).
- **Cohort characteristics:** Mean age ranged 30.0–58.7 years across studies. Mean post-COVID symptom duration 12–72 weeks. 74.9% female across pooled cohort. Severity mix: 19/21 studies mild acute COVID-19, 1 moderate, 1 severe.
- **Statistical model:** Generalized Linear Mixed Model (GLMM) with random effects; Hartung-Knapp adjustment for CIs; Q-profile methods for tau estimation. Between-study heterogeneity: Cochran's Q and I² statistics.
- **Meta-regression approach:** Univariate and multivariable (adjusted for sex, PASC duration). Covariates: mean age, proportion female, PASC duration, acute-phase severity. Inverse-variance weighted.
- **Sensitivity analysis:** Sequential leave-one-out elimination.
- **Subgroup analyses:** By PASC duration (<52 vs ≥52 weeks) and acute-phase severity (mild vs moderate/severe).
- **Risk of bias:** JBI Critical Appraisal Checklist for prevalence studies (two independent raters).
- **Evidence certainty:** GRADE framework.

## Key Findings

### Pooled prevalence estimates

| Outcome | Studies (n) | Participants | Pooled prevalence (95% CI) | I² |
|---|---|---|---|---|
| Orthostatic intolerance (OI) | 3 | 1,641 | 70.6% (66.8%–74.5%) | 39.4% |
| POTS | 15 | 1,058 | 36.2% (18.6%–53.8%) | 98.2% |
| Orthostatic hypotension (OH) | 12 | 689 | 18.6% (8.6%–28.7%) | 91.3% |

### POTS meta-regression results (the load-bearing finding for this project)

- **Age (univariate):** Advancing age significantly negatively associated with POTS prevalence (P < 0.001; R² = 0.664). Effect persisted in multivariable model adjusted for sex and PASC duration (P = 0.002; R² = 0.667).
- **Female sex proportion (univariate):** Not significantly associated with POTS prevalence (P = 0.083).
- **PASC duration:** Not significantly associated with POTS prevalence (P = 0.875).

### OH meta-regression results

- **Age (univariate):** Advancing age significantly negatively associated with OH prevalence (P = 0.038; R² = 0.364). Persisted in multivariable model (P = 0.011; R² = 0.469).
- **Female sex proportion:** Not significantly associated with OH prevalence (P = 0.959).
- **PASC duration:** Not significantly associated with OH prevalence (P = 0.651).

### Sex-stratified robustness check (discussed in paper)

The authors conducted additional stratified meta-regression grouping cohorts by female-proportion threshold (>50% vs ≤50%) and also implemented inverse-variance weighted meta-regression operationalizing sex as continuous proportion of female participants. Neither approach yielded a significant association between female sex and POTS or autonomic dysfunction incidence.

### Subgroup findings

- **Severity:** POTS prevalence higher in mild (37.8%, 95% CI 19.1%–56.4%) than moderate (15.0%, 95% CI 9%–23%) acute COVID-19. OH shows a similar pattern.
- **PASC duration:** Duration-dependent increase in POTS: 29.1% (<52 weeks) vs 44.1% (≥52 weeks), though multivariate meta-regression found no linear correlation after adjusting for age and sex. Authors hypothesize a non-linear temporal relationship.
- **Sensitivity:** Leave-one-out analysis confirmed POTS estimate stability (range 31%–39%).

### Publication bias

Minimal for OH; evident for POTS (Egger's test asymmetry). GRADE evidence certainty rated low to moderate.

## Relevance

This paper is the **primary meta-analytic evidence** supporting the inference that the female skew in post-COVID POTS reflects POTS's baseline female predominance being carried through to the post-infectious context, not amplified by infection. Specifically:

1. **Female proportion null (P = 0.083 for POTS, P = 0.959 for OH):** Across 15 POTS studies with pooled cohort 74.9% female, the proportion female in a study does not predict how much POTS that study finds. If infection specifically amplified a sex-based vulnerability, we would expect more female-heavy cohorts to show higher POTS rates — they do not.
2. **Younger age IS the predictor (P < 0.001, R² = 0.664):** This aligns with POTS's known epidemiology (predominantly young women) and suggests the post-infectious POTS burden is tracking the baseline POTS susceptibility distribution, not creating a new sex-specific risk amplification.
3. **Connects to question:0007:** This is the strongest quantitative counter-evidence to a "per-infection female amplification" model for PAIS dysautonomia. It supports the position that the female excess in clinical PASC-POTS series reflects referral patterns and the baseline demographics of POTS rather than an infection-specific sex effect. The age-specific vulnerability is the biologically informative signal.
4. **Task t018 (compare female and reproductive excess across triggers):** This meta-regression provides the anchor for the POTS/dysautonomia arm of t018's cross-trigger comparison — female proportion is a null predictor, younger age is a positive predictor, establishing a template for asking whether the same pattern holds in post-dengue and post-Q-fever dysautonomia.
5. **Hypothesis h0005 (reproductive-stage immune-homeostatic margin):** The age-negative association (younger = more POTS) could reflect higher autonomic plasticity/reactivity in younger patients rather than a reproductive-stage immune mechanism per se. The null female result does not support hormonal amplification as a primary mechanism at the population level; age may proxy developmental autonomic set-point rather than estrogen exposure.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Orthostatic intolerance (OI) | Dysautonomia subphenotype | Umbrella term; POTS and OH are subtypes |
| POTS prevalence meta-regression | Dysautonomia: sex-amplification null | Core result for q0007 and t018 |
| Age negative predictor of POTS | Younger-age POTS vulnerability | Consistent with baseline POTS demographics; not a PAIS-specific finding |
| Female proportion null predictor | Sex-carried-through vs sex-amplified distinction | Female predominance is baseline-POTS, not infection-specific amplification |
| PASC case definition (≥3 months, WHO framework) | PAIS case definition heterogeneity | One of multiple case definitions used across the literature |
| Publication bias evident for POTS | Evidence maturity caveat | Funnel plot asymmetry inflates pooled POTS estimates |

## Limitations

1. **All studies are observational and predominantly cross-sectional.** No pre-infection baselines; cannot distinguish pre-existing OI/POTS from post-COVID new onset. Reverse causation is unexcluded — individuals with pre-existing autonomic vulnerability may seek post-COVID care.
2. **Case definition heterogeneity is substantial.** OI assessed by COMPASS-31 (symptom scale) in the three OI studies; POTS and OH assessed by HUT or active standing test but with heterogeneous protocol details. Mixing questionnaire-based OI with objective POTS/OH data inflates within-meta-analysis heterogeneity (I² = 98% for POTS).
3. **Extreme POTS heterogeneity (I² = 98.2%).** The pooled 36.2% estimate carries enormous uncertainty (95% CI 18.6%–53.8%) and should not be cited as a point prevalence; the CI spans the range of estimates in primary studies. The high I² means most variance is between studies, not sampling error.
4. **Female-proportion null is moderately powered.** P = 0.083 for female proportion vs. POTS is not strongly null (marginal significance; R² not reported for the null). With only 15 POTS studies and high heterogeneity, a moderate sex effect could be missed.
5. **Cohort characteristics limit generalizability.** 19/21 studies enrolled mild acute COVID-19 patients — the POTS/OH prevalence estimates cannot be generalized to hospitalized or severe COVID-19 populations. Majority are clinic-based or convenience samples, introducing selection bias.
6. **Variant, vaccination, and reinfection data missing.** No studies provided granular variant-level or vaccination-status data sufficient for subgroup analysis. Given attenuated long COVID risk with Omicron (RR 0.66) and prophylactic vaccination effects, the pooled estimates are likely variant-era confounded.
7. **Self-report instruments in a minority of included studies may overestimate true prevalence** (particularly the OI estimate via COMPASS-31, which captures autonomic symptoms broadly).
8. **GRADE evidence certainty: low to moderate.** The combination of selection bias, heterogeneity, and probable publication bias for POTS yields low confidence in the pooled POTS estimate.
9. **Age–sex confounding not fully resolved.** The meta-regression adjusts for sex and age simultaneously, but with n = 15 studies and high I², the multivariable model may be underpowered to fully disentangle age from sex (POTS predominantly affects young women — both predictors co-vary in the real population).

## Model / Tool Availability

No computational model or tool released. Statistical code referenced (R 4.3.2; `meta` and `metafor` packages). Supplementary tables (S1–S3) and figures (S1–S9) archived with journal.

## Follow-up

- **Directly linked:** question:0007 (female predominance mechanism), task:t018 (cross-trigger sex effect comparison), hypothesis:0005 (reproductive-stage margin).
- **Complementary paper to read:** Yong/Halim et al. (Autonomic Neuroscience 2023, doi:10.1016/j.autneu.2023.103132) is a related meta-analysis reporting POTS RR 2.12 (infected vs uninfected) with age as a meta-regression predictor of pooled POTS rate; it is currently blocked_but_oa and could triangulate the age-but-not-sex finding from the infected-vs-uninfected angle rather than the within-PASC prevalence angle.
- **Gap:** No study in this meta-analysis had pre-infection autonomic baseline measurements. A prospective cohort with pre-infection + post-infection tilt-table data, stratified by age and sex, is needed to establish new-onset POTS attributable fraction vs. pre-existing subclinical POTS unmasked by COVID-19.
- **Methodological gap:** The OI estimate (70.6%) relies on COMPASS-31 symptom scores, not objective testing, and comes from only 3 studies. A meta-analysis restricted to objective tilt-table-confirmed OI would yield a more clinically actionable prevalence.
- **Within-project synthesis needed:** This paper's female-proportion null and age-effect should be added to `interpretation:0002-t013-cross-trigger-sex-effect-sizes` as the dysautonomia-subphenotype anchor point.
