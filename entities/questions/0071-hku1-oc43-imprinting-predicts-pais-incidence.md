---
id: question:0071-hku1-oc43-imprinting-predicts-pais-incidence
kind: question
title: Does prior HKU1/OC43 seasonal coronavirus exposure predict PAIS incidence via
  immunological imprinting of SARS-CoV-2 responses?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Mak2025
related:
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
- hypothesis:0002-tissue-reservoir-antigen-fragment
created: '2026-07-10'
updated: '2026-07-10'
---

# Does prior HKU1/OC43 seasonal coronavirus exposure predict PAIS incidence via immunological imprinting of SARS-CoV-2 responses?

## Summary

Mak2025 reports that LC patients have significantly elevated IgG against the spike proteins of seasonal betacoronaviruses HKU1 and OC43 — which share ~40% C-terminal S protein sequence identity with SARS-CoV-2 — alongside reduced SARS-CoV-2 S1-specific IgG and IgA and an elevated IgM/IgG ratio consistent with impaired class switching. The authors interpret these as evidence for immunological imprinting (original antigenic sin): prior HKU1/OC43 infection imprints memory B cells to respond to shared (conserved) epitopes when SARS-CoV-2 is encountered, deflecting responses away from SARS-CoV-2-unique S1 epitopes and interfering with class-switch recombination to high-affinity IgG. This question asks whether this imprinting can be detected prospectively (pre-COVID HKU1/OC43 seropositivity / titer) as a predictor of subsequent LC development, and whether the imprinting mechanism is causally upstream of impaired SARS-CoV-2 clearance and PAIS entry.

## Why It Matters

- **Decision:** Whether prior seasonal betacoronavirus exposure should be incorporated into PAIS risk stratification models, and whether boosting SARS-CoV-2-specific (non-imprinted) immunity is a viable prevention strategy.
- **Mechanism gap:** Mak2025 demonstrates the imprinting correlate in established LC but cannot distinguish cause from consequence — impaired SARS-CoV-2 IgG could reflect LC immune dysregulation independently of imprinting history.
- **Therapeutic relevance:** If imprinting by HKU1/OC43 is a causal upstream factor, SARS-CoV-2 vaccines engineered to target S1-unique epitopes could reduce LC risk; the question must be answered to justify such an approach.
- **Risk if unanswered:** The imprinting hypothesis remains an appealing but untested mechanistic story; without prospective evidence it may deflect effort from other drivers of impaired viral clearance.

## Current Evidence

**Supporting:**
- Mak2025 (n = 47 LC, n = 41 HC): elevated HKU1 and OC43 anti-S IgG in LC (p = 0.004 for both); reduced SARS-CoV-2 S1-IgG (p = 0.009); elevated S IgM/IgG ratio (p < 0.0001). Cross-reactive S protein homology between betacoronaviruses and SARS-CoV-2 provides structural plausibility.
- Spatola et al. 2023 (Brain 146:4292): immunological imprinting by prior coronaviruses in neurological LC sequelae.
- Herman et al. 2023 (Sci Transl Med): endemic coronavirus immunity associates with post-acute sequelae in rheumatic disease patients.
- Aguilar-Bretones et al. 2021 (J Clin Invest): seasonal CoV cross-reactive B cells dominate the IgG response in severe acute COVID-19 (n = 70).
- Tortorici et al. 2024 (Immunity): persistent immune imprinting after XBB1.5 booster vaccination confirms imprinting is sustained across re-exposures and vaccine antigens.

**Challenging / absent evidence:**
- No study has measured pre-COVID HKU1/OC43 titers prospectively and linked them to LC incidence; the question is not yet testable with existing published cohorts.
- HC samples in Mak2025 were collected a median 316 days later than LC samples, introducing a differential waning confound that could independently explain some of the between-group antibody differences.
- Elevated HKU1/OC43 IgG in LC could reflect cross-reactive recall boosted by the acute SARS-CoV-2 infection rather than a pre-existing imprint that shaped clearance.

## Thoughts

- **Best current interpretation:** The cross-sectional evidence is consistent with immunological imprinting but remains consistent with alternative explanations (LC-associated immune dysregulation drives elevated cross-reactive B cell recall; sampling-time differences contribute to lower SARS-CoV-2 IgG in LC). A causal role for imprinting in LC etiology is plausible but unconfirmed.
- **Major uncertainty:** Whether the imprinting signal is detectable before SARS-CoV-2 infection and precedes LC development — the necessary temporal ordering to implicate it as a risk factor rather than a consequence.
- **Actionable test:** A prospective cohort with pre-COVID HKU1/OC43 titers and post-infection LC outcomes, or a natural experiment using seroprevalence variation by birth year / exposure history, could adjudicate the causal direction.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (imprinting as a host factor determining attractor entry probability); `hypothesis:0002-tissue-reservoir-antigen-fragment` (impaired IgG → impaired viral clearance → tissue antigen persistence); `hypothesis:0003-immune-exhaustion-feedback` (impaired class switching as B cell counterpart to T cell exhaustion).
- Required data or analyses: Pre-COVID serology linked to LC outcomes; B cell clonotyping from LC vs. recovered patients to identify imprinted cross-reactive clones.
- Priority level: Medium-high — mechanistically novel and potentially actionable for vaccine design, but blocked on prospective cohort data.

## Related

- Topic notes: `topic:long-covid-immune-dysregulation`
- Article notes: `paper:Mak2025`; Spatola et al. 2023 (Brain); Herman et al. 2023 (Sci Transl Med); Aguilar-Bretones et al. 2021 (J Clin Invest)
- Methods/Datasets: Pre-COVID seroprevalence data with longitudinal LC follow-up; single-cell B cell sequencing from LC cohorts
