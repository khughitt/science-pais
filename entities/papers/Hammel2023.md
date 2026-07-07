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
- **Source:** Full text PDF (user-provided, `papers/pdfs/2023_Hammel_frailty-risk-factor-pasc-covid19-veterans-delta-omicron.pdf`; OA CC-BY-NC-ND). Upgraded from abstract-only + web-index on 2026-07-07 (t113 full-text pass).
-->

## Key Contribution

This retrospective cohort study of 245,857 US veterans shows that pre-existing frailty, measured by the 31-item VA Frailty Index (a deficit-accumulation instrument derived from electronic health records), predicts *early* (within-6-month) documented PASC risk after SARS-CoV-2 infection. Frail veterans had a 41% increase in PASC risk (aHR 1.41; 95% CI 1.35–1.47) and pre-frail veterans a 15% increase (aHR 1.15; 95% CI 1.11–1.19) relative to robust veterans, after covariate adjustment (values from Table 2 / body text; the abstract's "1.40 / 1.17" are internal typos). It operationalizes reduced host reserve in a large administrative dataset spanning both the Delta and Omicron waves. **Two full-text scope limits (t113 resolution, 2026-07-07, direct PDF read):** (1) the Cox models did **not** adjust for acute-illness severity (hospitalization/ICU/oxygen) — the covariate set captures *predictors of* severe infection, not realized acute severity — so this is *not* a clean separation of host reserve from acute severity; frailty's effect is unadjusted for the frailty→acute-severity→PASC path. (2) Because the proportional-hazards assumption failed over full follow-up, the authors split into two time-stratified Cox models, and frailty was **not** significantly associated with PASC *beyond* 6 months (p=0.21 frail, p=0.13 pre-frail) — the reserve signal is on early documented PASC and attenuates for the durable state that h0004 actually concerns.

## Methods

**Study design:** Retrospective cohort using the VA COVID-19 Shared Data Resource; enrolled US veterans testing SARS-CoV-2-positive between July 2021 and February 2022 (Delta + Omicron era), without prior positive tests, and surviving 30 days after infection.

**N:** 245,857 veterans. Mean age 57.5 ± 16.5 years; 87.2% male; 68.1% white; 9.0% Hispanic.

**Frailty instrument:** 31-item VA Frailty Index (VA-FI) — a deficit-accumulation index derived from EHR data. Categories: robust (FI ≤ 0.10; 48.9%), pre-frail (FI >0.10 to <0.21; 28.3%), frail (FI ≥ 0.21; 22.7%).

**PASC definition (resolved via full text, t113):** primary outcome was a **coded PASC diagnosis** — ICD-10 **U09.9** ("Post COVID-19 condition, unspecified"), **U07.1** ("COVID-19"), **Z86.16** ("Personal history of COVID-19"), and/or **J12.82** ("Pneumonia due to COVID-19"), recorded ≥4 weeks after SARS-CoV-2 infection (CDC-based, ICD-10 computable phenotype). The authors explicitly chose specificity over sensitivity, so this captures a more severely-symptomatic / care-seeking subset and undercounts mild PASC; VHA-external care further undercounts.

**Outcome window:** followed from positive PCR/antigen test until PASC diagnosis or 2022-09-22, whichever first. Median follow-up 143 days (IQR = 101). 80.2% of PASC diagnoses fell within 6 months of infection.

**Analysis:** Cox proportional hazards. The PH assumption **failed** over full follow-up (Schoenfeld residuals, p<0.001), so the association was assessed in **two time-stratified models** (≤6 months and >6 months). **Covariate set (confirmed verbatim from full text, t113, 2026-07-07):** age, gender, race, ethnicity, BMI (multiply imputed), smoking status, number of primary-care visits in the prior 24 months (0–5 / 6–11 / ≥12), rurality (urban / city-town / small-town-rural), vaccination status (unvaccinated / fully vaccinated / booster), and infection wave (Delta vs Omicron) — the paper describes these as "known risk factors for severe infection." **Acute-illness severity — hospitalization, ICU admission, oxygen/ventilation, or a severity score — was NOT among the covariates.** The "independent of acute severity" reading is therefore **not supported**: the model adjusts for *predictors of* severe infection but not *realized* acute severity, so the frailty→PASC estimate is unadjusted for the frailty→acute-severity→PASC path (frail patients are more likely to be hospitalized; hospitalization independently predicts PASC — Cai2024). Frailty×age (p=0.26) and frailty×vaccination interactions were both non-significant. *Provenance note:* originally recovered from a Google-indexed copy under web-index caveat; now **confirmed verbatim** against the user-provided full-text PDF.

**Vaccination status:** 40.6% fully vaccinated; 13.6% received booster doses prior to infection.

## Key Findings

**Frailty and PASC risk (≤6 months):**
- Frail vs robust: aHR 1.41 (95% CI 1.35–1.47) — 41% increased risk.
- Pre-frail vs robust: aHR 1.15 (95% CI 1.11–1.19) — 15% increased risk.
- (The abstract prints "1.40 / 1.17"; Table 2 and the Results text give 1.41 / 1.15 — treat the latter as authoritative.)
- 23,890 of 245,857 veterans (9.7%) developed PASC overall; 19,151 (80.2% of cases) within 6 months.
- Effect was similar in <65 and ≥65 subgroups (frailty×age interaction p=0.26).

**Frailty and PASC risk (>6 months) — NULL:**
- Among the 85,137 still at risk after 6 months, 4739 (5.6%) were newly diagnosed with PASC. After covariate adjustment, frailty was **not** associated with late PASC (frail p=0.21; pre-frail p=0.13). The reserve signal is confined to early documented PASC.

**Wave-specific (Table 2):** frailty effect similar across waves — frail aHR 1.35 (1.26–1.41) Delta, 1.47 (1.39–1.55) Omicron; pre-frail ~1.15 in both. Delta-vs-Omicron PASC HR was 1.61 (1.58–1.67). A formal wave×frailty interaction p-value is not reported.

**Vaccination and PASC risk (≤6 months):**
- Fully vaccinated prior to infection: aHR 0.73 (95% CI 0.71–0.75) — 27% reduction.
- Booster dose prior to infection: aHR 0.66 (95% CI 0.63–0.69) — 33% reduction.
- Vaccination×frailty interaction non-significant (protection similar regardless of frailty). No vaccination–PASC association beyond 6 months.

**Demographics (Table 2):** male aHR 0.90, African-American aHR 0.84 (both lower PASC); Hispanic aHR 1.40 (higher) — consistent with the female-predominance PASC literature (cohort is 87% male, which likely lowers the absolute PASC rate here).

## Relevance

This paper is a *graded frailty→early-PASC* anchor relevant to `hypothesis:0004-acute-severity-threshold`. It bears on whether host reserve — operationalized as frailty — predicts PASC, the h0004 claim that severity and reserve are separate moderators of chronicity. Implications for h0004, with the two full-text caveats front-loaded:

1. **Host reserve predicts early PAIS documentation.** The frailty gradient (robust → pre-frail → frail producing a dose-response in early-PASC aHR: 1.00 → 1.15 → 1.41) operationalizes the "threshold position is modulated by host reserve" proposition in h0004's Organizing Conjecture — a lower-reserve host faces a lower threshold to *enter* the documented post-acute state.

2. **But not the *durable* state — the frailty effect vanishes after 6 months (t113 full-text).** Frailty was not associated with PASC beyond 6 months (p=0.21 frail). h0004 is specifically about entry into a *self-sustaining* chronic state; a reserve signal confined to early documented PASC (and possibly reflecting care-seeking/ascertainment more than durable chronicity) is weaker support for the reserve-threshold gate than an effect that persisted. This aligns with the h0004 reading that reserve is one axis among several, not a durable gate on its own.

3. **Severity was NOT in the adjustment set (t113 full-text, confirmed).** The covariate set (demographics, BMI, smoking, primary-care-visit count, rurality, vaccination, wave — "known risk factors for severe infection") contains **no** realized acute-severity term (hospitalization/ICU/oxygen). The "independent of severity" reading is **not supported**: frailty's effect is unadjusted for the frailty→acute-severity→PASC path (frail patients hospitalize more; hospitalization independently predicts PASC — Cai2024). So this is not a clean reserve-vs-severity separation, though the graded frailty→early-PASC dose-response itself stands.

4. **Scale correction.** The project's prior characterization of this study as ~3,000 veterans is incorrect — the actual N is 245,857. This makes it one of the largest single-cohort frailty–PASC studies in the literature and substantially strengthens the precision of the aHR estimates.

3. **Scale correction.** The project's prior characterization of this study as ~3,000 veterans is incorrect — the actual N is 245,857. This makes it one of the largest single-cohort frailty–PASC studies in the literature and substantially strengthens the precision of the aHR estimates.

The vaccination findings (27–34% PASC reduction) are consistent with hypothesis 0004's "prevention/modification evidence" supporting a pre-cross-threshold intervention window, but as with other vaccination studies, the mechanism is mixed (lower infection probability, lower acute severity, altered immune priming).

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| VA Frailty Index (31-item deficit accumulation) | Host reserve / homeostatic margin | Deficit accumulation operationalizes the h0004 "reserve" axis as a composite of accumulated physiological deficits |
| Robust / pre-frail / frail gradient → graded PASC aHR | Threshold position modulated by host reserve | Dose-response in aHR (1.00 → 1.15 → 1.41) is consistent with a threshold that shifts leftward as reserve decreases — but only for ≤6-month PASC |
| Frailty effect present ≤6 mo, absent >6 mo | Failure to return to homeostatic baseline | The reserve signal does *not* persist to the durable state h0004 concerns; may reflect early ascertainment more than durable chronicity |
| Vaccination → lower PASC aHR | Pre-infection modification of acute insult | Compatible with reducing insult below threshold, but mechanism-underdetermined |
| VA COVID-19 Shared Data Resource | EHR administrative cohort | Same data resource as Cai2024; enables methodological cross-comparison |
| Delta + Omicron era (July 2021–Feb 2022) | Variant-era generalizability | Contrasts with Cai2024's ancestral-only (2020) cohort; covers attenuated and escape variants |

## Limitations

1. **Severity was NOT adjusted for (resolved, t113).** The most load-bearing claim for hypothesis 0004 — that frailty predicts PASC *independent of acute illness severity* — is **not supported**: the full-text covariate list contains no acute-severity term (hospitalization/ICU/oxygen). Frailty's effect is thus partly mediated by hospitalization rates, and this study does **not** establish a host-reserve effect independent of acute severity. The frailty→PASC association and its dose-response remain valid; only the "independent of severity" property is retracted.

2. **VA cohort demographics.** 87.2% male, predominantly older (mean age 57.5), 68.1% white. Very different from the younger, predominantly female demographics of long-COVID cohorts in population-based studies. Generalizability to women, younger adults, or non-VA settings is uncertain.

3. **Retrospective EHR design.** PASC defined by coded/computable criteria in EHR. Under-coding of mild PASC and care-seeking variation introduce measurement error; more severe and more-engaged patients may be preferentially ascertained.

4. **VA-FI is not Fried frailty phenotype.** The 31-item VA Frailty Index is a deficit-accumulation instrument, not the Fried physical-phenotype battery (grip strength, gait speed, weight loss, exhaustion, activity). These instruments capture overlapping but distinct constructs; VA-FI incorporates comorbidities and medications, meaning the frailty–PASC association may partly reflect disease burden rather than functional reserve per se.

5. **Frailty effect does not persist past 6 months.** The authors did analyze >6-month PASC (in a separate Cox model, forced by a PH-assumption violation) and found frailty was **not** significantly associated (p=0.21 frail, p=0.13 pre-frail). The reported frailty→PASC signal is therefore specific to early (≤6-month) documented PASC; the study cannot support a frailty effect on durable/late PASC, and the authors attribute the attenuation partly to the drop in PASC documentation after ~6 months and the non-hospitalized-predominant sample.

6. **No formal wave-heterogeneity test.** Wave (Delta vs Omicron) was a model covariate and wave-stratified estimates are reported (frail 1.35 Delta / 1.47 Omicron), but no formal wave×frailty interaction p-value is given (unlike the age and vaccination interactions, which were tested) — so the apparent across-wave difference is not statistically characterized.

7. **No causal identification.** Observational design; no propensity-score/IV approach to isolate the causal effect of frailty. Residual confounding by unmeasured factors (socioeconomic status, baseline immune function, care access) — and, critically, by unadjusted acute severity (Limitation 1) — is possible.

8. **Internal inconsistencies in the paper.** The abstract prints aHRs (1.40/1.17) that disagree with Table 2 and the Results text (1.41/1.15); the Discussion states a frailty cutoff of ">0.25" whereas Methods and Table 1 use FI ≥0.21; and the Table 2 footnote labels the models "multivariable logistic regression" though the Methods specify Cox proportional hazards. None change the conclusions, but the Table 2 / Methods values are treated as authoritative here.

## Model / Tool Availability

No computational model or software tool released. VA data available through the VA Information Resource Center (VIReC) via data use agreement. The 31-item VA Frailty Index algorithm has been described in prior VA frailty literature (Orkaby et al.) and is computable from standard VA EHR variables.

## Follow-up

**Full-text verification status (t113, closed 2026-07-07 — direct PDF read of user-provided full text):**
- ✅ *Resolved & confirmed:* covariate list — the Cox models did **not** adjust for acute-illness severity (hospitalization/ICU/oxygen). "Independent of severity" retracted. (Now verbatim from the PDF, superseding the earlier web-index provenance.)
- ✅ *Resolved:* frailty–PASC across both waves (frail 1.35 Delta / 1.47 Omicron); wave a covariate; no formal wave×frailty interaction p-value.
- ✅ *Resolved:* PASC operational definition — CDC-based ICD-10 codes (U09.9 / U07.1 / Z86.16 / J12.82), ≥4 weeks post-infection, specificity-over-sensitivity computable phenotype.
- ✅ *New (not previously flagged):* frailty effect is confined to ≤6 months; the authors' own >6-month model found **no** frailty association (p=0.21). Propagated to h0004 as a durability caveat.
- All `[UNVERIFIED]` markers on this entity are now cleared.

**Related papers for cross-reference:**
- Cai2024 — 3-year VA outcomes; same data resource; severity-stratified trajectories; confirms hospitalization as dominant predictor of multi-year burden.
- Orkaby et al. (VA-FI development) — the original VA Frailty Index validation paper; important for interpreting the instrument.
- Fried LP et al. 2001 (JAGS) — original Fried frailty phenotype; the contrasting instrument.

**Questions this raises:**
- Does controlling for frailty attenuate severity-PASC associations in large VA cohorts, or do frailty and severity contribute independently? (The complementary causal analysis to what this paper provides.)
- Does the frailty–PASC gradient replicate in non-VA (general population, female-enriched) cohorts?
