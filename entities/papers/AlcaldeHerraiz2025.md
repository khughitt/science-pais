---
id: paper:AlcaldeHerraiz2025
type: paper
title: "Sociodemographic factors, biomarkers and comorbidities associated with post-acute COVID-19 sequelae in UK Biobank"
status: active
ontology_terms:
  - long COVID
  - post-acute complications of SARS-CoV-2
  - sex hormone-binding globulin
  - UK Biobank
  - biomarker risk factors
  - post-acute sequelae of SARS-CoV-2
  - sex differences
  - case-control study
dataset_usage: []
datasets: []
source_refs:
- cite:AlcaldeHerraiz2025
related:
- task:t015
- task:t016
- task:t017
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- topic:menopause-sex-hormones-and-pais-risk
created: "2026-06-19"
updated: "2026-06-19"
---

# Sociodemographic factors, biomarkers and comorbidities associated with post-acute COVID-19 sequelae in UK Biobank

<!--
- **Authors:** Marta Alcalde-Herraiz, Shahed Iqbal, Jeffrey J. Wallin, Yunhao Liu, Wildaliz Nieves, Mark Berry, Marti Catala, Daniel Prieto-Alhambra, Junqing Xie
- **Affiliations:** Centre for Statistics in Medicine, NDORMS, University of Oxford; Gilead Sciences, Inc.; Erasmus University Medical Center
- **Year:** 2025
- **Journal:** Nature Communications, Vol 16, p. 7009
- **DOI:** 10.1038/s41467-025-62354-0
- **PMID:** 40738888
- **PMC:** PMC12311030
- **BibTeX key:** AlcaldeHerraiz2025
- **Source:** Europe PMC full text (XML)
-->

> **Note on paper title:** The stub title in this repo ("Pre-infection sex
> hormone-binding globulin and the risk of long COVID in UK Biobank") does not
> match the published title. The actual paper is a broad hypothesis-free
> biomarker/sociodemographic screen across 55 pre-specified candidate
> determinants; SHBG is one of 30 biomarkers tested and its sex-stratified
> result is a secondary/sensitivity finding. The stub characterization reflects
> how the t015 search framed this paper's SHBG result, not the primary scope.

> **Relevance for t016/t017:** Surfaced by the t015 cohort search as the
> nearest existing UK Biobank analysis using pre-infection baseline measures to
> predict long-COVID risk. SHBG (field 30830) emerged in sex-stratified
> sensitivity analyses as protective in females only. The paper does **not**
> examine menopause stage, HRT, or oestradiol vs long COVID — the exact gap
> t016 targets. However, its outcome engineering (LC via self-report
> questionnaire; PACS via HES ICD-10 codes) and covariate handling provide a
> directly reusable template for the t017 UKB schema.

## Key Contribution

Two parallel nested case-control studies in UK Biobank (UKB) — one using patient-reported long-COVID (LC) symptoms, one using clinically-coded post-acute complications of SARS-CoV-2 (PACS) via HES — characterise pre-infection sociodemographic, biomarker, and comorbidity risk factors for these two distinct PCC phenotypes. The paper's primary contribution is to demonstrate that LC and PACS have divergent risk profiles (opposite age and sex direction; partially overlapping biomarker signatures), arguing they should be tracked and studied as distinct phenotypes. A secondary sex-stratified sensitivity analysis finds that pre-infection SHBG is associated with lower LC and PACS risk in females but not males, which is the result that attracted the t015 search.

## Methods

**Study design:** Two case-control studies nested within a cohort of UKB participants with confirmed COVID-19, 2020–2022.

**Cohort sizes:**
- LC cohort: 8,668 participants total (2,751 cases [32%]; 5,917 controls [68%])
- PACS cohort: 108,407 participants total (1,940 cases [2%]; 106,467 controls [98%])

**Sex restriction:** Neither study restricted to females; both sexes included. Sex-specific SHBG analysis was a secondary sensitivity analysis (sex-stratified subgroup).

**Age at baseline:** UKB recruited ages 40–69 (2006–2010); COVID-19 infection occurred 2020–2022, so participants were approximately 50–80 at index date. Mean age at infection: LC cohort ~66 years; PACS cohort ~67 years (cases older: ~72).

**Time window:** COVID-19 infections 2020 through end of 2022.

**Baseline period:** Biomarkers and sociodemographics from UKB first assessment visit, 2006–2010.

**Analysis:** LASSO penalised logistic regression for variable selection (k-fold CV), followed by multivariable logistic regression. Natural cubic splines (3 knots) tested for biomarker non-linearity (ANOVA comparison vs linear). VIF > 5 exclusion to control collinearity.

**Missing data:** Variables with "I don't know" or "prefer not to answer" treated as missing. Variables with >50% missing data excluded. Multiple imputation (MICE package) for variables with <50% missing.

**Software:** R 4.3.0; packages: mice, dplyr 1.1.3, ggplot2 3.5.1, glmnet 4.1.8.

---

### Long-COVID (LC) Outcome Definition

**Source:** UKB Health and Well-Being online questionnaire (self-report), completed June 2022 to May 2023; 201,684 participants, 45 COVID-related symptom questions. Field IDs for specific questions listed in Supplementary Table 5 (not provided verbatim in the main text).

**Case definition:** Participants reporting one or more WHO Delphi consensus LC symptoms at questionnaire completion, where the positive COVID-19 PCR test occurred 30 days to 1 year before questionnaire completion. Symptoms were mapped from the questionnaire to the WHO definition (mapping in Supplementary Table 6; not given verbatim in main text). Pre-existing symptoms excluded (Supplementary Note 2).

**Time threshold used:** Symptoms persisting beyond 30 days post-infection. The paper explicitly notes this differs from WHO's 90-day definition; 30 days was used because NHS guidance advises GP contact at 4 weeks and prior studies used a 30-day threshold. A 90-day sensitivity analysis was also conducted (results consistent).

**Index date / time origin:** Date of the most recent positive COVID-19 PCR test, occurring 30 days to 1 year before questionnaire completion. Only the most recent qualifying infection was used (Supplementary Fig. 11).

**Data source for infection:** Public Health England's Second-Generation Surveillance System, linked to UKB — three component datasets covering England (early 2020–September 2022), Scotland (2020–November 2022), Wales (2020–December 2022). PCR-confirmed positive test results only. Field numbers for these linkage tables are not cited verbatim in the main text.

**LC control definition:** COVID-19-infected participants who did not report any WHO-listed LC symptoms beyond 30 days.

---

### PACS Outcome Definition

**Source:** Hospital Episode Statistics (HES), linked to UKB; diagnostic and procedure data 1997–October 2022, England residents only.

**Case definition:** A PACS-associated ICD-10 diagnosis recorded in HES between 30 days and 1 year after positive COVID-19 test. The ICD-10 code list was drawn from clinical knowledge and prior literature (Supplementary Table 7; codes not given verbatim in main text). Does not include the long-COVID-specific code U09.9; targets cardiovascular/thromboembolic/organ-damage complications (e.g. angina, MI, PE). HES captures hospitalisation data only — GP/primary-care PACS not captured.

**Time threshold:** Diagnoses between 30 days and 1 year post-infection; diagnoses in the year before infection or within 30 days post-infection were excluded to avoid prevalent/acute cases.

**Index date:** Date of earliest positive COVID-19 PCR test (not most recent, unlike LC). Multiple infections — earliest used.

**PACS control definition:** All other COVID-19-infected UKB participants without a qualifying PACS diagnosis.

---

### COVID-19 Infection Ascertainment

**Source:** Public Health England's Second-Generation Surveillance System (PHE SGSS), linked to UKB; PCR-confirmed positive tests only. Three sub-datasets (England / Scotland / Wales) as above. Of the 275,234 UKB participants with valid COVID linkage, 46,793 tested positive and completed the Health and Well-Being questionnaire (LC study); 115,007 tested positive and had valid HES linkage (PACS study). Field IDs for the COVID surveillance linkage tables (e.g. field 40100 / covid19_result tables) are not cited verbatim in the main text — the paper refers only to the PHE SGSS linkage and Supplementary Figs 11–12.

---

### Covariates

**Sociodemographic (6 variables):**
- Age at COVID-19 infection (continuous; categorised for modelling: <55, 55–65, 65–75, ≥75)
- Sex (binary; from UKB baseline)
- BMI (from UKB baseline; categorised as normal/overweight/obese for modelling)
- Index of Multiple Deprivation (IMD; continuous; categorised for modelling — specific cut-points in Supplementary Note 4)
- Ethnicity (White vs non-White)
- Smoking status (never/previous/current; from UKB baseline)

**Comorbidities (19 variables):** Selected based on the Charlson Comorbidity Index; phenotyped using linked HES ICD-10 codes prior to COVID-19 test date. Conditions include: AIDS, asthma, cancer (non-metastatic and metastatic), cerebrovascular disease, congestive heart failure, CKD, COPD, dementia, diabetes (with and without organ damage), fracture, hemiplegia, liver disease (mild, moderate/severe), MI, peptic ulcer, peripheral vascular disease, rheumatoid arthritis.

**Biomarkers (30 variables; from UKB baseline 2006–2010):** All z-score standardised before analysis. Includes: alanine aminotransferase (ALT), albumin, alkaline phosphatase (ALP), apolipoprotein A, apolipoprotein B, aspartate aminotransferase (AST), C-reactive protein (CRP), calcium, cholesterol, creatinine, cystatin C, direct bilirubin, direct LDL, gamma-glutamyltransferase (GGT), glucose, HbA1c, HDL-cholesterol, IGF-1, lipoprotein(a), phosphate, SHBG (field 30830), testosterone (field 30850), total bilirubin, total protein, triglycerides, urate, urea, vitamin D. Oestradiol (field 30800) is not mentioned in the paper; it was not included in the biomarker panel — see SHBG/hormone handling below.

**SHBG/sex-hormone handling:** SHBG (UKB field 30830) and testosterone (UKB field 30850) were included in the main biomarker panel as continuous variables (z-scored). In the main multivariable analysis, testosterone was excluded due to high collinearity with creatinine (|r| > 0.5; VIF criterion). A pre-specified sex-stratified sensitivity analysis examined SHBG (and testosterone where not collinear) separately in females and males. Oestradiol (field 30800) was not examined — the assay detection floor issue (175 pmol/L censoring) is not mentioned in the paper; oestradiol was not part of the biomarker set. Field IDs 30830/30850 are not cited numerically in the main text; the paper refers to the markers by name only.

## Key Findings

**LC risk factors (adjusted multivariable, statistically significant):**
- Sociodemographics: Female sex (OR 1.25, 95% CI 1.14–1.35), younger age <55 vs ≥75 (OR 1.23, 95% CI 1.00–1.42), obesity (OR 1.20, 95% CI 1.02–1.41), socioeconomic deprivation (OR 1.41, 95% CI 1.22–1.63)
- Biomarkers (adjusted): Lower HDL-cholesterol (OR 0.83, 95% CI 0.70–0.98 for Q4), higher triglycerides (OR 1.08, 95% CI 1.01–1.15), higher vitamin D (OR 1.05, 95% CI 1.00–1.11), lower IGF-1 (OR 0.93, 95% CI 0.88–0.98)
- Comorbidities: CKD (OR 1.48, 95% CI 1.11–1.97), COPD (OR 1.29, 95% CI 1.08–1.54), metastatic cancer protective (OR 0.49, 95% CI 0.28–0.86)
- SHBG in crude analysis: Higher SHBG associated with lower LC risk (OR_crude 0.92, 95% CI 0.87–0.97); this did not survive multivariable adjustment in the main model but was significant in the female-stratified sensitivity analysis

**PACS risk factors (adjusted, statistically significant):**
- Older age ≥75 vs <55 (OR 2.41, 95% CI 1.70–3.42), male sex (OR 1.40, 95% CI 1.24–1.59), obesity (OR 1.39, 95% CI 1.19–1.62), deprivation (OR 1.36, 95% CI 1.17–1.58), smoking (OR 1.30, 95% CI 1.11–1.51)
- Biomarkers: higher alkaline phosphatase (OR 1.35, 95% CI 1.14–1.59, Q5), higher HbA1c (OR 1.29, 95% CI 1.09–1.54, Q5), higher cystatin C (OR 1.09, 95% CI 1.03–1.15), lower IGF-1 (OR 0.84, 95% CI 0.72–0.98)
- Most comorbidities associated with increased PACS risk; exceptions: cerebrovascular disease, dementia, fracture, hemiplegia, liver disease

**SHBG sex-stratified sensitivity analysis:** Higher SHBG was associated with decreased risk of both LC and PACS in females only (not males). Specific OR estimates for the sex-stratified result are in Supplementary Figs 5 and 6 (not given verbatim in main text).

**Key divergence between LC and PACS:** Age operates in opposite directions (younger → higher LC risk; older → higher PACS risk); sex operates in opposite directions (female → higher LC; male → higher PACS). The paper frames LC as symptom-dominated and immune-mediated, PACS as organ-damage-dominated and severity-driven.

## Relevance

This paper is directly relevant to the t016/t017 UKB analysis design. It establishes:

1. That UKB-linked COVID surveillance data (PHE SGSS PCR data) + the Health and Well-Being questionnaire + HES ICD-10 data are adequate and co-deployable to generate two separable PCC phenotypes.
2. That SHBG (pre-infection baseline, field 30830) associates with lower LC/PACS risk in females — providing a proof-of-concept that pre-baseline reproductive hormones predict long-COVID phenotypes in the exact cohort t016 targets.
3. The outcome engineering template (self-report questionnaire-mapped to WHO symptoms at 30+ days; HES PACS codes at 30+ days) for reuse in t017.
4. That LC and PACS must be separated as distinct outcomes; effect directions for sex and age are reversed between them.

The paper does not test menopause status, HRT use, or oestradiol — leaving the central t016 exposure space open.

## Project Framework Mapping

- **Hypothesis 0005 (reproductive-stage immune homeostatic margin):** The SHBG→LC female-specific association is consistent with this hypothesis's proposition that pre-infection endocrine state modifies risk of failed recovery. SHBG is a marker of sex-hormone bioavailability (inversely related to free testosterone and oestrogen), making this finding mechanistically ambiguous (could reflect higher free testosterone protection, lower free oestrogen protection, or confounding by metabolic state). The paper does not propose a mechanism.
- **Hypothesis 0001 (shared dysregulated attractor):** The divergent risk profiles of LC vs PACS suggest different entry paths into failed recovery — LC more immune/autonomic dysregulation, PACS more acute severity/organ damage — consistent with multiple attractor-entry routes.
- **Hypothesis 0003 (immune exhaustion feedback):** Pre-infection CRP elevation → LC risk is consistent with a "pre-primed" inflammatory state lowering the threshold for failed immune resolution.
- **Topic: menopause-sex-hormones-and-pais-risk:** This paper provides the UKB outcome engineering template and the SHBG proof-of-concept for that topic.

## Limitations

1. **LC ascertainment via self-report:** Subjective questionnaire data is inherently prone to recall bias, misclassification, and variability in symptom reporting. Cases defined by ≥1 WHO symptom beyond 30 days is a low threshold; sensitivity analysis with ≥3 symptoms gave consistent direction but much smaller case count (594, 3%).
2. **30-day threshold:** The paper uses 30 days (not the WHO-canonical 90 days) as the LC time threshold, which may inflate case count and pull in subacute cases. A 90-day sensitivity analysis was run and results were consistent, but the main estimates use 30 days.
3. **PACS defined by HES hospitalisation codes only:** Primary-care / GP PACS not captured. This likely leads to substantial undercounting of mild-to-moderate post-COVID complications and biases PACS toward older, sicker, hospitalised patients. The paper explicitly notes this limitation.
4. **UKB survivor/healthy bias:** UKB participants are healthier and older than the general UK population; results may not generalise.
5. **Baseline biomarker measurement 10–15 years before COVID index date:** Biomarkers measured at UKB enrolment (2006–2010); substantial time-lag to COVID exposure. Random misclassification likely attenuates associations rather than inflating them, but secular changes in biomarker levels are unaddressed.
6. **No vaccination data:** Vaccination could confound or mediate LC/PACS risk; not captured.
7. **No oestradiol:** Field 30800 oestradiol, which has a detection floor of 175 pmol/L causing left-censoring in post-menopausal women, was not included in the analysis. The oestradiol floor censoring problem for UK Biobank analyses of post-menopausal women is not addressed or mentioned.
8. **Testosterone collinearity:** Testosterone dropped from multivariable model due to |r| > 0.5 with creatinine; sex-hormone panel is therefore incomplete.
9. **White majority:** >94% White in both cohorts; limited generalisability to other ethnic groups.
10. **No GP/primary-care linkage:** The long-COVID-specific ICD-10 code U09.9 (which resides mainly in primary-care records) was not used; only questionnaire self-report (LC) and HES hospitalisation (PACS) were employed.
11. **Specific UKB field IDs not cited:** The paper does not enumerate UKB field IDs or COVID linkage table names for the SGSS COVID data, Health and Well-Being questionnaire fields, or biomarker fields in the main text; these are referenced via Supplementary Tables 5–7 (not reproduced).

## Model / Tool Availability

No model or tool released. R code not published. Analysis described in sufficient detail to replicate using standard R packages (mice, glmnet, ggplot2, dplyr).

## Follow-up

- **t017 (immediate):** Use this paper's outcome engineering directly: LC outcome = ≥1 WHO symptom from Health and Well-Being questionnaire, PCR-confirmed positive 30–365 days before questionnaire; PACS outcome = HES ICD-10 PACS codes 30–365 days post-infection. Obtain Supplementary Table 7 (PACS ICD-10 codes) and Supplementary Table 6 (questionnaire-to-WHO symptom mapping) from the paper's supplementary material to inform the t017 code list.
- **t016 (design gap):** This paper confirms SHBG → LC protection in females. t016 should specifically test menopause stage, oestradiol (with floor-censoring treatment), and HRT, which this paper did not test.
- **Oestradiol floor:** t017/t016 should explicitly address the 175 pmol/L floor censoring for oestradiol (field 30800) — this paper provides no guidance on that.
- **Consider requesting supplementary tables:** Supplementary Tables 5, 6, 7 from this paper contain the specific questionnaire field-to-symptom mapping and PACS ICD-10 codes needed to replicate outcome engineering.
- **PACS ICD-10 code overlap:** The PACS code list (Supp Table 7) should be compared against U09.9 usage to understand what is captured vs missed.
