---
id: paper:Abubasheer2025
type: paper
title: "Sex-Based Differences in Cardiovascular Outcomes Associated With COVID-19: A Systematic Review and Meta-Analysis"
status: active
ontology_terms:
  - sex differences
  - cardiovascular outcomes
  - venous thromboembolism
  - myocardial infarction
  - ischemic stroke
  - thromboinflammation
  - COVID-19 complications
  - meta-analysis
  - ECMO
  - mortality
dataset_usage: []
datasets: []
source_refs:
- cite:Abubasheer2025
related:
- paper:CerviaHasler2024
- question:0007-mechanism-of-female-predominance-in-pais
- question:0010-vascular-microclot-subphenotype
created: '2026-06-22'
updated: '2026-06-22'
---
# Sex-Based Differences in Cardiovascular Outcomes Associated With COVID-19: A Systematic Review and Meta-Analysis

- **Authors:** Tareq M. Abubasheer, Hanan M. A. Abubasheer, Ramez M. Odat, Anas Elgenidy, Ahmed M. Afifi
- **Year:** 2025
- **Journal:** Reviews in Medical Virology, vol. 35, no. 3, e70022
- **DOI:** 10.1002/rmv.70022
- **PMID:** 40148238
- **BibTeX key:** Abubasheer2025
- **Source:** Europe PMC abstract + PubMed metadata (full text inaccessible — Wiley 403)

## Key Contribution

This systematic review and meta-analysis of 11 studies (31,044 males; 25,917 females) quantifies a consistent **male-biased cardiovascular risk signal** across multiple endpoints in COVID-19 patients. Males show significantly higher pooled relative risks for venous thromboembolism (RR 1.43), ischemic stroke (RR 1.46), myocardial infarction (RR 1.24), major bleeding (RR 1.22), ECMO use (RR 2.14), and overall mortality (RR 1.21) compared to females. Heart failure and hospitalization length show no sex disparity. This paper provides the best available pooled effect sizes for a male-biased thromboinflammatory/vascular phenotype in the acute and post-acute COVID-19 context.

## Methods

**Study design:** Systematic review and meta-analysis following PRISMA guidelines. Searches conducted in PubMed/MEDLINE, SCOPUS, and EMBASE up to January 2024.

**Inclusion criteria:** [INACCESSIBLE — full text not retrieved] Studies measuring sex-based differences in pre-specified cardiovascular outcomes in patients diagnosed with COVID-19.

**Studies included:** 11 studies; total N = 56,961 (31,044 males, 25,917 females). [UNVERIFIED: individual study designs, years, and countries — not available from abstract.]

**Outcomes of interest:** Myocardial infarction (MI), venous thromboembolism (VTE), ischemic stroke, major bleeding, mortality, heart failure, hospitalization length, and ECMO utilization.

**Statistical software:** Stata version 18. Pooled relative risks (RR) with 95% confidence intervals computed. Heterogeneity statistics (I²) and publication bias assessment [INACCESSIBLE — methods details not recoverable from abstract].

**Severity adjustment:** [INACCESSIBLE] The abstract does not state whether pooled RR estimates were adjusted for or stratified by acute COVID-19 severity (hospitalization status, ICU admission, or disease severity score). This is an **important unresolved limitation** — see Limitations section.

## Key Findings

All effect estimates below are from the abstract and represent males vs females (RR > 1 = higher risk in males). These numbers are drawn verbatim from the abstract and are treated as verified from that source.

### Thrombotic / Vascular Endpoints

| Outcome | Pooled RR (males vs females) | 95% CI | p-value |
|---|---|---|---|
| Venous thromboembolism (VTE) | **1.43** | [1.19, 1.71] | 0.0001 |
| Ischemic stroke | **1.46** | [INACCESSIBLE] | 0.05 |
| Myocardial infarction (MI) | **1.24** | [1.03, 1.49] | 0.02 |

> Note: the abstract reports stroke RR 1.46 with p = 0.05 but does not provide the 95% CI in the available text. CI for stroke is [INACCESSIBLE].

### Bleeding and Procedural Endpoints

| Outcome | Pooled RR (males vs females) | 95% CI | p-value |
|---|---|---|---|
| Major bleeding | **1.22** | [1.06, 1.40] | 0.0001 |
| ECMO utilization | **2.14** | [1.11, 4.13] | 0.02 |

### Mortality

| Outcome | Pooled RR (males vs females) | 95% CI | p-value |
|---|---|---|---|
| Overall mortality | **1.21** | [INACCESSIBLE] | 0.0001 |

> Note: the abstract quotes mortality RR 1.21 with p = 0.00 but does not provide the 95% CI in the available text. CI for mortality is [INACCESSIBLE].

### Null Findings

- **Heart failure:** No sex disparity (RR and CI [INACCESSIBLE]).
- **Hospitalization length:** No sex disparity (RR and CI [INACCESSIBLE]).

## Relevance

This paper is directly load-bearing for a project proposition about a **male-biased vascular/thromboinflammatory signal in post-acute COVID**. Key connections:

- **Thromboinflammation hypothesis (`question:0010-vascular-microclot-subphenotype`):** The male-biased VTE RR 1.43 and MI RR 1.24 support the vascular/thromboinflammatory mechanistic axis being sex-dimorphic in direction — male-predominant for acute thrombotic outcomes, in contrast to the female-predominant fatigue/PASC phenotype. If thromboinflammation is the driver of a vascular PASC subphenotype, this paper predicts that subphenotype should be male-enriched.

- **Sex-differences framing (`question:0007-mechanism-of-female-predominance-in-pais`):** The pattern here is the *mirror image* of the PAIS sex effect: females predominate in post-acute fatigue/neurological sequelae, while males predominate in acute cardiovascular/vascular complications. This dissociation is mechanistically informative — it suggests either (a) the vascular/thrombotic axis does not drive the neurological/fatigue PASC phenotype, or (b) females surviving acute vascular injury are under-represented in acute-mortality datasets, creating differential selection into PASC cohorts.

- **Hypothesis 0005 (`reproductive-stage-immune-homeostatic-margin`):** The male-biased acute vascular signal provides a baseline against which the female predominance of post-acute immune/fatigue sequelae should be interpreted; possible that estrogen-mediated vascular protection in premenopausal females is part of the sex-difference mechanism.

- **Hypothesis 0004 (`acute-severity-threshold`):** ECMO RR 2.14 in males is the most striking finding and supports that males are substantially more likely to cross the critical-severity threshold during acute COVID-19. This is relevant to the gating question — if males die or have severe acute vascular events at higher rates, survivors entering PASC cohorts may be a selected subpopulation.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Venous thromboembolism (VTE) | Thromboinflammation / microclot axis | VTE is the clinical expression; complement/platelet/fibrin biology is the proposed mechanism |
| Male sex as cardiovascular risk modifier | Sex as modifier of homeostatic margin (h0005) | Here sex shifts *vascular* risk, not fatigue/PASC risk |
| ECMO utilization (RR 2.14) | Acute-severity threshold (h0004) | Extreme severity endpoint; largest male excess |
| Ischemic stroke (RR 1.46) | Endothelial dysfunction / thromboinflammation | Overlaps with microclot/vascular PASC subphenotype |
| No sex disparity in heart failure or LOS | Null signal for fluid/cardiac remodeling axis | Heart failure and hospitalization length not sex-dimorphic |

## Limitations

**Critical limitation — severity adjustment absent or unclear:**
The abstract does not state whether pooled RR estimates were adjusted for, or stratified by, acute COVID-19 severity (e.g., outpatient vs hospitalized vs ICU). This is a fundamental confound: males are hospitalized and admitted to ICU at substantially higher rates than females in COVID-19 cohorts. If the 11 included studies do not control for severity, the male-biased cardiovascular RRs may partially reflect male-biased acute severity rather than a sex-specific biological susceptibility to vascular complications at equivalent severity. **The full text would be required to determine whether severity was a covariate or whether any subgroup analysis by severity was conducted.** This limitation substantially constrains causal interpretation.

**Additional limitations (partially inferable from abstract):**
- Only 11 studies included (N ~57k total); pooled CI for ischemic stroke and mortality not recoverable from abstract text.
- Ischemic stroke p = 0.05 is borderline; wide CI is likely given the borderline significance.
- ECMO RR 2.14 [1.11, 4.13] has a very wide CI reflecting small event counts.
- Study-level heterogeneity (I², Cochran Q) and publication bias assessment are [INACCESSIBLE].
- No subgroup analyses described in abstract (e.g., by age, comorbidity, vaccination status, COVID variant era).
- "Sex" vs "gender" terminology is conflated in the abstract (uses both "sex-based" and "gender disparity"), which may reflect variable operationalization across included studies.
- Search cutoff January 2024 — does not include studies from the Omicron-dominant era with potentially different cardiovascular event profiles.
- Post-acute (PASC-period) vs acute-phase outcomes are not distinguished; the endpoints likely reflect predominantly acute and subacute (30–90 day) COVID-19 cardiovascular complications rather than post-12-month sequelae.

## Model / Tool Availability

Not applicable. No model, tool, or dataset is released.

## Follow-up

- **Obtain full text** to recover: (a) severity-stratification or severity-adjustment details, (b) 95% CI for ischemic stroke and mortality, (c) individual study-level data, (d) heterogeneity statistics, and (e) any subgroup analyses by age, severity, or variant era.
- **Compare** with Xie2024 (post-acute multi-organ burden by sex and severity after COVID-19 and influenza) to check whether the male-biased acute vascular signal attenuates in post-acute follow-up.
- **Question:** does the male-biased acute cardiovascular signal persist into PASC (3–12 months), or does it reverse/disappear, leaving the female-predominant neurological/fatigue phenotype as the dominant PASC signal? This would sharpen mechanistic inference about the relationship between acute vascular injury and long-COVID pathophysiology.
- **Related paper to read:** CerviaHasler2024 (complement/thromboinflammation as biological substrate of the vascular PASC signal); Stahlberg2025 (microclots).
