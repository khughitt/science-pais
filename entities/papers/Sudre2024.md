---
id: paper:Sudre2024
kind: paper
title: 'Symptoms before and after COVID-19: a population and case-control study using
  prospective data'
status: active
paper_kind: ""
ontology_terms:
- long COVID
- post-COVID syndrome
- post-COVID-19 condition
- pre-morbid symptoms
- symptom burden
- ascertainment bias
- comorbidity
- ZOE COVID Symptom Study
- community cohort
- case-control study
- survival analysis
- prospective cohort
dataset_usage: []
source_refs:
- cite:Sudre2024
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- hypothesis:0020-host-immune-baseline-reserve-gate
- hypothesis:0004-acute-severity-threshold
- hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0075-pre-covid-symptom-burden-vulnerability-vs
- question:0082-baseline-to-postcovid-symptom-continuity-mechanism
created: '2026-07-10'
updated: '2026-07-10'
---
# Symptoms before and after COVID-19: a population and case-control study using prospective data

<!--
- **Authors:** Carole H. Sudre, Michela Antonelli, Nathan J. Cheetham, Erika Molteni, Liane S. Canas, Vicky Bowyer, Ben Murray, Khaled Rjoob, Marc Modat, Joan Capdevila Pujol, Christina Hu, Jonathan Wolf, Tim D. Spector, Alexander Hammers, Claire J. Steves, Sebastien Ourselin, Emma L. Duncan
- **Year:** 2024
- **Journal:** European Respiratory Journal, 64: 2301853
- **DOI/URL:** https://doi.org/10.1183/13993003.01853-2023
- **PMCID:** PMC11255388
- **BibTeX key:** Sudre2024
- **Source:** PDF
-->

## Key Contribution

This paper establishes that pre-infection (baseline) symptoms and comorbidities predict longer COVID-19
illness duration in a large community cohort, with any baseline symptom doubling the odds of long illness
(OR 2.14, 95% CI 1.78–2.57). However, two-thirds (67.4%) of individuals with long illness were
asymptomatic before SARS-CoV-2, meaning pre-COVID symptom status is a risk modifier — not a prerequisite.
Baseline and post-COVID symptoms correlate closely in long illness, with each additional baseline symptom
increasing post-COVID burden by ~5.6%, suggesting continuity between pre- and post-COVID symptom
experience that may partially reflect comorbidity load, reporting tendency, or shared pathophysiology.

## Methods

**Study design:** Combined population-level survival analysis and 1:1 matched case-control study.

**Data source:** ZOE COVID Symptom Study app (UK). Participants prospectively self-logged symptoms at
least weekly on a smartphone app across the pandemic. The current dataset was cut at 30 May 2022.

**Population cohort (survival analysis):** n=23,452 UK adults with PCR- or LFAT-confirmed,
community-managed SARS-CoV-2 infection (30 December 2020 to 2 March 2022). Logged at least weekly from
≥8 weeks before to ≥12 weeks after COVID-19 onset, with ≥1 week of asymptomatic logging immediately
before infection. Vaccinations occurring in the baseline (4–8 weeks pre-COVID) or post-COVID (8–12 weeks)
periods were excluded to remove vaccination symptom overlap.

**Case-control cohort:** 1350 individuals with long illness (≥56 days / 8 weeks; 906 [67.1%] had illness
≥12 weeks) matched 1:1 to 1350 with short illness (<28 days / 4 weeks), using the Hungarian algorithm to
minimise Euclidean distance on age, sex, BMI, testing week, number of prior SARS-CoV-2 infections,
vaccination number, smoking status, and index of multiple deprivation.

**Baseline period:** 4–8 weeks before COVID-19 onset. **Post-COVID period:** 8–12 weeks after onset.

**Statistical models:**
- Cox proportional hazards for illness duration in full cohort (adjusted for demographics, comorbidities,
  vaccination, smoking, deprivation).
- Conditional logistic regression with three covariate-adjustment models (Model 1: demographics only;
  Model 2: + comorbidities; Model 3: + prior mental health diagnosis) for odds of long illness by baseline
  symptom status.
- Logistic regression for symptom concordance between baseline and post-COVID periods.
- Benjamini–Hochberg false discovery rate adjustment across all tested symptoms.
- Sensitivity: fortnightly (rather than weekly) minimum logging frequency gave equivalent results.

**Key exclusion:** Participants vaccinated during baseline or post-COVID windows (n=8,996) were excluded to
disentangle vaccination side-effects from COVID symptom profiles.

## Key Findings

**Baseline symptom prevalence and illness duration:**
- Reporting any symptom at baseline increased median illness duration from 10 days (IQR 9–12) to 15 days
  (IQR 13–16).
- Five commonest baseline symptoms regardless of illness duration: headache, sore throat, rhinorrhoea,
  fatigue, sneezing — all significantly more prevalent in long vs short illness.

**Case-control: long vs short illness:**
- Baseline symptoms in long illness: 440/1350 (32.6%) vs 255/1350 (18.9%) with short illness (p<0.0001).
- **Two-thirds (67.4%) of individuals with long illness were asymptomatic before COVID-19.**
- Adjusted OR for any baseline symptom predicting long illness: **2.14 (95% CI 1.78–2.57)** (Model 1).
  Remained significant after comorbidity adjustment (Model 2) and mental health adjustment (Model 3).
- Nearly all individual baseline symptoms increased the odds of long illness (Figure 3); exceptions after
  full adjustment: cutaneous symptoms (red welts, blisters, alopecia), rigors, myalgia, dyspnoea, and
  anorexia/low appetite.

**Comorbidities:**
- Long illness more likely to carry comorbidities than short illness: allergic rhinitis (p<0.001),
  asthma/lung disease (p<0.001), heart disease (p=0.044), diabetes (p=0.037), prior mental health
  diagnosis (p=0.003).
- 926/1350 (68.6%) of long illness vs 668/1350 (49.5%) of short illness had ≥1 comorbidity (p<0.001).
- Within long illness, those with ≥1 prior comorbidity showed elevated baseline symptom rate (35.2% vs
  26.9% without comorbidity; p=0.003) and greater post-COVID burden (median IQR 5 (2–9) vs 3 (2–6);
  p<0.0001).

**Demographics of symptomatic long illness individuals:**
- Among long illness individuals, those who were symptomatic at baseline (vs asymptomatic) were more
  likely to be: female (76.4% vs 66.9%, p=0.0004), younger (median 54 vs 59 years, p<0.0001), have
  allergic rhinitis, and have a prior mental health diagnosis.

**Symptom concordance over time:**
- In long illness, individual symptoms present at baseline were more likely to be reported in the
  post-COVID period, for nearly all symptoms — except anosmia/dysosmia, which was *less* likely
  post-COVID if present at baseline (OR 0.75, 95% CI 0.58–0.96).
- Baseline symptom burden predicted post-COVID symptom burden (β=+5.6%, 95% CI 4.4–6.8%, per additional
  baseline symptom; p<0.0001), after adjustment for matching covariates.
- In short illness individuals, fewer post-COVID symptoms were observed, consistent with study design;
  concordance was lower than in long illness.

**Sex differences:**
- Most symptoms were more commonly reported by females than males in both baseline and post-COVID periods,
  across both illness-duration groups. Sex differences appeared least in the post-COVID period among long
  illness individuals. Authors note results are descriptive (no formal interaction test).

**Seasonality:**
- Long illness individuals were less likely to report baseline symptoms in summer (May–September; 280
  [30.8%]/910 vs 97 [22.0%]/440; p=0.002); winter months showed higher baseline symptom prevalence for
  several symptoms including low mood, headache, rhinorrhoea.

## Relevance

**h0008 — Measurement-channel and ascertainment bias:** This paper is a primary data point for M2
(ascertainment inflation) and provides nuanced support. It demonstrates that a substantial fraction
(32.6%) of individuals with long illness already had baseline symptoms before COVID, and that these
individuals are more likely female, younger, and to have prior mental health diagnoses — demographic
features common to self-referred PAIS cohorts. This quantifies the pre-morbid symptom contribution to
apparent long COVID burden. Conversely, the 67.4% asymptomatic majority in long illness constrains the
ascertainment-only reading — most long illness is not simply confounded baseline symptom continuation.
The close baseline-to-post-COVID symptom correlation in long illness is consistent with both reporting
continuity and pathophysiological continuity; the paper cannot distinguish these mechanisms (an explicit
limitation authors note in the Conclusion, flagging Mendelian randomisation as a potentially unbiased
approach).

**h0020 — Host immune baseline reserve gate:** Direct evidence for pre-infection comorbidity burden as
a PAIS risk modifier. Comorbidities (asthma/lung disease, allergic rhinitis, heart disease, diabetes,
prior mental health) are more prevalent in long illness, both raising baseline symptom probability and
independently increasing post-COVID burden. This supports P1 (reduced reserve raises failed-recovery
probability) and P5 (atopic conditions shift phenotype). The paper stops short of mechanistically
separating immune-reserve depletion from symptom-reporting/attribution effects.

**h0004 — Acute severity threshold:** The cohort is exclusively community-managed (mild) COVID-19,
demonstrating that long illness occurs at substantial rates without hospitalisation-level severity. The
finding that 2/3 of long illness were pre-COVID asymptomatic supports the view that host pre-morbid state
is neither necessary nor the only driver of illness duration — consistent with h0004's framing where the
effective threshold is modulated by host reserve but is not equivalent to reserve alone.

**h0011 — Severity-fatigue null:** The community-managed design means the entire cohort reflects mild
acute illness, yet long illness (≥8 weeks) occurs in ~5.8% (1350/23,452). Baseline symptom status acts
as an *additional modifier* of illness duration within a mild-illness population, consistent with h0011's
proposal that severity is one axis but host predisposition axes independently shape chronicity.

**h0005 — Reproductive stage and immune margin:** Among symptomatic long-illness individuals, females are
over-represented (76.4%) and are younger than asymptomatic long-illness individuals. This is consistent
with the project's female-excess framing, though the paper does not analyse menopausal status or
reproductive-stage stratification directly.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Baseline symptom period (4–8 weeks pre-COVID) | Pre-morbid immune/physiological state | Operationally clean window for pre-infection status |
| Long illness (≥8 weeks / ≥56 days) | PAIS / long COVID | Operationally ≥28 days is more standard WHO; here ≥56 days is conservative |
| Short illness (<4 weeks / <28 days) | Recovery within 4 weeks | Lower bound control; excludes the intermediate 28–56 day window (n=2627) |
| Prior comorbidities (atopic, cardiac, mental health) | Baseline reserve depletion (h0020) | Proxies used; no immune reserve measurement |
| Symptom concordance (baseline↔post-COVID) | Reporting continuity vs biological continuity | Cannot be distinguished without objective endpoints |
| App-based self-reported symptoms | Self-report channel (h0008 M1) | All symptom data is self-report; no objective measurement |
| Community-managed COVID-19 | Non-severe / mild acute illness | Excludes hospitalised; constrains severity confounding |

## Limitations

1. **Self-report only:** All symptoms (baseline and post-COVID) are self-reported via a smartphone app;
   no objective measurements, clinical records, or biomarkers. Cannot distinguish reporting-tendency
   continuity from pathophysiological continuity, which is the project's central mechanistic ambiguity.

2. **Healthy-logger bias:** Requirement for ≥1 week of asymptomatic logging immediately before COVID-19
   onset selects for healthier individuals less affected by pre-existing comorbidities, underestimating
   the true relationship between prior symptoms and illness duration.

3. **App-user selection:** ZOE app users are younger, more female, higher educational attainment, and
   over-represent healthcare workers relative to the UK population. Results may not generalise to
   older, less digitally connected, or more comorbid populations. Authors verified that app fatigue
   did not explain results (positive Spearman correlation between symptom duration and app use persistence).

4. **Pre-COVID symptom completeness:** Direct symptom questions were expanded from November 2020; pre-2020
   symptoms used a smaller question set, potentially missing some PCS-relevant baseline symptoms.

5. **Vaccination and antiviral confounding:** Antiviral availability began on the data cut-off date (30
   May 2022), so antiviral effects are excluded by design. Vaccination was controlled by excluding
   individuals vaccinated during baseline/post-COVID windows, but systemic vaccine effects on immune
   set-point remain uncontrolled.

6. **Symptom attribution difficulty:** Clinically distinguishing whether a non-COVID symptom at 8–12
   weeks represents continued COVID illness versus a worsening pre-existing condition is impossible in
   a self-report study — a core limitation for interpretability.

7. **Excluding intermediate-duration illness:** The analytical design drops 2,627 individuals with
   illness 28–56 days, creating an analytical gap in the middle of the duration spectrum.

8. **No mechanistic resolution:** Authors call for Mendelian randomisation studies and genetic studies
   to disentangle association from causation for baseline symptoms and illness duration.

9. **Community-only cohort:** Results are not generalisable to hospitalised individuals, where mechanisms
   underlying illness duration may be qualitatively different.

10. **Single infection per participant by design:** 45 individuals with evidence of repeat infection were
    matched but contributed only one episode; repeat-infection biology is excluded from the analysis.

## Model / Tool Availability

Data from the ZOE COVID Symptom Study app are available to researchers through the UK National Health
Service-funded Health Data Research UK and Secure Anonymised Information Linkage (SAIL) consortium, via
the UK Secure Research Platform (Swansea, UK). Access is through established protocols for public
interest research: https://web.www.healthdatagateway.org/dataset/594cfe55-96e3-45ff-874c-2c0006eeb881.

## Follow-up

**Papers to read next:**
- Ballering 2022 [@Ballering2022] (Dutch Lifelines cohort): prospective pre- vs post-COVID symptoms in 4231 + 8462
  controls — structural comparator to this study; addresses the symptom-attribution limitation by using
  uninfected controls.
- Walitt et al. 2024 [@Walitt2024] (ME/CFS longitudinal study): objective vs subjective dissociation in post-COVID
  — directly tests whether self-report excess in long illness reflects objective deficit.
- Mendelian randomisation studies of long COVID risk factors: would address the baseline-symptom →
  long-COVID directionality question the paper's authors identify.

**Questions this raises for the project:**
- See `question:0075-pre-covid-symptom-burden-vulnerability-vs` (mechanism of the baseline symptom →
  long illness association: comorbidity / immune reserve, reporting tendency, or both).
- See `question:0082-baseline-to-postcovid-symptom-continuity-mechanism` (biological vs behavioural
  continuity explaining baseline-to-post-COVID symptom correlation in long illness).
