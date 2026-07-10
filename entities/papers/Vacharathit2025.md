---
id: "paper:Vacharathit2025"
kind: "paper"
title: "Persistent IP-10/CXCL10 dysregulation following mild Omicron breakthrough infection: Immune network signatures across COVID-19 waves and implications for mRNA vaccine outcomes"
status: "active"
paper_kind: ""
ontology_terms:
- CXCL10
- IP-10
- long COVID
- SARS-CoV-2
- cytokine dysregulation
- hybrid immunity
- breakthrough infection
- mRNA vaccine
dataset_usage: []
source_refs:
- cite:Vacharathit2025
related:
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
- hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver
- hypothesis:0020-host-immune-baseline-reserve-gate
created: "2026-07-10"
updated: "2026-07-10"
Source: PDF
---

# Persistent IP-10/CXCL10 dysregulation following mild Omicron breakthrough infection: Immune network signatures across COVID-19 waves and implications for mRNA vaccine outcomes

<!--
- **Authors:** Vimvara Vacharathit, Mutita Pluempreecha, Suwimon Manopwisedjaroen, Chanya Srisaowakarn, Sirawat Srichatrapimuk, Paskorn Sritipsukho, Naiyana Sritipsukho, Arunee Thitithanyanont
- **Year:** 2025
- **Journal:** Clinical Immunology 278 (2025) 110507
- **DOI:** https://doi.org/10.1016/j.clim.2025.110507
- **BibTeX key:** Vacharathit2025
- **Source:** PDF
-->

## Key Contribution

IP-10/CXCL10 remains persistently elevated — 7–10× above pre-pandemic controls — in vaccinated individuals with mild Omicron breakthrough COVID-19 for up to 6–8 months post-infection, a pattern not observed after earlier SARS-CoV-2 variant waves (Wuhan, D614G, Alpha, Delta), where IP-10 returned toward baseline by the same timepoints. This sustained chemokine elevation occurs in the absence of statistical correlation with Long COVID symptom scores in this cohort, but mRNA-inclusive vaccination regimens were independently associated with significantly lower Long COVID scores at 3–4 months post-infection. Additionally, elevated anti-CoV-229E antibody titers at convalescence correlated positively with Long COVID symptom severity, suggesting individual-level immune dysregulation as a marker, not a direct cause, of prolonged sequelae.

## Methods

**Cohort:** 114 mild symptomatic COVID-19 patients diagnosed by nasopharyngeal RT-PCR at three Thai hospitals (Chakri Naruebodindra Medical Institute, Ramathibodi Hospital, Thammasat University Hospital), enrolled from multiple pandemic waves: Wuhan (n=25), D614G (n=28), Alpha (n=11), Delta (n=20), Omicron (n=30). Two control groups: pre-pandemic healthy donors (before December 2019, no known SARS-CoV-2 exposure) and RT-PCR-negative controls (tested negative despite reported exposure or mild symptoms during the Omicron wave).

**Longitudinal design:** Serum collected at three timepoints post-infection onset — T1 (2–4 weeks), T2 (3–4 months), T3 (6–8 months).

**Cytokine multiplex:** 20-plex Luminex panel (Milliplex Human Cytokine/Chemokine/Growth Factor Panel A, HCYTA-60 K; Merck Millipore) measuring G-CSF, IFN-α2, IFN-γ, IL-1β, IL-2, IL-6, IL-7, IL-8, IL-9, IL-12p70, IL-17A, IL-22, IP-10, MCP-1, MIP-1α, MIP-1β, PDGF-AA, TNF-α, VEGF-A in duplicates. Viral inactivation by Triton X-100 at BSL-3 prior to assay.

**Antibody multiplex:** 13-plex ProcartaPlex total coronavirus immunoglobulin panel (PPX-13-MXT2AVE; Thermo Fisher Scientific) detecting total Ig against SARS-CoV-2 Spike (trimer), S1, RBD, Nucleocapsid; four VOC Spikes (Alpha, Beta, Gamma, Delta); and four seasonal coronaviruses (CoV-NL63, CoV-HKU1, CoV-229E, CoV-OC43). Separate 6-plex neutralizing antibody panel (EPX060-16018-901; Thermo Fisher Scientific) against five SARS-CoV-2 variants (WT, Alpha, Beta, Gamma, Delta). Live-virus microneutralization against Omicron BA.2, BA.5, and BM1.1 sub-variants.

**Cytokine network analysis:** Graphia (v5.1) Spearman absolute correlation |r| > 0.8 threshold; Markov clustering; network density = 2E / N(N-1).

**Long COVID scoring (Omicron cohort only):** Telephone-interview-administered validated questionnaire at T2 and T3 per WHO clinical definitions (age ≥ 18 years, RT-PCR-confirmed). Long COVID score composite derived from symptom frequency responses.

**Statistical analysis:** GraphPad Prism 9.0 and Python (pandas 1.5.0, seaborn 0.12.0, statsmodels 0.13.2); repeated-measures ANOVA with Tukey's HSD post-hoc; Spearman correlations; linear regression controlling for age and sex; Jaccard similarity coefficients for cross-wave cytokine network overlap.

**Vaccination:** Thai multi-platform rollout captured as-observed; Omicron cohort averaged 3.3 vaccine doses per participant with 19 distinct vaccination permutation regimens. Most common regimen: 2× ChAdOx1 (Oxford-AstraZeneca) + 1× BNT162b2 (Pfizer-BioNTech) (20% of cohort).

## Key Findings

### 1. Persistent IP-10/CXCL10 elevation uniquely characterizes Omicron breakthrough infection

- IP-10 was notably elevated across all five SARS-CoV-2 variant waves at T1 relative to pre-pandemic controls (geometric mean ~94.4 pg/mL in pre-pandemic vs. ~129.3 pg/mL at Omicron T1).
- All pre-Omicron waves showed progressive decline in IP-10: values at T2 and T3 returned toward or below baseline.
- Omicron breakthrough patients showed **sustained high IP-10 at all three timepoints**: geometric mean T1 = 129.3 pg/mL, T2 = 122.8 pg/mL, T3 = 100.4 pg/mL — all significantly above the pre-pandemic mean of 13.5 pg/mL and RT-PCR-negative controls of 94.4 pg/mL.
- Heatmap z-scores confirmed the Omicron wave's uniquely sustained high z-scores at T2 and T3 (warming pattern), compared to the cooling/declining patterns in earlier waves.
- IP-10 elevation at T1–T3 in Omicron patients was statistically significant vs. pre-pandemic controls (p < 0.01 to p < 0.001); however, IP-10 levels did **not** significantly correlate with Long COVID symptom scores at any timepoint (no statistically significant correlation by either Pearson or Spearman analysis).

### 2. Wave-specific cytokine network dynamics with distinct coordination patterns

- **Wuhan wave:** Progressive density decline (ND: 0.29 → 0.21 → 0.14), reflecting gradual loss of coordinated immune signaling; IFN-γ, IL-2, IFN-α2 as early hubs.
- **D614G wave:** Progressive density increase (ND: 0.26 → 0.32 → 0.36), suggesting strengthening and sustained immune coordination; IFN-α2 most connected at T1.
- **Alpha wave:** Density decrease from T1 to T3 (0.32 → 0.20 → 0.21); IL-1β most connected at T1 (Node Degree = 8).
- **Delta wave:** Density peak at T2 (0.22 → 0.41 → 0.27); IL-17A most connected at T2 (Degree = 8); IP-10 largely peripheral.
- **Omicron wave:** Highest initial density (ND = 0.48 at T1), declining to 0.33 by T3 — yet IP-10 remained in the dominant cluster at T3 (Degree = 1, minimal connectivity but persistent), contrasting with the marginal or absent IP-10 at T3 in earlier waves. Consistent regulatory hubs across waves: IL-1β, IFN-γ, IL-2, IFNα2.
- Cross-wave Jaccard similarity coefficients (cytokine network edges): Wuhan vs. D614G = 0.30; Wuhan vs. Alpha = 0.35; D614G vs. Alpha = 0.52; Delta vs. Omicron = 0.42; indicating distinct but partially overlapping immune network architectures across variant transitions.

### 3. Hybrid immunity antibody profile: broad cross-variant recognition with waning neutralization

- **Nucleocapsid-specific total Ig:** Rose significantly at T1 in Omicron patients (confirming natural infection on top of vaccination), then waned considerably by T2–T3, though remained above pre-pandemic baseline.
- **Spike-specific total Ig (Spike trimer, S1, RBD):** Peaked at T1 (superposition of infection + vaccine-elicited immunity); partial waning by T2–T3 but remained significantly elevated above pre-pandemic and RT-PCR-negative controls.
- **Cross-variant Spike Ig (Alpha, Beta, Gamma, Delta):** All significantly elevated vs. pre-pandemic at T1, T2, and T3 — evidence of broad cross-variant humoral immunity elicited by hybrid immunity.
- **Neutralization (Luminex panel, WT and VOCs):** WT and Alpha showed highest neutralization at T1, declining steadily — 1.74-fold reduction in WT live-virus neutralizing GMT from T1 (253.98) to T3 (231.56 at T2, decline continuing). Omicron variants showed lowest and most rapidly waning neutralization, particularly BM1.1 (GMT: 30.31 at T1, declining to 19.10 at T3).
- **Live-virus neutralization (Omicron sub-variants):** GMT for WT = 253.98 at T1; Omicron BA.2 = 63.50 at T1 (~4× lower than WT). Omicron BM1.1 showed lowest titers (GMT 30.31 at T1 vs. 253.98 for WT). Consistent decline across T1→T3 for all Omicron sub-variants, underscoring continued immune evasion by newer strains.

### 4. Seasonal coronavirus antibody responses: CoV-229E correlates with Long COVID severity

- Total Ig against four seasonal coronaviruses (CoV-229E, CoV-HKU1, CoV-NL63, CoV-OC43) showed **no statistically significant group-level elevations** at any timepoint vs. pre-pandemic baseline in Omicron breakthrough cases — Omicron infection does not robustly or persistently boost cross-reactive humoral immunity against seasonal CoVs.
- **Individual-level linear regression** revealed that higher anti-CoV-229E total Ig at T2 and T3 was significantly associated with higher Long COVID scores: T2: R = 0.53, p = 0.00281; T3: R = 0.49, p = 0.00635.
- No significant associations with CoV-HKU1, CoV-NL63, or CoV-OC43 at any timepoint.
- Authors interpret CoV-229E elevation as an indirect marker of broader immune dysregulation or ongoing antibody generation rather than a direct effect of SARS-CoV-2 on CoV-229E antibody production.

### 5. mRNA-inclusive vaccination associated with lower Long COVID scores

- Linear regression at T2 (3–4 months): mRNA-inclusive vaccine regimens were associated with significantly lower Long COVID scores (coefficient = −0.86, p = 0.013), controlling for age and sex.
- Non-mRNA vaccine combinations (viral vector, inactivated) showed a trend toward reduced scores but were not statistically significant (coefficient = −0.66, p = 0.09).
- Age (p = 0.187) and male sex (p = 0.294) were not significant predictors.
- The mechanism is speculative; authors suggest mRNA vaccines may elicit more robust and durable immune responses that facilitate cytokine resolution, referencing evidence that BNT162b2 triggers an IL-15–IFN-γ–IP-10/CXCL10 innate signature (Bergamaschi et al.) that co-regulates adaptive immunity — but this is a hypothesis, not a finding of this study.

## Relevance

**To `hypothesis:0001-shared-dysregulated-attractor`:** The prolonged IP-10/CXCL10 elevation in Omicron breakthrough cases (up to 6–8 months post-infection) provides direct evidence of a **persistent post-infectious immune-state displacement** in mild, clinically recovered individuals who did not require hospitalization. The Omicron wave's distinctively sustained IP-10 — compared to return to near-baseline in earlier waves — aligns with the attractor hypothesis's claim that a subset of post-infectious individuals remain in a self-sustaining immune-activated state. The fact that IP-10 elevation is dissociated from clinical Long COVID symptom scores in this cohort is consistent with the attractor hypothesis's description of "sub-clinical" or low-grade immune activation below the threshold of overt PAIS — neither confirming nor rejecting the displacement as PAIS-specific. The wave-specific cytokine network topology changes (Jaccard < 0.52 across wave pairs) further support the "heterogeneous molecular configurations" reading of the attractor hypothesis.

**To `hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver`:** Persistent IP-10/CXCL10 elevation in the absence of ongoing viral replication (mild cases, largely resolved clinical symptoms by T2–T3) is consistent with sterile innate immune sensing as an ongoing driver. IP-10 is an IFN-γ-induced gene produced downstream of TBK1/IRF3 signaling, the same pathway activated by cGAS-STING. The prolonged IP-10 elevation 6–8 months post-infection in a vaccinated population, **after apparent clinical recovery**, strengthens the premise that a sterile (non-replication-driven) innate sensing loop may be operative. However, this paper does not measure cGAMP, phospho-TBK1, or any direct cGAS-STING activation marker, so the mechanism remains inferred.

**To `hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune`:** The CoV-229E Ig–Long COVID correlation is a novel finding: individual-level CoV-229E antibody levels at T2 and T3 predict Long COVID severity, but there is no group-level elevation. This pattern is consistent with heterogeneous ongoing antibody generation in a subset — potentially reflecting broader immune dysregulation or persistent antigen stimulation — rather than Omicron directly cross-boosting seasonal CoV immunity. This is partial support for the immune-set-point-shift frame: individuals with more perturbed immune states (as indexed by aberrant CoV-229E Ig) have worse Long COVID outcomes.

**To `hypothesis:0020-host-immune-baseline-reserve-gate`:** The mRNA-inclusive vaccine finding (significantly lower Long COVID scores) introduces vaccine-type as a modifier of PAIS risk beyond acute severity or prior immune reserve. This is directly relevant to the reserve-gate hypothesis: even when controlling for age and sex, the mode of pre-infection priming (vaccine platform) materially shapes post-infection immune resolution. The mechanism linking mRNA vaccination to Long COVID protection likely involves the IL-15–IFN-γ–IP-10 innate signature, which may prime myeloid cells and CD8+ T cells differently than inactivated or viral-vector platforms.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Persistent IP-10/CXCL10 elevation (6–8 mo post-mild Omicron) | Persistent post-infectious immune-state displacement | Supports sub-clinical attractor state |
| Wave-specific cytokine network topology | Heterogeneous molecular configurations of immune-state displacement | Jaccard < 0.52 across wave pairs |
| CoV-229E Ig correlates with Long COVID score | Individual immune dysregulation marker for PAIS severity | Indirect; not causal per authors |
| mRNA-inclusive vaccine → lower Long COVID score | Vaccine-platform modulation of host immune reserve | Adds vaccine type to reserve-gate modifiers |
| Sustained IP-10 dissociated from Long COVID symptoms | Sub-clinical PAIS attractor; symptom threshold not crossed in all IP-10-elevated individuals | Consistent with attractor-entry threshold |
| Neutral cross-reactive CoV Ig at group level | Limits cross-CoV-family boosting argument for PAIS | Group-level null; individual variation persists |

## Limitations

- **Small cohort per wave:** Omicron n=30 for Long COVID analysis; Alpha n=11. Underpowered for multivariable regression and subgroup analyses; the mRNA vaccine association should be treated as preliminary.
- **No prior-infection data:** Asymptomatic prior SARS-CoV-2 infections could not be ruled out for any participant, potentially confounding wave-specific comparisons.
- **Long COVID scoring by telephone only:** No in-person clinical validation, objective functional tests, or standardized ME/CFS diagnostic criteria applied. Scores are symptom frequency composites rather than validated diagnostic instruments.
- **Vaccination confounding:** 19 distinct vaccine permutations in the Omicron cohort; the vaccine platform analysis is observational, not randomized, with unequal cell sizes and limited covariate adjustment.
- **IP-10 not correlated with Long COVID:** Despite persistent elevation, no significant statistical association between IP-10 levels and Long COVID symptom scores was detected — the study cannot determine whether sustained IP-10 is pathogenic, a benign footprint, or a vaccine-induced innate priming epiphenomenon.
- **Data confidentiality:** Raw data not publicly available; no independent replication possible without collaboration with the authors.
- **Observational / cross-sectional per timepoint:** No mechanistic experiments; causal ordering between cytokines, antibodies, and outcomes cannot be established.
- **Generalizability:** Thai population, primarily Sinovac-immunized initially (Delta wave), with diverse subsequent platforms; may not generalize to homogeneously mRNA-vaccinated cohorts or other LMIC settings.
- **No IFN-type I or IFN-stimulated gene data:** IP-10 is measured but upstream type-I-IFN or ISG expression is not; cannot distinguish cGAS-STING-driven vs. IFN-γ-driven IP-10.
- **No antigen-persistence or viral-load data:** No measures of SARS-CoV-2 RNA, antigen, or spike protein persistence to adjudicate between antigen-driven vs. sterile immune activation of IP-10.

## Model / Tool Availability

No model, tool, or dataset is released for reuse. Data are described as confidential per the Data Availability statement.

## Follow-up

**Papers to read next:**
- Bergamaschi et al. (Cell Rep 2021, 36(6):109504): COVID-19 mRNA vaccination (BNT162b2) triggers IL-15–IFN-γ–IP-10/CXCL10 innate signature — the mechanistic underpinning of mRNA vaccine protection invoked in Discussion; linked to h0019.
- Espín et al. (eBioMedicine 2023): scoping review of IP-10 elevation in Long COVID — would contextualize the dissociation between IP-10 and Long COVID scores observed in this cohort.
- Ratjanawich et al. (Sci Rep 2024): prior Thai cohort reporting Long COVID at 3 and 6 months post-COVID-19, cited as the local population base for Omicron-era Long COVID scores — cross-cohort context.

**Questions this raises for the project:**
- Does persistent IP-10/CXCL10 elevation in mild Omicron breakthrough cases stratify future autoimmune conversion risk (linking to `hypothesis:0009`)? Follow-up beyond 8 months is needed.
- Is the mRNA vaccine–Long COVID protective association driven by the IL-15–IFN-γ–IP-10 innate axis (as Bergamaschi suggests), and if so, does it represent a form of trained myeloid priming that resolves the IP-10-sustaining loop? (Relevant to `hypothesis:0019` and `hypothesis:0020`.)
- What explains the CoV-229E–Long COVID score correlation at the individual level in the absence of any group-level CoV-229E elevation — is this heterogeneous ongoing antigen-driven antibody production, immune dysregulation-driven bystander activation, or a statistical artefact of the small n?
- Should persistent IP-10 elevation be added as a monitoring biomarker recommendation for mild Omicron breakthrough cases, even in the absence of Long COVID symptom expression?
