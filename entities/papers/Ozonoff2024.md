---
id: paper:Ozonoff2024
type: paper
title: 'Features of acute COVID-19 associated with post-acute sequelae of SARS-CoV-2
  phenotypes: results from the IMPACC study'
status: active
ontology_terms:
  - post-acute sequelae of SARS-CoV-2 (PASC)
  - patient-reported outcomes (PROs)
  - latent class mixture modeling (LCMM)
  - SARS-CoV-2 viral burden
  - anti-SARS-CoV-2 antibody response
  - B lymphocyte frequency
  - fibroblast growth factor 21 (FGF21)
  - CyTOF mass cytometry
dataset_usage: []
datasets: []
source_refs:
- cite:Ozonoff2024
related: []
created: '2026-06-11'
updated: '2026-06-11'
---
# Features of acute COVID-19 associated with post-acute sequelae of SARS-CoV-2 phenotypes: results from the IMPACC study

<!--
- **Authors:** Al Ozonoff, Naresh Doni Jayavelu, Shanshan Liu, Esther Melamed, Carly E. Milliren, Jingjing Qi, Linda N. Geng, Grace A. McComsey, et al. (IMPACC Network)
- **Year:** 2024
- **Journal:** Nature Communications, Vol. 15, Article 216
- **DOI:** 10.1038/s41467-023-44090-5
- **BibTeX key:** Ozonoff2024
- **Source:** PDF
-->

## Key Contribution

Using longitudinal patient-reported outcomes (PROs) and dense immunophenotyping from the NIH-funded IMPACC prospective cohort (n=590 hospitalized COVID-19 survivors followed 12 months post-discharge), this study identifies four distinct PASC clinical phenotypes: minimal deficit (60.7%), physical predominant (15.6%), mental/cognitive predominant (13.9%), and multidomain deficit (9.8%). It then links PASC cluster membership to acute-phase biological features — specifically showing that higher respiratory viral burden (lower N1 Ct values) and lower anti-RBD/Spike IgG titers during the acute phase are independently associated with the most severe (multidomain) and physical-predominant clusters, while reduced circulating B lymphocyte frequency and elevated fibroblast growth factor 21 (FGF21) mark the multidomain cluster. This is among the first large prospective studies to bridge the acute immunobiology of COVID-19 to specific post-acute outcome phenotypes in hospitalized patients.

## Methods

**Design:** Prospective, multi-site observational cohort (IMPACC — Immunophenotyping Assessment in a COVID-19 Cohort). Enrolled 1,164 participants admitted to 20 US hospitals (affiliated with 15 academic institutions) between May 2020 and March 2021. NCT04438777.

**Survey respondent cohort (n=590):** Of 702 participants who survived hospitalization and were alive and on study at 3 months post-discharge, 590 (84%) completed at least one quarterly survey. Median age 57 years (IQR 19); 61% male; 22% Black/African American; 32% Hispanic/Latinx; 94% had at least one comorbidity; none had received a COVID-19 vaccine prior to admission.

**PRO instruments (8 domains):**
- EQ-5D-5L (health-related quality of life)
- PROMIS Cognitive Function Score
- PROMIS Physical Function Score
- PROMIS Dyspnea Score
- PROMIS Global Mental Health Score
- PROMIS Psychosocial Illness Impact Positive Score
- Health Recovery Score (Visual Analog Scale vs. pre-illness baseline)
- Surveys at 3, 6, 9, and 12 months post-discharge

**Clustering approach:** Latent class mixed models (LCMMs) applied longitudinally to each PRO; quadratic models with three groupings selected for most PROs. Cluster assignments then aggregated across all PROs using Ward algorithm with six clustering algorithms and four fit statistics (within-cluster SS, silhouette width, Dunn index, ratio of within-to-between SS). Four PRO clusters were identified.

**Immunophenotyping (acute phase, days 0–28):**
- SARS-CoV-2 viral load: RT-PCR of nasal swabs, N1 and N2 genes
- Serology: anti-RBD IgG and anti-Spike IgG by ELISA
- CyTOF 65-cell-subset blood immunophenotyping (43-antibody panel)
- Autoantibodies against type I IFNs (IFN-alpha, -beta, -omega) by multiplex particle-based assay
- Proximity Extension Assay (Olink): 92-protein inflammatory panel
- Plasma global metabolomics: liquid chromatography-mass spectrometry
- WCGNA on 658 serum metabolites identified 27 modules

**Statistical methods:** Generalized linear mixed effects models (GLMs) and generalized additive mixed effects models (GAMs); Benjamini-Hochberg correction for multiple comparisons (FDR <0.05); multinomial logistic regression for cluster membership predictors. R 4.2.1.

## Key Findings

**PASC phenotype clusters (all compared to minimal deficit cluster MIN, n=358, 60.7%):**

| Cluster | n | % | Characteristic deficit |
|---|---|---|---|
| MIN — minimal deficit | 358 | 60.7% | Reference (minimal ongoing impairment across all PROs) |
| PHY — physical predominant | 92 | 15.6% | Dyspnea, physical function deficit |
| COG — mental/cognitive predominant | 82 | 13.9% | Cognitive, mental, psychosocial deficit |
| MLT — multidomain deficit | 58 | 9.8% | Deficits across all PRO domains simultaneously |

**Demographic and clinical predictors of deficit clusters (adjusted multinomial logistic regression):**
- PHY cluster: associated with chronic pulmonary disease (OR 2.46, 95% CI 1.41–4.29) or chronic neurologic disorder (OR 2.13, 95% CI 1.20–3.78); less likely to be male (OR 0.55, 95% CI 0.35–0.87)
- COG cluster: less likely to be age ≥65 (OR 0.41, 95% CI 0.18–0.94); less likely male (OR 0.54, 95% CI 0.36–0.82); more likely to have chronic cardiac disease (OR 1.72, 95% CI 1.02–2.88)
- MLT cluster: associated with chronic pulmonary disease (OR 1.78, 95% CI 1.01–3.13) or chronic neurologic disorder (OR 4.37, 95% CI 2.14–8.94); more likely to have received supplemental oxygen vs. none (OR 0.54, 95% CI 0.34–0.87); longer hospitalization (OR per week 1.44, 95% CI 1.19–1.75)
- Acute COVID-19 disease severity (SOFA, ICU, mechanical ventilation) was NOT associated with PRO cluster assignment; use of remdesivir and steroids was also not associated

**Viral burden and serology by cluster (acute phase, days 0–28):**
- N1 Ct values were significantly lower (higher viral loads) in PHY and MLT clusters throughout the first 28 days compared to MIN (GAM, adj. p=0.015 for MLT vs. MIN)
- Anti-RBD IgG and anti-Spike IgG levels were significantly lower in the MLT cluster vs. MIN and COG (GAM, adj. p=0.023) and in the PHY cluster vs. MIN and COG (GLM, adj. p=0.014)
- Faster rise in antibody levels between days 7–20 was seen in PHY and MLT clusters vs. others (adj. p=0.005 for anti-RBD IgG; p=0.0017 for anti-Spike IgG) — but overall titers remained lower
- Ratio of anti-RBD IgG to N1 Ct (IgG/Ct): this ratio associates with PRO cluster in both acute and convalescent phases, suggesting it may serve as a practical patient-risk-stratification marker

**B lymphocyte immunophenotyping (CyTOF, days 0–28):**
- Circulating B cell frequency (B to non-granulocyte ratio) was significantly lower in MLT (adj. p=0.0005) and COG clusters (adj. p=0.025) compared to MIN cluster
- Naïve B cell frequency was lower in MLT vs. MIN (trend; not significant after multiple comparison correction for all B cell subsets)
- Other immune cell subtypes (T cells, NK cells, monocytes) were not significantly associated with PRO cluster

**Autoantibodies against type I IFNs:**
- Detected in 4.3% of participants at hospital onset (24/563 with blocking activity against IFN-alpha, -beta, and/or -omega)
- 5.3% males, 2.7% females (P=0.14); more common in individuals >65 years (8.9% vs. 2.8% younger, P=0.039)
- Proportionally more frequent in PHY (6.9%) and MLT (7.3%) clusters compared to MIN (3.2%) and COG (3.8%) (p=0.2, not significant)
- Individuals with IFN autoantibodies had significantly higher viral loads (N1 Ct P=0.012, N2 Ct P=0.006) vs. matched controls without IFN autoantibodies; no difference in Ab titers

**Inflammatory proteomics (Olink, 92 proteins):**
- FGF21 was significantly elevated in the COG cluster (adj. p=0.0025) and MLT cluster (adj. p=0.000033) relative to MIN
- Highest mean FGF21 values in the MLT cluster

**Metabolomics (plasma, WCGNA, 658 metabolites):**
- 27 metabolic modules identified; significant cluster differences in:
  - Methylhistidine metabolism module (global metabolomics module 3): lower levels in PHY and MLT clusters vs. MIN (shape adj. p=0.049)
  - Acylcarnitine metabolism module (global metabolomics module 18): significantly higher levels in PHY cluster vs. MIN (adj. p=0.049)
- Authors interpret methylhistidine association as consistent with inverse relationship between 3-methylhistidine and FGF21 (potentially mediated by insulin sensitivity); acylcarnitine connection as consistent with ME/CFS literature on metabolic dysfunction

**Female sex and PASC:**
- Female sex was a consistent risk factor across PHY and COG clusters
- The biological basis was not resolved; discussed as potentially involving autoimmunity, hormonal influences on inflammation, or differences in acute immune activation

## Relevance

This study directly addresses `research-question:post-acute-infection-syndromes` — why do some people fail to recover after acute infection? — by demonstrating that: (1) PASC is not a single phenotype but a heterogeneous collection of at least four distinct deficit patterns detectable as early as 3 months post-discharge; and (2) specific acute-phase immune features (higher viral burden, lower antibody response, fewer circulating B cells) predict which phenotype trajectory a patient enters. This is directly compatible with the project's homeostatic recovery frame: patients who mount a poorer antiviral response during the acute phase (lower antibody titers, higher viral burden, B cell depletion) are more likely to end up in the most severe deficit cluster, consistent with the hypothesis that a suboptimal initial clearance event sets a failed-recovery trajectory.

Key connections to the project's working frame:

1. **Failed clearance as the initiating event:** The finding that higher viral burden and lower antibody response during acute hospitalization predict PHY and MLT clusters supports the view that inadequate acute-phase viral control seeds the post-acute dysregulated state. This is a prospective, longitudinal confirmation of the mechanism, not a retrospective association.

2. **B cell depletion links viral persistence and immunological failure:** Fewer circulating B cells during acute illness predicts the most severe PASC cluster (MLT). This may reflect a vicious cycle — fewer B cells mean suboptimal antibody production, incomplete viral clearance, and persistent antigen driving continued immune activation (see also Peluso2024 on antigen persistence).

3. **FGF21 as a marker of metabolic/mitochondrial dysfunction in PASC:** Significantly elevated FGF21 in COG and MLT clusters, combined with acylcarnitine and methylhistidine metabolic signatures, provides a molecular bridge to the metabolic dysfunction hypothesis that the project tracks. FGF21 has also been elevated in ME/CFS patients, reinforcing cross-PAIS biology.

4. **PASC sub-phenotypes match the project's heterogeneity acknowledgement:** The research question explicitly notes that "apparent between-study differences often reflect these covariates rather than distinct biology." Here, four phenotypes are defined by functional domain (not symptom list), providing a more principled taxonomy than most prior work — directly useful for cross-study harmonization.

5. **Hospital severity does not predict PASC cluster:** Consistent with multiple prior studies cited in the paper, ICU admission and mechanical ventilation were NOT associated with PRO cluster membership. This is directly relevant to the project's Working Frame, which notes that "acute-illness severity" is a covariate that must be handled carefully — here, severity proxies do not cleanly predict post-acute failure.

6. **Implications for PAIS case definition:** The MLT cluster is the most severe; it is enriched for female sex, comorbidities (chronic pulmonary disease, chronic neurologic disorder), longer hospitalization, lower viral control markers, and lower B cells. This profiling could inform biomarker-based case stratification in future clinical trials.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| PRO cluster assignment (MIN/PHY/COG/MLT) | PASC sub-phenotype heterogeneity | Dimensionality-reduction approach to defining functional recovery trajectories |
| Higher SARS-CoV-2 viral burden (lower N1 Ct) in acute phase | Failed acute viral clearance → PAIS trajectory seeding | Direct acute-phase predictor of post-acute deficit cluster |
| Lower anti-RBD / anti-Spike IgG in acute phase | Suboptimal humoral response → persistent antigen burden | Links to antigen-persistence mechanism (see Peluso2024) |
| Lower circulating B cells (CyTOF) in MLT cluster | B cell depletion as immune failure mode | May mechanistically connect viral burden → Ab response → B cell feedback loop |
| Anti-IFN autoantibodies correlated with higher viral load | IFN pathway disruption → impaired clearance | Autoimmune contribution to acute virological failure, feeding forward to PASC |
| Elevated FGF21 in COG and MLT clusters | Metabolic/mitochondrial dysfunction in PASC | Shared with ME/CFS biology; bridges metabolic and immune dysfunction |
| Acylcarnitine metabolic module elevated in PHY cluster | Mitochondrial beta-oxidation impairment | ME/CFS metabolic overlap; acylcarnitines as surrogate biomarkers |
| Methylhistidine module decreased in PHY and MLT | Muscle protein catabolism / skeletal muscle toxicity | 3-MH is a skeletal muscle toxicity biomarker; links FGF21-mediated mitochondrial uncoupling |
| Female sex predominance across PHY and COG clusters | Sex as covariate in PAIS susceptibility | Project notes sex as intrinsic covariate; mechanism unresolved here |
| Lack of association between ICU/severity and PRO cluster | Acute severity does not determine PAIS trajectory | Nuance: severity proxies are not the same as viral clearance success |
| Supplemental oxygen therapy → lower MLT odds | Early supportive care may modulate post-acute trajectory | Suggests acute treatment may influence long-term homeostatic recovery pathway |
| IgG/Ct ratio (Ab titer to viral burden) | Practical biomarker for PASC risk stratification | Proposed as a clinically actionable acute-phase risk score |

## Limitations

1. **Pre-Omicron, unvaccinated cohort (enrolled May 2020 – March 2021):** None of the participants had received COVID-19 vaccines prior to admission; 62% received primary vaccine series after discharge but this was post-PASC onset. Findings may not generalize to vaccinated or Omicron-era patients where immune priming and viral biology differ substantially.

2. **Hospitalized patients only:** The cohort is enriched for severe acute disease. The study explicitly excludes non-hospitalized patients, limiting generalizability to the majority of PASC cases that follow mild-to-moderate acute illness — which constitute the bulk of the long-COVID burden.

3. **No pre-infection baseline immunophenotyping:** Immune features (B cell counts, FGF21, antibody titers) at hospital admission may reflect pre-existing individual variation as much as acute COVID-19 effects; without pre-infection baselines, directionality is inferred but not proven.

4. **Symptom attribution to PASC vs. pre-existing conditions:** Pre-COVID symptomatology was not recorded (study designed before PASC reporting became standard practice); proportion of persistent symptoms attributable to PASC vs. pre-existing comorbidities cannot be fully disentangled.

5. **No T cell dysfunction analysis:** T-cell exhaustion is a described feature of PASC, but was not captured in this study's CyTOF panel analysis; the paper explicitly notes this as a gap.

6. **No independent validation cohort:** Multi-site enrollment at 20 hospitals and diverse participant demographics are strengths, but the absence of a held-out replication cohort means clustering structure and biomarker associations require external validation.

7. **No occupational or socioeconomic data:** Known associations between socioeconomic status/occupation and PASC risk could not be assessed.

8. **No control groups for hospital stay:** No concurrent non-COVID hospitalized respiratory illness comparators or elective-surgery controls to rule out hospitalization-related effects on PRO recovery.

9. **Multiple comparison burden:** Despite Benjamini-Hochberg correction, the high-dimensional 'omics analyses across 92 proteins and 658 metabolic features carry residual false-discovery risk.

## Model / Tool Availability

- All analysis code deposited at: https://bitbucket.org/kleinstein/impacc-public-code/src/master/convalescent_manuscript/ (publicly available at publication)
- Raw LC-MS metabolomics data: Metabolights repository, accession MTBLSS0
- IMPACC clinical and immunological data: NIAID Immunology Database and Analysis Portal (ImmPort), accession SDY1760 (restricted access under NIH public data sharing policy for IRB-exempted public health surveillance studies; access via https://accessclinicaldata.niaid.nih.gov)

## Follow-up

- **Talla et al. (2023, in this project — stub):** The IMPACC multi-omics longitudinal study; read for deeper mechanistic context from the same cohort.
- **Ryan et al. 2022 (in this project):** Long-term peripheral immune perturbation after SARS-CoV-2 — complements the acute-phase immune features described here with convalescent-phase immune dynamics.
- **Peluso et al. 2024 (in this project):** Antigen persistence in post-acute COVID-19 — the viral burden / antibody imbalance described here is mechanistically upstream of persistent antigen; the two papers connect the acute-phase failure to the chronic post-acute state.
- **Zhang et al. 2023 (Nat. Med. 29, 226–235):** Data-driven identification of post-acute SARS-CoV-2 infection subphenotypes — independent subtyping approach for external validation of the IMPACC cluster structure.
- **Reese et al. 2022 (NIH N3C / RECOVER Programs):** Generalizable long COVID subtypes — compare with IMPACC cluster structure from a non-hospitalized cohort.
- **Mechanistic question:** Does the IgG/Ct ratio at acute illness represent a practical clinical biomarker for identifying patients at admission who will develop PASC? Prospective validation in a separate cohort with PASC outcome data would be the key next step.
- **FGF21 and ME/CFS overlap:** FGF21 elevation reported in ME/CFS patients (Domingo et al. 2021, cited in paper) — this paper's FGF21 elevation in MLT/COG clusters warrants a direct cross-PAIS comparison with ME/CFS cohort data in this project.
