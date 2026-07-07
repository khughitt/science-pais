---
id: paper:Vinson2024
kind: paper
title: "The prevalence of postacute sequelae of coronavirus disease 2019 in solid organ
  transplant recipients: Evaluation of risk in the National COVID Cohort Collaborative"
status: active
ontology_terms:
- solid organ transplant
- post-acute sequelae of COVID-19
- PASC
- immunosuppression
- mycophenolate mofetil
- propensity score matching
- N3C
- EHR cohort
- SARS-CoV-2
dataset_usage:
- ref: dataset:n3c-recover-longcovid
  role: analyzed
source_refs:
- cite:Vinson2024
related:
- hypothesis:0004-acute-severity-threshold
- hypothesis:0002-tissue-reservoir-antigen-fragment
created: '2026-07-07'
updated: '2026-07-07'
---

# The prevalence of postacute sequelae of coronavirus disease 2019 in solid organ transplant recipients: Evaluation of risk in the National COVID Cohort Collaborative

<!--
- **Authors:** Vinson AJ, Schissel M, Anzalone AJ, Dai R, French ET, Olex AL,
  Lee SB, Ison M, Mannon RB, and the National COVID Cohort Collaborative
- **Year:** 2024
- **Journal:** American Journal of Transplantation (vol 24, pp 1675-1689)
- **DOI/URL:** https://doi.org/10.1016/j.ajt.2024.06.001
- **PMID:** 38857785 · PMCID: PMC11390303
- **BibTeX key:** Vinson2024
- **Source:** full-text XML via Elsevier text-mining API + PMC

CITEKEY-CORRECTION NOTE (resolved 2026-07-07, t109): this entity was originally
seeded under the citekey `Frontera2024` with corrupt bib identifiers inherited
from an earlier abstract-only placeholder — wrong first author ("Frontera,
Jennifer A.", not in the author list), wrong DOI (10.1111/tid.14365, which
resolves to an unrelated Casias et al. MMR-vaccine case report), wrong journal
(Transplant Infectious Disease), and wrong PMID (39030943, an unrelated
colorectal-cancer-screening paper). Only PMCID PMC11390303 was correct.
Verified against NCBI: the true first author is Amanda J. Vinson, journal
American Journal of Transplantation, DOI 10.1016/j.ajt.2024.06.001, PMID
38857785. The citekey has been renamed Frontera2024 → Vinson2024 and all
cross-references (bib, topic, h0004, q0057) updated.
-->

## Key Contribution

This propensity-score-matched analysis of the N3C EHR database (8,756 solid organ transplant recipients [SOTRs] vs 8,756 non-immunosuppressed controls) found that SOTRs had significantly higher PASC incidence (2.2% vs 1.4%, aOR 1.48, 95% CI 1.09–2.01). Mycophenolate mofetil (MMF) was independently associated with PASC among SOTRs (aOR 2.04, 95% CI 1.38–3.05). The finding is counterintuitive — immunosuppression should dampen immune-dysregulation-driven post-infectious illness — and represents the "SOT PASC paradox" that constrains naive immune-activation models of PAIS pathogenesis.

## Methods

**Data source:** National COVID Cohort Collaborative (N3C), a federated U.S. EHR network. Study period August 1, 2021 – January 13, 2023 (Delta/early Omicron variant era).

**Cohort assembly:** 8,769 SOTRs and 1,576,769 non-immunosuppressed controls (non-ISC) with documented acute COVID-19 before matching. After 1:1 propensity-score matching: 8,756 SOTR–non-ISC pairs (n = 17,512).

**Propensity-score matching:** Exact matching on sex, race/ethnicity, data partner, acute COVID-19 severity tier, vaccination status, and variant period; nearest-neighbor matching on age. This explicitly controls for severity and vaccination status.

**PASC definition (coded diagnosis):** ICD-10-CM codes U09.9 (post-COVID condition) or B94.8 (sequelae of other infectious/parasitic disease), or an OMOP extension diagnosis, or a documented visit to a long COVID specialty clinic; index ≥30 days post-acute infection. This is an *ascertainment-limited coded-diagnosis* phenotype — it captures only diagnosed and coded PASC, which is especially prone to underdiagnosis in SOTRs whose baseline symptom burden masks incident post-acute symptoms.

**Statistical analysis:** Multivariable logistic regression for aOR in the matched cohort, with separate models for SOTRs and non-ISC. Sensitivity analyses addressed variant period, matching on Elixhauser Comorbidity Index, vaccination effects, and time from transplant.

## Key Findings

**PASC incidence (primary):**
- SOTRs: 192 / 8,756 = 2.2%
- Non-ISC controls: 122 / 8,756 = 1.4%
- P < 0.001; aOR for SOT status 1.48 (95% CI 1.09–2.01)

**Other predictors in the overall matched model:**
- Severe vs mild COVID-19: aOR 11.5 (95% CI 4.69–25.6) — the strongest single predictor
- Older age: aOR 1.02 per year (95% CI 1.01–1.03)
- COPD/asthma: aOR 1.43 (95% CI 1.09–1.85)
- Depression: aOR 1.38 (95% CI 1.05–1.82)

**Within-SOTR analysis:**
- Severe COVID-19: aOR 11.6 (95% CI 3.93–30.0)
- Older age: aOR 1.02 per year (95% CI 1.01–1.03)
- **Mycophenolate mofetil:** aOR 2.04 (95% CI 1.38–3.05)
- No other immunosuppressant reached significance in the main within-SOTR model

**Within-non-ISC analysis:**
- Depression: aOR 1.96 (95% CI 1.24–3.07)
- Severe COVID-19: aOR 16.5 (95% CI 2.31–77.6)

**Mechanistic explanations the authors discuss for the SOT PASC paradox:**

1. **Impaired antigen clearance / viral persistence:** Immunosuppression impairs viral clearance, resulting in prolonged SARS-CoV-2 antigen presence that sustains immune activation despite suppression of the downstream effector arm. This is conceptually the most mechanism-specific explanation and aligns with the broader antigen-persistence hypothesis.

2. **Comorbidity burden / host reserve depletion:** SOTRs carry high baseline organ dysfunction, multimorbidity, and symptom burden independent of COVID-19. The accumulated comorbidity depletes the homeostatic reserve available for recovery, making the post-infectious return to baseline harder even after mild acute infection. The authors note that baseline symptom burden may also inflate PASC detection (attribution bias) and complicate the direction of this effect.

3. **Drug-specific antiviral/immunological impairment:** Mycophenolate mofetil (MMF) inhibits inosine monophosphate dehydrogenase (IMPDH), blocking *de novo* purine synthesis in T and B lymphocytes and impairing their proliferative response. MMF independently doubled PASC risk among SOTRs, suggesting that specific agents — rather than "immunosuppression in general" — may impair resolution of post-acute pathology through drug-specific cellular mechanisms. The authors call this an observation requiring further investigation; the direct antiviral mechanism is not established in this dataset.

## Relevance

This paper is load-bearing for `hypothesis:0004-acute-severity-threshold` (acute-severity/host-reserve threshold):

- **Constrains the reserve axis:** The SOT PASC paradox rules out a naive "less immune activation → less post-infectious illness" model. Higher PASC in SOTRs forces the host-reserve construct to be framed as *reserve depletion and/or impaired antigen clearance*, not just as immune activation magnitude. H0004's reserve axis must accommodate scenarios where reduced effector immunity paired with impaired clearance increases chronicity risk.

- **Compatible with threshold frame:** SOTRs' elevated PASC risk is consistent with a severity-conditional reserve-depletion gate — immunosuppression may lower the effective reserve threshold (making it easier to cross into the self-sustaining state) rather than eliminating post-infectious risk.

- **Reinforces antigen persistence (h0002):** The impaired-clearance mechanistic arm is consistent with `hypothesis:0002-tissue-reservoir-antigen-fragment`, which posits that antigen/fragment persistence drives sustained immune activation.

- **Ascertainment considerations for h0004:** Because PASC here is coded ICD-10 diagnosis, the 2.2% vs 1.4% absolute rates are almost certainly underestimates of functional PASC. However, the directional finding (SOT > non-ISC after severity matching) is the key signal for hypothesis constraint; the absolute rates do not anchor the quantitative threshold.

- **Severe COVID remains the dominant predictor:** aOR 11.5 for severe vs mild COVID in the overall model and aOR 11.6 in the SOTR-stratified model — this is consistent with h0004's core claim that acute severity drives post-acute burden, even within the immunosuppressed population.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| SOT PASC paradox (immunosuppression → higher PASC) | host-reserve depletion + impaired clearance | Forces h0004 reserve axis away from activation-magnitude framing |
| Mycophenolate mofetil association | drug-specific antigen clearance impairment | IMPDH inhibition → impaired T/B proliferation → impaired viral resolution |
| Severe COVID aOR 11.5–11.6 | acute-severity threshold (h0004) | Largest single predictor; validates severity-dominant signal in immunosuppressed cohort |
| Coded ICD-10 PASC definition (U09.9/B94.8) | ascertainment-limited PASC phenotype | Coded diagnoses in SOTRs are especially prone to under-detection due to high baseline symptom burden |
| 1:1 propensity-matched N3C EHR design | observational administrative cohort | Adjusted for severity and vaccination; residual confounding by comorbidity burden remains |

## Limitations

- **Ascertainment-limited PASC definition:** ICD-10 coded diagnosis (U09.9, B94.8) reflects only clinician-coded, documented PASC. SOTRs have high baseline symptom burden that likely masks post-COVID symptoms, creating differential misclassification that could either inflate (attribution of pre-existing symptoms to COVID) or deflate (undiagnosed post-COVID symptoms attributed to chronic disease) PASC rates. This is the central limitation for interpreting the 2.2% vs 1.4% absolute rates.

- **Comorbidity confounding:** Despite propensity-score matching on acute severity and vaccination, SOTRs have substantially higher baseline comorbidity. The elevated PASC rate may partly reflect difficulty returning to (lower) baseline health rather than a specific post-COVID mechanism. Sensitivity analyses matching on Elixhauser Comorbidity Index were conducted but could not eliminate this concern entirely.

- **Home testing gap:** Home COVID-19 tests were not captured in N3C, likely inflating mild/asymptomatic cases in the non-ISC arm and potentially shifting apparent severity distributions.

- **No acute treatment data:** Antiviral use (nirmatrelvir/ritonavir, remdesivir) was not examined; differential antiviral use by SOT status could confound both severity and PASC risk.

- **Cross-sectional PASC capture:** The study period ends in January 2023; very long-term follow-up is not assessed.

- **Observational design:** No causal inference possible for the MMF–PASC association; MMF recipients may differ from other SOTR subgroups in ways not fully captured by available covariates.

- **Reproducibility class (N3C):** N3C is a federated enclave dataset requiring DUA and institutional agreement; the underlying data is not publicly downloadable. Results are verifiable only via N3C enclave access.

## Model / Tool Availability

No models or tools released. Data accessed within the N3C enclave (gated; not publicly downloadable).

## Follow-up

- Confirm whether any sensitivity analyses tested the MMF association against specific MMF dose or duration, or whether MMF was a proxy for more recent transplant with more intensive immunosuppression.
- Look for papers examining antiviral treatment (nirmatrelvir, remdesivir) in SOTRs and PASC outcomes — the drug-specific mechanism is incomplete without antiviral data.
- See `hypothesis:0004-acute-severity-threshold` Current Uncertainty for the SOT paradox framing already integrated.
- Cross-reference with Wester2024 and Yotsuyanagi2024 for immunocompromised PAIS comparators if these cover the SOT or HIV-positive subgroup.
