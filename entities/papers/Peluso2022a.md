---
id: paper:Peluso2022a
kind: paper
title: "Post-acute sequelae and adaptive immune responses in people with HIV recovering from SARS-CoV-2 infection"
status: active
paper_kind: ""
ontology_terms:
- PASC / long COVID
- HIV
- T cell exhaustion
- PD-1 expression
- adaptive immunity
- immune dysregulation
- post-acute sequelae
- SARS-CoV-2-specific T cells
- inflammation
dataset_usage: []
source_refs:
- cite:Peluso2022a
related:
- hypothesis:0003-immune-exhaustion-feedback
- hypothesis:0004-acute-severity-threshold
created: '2026-07-07'
updated: '2026-07-07'
---
# Post-acute sequelae and adaptive immune responses in people with HIV recovering from SARS-CoV-2 infection

<!--
- **Authors:** Michael J. Peluso, Matthew A. Spinelli, Tyler-Marie Deveau, Carrie A. Forman, Sadie E. Munter, Sujata Mathur, Alex F. Tang, Scott Lu, Sarah A. Goldberg, Mireya I. Arreguin, Rebecca Hoh, Viva Tai, Jessica Y. Chen, Enrique O. Martinez, Brandon C. Yee, Ahmed Chenna, John W. Winslow, Christos J. Petropoulos, Alessandro Sette, Daniella Weiskopf, Nitasha Kumar, Kara L. Lynch, Peter W. Hunt, Matthew S. Durstenfeld, Priscilla Y. Hsue, J. Daniel Kelly, Jeffrey N. Martin, David V. Glidden, Monica Gandhi, Steven G. Deeks, Rachel L. Rutishauser, Timothy J. Henrich
- **Year:** 2022
- **Journal:** AIDS, Vol. 36, No. 12, pp. F7–F16
- **DOI/URL:** https://doi.org/10.1097/QAD.0000000000003338
- **PMID:** 35866847 · **PMCID:** PMC9444925
- **BibTeX key:** Peluso2022a
- **Source:** PDF (medRxiv preprint 2022.02.10.22270471) + published abstract via Europe PMC (AIDS 2022)
- **Disambiguation:** Peluso2022a = this HIV/PASC paper in AIDS (2022); distinct from Peluso2022 = JCI viral-coinfection paper (DOI 10.1172/jci163669).
-->

## Key Contribution

People with HIV (PWH) on suppressive antiretroviral therapy (ART) who recovered from SARS-CoV-2 infection had approximately four-fold higher adjusted odds of post-acute sequelae of SARS-CoV-2 infection (PASC) compared with a well-matched group of HIV-negative individuals (adjusted OR 4.01; 95% CI 1.45–11.1; p=0.008). PWH also showed qualitatively distinct SARS-CoV-2-specific T-cell profiles: markedly lower SARS-CoV-2-specific memory CD8+ T cells and elevated PD-1 expression on SARS-CoV-2-specific CD4+ T cells — a signature consistent with impaired CD8 cytotoxicity and CD4 co-inhibitory upregulation that may reflect an exhausted or dysregulated immune state. This study from the LIINC cohort is the first controlled comparison of PASC prevalence and SARS-CoV-2 adaptive immune responses in PWH vs HIV-negative individuals, establishing HIV as a strong clinical predictor of PASC in this pre-vaccination, pre-Delta cohort.

## Methods

**Cohort and design:** Prospective observational study within the LIINC (Long-term Impact of Infection with Novel Coronavirus) COVID-19 recovery cohort at UCSF (NCT04362150). Participants were enrolled between March and December 2020 (pre-Delta, pre-Omicron variants), all pre-vaccination.

**Population:**
- PWH: n=39 (all who enrolled prior to SARS-CoV-2 vaccination, recruited through two UCSF-based HIV clinics)
- HIV-negative comparators: n=43, randomly selected and matched for age, sex, COVID-19 hospitalization history, and time since infection
- Total N=82
- Acute illness was predominantly outpatient; 13% vs 17% hospitalized (p=0.41, non-significant difference); one participant per group required mechanical ventilation
- The PWH group was predominantly male (reflecting local HIV epidemic demographics) and virally suppressed on ART with strong immune reconstitution

**Assessment timing:** Median 117 days post-infection for PWH (IQR 85–128), 111 days for HIV-negative (IQR 94–131); both approaching a 16-week post-infection target

**PASC definition (primary):** Any COVID-19-attributed symptom (new or worsened since initial infection) present at study visit >6 weeks post-infection, assessed via 32 somatic symptoms from the CDC COVID-19 symptoms list and the Patient Health Questionnaire Somatic Symptom Scale. Stable pre-existing chronic symptoms not counted. Sensitivity analysis: ≥3 symptoms vs. <3 or none.

**Immune assays:**
- Humoral: SARS-CoV-2-specific antibody binding (Pylon/ET Health) and surrogate virus neutralization (sVNT, measures RBD/ACE2 competitive inhibition)
- Cellular: Intracellular cytokine staining (ICS) using SARS-CoV-2 CD4-E and CD8-E epitope megapools (La Jolla Institute); IFNγ production identifies antigen-specific memory T cells; PD-1 expression measured on antigen-specific T cells
- Inflammation: HD-X Simoa platform plasma biomarkers (IL-6, IL-10, TNFα, IP-10/CXCL10, IFNγ, MCP-1) in a subset with available specimens

**Statistics:** Linear regression (humoral and inflammatory markers, log-transformed) and generalized linear models with binomial distribution and bootstrapped standard errors (cellular responses), adjusting for days since infection, age, sex, and COVID-19 hospitalization history. Logistic regression for PASC prevalence by HIV status with the same covariates.

## Key Findings

### PASC prevalence
- **Primary analysis (any PASC symptom >6 weeks):** 82.8% of PWH vs 54.4% of HIV-negative comparators; adjusted OR 4.01 (95% CI: 1.45–11.1; p=0.008), controlling for time since infection, hospitalization, and age. PWH reported a median of 3 symptoms (IQR 1–6) vs. 1 (IQR 0–5; p=0.02) in HIV-negative individuals, and had 1.91-fold higher number of individual PASC symptoms (p=0.02).
- **Sensitivity (≥3 symptoms):** AOR 2.72 (95% CI: 1.08–6.88; p=0.03; 59.8% vs 33.6%).

### SARS-CoV-2-specific T-cell responses
- **CD8+ T cells (memory, IFNγ+):** PWH had 70% lower relative levels of SARS-CoV-2-specific memory CD8+ T cells (0.30-fold; 95% CI: 0.13–0.72; p=0.007; medians: 0.016% vs 0.034% of non-naive CD8+ T cells).
- **CD4+ T cells (overall IFNγ+):** No significant difference in SARS-CoV-2-specific memory CD4+ T cells by HIV status (1.14-fold; 95% CI: 0.76–1.71; p=0.55).
- **PD-1 expression on CD4+ T cells:** Published AIDS paper (Europe PMC abstract) reports 53% higher relative PD-1+ SARS-CoV-2-specific CD4+ T cells in PWH (p=0.007). Note: the preprint version reports a smaller estimate (1.18-fold higher; 95% CI: 1.07–1.30; p=0.001; medians 65% vs 57.1%), suggesting revision between preprint and publication; the published figure (53% / p=0.007) is cited here as the canonical value but the preprint CI is not available for the published estimate [UNVERIFIED: published CI for the CD4+ PD-1 result].
- **PD-1 expression on CD8+ T cells:** Non-significant (1.21-fold; 95% CI: 0.83–1.76; p=0.33).
- **CD4/CD8 ratio effect:** Higher ratio associated with 66% lower PD-1 expression on SARS-CoV-2-specific CD8+ T cells (0.34-fold; 95% CI: 0.13–0.87; p=0.02), suggesting preserved CD4/CD8 ratio — a marker of immune reconstitution on ART — partially mitigates the exhaustion-like phenotype.

### SARS-CoV-2-specific humoral responses
- No significant difference in antibody binding titers (1.31-fold; 95% CI: 0.70–2.46; p=0.40) or surrogate virus neutralization (1.01-fold; 95% CI: 0.63–1.63; p=0.95) by HIV status. Hospitalization predicted higher antibody titers (4.29-fold binding, 2.57-fold neutralization).

### Inflammatory markers (plasma, subset with available samples)
- PWH had elevated baseline inflammatory markers: IL-6 1.55-fold higher (95% CI: 1.06–2.26; p=0.02), IP-10/CXCL10 1.31-fold higher (95% CI: 1.06–1.62; p=0.01), TNFα 1.26-fold higher (95% CI: 1.08–1.47; p=0.003).
- IL-6 and IP-10 levels were associated with PASC across the full cohort (after adjusting for HIV status): OR 1.10 per 10% IL-6 increase (p=0.04) and OR 1.18 per 10% IP-10 increase (p=0.04).

### Immune correlates of PASC
- Antigen-specific antibody and T-cell magnitudes did not correlate with PASC within the cohort.
- Inflammatory markers (IL-6, IP-10) were independently associated with PASC, consistent with residual/ongoing inflammation as a PASC driver.
- PD-1 expression on antigen-specific T cells was not significantly associated with PASC after stratifying by HIV status; the association seen in the full-cohort model was driven by HIV-status group differences in PD-1 expression rather than within-group PASC discrimination.

## Relevance

**Primary relevance to `hypothesis:0003-immune-exhaustion-feedback`:** This paper provides boundary-population evidence for the exhaustion-loop hypothesis. PWH on ART have a pre-existing chronic immune activation and altered T-cell homeostasis (from years of HIV-driven CD4 depletion and reconstitution). Their elevated PD-1 on SARS-CoV-2-specific CD4+ T cells and markedly reduced SARS-CoV-2-specific memory CD8+ T cells — in a setting where humoral immunity is intact — is consistent with impaired cytotoxic clearance and co-inhibitory upregulation. This pattern mirrors the exhaustion signature proposed in h0003, but its association with PASC outcomes here is indirect (the PASC OR is driven by HIV status, not by PD-1 level within the cohort). HIV thus functions as a "loaded-gun" background: the chronic inflammatory state pre-existing from HIV may interact with COVID-19 to lower the threshold or deepen the exhaustion loop.

**Primary relevance to `hypothesis:0004-acute-severity-threshold`:** HIV status predicts PASC in a cohort where acute-illness severity was matched (similar hospitalization rates, p=0.41), suggesting that host immune reserve — specifically, a chronic immunological alteration distinct from acute-severity per se — is an independent determinant of PASC risk. This supports h0004's framing that the threshold for self-sustaining post-infectious illness is modulated by host reserve (CD4/CD8 history, chronic HIV inflammation) rather than being a pure function of acute insult magnitude. The result is consistent with the "immunosuppressed/altered-reserve host paradox" noted in h0004.

**Population-boundary value:** PWH on suppressive ART with strong immune reconstitution are not a general immunosuppression model. They represent a specific profile: chronic innate inflammatory tone (elevated IL-6/TNFα/IP-10), altered CD4/CD8 ratio, prior T-cell exhaustion history from HIV, but intact humoral responses. This makes them a targeted boundary probe: they isolate the T-cell/innate-immune-dysregulation axis from severity, humoral competence, or acute viremia. The four-fold PASC odds elevation in this well-controlled, virologically suppressed group strengthens the case that immune reserve depletion and chronic inflammation per se (not just acute viral load) contribute to PASC risk.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| PASC (any COVID-19-attributed symptom >6 weeks) | PASC/long COVID definition | Broad symptom-based definition; no functional or severity grading |
| HIV on ART, virally suppressed | Host immune reserve depletion (chronic but controlled) | Not a naive immunosuppression model; humoral responses intact |
| Reduced SARS-CoV-2-specific memory CD8+ T cells | Impaired cytotoxic clearance (h0003 exhaustion arm) | 70% lower; may reflect competition with CMV-specific CD8+ pool or genuine SARS-CoV-2-specific deficit |
| Elevated PD-1 on SARS-CoV-2-specific CD4+ T cells | Co-inhibitory exhaustion signature (h0003) | Effect smaller in preprint than published; CD4+ PD-1 not directly predictive of PASC within-group |
| Elevated IL-6, TNFα, IP-10 in PWH | Persistent low-grade inflammatory tone (h0003 activation arm) | Pre-existing HIV-associated; not COVID-specific; but associated with PASC |
| Higher CD4/CD8 ratio → lower PD-1 on CD8+ T cells | Immune reconstitution as protective reserve | Supports host-reserve framing of h0004 |
| HIV status OR 4.01 for PASC | Host immune alteration as PASC risk factor | Independent of acute severity; boundary-population probe |

## Limitations

1. **Small cohort (N=82):** Substantially underpowered for subgroup analyses within PWH (e.g., CD4 nadir, duration of HIV, ART regimen). Wide CI on primary OR (1.45–11.1) reflects this.
2. **Non-representative prevalence:** LIINC recruitment included both self- and clinician-referrals; the 82.8% PASC prevalence in PWH and 54.4% in HIV-negative individuals almost certainly overestimate population-level PASC. The cohort cannot support prevalence claims.
3. **Cross-sectional immune profiling:** A single time-point (~16 weeks post-infection) captures neither the trajectory from acute to chronic nor any causal direction. Elevated PD-1 and low CD8 responses are association findings; it cannot be determined whether they preceded or followed PASC, nor whether they drove or resulted from persistent symptoms.
4. **Matched but not fully randomized:** Groups were matched for key variables, but residual confounding by socioeconomic factors, substance use, comorbid mental health conditions, and concurrent medications (beyond ART) is possible and could not be adjusted for.
5. **Pre-Delta, pre-vaccination cohort (2020):** May not generalize to post-vaccination PASC or Omicron-era infection, where immune dynamics differ substantially.
6. **PWH profile is specific:** Mostly male, virally suppressed with strong immune reconstitution. Not a model for advanced or untreated HIV or for other immunosuppressed populations (e.g., transplant recipients).
7. **PD-1 on CD4+ T cells — preprint vs. published discrepancy:** The preprint reports 1.18-fold higher (18% higher; p=0.001), while the published AIDS abstract reports 53% higher (p=0.007). The revision between preprint and publication changed both the effect estimate and p-value substantially. The CI for the published 53% figure is not available from the abstract alone [UNVERIFIED].
8. **IFNγ ICS assay:** May underestimate total T-cell response (IFNγ is one effector function; cytotoxicity, IL-2, and other readouts not measured).
9. **Inflammatory markers in a subset only:** Simoa plasma protein data not available for all 82 participants; limits power for inflammation-PASC correlations.
10. **PASC definition breadth:** The primary definition (any symptom >6 weeks) is intentionally inclusive/sensitive; higher threshold analysis (≥3 symptoms) confirms direction but shows attenuated effect (AOR 2.72 vs 4.01), suggesting some PASC signal reflects very mild or nonspecific symptoms.

## Model / Tool Availability

This paper does not release a model, tool, or reusable computational artifact. The LIINC cohort (NCT04362150) is an ongoing UCSF cohort; ongoing or future data-sharing terms are not described in this paper.

## Follow-up

- Larger HIV-specific PASC studies are needed (the paper's own call to action); the LIINC cohort has published follow-up work (see `paper:Peluso2024`, `paper:Peluso2024b`, `paper:Peluso2026` for later LIINC publications).
- The CD4/CD8 ratio → PD-1 relationship suggests that earlier ART initiation (preserving CD4/CD8 ratio) may be associated with lower exhaustion markers; longitudinal ART-era comparisons could test this.
- Whether the PASC-associated inflammation (IL-6, IP-10) in PWH precedes PASC chronification or is a consequence remains unresolved — addresses the causal-loop question in `hypothesis:0003`.
- The finding of intact humoral but impaired CD8+ T-cell responses in PWH contrasts with expectations; future work should clarify whether the CD8 deficit reflects CMV-specific CD8+ T-cell pool dilution (as noted by the authors) or a genuine SARS-CoV-2-specific impairment.
- Comparison with other immunomodulated boundary populations (solid-organ transplant recipients, autoimmune patients on biologics) would further test the host-reserve axis of `hypothesis:0004`. The `topic:population-boundary-conditions-and-effect-modifiers-in-pais` topic is the right home for this synthesis.
