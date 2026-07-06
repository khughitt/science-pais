---
id: paper:Huang2024
kind: paper
title: Discriminating Myalgic Encephalomyelitis/Chronic Fatigue Syndrome and comorbid
  conditions using metabolomics in UK Biobank
status: active
ontology_terms:
- ME/CFS
- NMR metabolomics
- lipoprotein metabolism
- machine learning biomarker
- UK Biobank
- sex-specific metabolism
- VLDL triglycerides
- surface lipids
- multivariate disease score
dataset_usage: []
source_refs:
- cite:Huang2024
related:
- topic:mecfs-long-covid-convergence
- topic:biomarkers-and-objective-endpoints
- topic:menopause-sex-hormones-and-pais-risk
- question:0011-mitochondrial-basis-of-pem
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
- paper:Naviaux2016
created: '2026-06-20'
updated: '2026-06-20'
---

# Discriminating Myalgic Encephalomyelitis/Chronic Fatigue Syndrome and comorbid conditions using metabolomics in UK Biobank

- **Authors:** Katherine Huang, Alex G.C. de Sá, Natalie Thomas, Robert D. Phair, Paul R. Gooley, David B. Ascher, Christopher W. Armstrong
- **Year:** 2024
- **Journal:** Communications Medicine (4:248)
- **DOI/URL:** https://doi.org/10.1038/s43856-024-00669-7
- **BibTeX key:** Huang2024
- **Source:** Full-text PDF (papers/pdfs/2024_Huang_discriminating-mecfs-metabolomics-uk-biobank.pdf), read 2026-06-20.

## Key Contribution

This study applies large-scale NMR metabolomics from the UK Biobank to 1,194 ME/CFS participants alongside seven homogeneous comorbid cohorts (hypertension, depression, asthma, IBS, hay fever, hypothyroidism, migraine; total comorbid n up to 13,559 per condition) and a non-diseased control group (n = 53,009), identifying 168 significant individual biomarker associations with ME/CFS and building a LightGBM-based multi-variable disease score using 19 baseline characteristics and nine NMR biomarkers (AUC = 0.83, recall = 0.70 on a blind test set). The study's primary advance is situating ME/CFS metabolomics within a comorbidity-aware framework — demonstrating that the ME/CFS NMR profile is dominated by a lipoprotein/surface-lipid signature, is highly pleiotropic with comorbid conditions, and contains pronounced sex-specific differences in energy metabolism, particularly in females.

## Methods

**Dataset.** Participants were drawn from the UK Biobank (UKB), a prospective cohort of >500,000 volunteers aged 39–70 enrolled across 22 UK assessment centres 2006–2010. UK Biobank is an access-controlled resource requiring a formal application; this study operated under UKB Project #79568. ME/CFS cases (n = 1,194) were identified by self-report of a doctor-confirmed diagnosis at the baseline interview (data field 20002). Seven homogeneous comorbid cohorts were formed from participants who reported only the single comorbid condition of interest; a non-diseased cohort (C2, n = 53,009) served as the negative control. Baseline NMR metabolomics were available for 274,353 UKB participants in total; ME/CFS cases with NMR data numbered 1,194 (out of 2,161 self-reporters in the full UKB, i.e. ~0.4% of the NMR subset).

**Metabolite platform.** Nightingale Health NMR metabolomics panel — 249 measurements comprising 107 non-derived biomarkers and 61 composite biomarkers, plus 81 biomarker ratios. Classes include lipoprotein particle subclass concentrations/sizes, surface lipids (cholesterol esters, free cholesterol, phospholipids, sphingomyelins, phosphatidylcholines, total cholines), fatty acid fractions and ratios, amino acids (including BCAAs), ketone bodies (3-hydroxybutyrate, acetate, acetoacetate, acetone), glycolysis-related metabolites (glucose, lactate, pyruvate, citrate), and an inflammation marker (GlycA). The 249-measurement panel is the standard Nightingale Health UKB release that has been used in multiple UKB-scale epidemiology studies.

**Statistical analyses.** Logistic regression with sex, age, cholesterol-lowering medication, and fish oil supplements as covariates; Bonferroni thresholds adjusted for the number of biomarkers tested (P < 0.05/249 for ME/CFS; P < 0.05/8 for cross-cohort comparisons). Variance decomposition (variancePartition) used 61 baseline characteristics to parse explained variance of individual biomarkers. Sensitivity E-values were computed for unmeasured confounding.

**Machine learning workflow.** A two-stage pipeline: (1) LASSO feature selection with 10-fold cross-validation to filter features; (2) forward feature selection coupled with LightGBM, adaptive boosting, random forest, extreme gradient boosting, and explainable boosted machine. Models requiring recall > 0.7 and AUC > 0.8 on cross-validation were retrained; LightGBM was chosen as optimal (28 features: 19 baseline + 9 NMR). Multiple class-imbalance strategies were tested (undersampling ratios 1:1–1:20, SMOTE-NC, cluster-based undersampling). SHAP values were used for feature interpretation.

**Sex-stratified analyses.** Association testing was repeated separately in females (n = 882) and males (n = 312), and again in a sub-cohort of participants with disease duration < 2 years (n = 181).

## Key Findings

**Overall metabolic signature (168 significant biomarkers, P < 2.01 × 10⁻⁴).** The ME/CFS profile is dominated by lipoproteins: increased VLDL particle concentration and all VLDL lipid components (free cholesterol, cholesterol esters, phospholipids, triglycerides); decreased large HDL components (HDL-C, HDL-CE, HDL-PL) and decreased LDL-TG; decreased ApoA1 and ApoB/ApoA1 ratio. The strongest individual association was total triglycerides to phosphoglyceride ratio (TG/PG), with an OR of 1.46 per 1-SD increase (95% CI 1.38–1.56, P = 3.95 × 10⁻³³). VLDL size showed the largest non-derived effect (OR 1.41, 95% CI 1.32–1.50, P = 1.26 × 10⁻²⁴). Conversely, HDL-CE was inversely associated (OR 0.65, 95% CI 0.61–0.70, P = 4.96 × 10⁻³²).

**Surface lipids.** Total cholines, phosphatidylcholines, sphingomyelins, and phosphoglycerides were significantly decreased, consistent with altered membrane fluidity and dysregulated immune cell function.

**Low molecular weight metabolites (LMWM).** Elevated alanine and increased BCAA concentrations. Inverse associations with citrate, acetate, and acetone. No significant aromatic amino acid anomalies, in contrast to some prior serum/plasma studies.

**GlycA (inflammation marker).** Elevated (OR 1.39, 95% CI 1.31–1.47, P = 2.56 × 10⁻²⁸), representing the top explainable single biomarker for ME/CFS variation; C-reactive protein explained 20.5% of GlycA variance.

**Pleiotropic overlap with comorbidities.** 234 of 942 total significant associations at the trait-wise Bonferroni threshold were pleiotropic (present in ME/CFS and at least one comorbid condition). Hypertension shared 81% of ME/CFS associations, depression 85%, asthma 73%, IBS (97%), hay fever (46%), hypothyroidism (88%), migraine (89%). Only XXL-VLDL-TG % was uniquely associated with ME/CFS. Twenty-nine additional significant associations not found in any comorbid cohort included increased total branched-chain amino acids and inverse associations with citrate, acetate, and acetone.

**Sex differences.** In females (n = 882), 62 significant biomarker associations were identified; in males (n = 312), 14. Seven biomarkers were female-specific: polyunsaturated fatty acids (PUFA), linoleic acid (LA), M-VLDL-C, L-LDL-P, M-LDL-L, M-LDL-PL, and L-VLDL-TG%. Four additional biomarkers were male-specific (IDL-C, IDL-CE, S-HDL-P, S-LDL-C%). In females, elevated alanine and PUFA% were prominent, with inverse associations with ketone bodies, interpreted as a shift from amino acid catabolism toward lipid anabolism / anaplerosis — distinct from a male pattern that did not reveal discrete alternative energy pathways. The authors propose this sex asymmetry in energy metabolism may partly explain the female preponderance in ME/CFS (3:1 female-to-male ratio observed in this cohort). HDL maturation perturbations were also noted as gender-dependent rather than gender-specific.

**Variance decomposition.** The maximum variance explained in any single NMR biomarker by 61 baseline characteristics was ~20% (GlycA by C-reactive protein). Key explainable biomarkers in ME/CFS were GlycA, XL-HDL-FC%, creatinine, L-HDL-PL%, HDL-CE, and lactate. Lifestyle/environmental and psychological factors contributed < 1.3% average explained variance, suggesting the NMR signal is not driven primarily by behavioural confounders.

**Machine learning score.** The LightGBM model selected 28 features (19 baseline characteristics + 9 NMR biomarkers). The 9 NMR biomarkers selected were: Total-P, M-VLDL-P, S-LDL-P, S-LDL-TG, L-VLDL-FC, PUFA%, acetone, acetoacetate, and Immature Reticulocyte Fraction (a blood count feature). Performance on the blind test set: AUC = 0.83, recall = 0.70. The multi-variable score exhibited an OR of 3.61 (CI 3.45–3.78, P ≈ 0) per 1-SD increment — approximately 2.5× stronger than the top individual biomarker (TG/PG). Top features by mean SHAP value were frequency of tiredness/lethargy, whole body pain, sleep duration, headache pain, and female sex, followed by Total-P and S-LDL-TG. False positive rate was 0.20; false negative rate 0.30. The top 5 percentile bins captured 56% of ME/CFS cases.

**Disease severity stratification.** High ME/CFS score percentile participants showed greater ORs for TG/PG (1.46 → 1.74) and GlycA (1.39 → 1.64). Low-percentile ME/CFS participants showed negligible effects and may represent individuals near functional capacity who require a biological "stressor" for molecular perturbations to become detectable.

**Comparison to prior ME/CFS metabolomics.** The study corroborates prior findings of surface lipid decreases and elevated VLDL, and extends them to a large, population-based, comorbidity-adjusted cohort. It does not replicate the aromatic amino acid signal reported in some targeted studies. The authors note that the Nightingale NMR panel measures absolute concentrations of lipoproteins and LMWM, differing from Raman spectroscopic platforms used in some other studies.

## Relevance

**Relation to Naviaux2016 hypometabolic signature.** Naviaux et al. (2016) described a broad chemical hypometabolism in ME/CFS serum spanning 20 metabolic pathways including sphingolipid, phospholipid, purine, amino acid, and cholesterol metabolism. Huang2024 finds convergent evidence on phospholipids (decreased sphingomyelins, phosphatidylcholines, total cholines) and on the amino acid front (elevated BCAA/alanine; inverse citrate/acetate/acetone), but the two studies differ in platform (targeted LC-MS/MS vs Nightingale NMR), biofluid handling, and control strategy. The surface-lipid decrease and the membrane-fluidity hypothesis in Huang2024 aligns with the sphingolipid disruption central to Naviaux2016. Huang2024 did not identify the broad purine or organic acid abnormalities Naviaux2016 observed, likely due to panel scope (Nightingale covers lipoproteins and LMWM but not purines or acylcarnitines). The VLDL-dominant lipoprotein expansion in Huang2024 is not prominently featured in Naviaux2016, possibly reflecting the lipoprotein-specificity of NMR vs the small-molecule specificity of LC-MS/MS.

**Relevance to hypothesis:0001-shared-dysregulated-attractor.** The large-scale lipoprotein/surface-lipid disruption and elevated GlycA, combined with the dose-response relationship between comorbidity burden and metabolomic signal strength, are consistent with the view of ME/CFS as a self-reinforcing dysregulated state — individuals with more comorbidities displayed more pronounced metabolic perturbations, and the lowest-scoring individuals show negligible biomarker signal. This gradient supports the attractor framing.

**Relevance to question:0011-mitochondrial-basis-of-pem.** The inverse associations with ketone bodies (acetate, acetone, acetoacetate) in ME/CFS, particularly the female-specific pattern, suggest reduced ketolytic flux. The elevated alanine and BCAAs may reflect increased amino acid catabolism to feed the TCA cycle under impaired mitochondrial lipid oxidation — consistent with the PEM-linked mitochondrial insufficiency hypothesis. The absence of clear glycolysis perturbation (glucose not significantly altered) argues against a simple aerobic glycolysis switch and rather points to substrate-level constraints upstream.

**Relevance to question:0001-shared-molecular-signature-across-triggers.** The highly pleiotropic overlap between ME/CFS and comorbid metabolomic profiles (81–97% shared associations with hypertension/IBS/depression/hypothyroidism) cautions against treating any individual NMR biomarker as ME/CFS-specific. The study motivates composite multi-condition scores rather than single-marker diagnostics for identifying a genuine ME/CFS-specific perturbation layer.

**Relevance to topic:biomarkers-and-objective-endpoints.** The LightGBM score (AUC 0.83, recall 0.70) is the largest ML-based ME/CFS discrimination model from population-level NMR data. The 9-NMR-biomarker panel plus 19 baseline characteristics provides a concrete candidate feature set for replication in independent cohorts (DecodeME, UK ME/CFS Biobank, All of Us are cited as targets). The score has potential as a continuous disease-severity proxy for stratification in clinical trials.

**Relevance to topic:menopause-sex-hormones-and-pais-risk.** This paper uses the same UK Biobank Nightingale NMR metabolomics infrastructure that the menopause→PAIS analysis targets. The feasibility details are highly transferable: (a) the Nightingale panel returns 249 measurements including lipoprotein subclasses, fatty acids, LMWM, and GlycA; (b) disease labels come from self-reported diagnosis at baseline verbal interview (data field 20002); (c) analyses adjust for sex, age, cholesterol-lowering medication, and fish oil supplements; (d) missing values were median-imputed for continuous variables; (e) IQR-based outlier removal was applied (4×IQR±median for biomarkers, 5×SD±mean for baseline characteristics); (f) the ME/CFS cohort was 74% female, and sex-stratified NMR analysis is both feasible and biologically informative at this scale. The sex-specific energy metabolism differences found here (female shift toward amino acid catabolism / anaplerosis; female-specific PUFA and VLDL perturbations) are directly relevant to understanding how hormonal state (e.g. menopausal transition) might modulate the ME/CFS metabolic phenotype.

**Relevance to topic:mecfs-long-covid-convergence.** The authors note that reduced cortisol levels have been found in both ME/CFS meta-analyses and as a distinguishing feature of Long COVID. The absence of aromatic amino acid anomalies in UKB/Nightingale NMR (despite identification in some Raman spectroscopy studies of peripheral blood mononuclear cells) highlights platform-dependent signal differences that are relevant when comparing ME/CFS and Long COVID metabolomics literature.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| TG/PG ratio (top individual biomarker) | Metabolic dysregulation / thromboinflammation | VLDL-TG excess and phospholipid reduction maps to membrane and lipid transport dysfunction |
| Surface lipid decrease (sphingomyelins, phosphatidylcholines, total cholines) | Membrane / immune cell dysfunction | Aligns with Naviaux2016 sphingolipid disruption |
| GlycA elevation | Persistent low-grade inflammation | GlycA reflects glycoprotein acetyls on acute-phase proteins |
| VLDL particle expansion | Lipoprotein transport failure | Authors link to LPL dysregulation via microRNA-29a overexpression |
| Female-specific amino acid catabolism + ketolysis suppression | Sex-specific metabolic vulnerability | Directly relevant to menopause/hormonal modulation hypothesis |
| LightGBM ME/CFS score | Composite objective endpoint | Candidate for replication in DecodeME / All of Us cohorts |
| Comorbidity-aware cohort design | PAIS case-definition heterogeneity | Use of seven homogeneous comorbid positive controls is a methodological model for PAIS studies |

## Limitations

1. **Self-reported diagnosis.** ME/CFS status was ascertained by self-report of a doctor-confirmed diagnosis at the baseline interview (data field 20002). No standardised diagnostic criteria (Fukuda, CCC, ICC) were applied, and the case definition is not validated against clinical assessment. This is a major limitation acknowledged by the authors; it likely includes misdiagnosed individuals and excludes undiagnosed ME/CFS.

2. **Older, predominantly white, volunteer cohort.** Mean age ~55; UKB volunteers are healthier on average ("healthy volunteer bias"), skewing toward milder ME/CFS. The cohort is predominantly white British, limiting generalisability to other ethnicities.

3. **Baseline NMR only.** Longitudinal NMR data were unavailable for most participants; only 181 ME/CFS participants had NMR data at a follow-up visit. The cross-sectional design precludes inference about whether metabolic changes precede, accompany, or follow symptom onset.

4. **Panel scope.** The Nightingale NMR panel covers lipoproteins, fatty acids, LMWM, and a small set of amino acids/ketones/glycolysis metabolites, but does not cover purines, acylcarnitines, bile acids, prostaglandins, or tryptophan pathway metabolites — limiting comparison with LC-MS/MS-based ME/CFS metabolomics (e.g. Naviaux2016).

5. **Medication confounding.** The majority of the ME/CFS cohort was taking medication and supplements at baseline. Analyses adjusted for cholesterol-lowering medication and fish oil but not for other medications (antidepressants, pain medications, sleep aids), which may have influenced biomarker concentrations.

6. **No POTS or FM comorbid cohort.** POTS affected only 2.5% of the ME/CFS cohort (underreported in UKB), and fibromyalgia similarly. These common ME/CFS comorbidities could not be analysed as homogeneous cohorts.

7. **High false positive rate.** The LightGBM score had a false positive rate of 0.20 and false negative rate of 0.30 on the blind test set; the model was developed for exploratory/hypothesis-generation purposes, not clinical deployment.

8. **Disease heterogeneity.** ME/CFS is heterogeneous across case definition, severity, disease duration, and comorbidity burden. The UKB cohort does not capture PEM or specific symptom severity via standardised instruments (SF-36, MFI-20 data were collected only at follow-up visits after the NMR blood draw).

## Model / Tool Availability

The analysis code and supplementary data are published as supplementary materials to the article. The underlying UKB data are accessible through a formal application to the UK Biobank (ukbiobank.ac.uk). The LightGBM ME/CFS score weights and feature list are provided in Supplementary Data 12–14. No pre-packaged software tool or model checkpoint is released separately.

## Follow-up

**Papers to read next:**
- Naviaux2016 — already in project; compare sphingolipid/phospholipid disruption panels directly.
- Germain et al. 2022 (Metabolites) — comprehensive circulatory metabolomics in ME/CFS; cited as prior work on acyl lipid/steroid disruption.
- Hoel et al. 2021 (JCI Insight) — map of metabolic phenotypes in ME/CFS; provides context for the LMWM findings.
- Julkunen et al. 2023 (Nat. Commun.) — atlas of plasma NMR biomarkers in 118,461 UKB individuals; important baseline for interpreting Nightingale NMR effect sizes.
- Klein et al. 2023 (Nature) — Long COVID immune profiling; cited for ME/CFS–Long COVID convergence via cortisol.

**Questions this raises for the project:**
- Can the LightGBM ME/CFS score be replicated or adapted in the UKB menopause sub-cohort to test whether perimenopausal or postmenopausal women show systematically higher scores (i.e., greater metabolic similarity to the ME/CFS profile)? The data infrastructure is identical.
- The female-specific amino acid catabolism shift (elevated alanine + reduced ketone bodies) is proposed as a bioenergetic adaptation. Does this pattern worsen or improve with hormonal state (oestrogen levels, menopausal stage)? This is directly addressable in UKB with available hormone data.
- The TG/PG ratio is the strongest single biomarker. Is this driven by LPL dysfunction (as suggested by the microRNA-29a link), and if so, is LPL activity or LPL-regulating factors measurable in UKB? Angiopoietin-like proteins (ANGPTL3/4) regulate LPL and have UKB genomic instruments.
- Given that IBS shared 97% of ME/CFS metabolomic associations, what proportion of ME/CFS patients in UKB also report IBS, and does the ME/CFS score remain predictive after excluding those with IBS? (The paper created an ME/CFS+comorbidity sub-cohort but did not test IBS exclusion separately.)
