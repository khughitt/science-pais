---
id: paper:Sanford2026
kind: paper
title: 'Metabolic basis of post-infectious sequelae after Ebola virus disease'
status: active
ontology_terms:
- post-Ebola syndrome
- Ebola virus disease
- metabolomics
- post-infectious sequelae
- mitochondrial / metabolic dysfunction
- TCA cycle
- short-chain fatty acid metabolism
- preprint
dataset_usage: []
source_refs:
- cite:Sanford2026
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0001-shared-molecular-signature-across-triggers
- search:0002-cross-pathogen-pais-signatures
- discussion:0002-cross-pathogen-pais-signature-convergence
created: '2026-06-20'
updated: '2026-07-26'
---
# Metabolic basis of post-infectious sequelae after Ebola virus disease

<!--
- **Authors:** Anna Sanford, Nell Bond, Samuel Ficenec, Charlotte Osterman, Payton Farkas, Emily Engel, Bronwyn Gunn, Donald S. Grant, Robert Samuels, Kevin Zwezdaryk*, John Schieffelin* (*co-senior)
- **Affiliations:** Tulane University, New Orleans, LA, USA; Washington State University, Pullman, WA, USA; Kenema Government Hospital, Kenema, Sierra Leone
- **Year:** 2026
- **Journal:** medRxiv (preprint — not peer reviewed)
- **DOI:** 10.64898/2026.01.02.25343095
- **PMID:** 41542679 (PubMed indexes the medRxiv preprint record) / **Europe PMC preprint ID:** PPR1270156
- **BibTeX key:** Sanford2026
- **Source:** Full-text PDF (`~/.cache/science/paper-fetch/10.64898_2026.01.02.25343095.pdf`), read 2026-07-26.
- **Tier:** Core now
-->

**PREPRINT — medRxiv, posted 2026-01-06. Not certified by peer review. Treat all results as provisional and hypothesis-generating; the paper itself bears medRxiv's notice that findings should not guide clinical practice.**

## Key Contribution

This is the first untargeted metabolomic study of post-Ebola syndrome (PES), providing plasma LC-MS/MS profiles of EVD survivors with post-infectious sequelae (musculoskeletal/gastrointestinal or cardiopulmonary) compared to asymptomatic EVD survivors and household contacts (HCs). PES survivors display broad downregulation of TCA-cycle, amino-acid, nucleotide, glycolytic, and pyruvate metabolic pathways compared to asymptomatic survivors; a panel of ten metabolites drawn from these pathways achieves AUC > 0.8 on both discovery and validation cohorts in an internal split-sample analysis. The authors propose these metabolites as candidate PES biomarkers and interpret the TCA/SCFA alterations as consistent with immune dysfunction (CD8 T-cell exhaustion) seen in other chronic viral infections. The metabolic signature fills the otherwise-empty post-Ebola molecular cell in the cross-trigger PAIS matrix — but rests entirely on a single preprint from a small cohort, and the critical comparison (PES vs healthy uninfected HCs) did not reach statistical significance, leaving uncertain whether the signal represents a PAIS-specific biology or a generic EVD-survivor metabolic alteration.

## Methods

**Study design:** Cross-sectional convenience-sample comparison nested in an ongoing cohort study of EVD survivors and household contacts (Sierra Leone, previously described as Bond et al. 2021 Clin Infect Dis).

**Case definition — PES:** Defined as musculoskeletal/gastrointestinal (MSK/GI) or cardiopulmonary (CP) sequelae in EVD survivors. MSK/GI sequelae were identified by physical examination (decreased joint range of motion, extremity edema/effusion, joint tenderness, abdominal tenderness). CP sequelae were identified by multi-symptom cardiopulmonary presentation (chest pain, palpitations, shortness of breath, cough) or physical examination findings (abnormal heart sounds, murmurs, wheezes, rales, lower extremity edema, poor distal pulses). This is an OBJECTIVE CLINICAL EXAM-BASED case definition anchored to MSK/GI and cardiopulmonary phenotypes — it does NOT capture the fatigue or neurological sequelae most commonly studied in LC/ME/CFS contexts.

**Case definition — Asymptomatic survivors:** Glycoprotein (GP) IgG-positive EVD survivors classified as asymptomatic by principal components analysis clustering in a prior study; absence of MSK/GI or CP sequelae.

**Household contacts (HCs):** GP IgG-negative (uninfected) community controls, demographically matched on age, sex, and sample collection date; drawn from households overlapping those of enrolled survivors.

**Sample groups:**
- PES: n=37 (MSK/GI n=18; CP n=19)
- Asymptomatic GP IgG+ survivors: n=20
- HCs: n=20

**Time since acute infection:** Plasma samples were collected March 2016 to April 2019. The Sierra Leone Ebola epidemic peaked in 2014-2015; this implies samples were taken approximately 1–4 years post-acute illness. Per-sample time-since-infection is not individually reported.

**Covariates examined:** Age, sex, BMI, and sample collection date were tested by logistic regression as predictors of PES group membership (PES vs asymptomatic survivors). None were significant.

**Metabolomic platform:** Untargeted plasma LC-MS/MS by Gigantest Inc. (Baltimore, MD). Extraction: cold acetonitrile + formic acid. Metabolite identification using in-house databases; quantification by XCalibur software against authenticated external standards. Total metabolites identified: 544.

**Quality filtering and pre-processing (MetaboAnalyst 6.0):** Missing values (n=2,762; 8.9%) replaced with 1/5 the minimum positive value per variable. Variables with RSD > 25% removed; bottom quartile by IQR removed. Normalization to median; log10 transformation.

**Univariate analysis:** Student's t-test with Benjamini-Hochberg FDR correction; thresholds: FC > 2.0 AND FDR < 0.05.

**Multivariate:** PCA and PLS-DA (MetaboAnalyst). Spearman rank correlation (JMP). TCA-metabolite network visualization (Cytoscape).

**Biomarker analysis:** Two-thirds/one-third discovery/validation split (discovery n=39, validation n=18 from 57 total survivors). PLS-DA and Random Forest (RF) models trained on discovery set with 100 Monte Carlo cross-validation runs; top 10 metabolites from discovery models tested on validation cohort. ROC curves from 100 cross-validated runs.

**Ethics:** Tulane IRB #701226; Sierra Leone Ethics and Scientific Review Committee #021/11/2024. Written consent from adults ≥18; parental consent + child assent for 12–17 years; parental consent for <12 years.

## Key Findings

**Differential metabolites (PES vs asymptomatic survivors):**
- 544 metabolites identified total; 34 differentially expressed (FC > 2.0 and FDR < 0.05)
- 26 significantly DECREASED in PES; 8 significantly INCREASED in PES
- No significant differential metabolites between MSK/GI and CP subgroups within PES
- No significant differential metabolites when comparing PES to HCs (see Limitations — this is load-bearing)

**PLS-DA group separation:** EVD survivors with PES separated from asymptomatic survivors on metabolic profile. Best PLS-DA model: 2 components, accuracy = 0.86, R² = 0.66, Q² = 0.45.

**Pathway alterations (PES vs asymptomatic survivors; FDR < 0.05, impact score > 0.2):**
Predominantly DOWNREGULATED in PES:
- **TCA cycle:** broad downregulation (citrate-cycle metabolites including malate, succinate); TCA metabolites show dense mutual correlations in PES network analysis
- **Amino acid metabolism (multiple pathways):** taurine/hypotaurine, tyrosine, cysteine/methionine; amino acid changes are the most impactful pathways by MetaboAnalyst impact score
- **Nucleotide metabolism:** downregulated
- **Glycolysis and pyruvate metabolism:** downregulated

Predominantly UPREGULATED in PES:
- Starch and sucrose metabolism
- Tryptophan metabolism
- Arginine and proline metabolism
- Nicotinate and nicotinamide metabolism
- Pentose and glucuronate interconversions

**SCFA alterations (mixed directionality):**
- Acetate: INCREASED in PES
- Propanoate (propionate): DECREASED in PES
- Authors interpret this as consistent with gut microbiome dysregulation (analogous to reduced SCFA-producing symbionts reported in Long COVID)

**Biomarker panel (top 10, same in both PLS-DA and RF):** acrylate, glucose, acetate, 3-hydroxy-3-methylglutarate, malate, 2-Oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline, succinate, methylmalonate, threonate-1,4-lactone, propanoate.
- Discovery AUC (both models): > 0.8
- Validation AUC (both models): > 0.8
- Validation predictive accuracy: 0.799 (PLS-DA), 0.796 (RF)

**Mechanistic interpretation (authors'):** TCA dysregulation and CD8 T-cell exhaustion are linked in chronic viral infections (HIV, HBV, LCMV); SCFA changes (acetate up, propanoate down) parallel Long COVID gut-microbiome dysbiosis findings; EBOV-like particles have previously been shown to alter fatty-acid and amino-acid metabolism in cell models. Authors frame their findings as consistent with immune dysfunction driving metabolic reprogramming, though the plasma-level data cannot be directly linked to cellular mechanisms.

## Relevance

**For the cross-trigger convergence claim (`hypothesis:0001`):**

This paper is cited in `search:0002` as the sole source for the post-Ebola leg of the cross-pathogen PAIS signature matrix, graded "Thin-but-present | Sanford2026." That grade is honest, but the load-bearing question is how much weight it can carry for `hypothesis:0001`'s shared-attractor claim.

Assessment: **very limited, for four compounding reasons.**

1. **Wrong comparator for cross-trigger inference.** The significant metabolic signature is PES vs asymptomatic *survivors* — not PES vs healthy uninfected controls. The HCs comparison (the one that would show EVD-plus-sequelae vs healthy baseline) is NOT significant. This means the detected signal could reflect a survivor-specific metabolic state that is then amplified in those with sequelae — rather than a PAIS-specific pathophysiology separable from the sequelae of acute infection itself. All cross-trigger comparisons in the matrix (LC, ME/CFS) contrast PAIS vs healthy controls; the post-Ebola cell is measuring something categorically different.

2. **Phenotype mismatch with the fatigue-PAIS frame.** The PES case definition is clinical-exam-based MSK/GI or cardiopulmonary sequelae — joint range of motion, edema, chest-pain/palpitation phenotypes — not the cognitive/fatigue/PEM phenotype at the core of `hypothesis:0001`. A metabolomic signature of musculoskeletal/cardiopulmonary post-Ebola sequelae may not generalize to the neuroimmune fatigue attractor.

3. **Single unreviewed preprint, small cohort.** PES n=37, asymptomatic n=20 for the primary comparison; validation n=18 drawn from the same 57-survivor pool (not an independent cohort). This is a hypothesis-generating pilot, not a replication-ready dataset.

4. **Single-trigger, no cross-design.** No comparison to LC or ME/CFS metabolomes within the same pipeline. Cross-trigger inference requires assembling separately conducted studies — the provenance problem `discussion:0002` identifies as the decisive limitation for `hypothesis:0001`.

**Bottom line on grading:** "Thin-but-present" accurately marks that some molecular post-Ebola data exists. It does NOT mean the data can provide proportional evidential support for the cross-trigger convergence claim. The post-Ebola leg is structurally weaker than any other trigger in the matrix: its only evidence is an unreviewed preprint with a survivor-internal comparator and a phenotype mismatched to the fatigue-PAIS frame. `hypothesis:0001`'s cross-trigger breadth relies on this leg but should explicitly flag that post-Ebola evidence is insufficient to contribute independent support for a shared *fatigue* metabolic attractor.

**Relationship to `hypothesis:0001`'s metabolic/mitochondrial axis more broadly:** The TCA downregulation is plausibly consistent with mitochondrial/bioenergetic impairment seen in LC and ME/CFS (Shankar2025, Walitt2024, Liu2026), but the evidence that this is the same mechanism rather than a convergent endpoint reachable by multiple routes is not provided. TCA dysregulation is not PAIS-specific.

**SCFA-microbiome connection:** The divergent SCFA pattern (acetate up, propanoate down) is the most novel observation in the paper relative to other PAIS metabolomics. If replicated in a HC-controlled design, it would align with the gut-microbiome axis seen in Long COVID and support `search:0007-microbiome-gut-brain-pais`.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Post-Ebola Syndrome (PES) — MSK/GI or CP sequelae | Post-acute infection syndrome (PAIS) | Non-fatigue phenotype; primary scope but phenotype-mismatched to fatigue frame of `hypothesis:0001` |
| TCA cycle downregulation in PES | Metabolic / mitochondrial dysfunction axis | Single-trigger, plasma-level; consistent with but not identical to the bioenergetic deficits in ME/CFS / LC |
| SCFA alterations (acetate up, propanoate down) | Gut microbiome dysbiosis → immune modulation | Parallels LC SCFA findings; microclots/thromboinflammation axis tangentially |
| CD8 T-cell exhaustion (inferred from TCA/SCFA) | T-cell exhaustion / immune exhaustion axis | Inferred, not measured; plasma metabolomics cannot confirm cellular mechanism |
| PES vs asymptomatic survivors comparison | Within-trigger PES vs recovered | Comparator weakness — mismatched to HC-controlled cross-trigger designs |
| 10-metabolite biomarker panel (AUC > 0.8) | Candidate shared biomarker | Internal validation only; not tested against LC/ME/CFS panel; independent replication absent |
| Survivor-internal difference (PES vs asymptomatic GP IgG+) | PAIS pathophysiology vs post-infection sequela | The HC comparison being null complicates PAIS-specific interpretation |

## Limitations

1. **Null HC comparison is the primary limitation.** The comparison with household contacts (uninfected controls) did NOT yield significant differential metabolites. This is acknowledged by the authors as potentially attributable to limited sample size ("trends for several metabolites were similar in this comparison but not statistically significant"). However, the alternative interpretation — that EVD survivors broadly display metabolic changes and the PES vs asymptomatic signal captures relative amplification rather than a PAIS-specific footprint — cannot be ruled out. Until a HC-controlled PES design replicates the signature, the "PES biomarker" framing is premature.

2. **Small cohort and internal-only validation.** PES n=37, asymptomatic n=20; total n=57 survivors for all analyses. Validation set (n=18) is drawn from the same 57-survivor pool, not an independent cohort. The AUC > 0.8 figure requires external validation before it has biomarker meaning.

3. **Phenotype mismatch with fatigue-PAIS frame.** PES here is MSK/GI or cardiopulmonary sequelae, not neurological or fatigue/PEM phenotype. This limits comparability with the ME/CFS and Long COVID metabolomic signatures that dominate the cross-trigger matrix.

4. **Time-since-infection not individually reported.** Samples span 2016–2019 against a 2014–2015 epidemic, implying ~1–4 years post-acute illness, but exact timing is not reported per participant or controlled for in analysis. Cross-trigger comparisons require similar post-illness timing.

5. **Acute severity and viral load not assessed as covariates.** Acute EVD severity is a plausible confound — more severe acute illness may produce both more PES and more metabolic disruption. The analysis adjusted for age, sex, BMI, and sample collection date but not severity.

6. **Plasma metabolomics only; no cellular-level data.** The TCA/SCFA patterns are interpreted through the lens of CD8 T-cell exhaustion (mechanistic analogy from HIV/HBV/LCMV literature), but no T-cell data are collected. The inference is speculative and acknowledged as such.

7. **Data not yet deposited in a public repository.** Authors state data "will be uploaded to an online data repository" — no Metabolomics Workbench, MetaboLights, or other accession number is provided. Cross-trigger computational analyses are blocked until deposition occurs.

8. **Preprint status.** Not peer-reviewed at time of reading. Any quantitative claim should be treated as provisional until peer-reviewed publication and, ideally, independent replication.

## Model / Tool Availability

No software model or computational tool is released. Metabolomics data analysis used MetaboAnalyst 6.0, Cytoscape 3.10.3, and JMP 18.1.0 (all standard public tools). Raw data are stated to be available upon reasonable request and will be uploaded to an unspecified online repository; no accession number is available as of the preprint posting. Per the project's "author request is dead data" convention (MEMORY.md), this is classed as effectively not yet accessible for computational reuse.

## Follow-up

- **External validation with HC-controlled design is the decisive next step.** A replication comparing PES, asymptomatic survivors, AND healthy uninfected controls in a larger Sierra Leone or DRC survivor cohort is required to determine whether the 10-metabolite panel reflects a PAIS-specific vs. generic EVD-survivor metabolic state.
- **Deposit to Metabolomics Workbench or MetaboLights.** Once a public accession exists, this dataset becomes usable for the cross-trigger computational reanalysis contemplated in `discussion:0002` and `question:0001`.
- **Phenotype expansion.** Future PES metabolomics should include cognitive and fatigue outcomes (to enable comparison with LC/ME/CFS) in addition to MSK/GI and CP endpoints.
- **Direct cross-trigger metabolomics within one pipeline.** The decisive experiment for `hypothesis:0001`'s metabolic axis is a harmonized LC-MS/MS study running EVD survivors, LC, and ME/CFS samples through the same platform simultaneously.
- **Cellular immunometabolism follow-up.** The inferred CD8 T-cell exhaustion link requires paired T-cell exhaustion markers (TIM-3, PD-1, TOX) measured alongside metabolites in the same donors.
- **Related papers:** Ramundo2025 (post-chikungunya transcriptomics), Watton2026 (unified CPID model), Raijmakers2025 (cross-PIFS meta-analysis), Galbraith2011 (Dubbo head-to-head), Shankar2025 (shared oxidative-stress LC↔ME/CFS).
