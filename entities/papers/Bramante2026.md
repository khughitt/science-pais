---
id: paper:Bramante2026
kind: paper
title: 'Metformin on the Presence of COVID-19 Symptoms 6 Months after Infection: The
  ACTIV-6 Randomized Clinical Trial'
status: active
ontology_terms:
  - metformin
  - post-COVID-19 condition
  - prevention
  - randomized controlled trial
  - outpatient treatment
  - ACTIV-6
  - post-acute sequelae of SARS-CoV-2
  - Bayesian analysis
  - mTOR signaling
dataset_usage: []
datasets: []
source_refs:
- cite:Bramante2026
related:
- topic:therapeutics-and-clinical-trials
- topic:biomarkers-and-objective-endpoints
- topic:antigen-pathogen-persistence
- hypothesis:0004-acute-severity-threshold
- hypothesis:0001-shared-dysregulated-attractor
- question:0012-prevention-vaccination-antiviral-reduces-pais
- question:0002-antigen-clearance-rescues-symptoms
- paper:Bramante2023
created: '2026-06-20'
updated: '2026-06-20'
---
# Metformin on the Presence of COVID-19 Symptoms 6 Months after Infection: The ACTIV-6 Randomized Clinical Trial

- **Authors:** Carolyn T. Bramante, Thomas G. Stewart, David R. Boulware, Matthew W. McCarthy, Yue Gao, Russell L. Rothman, Ahmad Mourad, Florence Thicklin, Jonathan B. Cohen, Idania T. Garcia del Sol, Nirav S. Shah, Manisha Mehta, Orlando Quintero Cardona, Jake Scott, Adit A. Ginde, Mario Castro, Dushyantha Jayaweera, Mark Sulkowski, Nina Gentile, Kathleen McTigue, G. Michael Felker, Sean Collins, Sarah E. Dunsmore, Stacey J. Adam, Christopher J. Lindsell, Adrian F. Hernandez, Susanna Naggie, for the ACTIV-6 Study Group and Investigators
- **Year:** 2026
- **Journal:** Clinical Infectious Diseases
- **DOI:** 10.1093/cid/ciag335
- **BibTeX key:** Bramante2026
- **Source:** Full-text PDF (papers/pdfs/2026_Bramante_metformin-activ6-covid-symptoms-trial.pdf), read 2026-06-20.

## Key Contribution

This phase 3, quadruple-blinded RCT (ACTIV-6 platform) tested whether 14 days of immediate-release metformin given during acute SARS-CoV-2 infection prevents long-COVID symptoms in low-risk outpatient adults, most of whom had prior immunity from vaccination or prior infection. The primary symptom endpoint at 6 months was not met (posterior probability of efficacy [PPE] 0.83, below the pre-specified 0.975 threshold). However, metformin reduced the risk of a clinician-diagnosed long COVID on day 180 by approximately half (RR 0.50, 95% CrI 0.16–0.99; PPE 0.96). This represents a partial replication of the COVID-OUT signal (Bramante2023) — the direction of benefit is consistent, but the primary symptom endpoint did not cross the efficacy bar in this highly immune population, and the magnitude is attenuated compared to COVID-OUT.

## Methods

**Design.** Quadruple-blinded (patients, investigators, outcome assessors, and diagnosing clinicians all masked), randomised, placebo-controlled, decentralised platform trial embedded in the ACTIV-6 platform for repurposed medications in mild-to-moderate outpatient COVID-19. Simple 1:1 randomisation to metformin (500 mg immediate-release) or matched placebo; enrollment did not overlap with other agents on the platform. IRB-approved; independent data and safety monitoring committee.

**Population.** Outpatient adults ≥30 years with confirmed SARS-CoV-2 infection (PCR or home antigen test) and ≥2 COVID-19 symptoms for ≤7 days at consent, enrolled from 90 US sites between September 19, 2023 and May 1, 2024. Exclusion criteria included current hospitalisation for COVID-19, recent use (within 14 days) of metformin, insulin, or sulfonylureas, and known contraindications to metformin. Of 3214 randomised, 231 (7.2%) were administratively excluded (study drug not delivered within 7 days), leaving a modified intention-to-treat (mITT) sample of **2983 participants** (1439 metformin, 1544 placebo).

**Key demographics (mITT).** Median age 47 years (IQR 38–57); 63.4% female; 80.1% White, 11.7% Black, 46.5% Hispanic/Latino; 2% diabetes, 2% hypertension, 38.2% obesity. 68.3% had received ≥2 doses of a SARS-CoV-2 vaccine; 53.5% reported ≥1 prior COVID-19 infection; 83% reported either prior vaccination or prior infection. Enrollment was predominantly during the JN.1 variant wave.

**Intervention.** Metformin immediate-release, titrated over 14 days: 500 mg once daily (day 1), 500 mg twice daily (days 2–5), then 500 mg morning + 1000 mg evening (days 6–14; 36 tablets total). Matching placebo.

**Primary outcome.** Post-acute sequelae of SARS-CoV-2 or death (PASCD) on day 180 — a composite of mortality or any COVID-19 symptoms attributed by the participant to COVID-19 on day 180. Because no deaths occurred, the outcome was shortened to PASC. The pre-specified efficacy threshold was PPE ≥0.975 for the absolute risk difference.

**Secondary outcomes.** PASC on days 90 and 120; clinician-diagnosed long COVID (participant-reported receipt of a provider long-COVID diagnosis) on days 120 and 180; symptom burden (ordinal scale: none/mild/moderate/severe) on days 90, 120, 180.

**Statistical analysis.** Bayesian multivariate model of PASC using a first-order Markov chain across days 90, 120, and 180, with covariate adjustment (age, BMI, sex, symptom duration, prior infection/vaccination, geographic region, calendar date, call center, baseline symptom score). Treatment effect summarised as the absolute risk difference (posterior median) and credible interval; risk ratio from the same model. PPE is the posterior probability that metformin reduces risk (one-sided). Missing data handled via observed data likelihood. Analysis performed in R 4.5 using rstan and rstanarm. Exploratory heterogeneity of treatment effect (HTE) analyses examined age, symptom duration, BMI, baseline severity, calendar time, sex, and vaccination status.

## Key Findings

**Primary outcome — PASC symptoms at day 180.**
- 79 (2.6%) of mITT participants reported COVID-19 symptoms on day 180.
- Metformin group: 33 (2.3%); placebo group: 46 (3.0%).
- Covariate-adjusted absolute risk difference: −0.8 percentage points (95% CrI −2.2 to 0.6).
- PPE: 0.83. **Did not meet the pre-specified efficacy threshold of 0.975.**
- Risk ratio: 0.79 (95% CrI 0.474–1.230).

**Secondary outcomes — PASC at earlier timepoints.**
- Day 90: 96 (3.2%) had symptoms; 44 (3.1%) metformin vs. 51 (3.4%) placebo. Adjusted RD −0.3 pp (95% CrI −1.9 to 1.2); PPE 0.66.
- Day 120: 101 (3.4%); 40 (2.8%) metformin vs. 61 (4.0%) placebo. Adjusted RD −1.1 pp (95% CrI −2.7 to 0.4); PPE 0.93.

**Secondary outcomes — clinician-diagnosed long COVID.**
- Day 120: 29 (0.97%) participants; 13 (0.90%) metformin vs. 16 (1.04%) placebo. RD −0.1 pp (95% CrI −1.0 to 0.7); PPE 0.63; RR 0.879 (95% CrI 0.349–1.632).
- Day 180: **26 (0.87%) participants; 8 (0.56%) metformin vs. 18 (1.17%) placebo.** Adjusted RD −0.7 pp (95% CrI −1.5 to 0.1); **PPE 0.96; RR 0.50 (95% CrI 0.155–0.995).** This is the key secondary result: metformin halved the clinician-diagnosed long COVID rate.

**Heterogeneity of treatment effect.** Exploratory analyses suggest participants without known prior infection may benefit more. Among those with any prior immunity (vaccination or infection): 0.7% metformin vs. 1.6% placebo diagnosed with long COVID by day 180. Among all mITT: 3.2% metformin vs. 4.1% placebo had PASC on day 180 (eTable 6).

**Safety.** No episodes of lactic acidosis. Six participant-reported hypoglycemia episodes (2 metformin, 4 placebo). No deaths.

## Relevance

**Direct replication test for question:0012.** ACTIV-6 is the second phase 3 RCT of metformin for PASC prevention (after COVID-OUT / Bramante2023). The primary symptom endpoint was not met, but the direction of all estimates favours metformin and the clinician-diagnosed long COVID endpoint at day 180 was statistically significant (RR 0.50). This represents a *partial* replication: the signal direction holds, but the effect is attenuated and crosses the efficacy bar only for the secondary clinical-diagnosis endpoint. The attenuation is plausibly explained by a fundamentally different population (low-risk, mostly pre-immune) and a milder variant era (JN.1), not by the absence of a biological effect.

**Comparison with COVID-OUT (Bramante2023).**
- COVID-OUT: high-risk outpatients (overweight/obese), no prior infection permitted, delta/early-omicron era. Primary long-COVID outcome: provider-diagnosed long COVID over 10 months. HR 0.59 (95% CI 0.39–0.89); approximately 41% RRR.
- ACTIV-6: low-to-standard-risk outpatients (no BMI restriction), 83% with prior immunity, JN.1 era. Primary PASC symptom endpoint missed (PPE 0.83); clinician-diagnosed long COVID at 6 months RR 0.50 (PPE 0.96).
- The consistent direction and the significant secondary endpoint support the biological plausibility of the COVID-OUT result. The primary endpoint failure most likely reflects (a) a lower background long-COVID incidence in a pre-immune population and (b) a lower-morbidity variant, leaving less room for an intervention to show a difference, rather than a true null effect.

**Hypothesis 0004 (acute severity threshold).** The attenuation of benefit in a pre-immune, low-morbidity population is consistent with the hypothesis that only participants above an acute-severity threshold enter a PASC attractor. Most ACTIV-6 participants may not have crossed that threshold, limiting the detectable prevention signal.

**Hypothesis 0001 (shared dysregulated attractor).** The partial replication in a lower-risk population supports the view that the acute-phase metformin effect is real but context-dependent: it operates most strongly when acute immunopathology is sufficient to push individuals toward a dysregulated post-acute state.

**Mechanism — mTOR/gut axis.** The discussion highlights SARS-CoV-2 activation of mTOR complex 1, disruption of gut epithelial barrier function, and the correlation between reduced SCFA-producing bacteria and long COVID. Metformin's mTOR inhibition and enhancement of SCFA-producing bacteria are proposed as mechanistic mediators, consistent with the antigen-persistence and microbiome-dysbiosis threads in this project.

**question:0002 (antigen clearance).** If metformin reduces antigen/viral load or curtails the acute mTOR-driven gut permeability that seeds systemic antigen translocation, the mechanism intersects with antigen clearance as a rescue pathway.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| PASC (post-acute sequelae of SARS-CoV-2) | PAIS (post-acute infection syndrome) | Narrow to COVID; same failure-mode framing |
| Clinician-diagnosed long COVID | PAIS clinical phenotype | Provider-label endpoint; heterogeneous ascertainment |
| mTOR activation → gut barrier disruption | Antigen/pathogen persistence mechanism | One proposed pathway from acute to chronic |
| PPE (posterior probability of efficacy) | Bayesian efficacy threshold | Trial-specific; 0.975 pre-specified threshold not met for primary |
| Prior immunity (vaccination + prior infection) | Immune background covariate | Key covariate explaining attenuated effect vs. COVID-OUT |
| JN.1 dominant variant | Variant era covariate | Lower morbidity variant reduces event rate and power |

## Limitations

1. **Primary endpoint not met.** The pre-specified PPE threshold of 0.975 for the primary PASC symptom endpoint was not crossed (PPE 0.83). The trial is formally a negative result for the primary endpoint; the significant secondary endpoint (clinician-diagnosed long COVID) requires cautious interpretation given multiplicity.

2. **Low event rate.** Only 2.6% of participants had PASC symptoms on day 180 and 0.87% received a clinician long-COVID diagnosis — substantially lower than COVID-OUT (8.3% long-COVID incidence). The low event rate reduces statistical power and makes effect estimation highly uncertain even with n ≈ 3000.

3. **Predominantly pre-immune population.** 83% had prior vaccination or infection. This is different from COVID-OUT (no prior infection permitted), and makes the populations non-directly comparable. Benefit in a pre-immune population may genuinely be smaller, or the trial may simply be underpowered for the available event rate.

4. **JN.1 variant era.** The lower morbidity of JN.1 relative to earlier variants reduces the proportion of participants at meaningful risk of PASC, further limiting power.

5. **Symptom ascertainment.** The primary outcome captures symptoms on the day of the follow-up survey only; intermittent symptoms between survey days are missed. This likely underestimates true PASC prevalence and introduces measurement noise.

6. **~20% missing follow-up data.** Approximately 20% of participants did not complete the primary and secondary outcome surveys. Missing data were handled with the observed data likelihood in the Bayesian model, but dropout may correlate with outcome.

7. **Toleration not formally assessed.** Beyond lactic acidosis and hypoglycemia as safety events of interest, tolerability was not systematically collected. COVID-OUT showed the same regimen was well tolerated, providing indirect reassurance.

8. **Single drug; mechanism opacity.** As in COVID-OUT, this design cannot separate AMPK activation, complex-I inhibition, mTOR suppression, anti-inflammatory, or antifibrinolytic mechanisms.

9. **Pre-enrolled long-COVID symptom carryover.** Participants may have had pre-existing PASC symptoms from prior COVID-19 infections before ACTIV-6 enrollment; symptoms on day 90/120/180 attributed to COVID-19 could reflect earlier PAIS rather than the index ACTIV-6 infection.

## Model / Tool Availability

None. Trial registration: ClinicalTrials.gov NCT04885530.

## Follow-up

- **Head-to-head comparison with nirmatrelvir.** Given the antiviral mechanism hypothesis (mTOR suppression reducing viral load), does combining metformin with nirmatrelvir/ritonavir produce additive PASC prevention? The acute antigen-load and metabolic disruption mechanisms are not mutually exclusive.
- **Subgroup: immunologically naive individuals.** The HTE signal suggesting greater benefit in those without prior immunity deserves prospective testing; this would align ACTIV-6 and COVID-OUT by immune background.
- **Variant-stratified meta-analysis.** A pooled or formally meta-analysed comparison of COVID-OUT and ACTIV-6 controlling for variant era, prior immunity, and BMI would sharpen the causal estimate.
- **Dose-response and timing.** COVID-OUT found a stronger effect when metformin was started within 3 days. ACTIV-6 enrolled up to 7 days after symptom onset. A tighter treatment-initiation window analysis is warranted.
- **Mechanism studies.** Biomarker sub-studies (mTOR activation markers, gut microbiome composition, SCFA levels, viral load kinetics) embedded in future trials are needed to distinguish the mTOR/gut hypothesis from the metabolic/AMPK hypothesis.
- **Connects to `question:0012`:** This trial updates the evidence tier from single RCT proof-of-concept (COVID-OUT) to two independent RCTs with consistent direction; the failure to meet the primary threshold strengthens rather than eliminates the signal — it contextualises it to immune background and variant severity.
