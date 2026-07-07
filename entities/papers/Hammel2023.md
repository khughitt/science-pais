---
id: paper:Hammel2023
kind: paper
title: Frailty as a risk factor for post-acute sequelae of COVID-19 among US veterans during the Delta and Omicron waves
status: active
ontology_terms:
- frailty
- VA Frailty Index
- deficit accumulation index
- post-acute sequelae of COVID-19
- PASC
- long COVID
- SARS-CoV-2
- US veterans
- retrospective cohort
- Cox proportional hazards
- vaccination
- Delta variant
- Omicron variant
dataset_usage: []
source_refs:
- cite:Hammel2023
related:
- paper:Cai2024
- paper:ZhangRECOVEREHR2026
created: '2026-07-07'
updated: '2026-07-07'
---
# Frailty as a risk factor for post-acute sequelae of COVID-19 among US veterans during the Delta and Omicron waves

<!--
- **Authors:** Iriana S. Hammel, Dominique M. Tosi, Fei Tang, Henrique Pott, Jorge G. Ruiz
- **Year:** 2023
- **Journal:** Journal of the American Geriatrics Society (JAGS)
- **DOI/URL:** https://doi.org/10.1111/jgs.18584
- **BibTeX key:** Hammel2023
- **Source:** Abstract (Europe PMC via paper-fetch; full text OA but agent-inaccessible — Wiley 403)
-->

## Key Contribution

This retrospective cohort study of 245,857 US veterans demonstrates that pre-existing frailty, measured by the 31-item VA Frailty Index (a deficit-accumulation instrument derived from electronic health records), independently predicts PASC risk within 6 months of SARS-CoV-2 infection. Frail veterans had a 40% increase in PASC risk (aHR 1.40; 95% CI 1.35–1.47) and pre-frail veterans a 17% increase (aHR 1.17; 95% CI 1.11–1.19) relative to robust veterans, after covariate adjustment. This is the cleanest test of the hypothesis that reduced host reserve — not merely acute severity — is an independent predictor of post-acute chronicity, operationalized in a large administrative dataset spanning both the Delta and Omicron waves.

## Methods

**Study design:** Retrospective cohort using the VA COVID-19 Shared Data Resource; enrolled US veterans testing SARS-CoV-2-positive between July 2021 and February 2022 (Delta + Omicron era), without prior positive tests, and surviving 30 days after infection.

**N:** 245,857 veterans. Mean age 57.5 ± 16.5 years; 87.2% male; 68.1% white; 9.0% Hispanic.

**Frailty instrument:** 31-item VA Frailty Index (VA-FI) — a deficit-accumulation index derived from EHR data. Categories: robust (FI ≤ 0.10; 48.9%), pre-frail (FI >0.10 to <0.21; 28.3%), frail (FI ≥ 0.21; 22.7%).

**PASC definition:** [UNVERIFIED] — coded/computable definition from EHR (ICD codes or composite criteria); exact operational definition not specified in the abstract.

**Outcome window:** PASC incidence within 6 months of infection. Median follow-up 143 days (IQR = 101).

**Analysis:** Cox proportional hazards survival model adjusting for covariates. Specific covariates listed in abstract only as "covariates"; whether acute illness severity (e.g., hospitalization, ICU admission, oxygen requirement) was explicitly included as a covariate is [UNVERIFIED] — requires full text to confirm the "independent of severity" claim.

**Vaccination status:** 40.6% fully vaccinated; 13.6% received booster doses prior to infection.

## Key Findings

**Frailty and PASC risk:**
- Frail vs robust: aHR 1.40 (95% CI 1.35–1.47) — 40% increased PASC risk.
- Pre-frail vs robust: aHR 1.17 (95% CI 1.11–1.19) — 17% increased PASC risk.
- 23,890 of 245,857 veterans (9.7%) developed PASC within 6 months.

**Vaccination and PASC risk:**
- Fully vaccinated prior to infection: aHR 0.73 (95% CI 0.71–0.75) — 27% reduction in PASC risk.
- Booster dose prior to infection: aHR 0.66 (95% CI 0.63–0.69) — 34% reduction.

**Wave coverage:** Study period July 2021–February 2022 spans the Delta wave (dominant mid-to-late 2021) and Omicron emergence (late 2021–early 2022). Whether the frailty–PASC association was explicitly tested or reported separately by wave is [UNVERIFIED] — requires full text.

## Relevance

This paper is a primary anchor for `hypothesis:0004-acute-severity-threshold`. The core relevance is in testing whether host reserve — operationalized as frailty — predicts PASC independently of infection itself, which is the essential claim that severity and reserve are separate moderators of chronicity. Three implications for h0004:

1. **Host reserve as an independent predictor of PAIS entry.** The frailty gradient (robust → pre-frail → frail producing a clear dose-response in PASC aHR) directly operationalizes the "threshold position is modulated by host reserve" proposition in h0004's Organizing Conjecture. A lower-reserve host (frail) faces a lower threshold to enter the chronic state.

2. **Critical caveat — severity adjustment is unverified.** The "independent of severity" claim requires that acute illness severity was explicitly controlled in the Cox model. The abstract states covariate adjustment but does not itemize covariates. If hospitalization or acute illness severity was not included, the frailty effect could be partially confounded by frailty's association with more severe acute illness — frail patients are more likely to be hospitalized, and hospitalization independently predicts PASC (Cai2024). This is the single most important full-text verification needed.

3. **Scale correction.** The project's prior characterization of this study as ~3,000 veterans is incorrect — the actual N is 245,857. This makes it one of the largest single-cohort frailty–PASC studies in the literature and substantially strengthens the precision of the aHR estimates.

The vaccination findings (27–34% PASC reduction) are consistent with hypothesis 0004's "prevention/modification evidence" supporting a pre-cross-threshold intervention window, but as with other vaccination studies, the mechanism is mixed (lower infection probability, lower acute severity, altered immune priming).

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| VA Frailty Index (31-item deficit accumulation) | Host reserve / homeostatic margin | Deficit accumulation operationalizes the h0004 "reserve" axis as a composite of accumulated physiological deficits |
| Robust / pre-frail / frail gradient → graded PASC aHR | Threshold position modulated by host reserve | Dose-response in aHR (1.00 → 1.17 → 1.40) is consistent with a threshold that shifts leftward as reserve decreases |
| PASC within 6 months | Failure to return to homeostatic baseline | Short follow-up; does not resolve whether PASC is transient or persistent |
| Vaccination → lower PASC aHR | Pre-infection modification of acute insult | Compatible with reducing insult below threshold, but mechanism-underdetermined |
| VA COVID-19 Shared Data Resource | EHR administrative cohort | Same data resource as Cai2024; enables methodological cross-comparison |
| Delta + Omicron era (July 2021–Feb 2022) | Variant-era generalizability | Contrasts with Cai2024's ancestral-only (2020) cohort; covers attenuated and escape variants |

## Limitations

1. **Severity adjustment unverified.** The most load-bearing claim for hypothesis 0004 — that frailty predicts PASC *independent of acute illness severity* — cannot be confirmed from the abstract. If severity was not included as a covariate, frailty's effect may be partly mediated by hospitalization rates, and the study does not establish independent host-reserve effects. Full-text required to resolve. [UNVERIFIED]

2. **VA cohort demographics.** 87.2% male, predominantly older (mean age 57.5), 68.1% white. Very different from the younger, predominantly female demographics of long-COVID cohorts in population-based studies. Generalizability to women, younger adults, or non-VA settings is uncertain.

3. **Retrospective EHR design.** PASC defined by coded/computable criteria in EHR. Under-coding of mild PASC and care-seeking variation introduce measurement error; more severe and more-engaged patients may be preferentially ascertained.

4. **VA-FI is not Fried frailty phenotype.** The 31-item VA Frailty Index is a deficit-accumulation instrument, not the Fried physical-phenotype battery (grip strength, gait speed, weight loss, exhaustion, activity). These instruments capture overlapping but distinct constructs; VA-FI incorporates comorbidities and medications, meaning the frailty–PASC association may partly reflect disease burden rather than functional reserve per se.

5. **6-month follow-up only.** The outcome window is PASC within 6 months (median follow-up 143 days). This does not capture very-long-term PASC (> 6 months), may miss late-onset sequelae, and does not allow characterization of PASC trajectories (recovery vs persistence).

6. **Wave-stratified analysis unconfirmed.** Whether frailty–PASC associations were separately estimated or tested for heterogeneity by wave (Delta vs Omicron) is [UNVERIFIED]. If the analysis pooled both waves without interaction testing, reported estimates average across two variants with different pathogenicity and immune-escape profiles.

7. **No causal identification.** Observational design; propensity-score or IV approaches to isolate the causal effect of frailty from confounders are not mentioned in the abstract. Residual confounding by unmeasured factors (socioeconomic status, baseline immune function, care access) is possible.

## Model / Tool Availability

No computational model or software tool released. VA data available through the VA Information Resource Center (VIReC) via data use agreement. The 31-item VA Frailty Index algorithm has been described in prior VA frailty literature (Orkaby et al.) and is computable from standard VA EHR variables.

## Follow-up

**Key full-text verification needed (load-bearing for hypothesis 0004):**
- Confirm the exact covariate list in the Cox model — specifically whether hospitalization, ICU admission, or an acute severity score was included. This is the single most important unresolved claim.
- Confirm whether wave-stratified (Delta vs Omicron) analyses were reported.
- Confirm exact PASC operational definition (ICD codes, composite criteria, minimum symptom duration).

**Related papers for cross-reference:**
- Cai2024 — 3-year VA outcomes; same data resource; severity-stratified trajectories; confirms hospitalization as dominant predictor of multi-year burden.
- Orkaby et al. (VA-FI development) — the original VA Frailty Index validation paper; important for interpreting the instrument.
- Fried LP et al. 2001 (JAGS) — original Fried frailty phenotype; the contrasting instrument.

**Questions this raises:**
- Does controlling for frailty attenuate severity-PASC associations in large VA cohorts, or do frailty and severity contribute independently? (The complementary causal analysis to what this paper provides.)
- Does the frailty–PASC gradient replicate in non-VA (general population, female-enriched) cohorts?
