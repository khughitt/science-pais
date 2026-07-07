---
id: paper:Chavatza2025
kind: paper
title: "Persistent-relapsing SARS-CoV-2 infection following rituximab treatment for
  autoimmune rheumatic diseases: diagnosis and outcomes"
status: active
paper_kind: ""
ontology_terms:
- rituximab
- anti-CD20
- B-cell depletion
- SARS-CoV-2 persistence
- persistent COVID-19
- relapsing COVID-19
- autoimmune rheumatic diseases
- hypogammaglobulinemia
- bronchoalveolar lavage
- nasopharyngeal PCR
- viral clearance
- immunocompromised host
source_refs:
- paper:Chavatza2025
- cite:Chavatza2025
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- hypothesis:0004-acute-severity-threshold
created: "2026-07-07"
updated: "2026-07-07"
Source: europepmc (XML full text, CC BY 4.0)
---

# Persistent-relapsing SARS-CoV-2 infection following rituximab treatment for autoimmune rheumatic diseases: diagnosis and outcomes

<!--
- **Authors:** Katerina Chavatza, Elisavet Mastrostamati, Charalampos Charalampidis, Elvira-Markela Antonogiannaki, Ioannis Grigoropoulos, Emmanouil Karofylakis, Foteini Gkolemi, Georgios Koromvokis, Electra Kalara, Eleni Sambatakaki, Antonis Fanouriakis, Konstantinos Thomas
- **Year:** 2025
- **Journal:** RMD Open, vol. 11, e005756
- **DOI:** 10.1136/rmdopen-2025-005756
- **PMID:** 40695544 | **PMCID:** PMC12281322
- **BibTeX key:** Chavatza2025
- **Source:** europepmc (XML full text, CC BY 4.0)
-->

## Key Contribution

This single-centre retrospective cohort study is the largest reported series of persistent-relapsing COVID-19 (prCOVID-19) in rituximab (RTX)-treated patients with autoimmune rheumatic diseases (AIRDs). It documents that 11.6% of RTX-treated AIRD patients who contracted COVID-19 developed prCOVID-19, with zero cases in 661 comparator patients on other biologic, targeted synthetic, or conventional synthetic DMARDs. The study's mechanistically important secondary finding is that nasopharyngeal swab (NPS) PCR has poor diagnostic accuracy in this setting, with 32.1% of matched BAL/NPS pairs showing BAL-positive/NPS-negative discordance, meaning lower-respiratory viral persistence is systematically missed by upper-respiratory sampling.

**PAIS relevance caveat.** This paper documents *active persistent-relapsing viral infection* in profoundly immunocompromised patients, not a post-infectious symptom phenotype. Its relevance to PAIS is mechanistic: B-cell depletion by rituximab is a clean natural experiment demonstrating that humoral immunity is required for SARS-CoV-2 clearance. This supports the antigen/viral persistence arm of `hypothesis:0002`, but the evidence is from active viraemia during treatment, not from the post-acute chronic-symptom phase studied in typical long-COVID cohorts.

## Methods

**Design:** Single-centre retrospective cohort study, Attikon University Hospital, Athens, Greece. Study period: June 2021 – January 2025.

**Inclusion:** AIRD patients receiving RTX during the study period who developed COVID-19 and met criteria for prCOVID-19.

**prCOVID-19 case definition (requires all three):**
1. Respiratory and/or systemic symptoms persisting >30 days with either a chronic or a relapsing pattern.
2. Unilateral or bilateral pulmonary opacities on chest CT.
3. PCR detection of SARS-CoV-2 in nasopharyngeal or BAL samples.

**Resolution criterion:** End of patient symptoms (no confirmatory negative PCR required).

**Comparator group:** 661 patients on other b/tsDMARDs or csDMARDs from the same centre; screened for prCOVID-19.

**Concordance analysis:** NPS and BAL PCR results were matched per event (NPS "recent" = within 45 days of BAL during symptomatic period). BAL+/NPS- discordance was computed as the fraction of matched pairs showing this pattern.

**Statistics:** Descriptive (median, IQR, frequencies). Mann–Whitney–Wilcoxon and chi-squared for outcome comparisons. Swimmer plot (R 4.3.3, ggplot2).

**Study limitations (design):** Retrospective single-centre series; outcome comparisons are underpowered (N=27 events); no matched controls within the RTX-treated group; resolution of prCOVID-19 defined symptomatically rather than virologically; some IgG data missing (2/27 events).

## Key Findings

### Incidence and population

- 470 patients received RTX during the study period; 225 developed COVID-19 at least once.
- **26/225 (11.6%)** of RTX-COVID-19 patients developed **27 prCOVID-19 events** (one patient had two events, 15 months apart).
- Zero prCOVID-19 in 661 patients on other DMARDs (zero comparison is striking but uncontrolled for disease severity, disease mix, and era of treatment).
- Demographics: 77% female; median age 61 years; AIRD diagnoses — ANCA-associated vasculitis 35%, RA 31%, SLE 23%, inflammatory myopathies 12%.
- Median cumulative RTX dose prior to prCOVID-19 diagnosis: 12 g (IQR 6.5 g).
- Median time from last RTX infusion to SARS-CoV-2 infection: 3.6 months (IQR 3.8, max 11.4).
- 77% had received ≥3 COVID-19 vaccine doses.
- 54% had current or past lung involvement from the underlying AIRD.

### Hypogammaglobulinemia

- **17/25 events (68%) with available IgG data had IgG below 700 mg/L** at time of prCOVID-19 diagnosis (median 550 mg/L, IQR 367).
- Note on units: The paper reports IgG in "mg/L", but in clinical rheumatology the standard threshold for hypogammaglobulinemia is 700 mg/dL (= 7 g/L = 7000 mg/L). "700 mg/L" = 0.7 g/L would represent extreme hypogammaglobulinemia. The user's prompt references "700 mg/dL". This likely reflects a units transcription discrepancy within the paper (European labs typically report in g/L; the paper may have dropped the unit prefix). The 68% prevalence figure (17/25) is confirmed regardless of which unit is intended, but the precise threshold should be treated with caution until checked against the supplementary material or a corrigendum. [UNVERIFIED — units discrepancy between "mg/L" as printed and the standard clinical threshold of 700 mg/dL]

### Duration and severity

- **Median duration of prCOVID-19: 65 days (IQR 74); maximum: 361 days.** Confirmed.
- Relapsing pattern in 16/27 (59.3%) events.
- 96.3% required hospitalisation; median 10.5 days (IQR 14, max 70).
- 11 patients (42.3%) had ≥2 hospitalisations.
- 12 events experienced severe respiratory failure; 3 needed mechanical ventilation.
- **4 deaths (15.4%)**.

### Lower-respiratory viral persistence and BAL/NPS concordance

- Total samples: 113 NPS and 17 BAL PCR tests across 27 prCOVID-19 events.
- NPS PCR positivity rate: **59/113 (52.2%)** (median 3 tests per patient).
- BAL PCR positivity rate: **12/17 (70.6%)** during active COVID-19.
- **BAL+/NPS- discordance: 9/28 (32.1%)** of matched NPS/BAL pairs. (The Discussion section states "29%" — slight rounding inconsistency within the paper; the directly calculated figure from the Results is 32.1%.)
- Bronchoscopy **established the prCOVID-19 diagnosis** in **9/27 (33%)** events (cases where NPS was negative or inconclusive and BAL PCR was positive).
- Bacterial co-infection detected in 5/27 (19%) events, predominantly *H. influenzae*.

### Treatment

- 8 events received antivirals within the first week of symptoms.
- All but one received remdesivir; 13 events received both remdesivir and nirmatrelvir/ritonavir.
- 8/22 events received IVIG during hospitalisation.

## Relevance

**Primary link — `hypothesis:0002` (antigen/viral persistence):** Rituximab-induced B-cell depletion is among the cleanest available human models for failure of humoral viral clearance. This paper documents that, in the absence of B-cell–mediated immunity, SARS-CoV-2 persists and relapses in the lower respiratory tract for up to 361 days. The zero-case comparator group (661 patients on other DMARDs) reinforces that rituximab is specifically permissive of persistence. This directly supports the "impaired antigen clearance" mechanism proposed for the SOT PASC paradox (Vinson2024) and grounds the persistence arm of h0002 with controlled B-cell depletion data.

**Compartment discordance as a mechanism signal:** The 32.1% BAL+/NPS- discordance is mechanistically important: virus replicates in deep lung tissue while upper-airway sampling is negative. This provides clinical evidence for tissue-reservoir persistence (lower airways) that is invisible to standard surveillance, an observation structurally analogous to the tissue-reservoir component of h0002 (though h0002 focuses on macrophage-based antigen fragment reservoirs rather than live replicating virus).

**Scope boundary:** This study documents *active replicating virus in immunocompromised patients*, not the chronic post-infectious symptom phenotype of PAIS. The bridge to PAIS is indirect: if RTX patients who survive persistent infection eventually experience post-infectious sequelae, it is unknown whether these arise from prolonged active infection, exhausted immune recovery, or pathways shared with immunocompetent long-COVID patients. The paper does not follow patients to a post-infection symptom endpoint. Claims about PAIS mechanism derived from this paper should be restricted to the antigen-clearance route.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Persistent-relapsing COVID-19 (prCOVID-19) | Active viral persistence (pre-PAIS substrate) | Not a PAIS phenotype; upstream of post-acute sequelae |
| Rituximab-induced B-cell depletion | Natural experiment for impaired viral clearance | Analogous to SOT context in Vinson2024 |
| IgG hypogammaglobulinemia | Humoral immune deficiency as clearance predictor | IgG <700 (units uncertain) in 68% of events |
| BAL+/NPS- discordance | Lower-respiratory tissue-reservoir compartment | Deep persistence missed by upper-airway sampling |
| Zero prCOVID-19 in non-RTX controls | B-cell depletion as necessary condition for this phenotype | Confounded by disease mix and severity |
| Viral evolution within host | Within-host antigenic diversification during persistence | Cited in Introduction; not measured in this study |

## Limitations

1. **Retrospective single-centre design** (N=26 patients, 27 events): underpowered for multivariate outcome analysis; authors acknowledge no variables associated with severe prCOVID-19 were identified.
2. **Comparator group is uncontrolled:** 661 patients on other DMARDs differ in underlying disease, disease activity, and concurrent immunosuppression — the zero-prCOVID-19 rate is persuasive but not a rigorous controlled comparison.
3. **Symptom-based resolution criterion:** prCOVID-19 resolution was defined clinically (end of symptoms), not virologically. Duration estimates may undercount subclinical persistence.
4. **No post-infection follow-up for PAIS:** The paper does not report whether surviving patients developed post-acute fatigue, cognitive symptoms, or other PAIS phenotypes after resolution.
5. **IgG unit discrepancy** (see Key Findings): the threshold "700 mg/L" in the paper requires unit clarification.
6. **BAL sampling was clinical (not systematic):** bronchoscopy was performed at physician discretion, biasing the BAL cohort toward patients with higher clinical suspicion. The true BAL positivity rate in all prCOVID-19 events is unknown.
7. **Era and variant confounds:** study spans June 2021 – January 2025 (Delta through post-Omicron); variant composition and clinical management evolved substantially.
8. **Missing IgG data:** 2 events lacked IgG levels, so hypogammaglobulinemia prevalence denominator is 25, not 27.
9. **No genomic/evolutionary data within this study:** viral within-host evolution is cited from literature but not measured here.

## Model / Tool Availability

Not applicable. Swimmer plot code in standard R/ggplot2; no novel tool released.

## Follow-up

- **Vinson2024** (SOT PASC paradox): the same B-cell-depletion / impaired-clearance frame applied to post-acute sequelae incidence — the missing downstream link from this paper.
- Whether prCOVID-19 survivors in this cohort develop PAIS-like post-infectious symptoms is unknown and would be a direct follow-up study to commission.
- Sigal, Neher & Lessells 2025 (*Nat Rev Microbiol*, cited as R6): "The consequences of SARS-CoV-2 within-host persistence" — review of the within-host persistence and variant evolution literature cited by this study.
- Machkovech et al. 2024 (*Lancet Infect Dis*, cited as R7): "Persistent SARS-CoV-2 infection: significance and implications" — broader synthesis of persistent infection definition, evidence, and implications.
- IgG unit clarification: check supplementary material (online supplemental file 1) or contact authors to confirm whether the threshold is 700 mg/dL (standard) or 700 mg/L (very low; ~70 mg/dL).
