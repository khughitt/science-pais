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

This retrospective cohort study of 245,857 US veterans demonstrates that pre-existing frailty, measured by the 31-item VA Frailty Index (a deficit-accumulation instrument derived from electronic health records), independently predicts PASC risk within 6 months of SARS-CoV-2 infection. Frail veterans had a 40% increase in PASC risk (aHR 1.40; 95% CI 1.35–1.47) and pre-frail veterans a 17% increase (aHR 1.17; 95% CI 1.11–1.19) relative to robust veterans, after covariate adjustment. It operationalizes reduced host reserve in a large administrative dataset spanning both the Delta and Omicron waves. **Important scope limit (t113 full-text resolution, 2026-07-07):** the Cox model did **not** adjust for acute-illness severity (hospitalization/ICU/oxygen), so this is *not* a clean separation of host reserve from acute severity — frailty's effect may be partly mediated by frail patients' greater acute-illness severity (see Methods).

## Methods

**Study design:** Retrospective cohort using the VA COVID-19 Shared Data Resource; enrolled US veterans testing SARS-CoV-2-positive between July 2021 and February 2022 (Delta + Omicron era), without prior positive tests, and surviving 30 days after infection.

**N:** 245,857 veterans. Mean age 57.5 ± 16.5 years; 87.2% male; 68.1% white; 9.0% Hispanic.

**Frailty instrument:** 31-item VA Frailty Index (VA-FI) — a deficit-accumulation index derived from EHR data. Categories: robust (FI ≤ 0.10; 48.9%), pre-frail (FI >0.10 to <0.21; 28.3%), frail (FI ≥ 0.21; 22.7%).

**PASC definition:** [UNVERIFIED] — coded/computable definition from EHR (ICD codes or composite criteria); exact operational definition not specified in the abstract.

**Outcome window:** PASC incidence within 6 months of infection. Median follow-up 143 days (IQR = 101).

**Analysis:** Cox proportional hazards survival model. **Covariate list (resolved via full text, t113, 2026-07-07):** age, gender, race, ethnicity, BMI, smoking status, number of primary-care visits in the prior 24 months (0–5 / 6–11 / ≥12), rurality (urban / city-town / small-town-rural), vaccination status (unvaccinated / fully vaccinated / booster), and infection wave (Delta vs Omicron). **Acute-illness severity — hospitalization, ICU admission, oxygen/ventilation, or a severity score — was NOT among the adjusted covariates.** The "independent of acute severity" reading is therefore **not supported** by this model; the frailty→PASC estimate is unadjusted for the frailty→acute-severity→PASC path (frail patients are more likely to be hospitalized, and hospitalization independently predicts PASC — Cai2024). *Provenance:* the covariate list was read from the Google-indexed Wiley full text surfaced via web search (direct agent PDF access is 402/403-blocked); it is internally consistent with the abstract's vaccination/wave categories but is not a verbatim direct-PDF read — a user browser retrieval could confirm it word-for-word if desired.

**Vaccination status:** 40.6% fully vaccinated; 13.6% received booster doses prior to infection.

## Key Findings

**Frailty and PASC risk:**
- Frail vs robust: aHR 1.40 (95% CI 1.35–1.47) — 40% increased PASC risk.
- Pre-frail vs robust: aHR 1.17 (95% CI 1.11–1.19) — 17% increased PASC risk.
- 23,890 of 245,857 veterans (9.7%) developed PASC within 6 months.

**Vaccination and PASC risk:**
- Fully vaccinated prior to infection: aHR 0.73 (95% CI 0.71–0.75) — 27% reduction in PASC risk.
- Booster dose prior to infection: aHR 0.66 (95% CI 0.63–0.69) — 34% reduction.

**Wave coverage:** Study period July 2021–February 2022 spans the Delta wave (dominant mid-to-late 2021) and Omicron emergence (late 2021–early 2022). Wave was included as a covariate, and the frailty–PASC association was reported to hold across **both** the Delta and Omicron periods (t113, 2026-07-07); a separate formal wave×frailty interaction/heterogeneity test is not reported.

## Relevance

This paper is a primary anchor for `hypothesis:0004-acute-severity-threshold`. The core relevance is in testing whether host reserve — operationalized as frailty — predicts PASC independently of infection itself, which is the essential claim that severity and reserve are separate moderators of chronicity. Three implications for h0004:

1. **Host reserve as an independent predictor of PAIS entry.** The frailty gradient (robust → pre-frail → frail producing a clear dose-response in PASC aHR) directly operationalizes the "threshold position is modulated by host reserve" proposition in h0004's Organizing Conjecture. A lower-reserve host (frail) faces a lower threshold to enter the chronic state.

2. **Resolved caveat — severity was NOT in the adjustment set (t113, 2026-07-07).** The full-text covariate list (see Methods) shows the Cox model adjusted for demographics, BMI, smoking, primary-care-visit count, rurality, vaccination, and wave — but **not** acute-illness severity (hospitalization/ICU/oxygen). The "independent of severity" reading is therefore **not supported**: frailty's effect is partially confounded/mediated by frailty's association with more severe acute illness (frail patients are more likely to be hospitalized, and hospitalization independently predicts PASC — Cai2024). This weakens Hammel2023 as a *clean* reserve-vs-severity separation for h0004, though the graded frailty→PASC dose-response itself is unaffected.

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

1. **Severity was NOT adjusted for (resolved, t113).** The most load-bearing claim for hypothesis 0004 — that frailty predicts PASC *independent of acute illness severity* — is **not supported**: the full-text covariate list contains no acute-severity term (hospitalization/ICU/oxygen). Frailty's effect is thus partly mediated by hospitalization rates, and this study does **not** establish a host-reserve effect independent of acute severity. The frailty→PASC association and its dose-response remain valid; only the "independent of severity" property is retracted.

2. **VA cohort demographics.** 87.2% male, predominantly older (mean age 57.5), 68.1% white. Very different from the younger, predominantly female demographics of long-COVID cohorts in population-based studies. Generalizability to women, younger adults, or non-VA settings is uncertain.

3. **Retrospective EHR design.** PASC defined by coded/computable criteria in EHR. Under-coding of mild PASC and care-seeking variation introduce measurement error; more severe and more-engaged patients may be preferentially ascertained.

4. **VA-FI is not Fried frailty phenotype.** The 31-item VA Frailty Index is a deficit-accumulation instrument, not the Fried physical-phenotype battery (grip strength, gait speed, weight loss, exhaustion, activity). These instruments capture overlapping but distinct constructs; VA-FI incorporates comorbidities and medications, meaning the frailty–PASC association may partly reflect disease burden rather than functional reserve per se.

5. **6-month follow-up only.** The outcome window is PASC within 6 months (median follow-up 143 days). This does not capture very-long-term PASC (> 6 months), may miss late-onset sequelae, and does not allow characterization of PASC trajectories (recovery vs persistence).

6. **No formal wave-heterogeneity test.** Wave (Delta vs Omicron) was included as a model covariate and the frailty–PASC association was reported to hold across both periods (t113), but a separate formal wave×frailty interaction/heterogeneity test is not reported — so any across-wave difference in effect size is not statistically characterized.

7. **No causal identification.** Observational design; propensity-score or IV approaches to isolate the causal effect of frailty from confounders are not mentioned in the abstract. Residual confounding by unmeasured factors (socioeconomic status, baseline immune function, care access) is possible.

## Model / Tool Availability

No computational model or software tool released. VA data available through the VA Information Resource Center (VIReC) via data use agreement. The 31-item VA Frailty Index algorithm has been described in prior VA frailty literature (Orkaby et al.) and is computable from standard VA EHR variables.

## Follow-up

**Full-text verification status (t113, 2026-07-07):**
- ✅ *Resolved:* covariate list obtained — the Cox model did **not** adjust for acute-illness severity (hospitalization/ICU/oxygen). "Independent of severity" retracted. (Provenance: Google-indexed Wiley full text via web search; not a verbatim direct-PDF read.)
- ✅ *Resolved:* frailty–PASC association reported across both Delta and Omicron waves; wave included as a covariate (no separate formal interaction test reported).
- ⬜ *Still open:* exact PASC operational definition (ICD codes, composite criteria, minimum symptom duration) — not surfaced by the abstract or the indexed methods snippet. [UNVERIFIED]

**Related papers for cross-reference:**
- Cai2024 — 3-year VA outcomes; same data resource; severity-stratified trajectories; confirms hospitalization as dominant predictor of multi-year burden.
- Orkaby et al. (VA-FI development) — the original VA Frailty Index validation paper; important for interpreting the instrument.
- Fried LP et al. 2001 (JAGS) — original Fried frailty phenotype; the contrasting instrument.

**Questions this raises:**
- Does controlling for frailty attenuate severity-PASC associations in large VA cohorts, or do frailty and severity contribute independently? (The complementary causal analysis to what this paper provides.)
- Does the frailty–PASC gradient replicate in non-VA (general population, female-enriched) cohorts?
