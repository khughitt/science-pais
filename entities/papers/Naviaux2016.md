---
id: paper:Naviaux2016
type: paper
title: Metabolic features of chronic fatigue syndrome
status: active
ontology_terms:
  - ME/CFS
  - metabolomics
  - hypometabolism
  - dauer
  - cell danger response
  - bioenergetics
  - sphingolipid metabolism
  - purine metabolism
  - mitochondrial dysfunction
dataset_usage: []
datasets: []
source_refs:
  - cite:Naviaux2016
related:
  - question:0011-mitochondrial-basis-of-pem
  - topic:mecfs-long-covid-convergence
  - hypothesis:0001-shared-dysregulated-attractor
created: '2026-06-20'
updated: '2026-06-25'
---
# Metabolic features of chronic fatigue syndrome

- **Authors:** Robert K. Naviaux, Jane C. Naviaux, Kefeng Li, A. Taylor Bright, William A. Alaynick, Lin Wang, Asha Baxter, Neil Nathan, Wayne Anderson, Eric Gordon
- **Year:** 2016
- **Journal:** Proceedings of the National Academy of Sciences (PNAS), vol. 113, no. 37, pp. E5472–E5480
- **DOI:** 10.1073/pnas.1607571113
- **BibTeX key:** Naviaux2016
- **Source:** Full-text PDF (papers/pdfs/2016_Naviaux_metabolic-features-chronic-fatigue-syndrome.pdf), read 2026-06-20 (supersedes earlier abstract-only read).

## Key Contribution

This is the founding large-scale metabolomics study of ME/CFS and the paper that introduced the **"dauer" framing** of the disease as a hypometabolic syndrome. Naviaux and colleagues profiled 612 plasma metabolites across 63 biochemical pathways in 45 ME/CFS patients and 39 matched controls (n = 84 total), finding that 80% of the diagnostically informative metabolites were *decreased* — the opposite of an inflammatory metabolic activation signature. The authors interpret this global suppression as a conserved cellular stress response analogous to the *C. elegans* dauer state: a protective but self-sustaining hypometabolic mode triggered by environmental threat that, once entered, does not spontaneously reverse. The study achieved sex-stratified diagnostic AUCs of 94% (males, 8 metabolites) and 96% (females, 13 metabolites), demonstrating that the metabolic signature is robust and replicable in both sexes despite a heterogeneous clinical history.

The paper anchors the **hypometabolic pole** of a direction-of-effect tension in the PAIS metabolomics literature: Naviaux finds profound global suppression at rest, whereas later exercise-challenge studies (e.g. Che2025, Missailidis/Peppercorn lines) report secondary mitochondrial activation or specific pathway upregulation following exertional provocation. These two frames are not necessarily contradictory — a hypometabolic baseline state can coexist with a dysregulated or compensatory response to provocation — but the tension is unresolved.

## Methods

**Study design.** Case-control metabolomics study. 45 ME/CFS subjects (22 men, 23 women) and 39 age- and sex-matched normal controls (18 men, 21 women); total n = 84. Subjects recruited from 51 zip codes across the United States and Canada over a 1-year period (June 2014–May 2015). ME/CFS diagnosis required meeting all three of: IOM 2015, Canadian Consensus Criteria (CCC), and Fukuda 1994 criteria — a notably stringent triple requirement that selects a more homogeneous, severe phenotype than studies using a single criterion. IRB approval: University of California, San Diego (Project 140072).

**Demographics.** Males: mean age 53 ± 2.8 y (range 21–67); females: mean age 52 ± 2.5 y (range 20–67). Mean age of illness onset: 30 ± 2.6 y (men), 33 ± 2.3 y (women). Mean illness duration: 21 ± 3.0 y (men), 17 ± 2.3 y (women). Karnofsky performance scores: 62 ± 3.2 (males), 54 ± 3.3 (females), indicating moderate-to-severe functional impairment relative to healthy controls (score = 100).

**Metabolomics platform.** Targeted broad-spectrum, chemometric analysis of 612 metabolites from 63 biochemical pathways by hydrophilic interaction liquid chromatography (HILIC), electrospray ionization (ESI), and tandem mass spectrometry (MS/MS) in a single-injection method (described in reference 55 with minor modifications). Over 420 metabolites were detectable in all plasma samples. Regular quality control experiments showed metabolite AUC correlations over 0.98 and relative SDs of 9–12% (SI Appendix, Tables S2 and S3).

**Statistical approach.** Metabolomic data were log-transformed, scaled by control SDs, and analyzed by multivariate partial least squares discriminant analysis (PLSDA), PCA, t-test, and univariate ANOVA with pairwise comparisons. Multiple-testing correction applied using two complementary approaches: (i) Fisher's least significant difference (LSD) method in MetaboAnalyst, or (ii) the FDR method of Benjamini and Hochberg. All top-25 discriminating metabolites had false discovery rates (FDRs) less than 10%. Metabolites with variable importance in projection (VIP) scores determined by PLSDA greater than 1.5 were considered significant. Pathway impact scores were derived by summing VIP scores for metabolites within each pathway, then rank-ordering pathways. Sets of 5–15 metabolites were manually selected from the top 60 significant metabolites as candidate diagnostic classifiers using Random Forests (RF) and linear support vector machines (SVM) in MetaboAnalyst. Classifier robustness estimated by repeated double cross-validation (rdCV) and permutation testing (1,000 times). ROC curves calculated by bootstrap resampling. Metabolite correlations with Karnofsky performance scores calculated by Pearson parametric and Spearman nonparametric methods in Stata, Prism, GraphPad Software, and R.

**Feature selection for diagnostic panels.** Both forward selection and backward elimination methods were tested. The 8- and 13-metabolite diagnostic panels were selected manually to broadly interrogate the discriminating biochemical pathways. The specification of metabolites in each classifier was flexible: addition or removal of one or a few analytes had little effect on overall classifier quality. Single-analyte classifiers also performed significantly above chance (Table 4).

**Case definition note.** The triple-criterion requirement (IOM + CCC + Fukuda) is more conservative than most ME/CFS metabolomics studies; findings may be most representative of moderate-to-severe, diagnostically certain cases.

## Key Findings

**1. Hypometabolic signature (primary finding).** Of the metabolites best distinguishing ME/CFS from controls, 80% were *decreased* in ME/CFS plasma — a directional pattern consistent with systemic suppression of metabolic flux rather than inflammatory upregulation. This hypometabolic pattern held across both sexes and is the opposite direction from the acute cell danger response (CDR) and metabolic syndrome, in which sphingolipids, phospholipids, cholesterol, and uric acid are elevated.

**2. Twenty abnormal pathways — complete list.** Statistically significant abnormalities were detected in 20 of the 63 profiled biochemical pathways. Nine pathways were disturbed in both males and females; 11 showed sex-specific differences. The full ranked lists from Tables 2 and 3 are:

*Pathways disturbed in males (Table 2, ranked by VIP impact score):*
1. Sphingolipids (impact 49% of male metabolic disturbances) — 30 metabolites decreased, 0 increased
2. Phospholipids (16%) — 7 decreased, 2 increased
3. Pyrroline-5-carboxylate (P5C), Arginine, Ornithine, Proline (7%) — 3 increased, 1 decreased
4. Glycosphingolipids (6%) — 3 decreased, 0 increased
5. Cholesterol, nongonadal steroids (4%) — 3 decreased, 0 increased
6. Branch chain amino acids (4%) — 3 decreased, 0 increased
7. Purines (3%) — 2 decreased, 0 increased
8. Microbiome metabolism (2%) — 1 decreased, 0 increased
9. Vitamin B2 (riboflavin) (2%) — 1 decreased, 0 increased
10. Serine, 1-carbon metabolism (2%) — 1 increased, 0 decreased
11. SAM, SAH, methionine, glutathione (1%) — 1 increased, 0 decreased
12. Very long chain fatty acid oxidation (2%) — 1 decreased, 0 increased
13. Propiogenic acids (1%) — 1 decreased, 0 increased
14. Threonine metabolism (1%) — 1 increased, 0 decreased

*Pathways disturbed in females (Table 3, ranked by VIP impact score):*
1. Sphingolipids (35%) — 21 metabolites decreased, 0 increased
2. Phospholipids (26%) — 11 decreased, 6 increased
3. Glycosphingolipids (9%) — 5 decreased, 0 increased
4. Purines (5%) — 3 decreased, 0 increased
5. Microbiome metabolism (5%) — 1 decreased, 2 increased
6. Fatty acid oxidation and synthesis (3%) — 2 decreased, 1 increased
7. P5C, Arg, Ornithine, Pro (3%) — 2 increased, 0 decreased
8. Cholesterol, nongonadal steroids (2%) — 1 decreased, 0 increased
9. Collagen/hydroxyproline metabolism (2%) — 1 increased, 0 decreased
10. Vitamin B2 (riboflavin) (2%) — 1 decreased, 0 increased
11. Bile salt metabolism (2%) — 1 decreased, 0 increased
12. Endocannabinoids (1%) — 1 decreased, 0 increased (females only)
13. Branch chain amino acids (1%) — 1 decreased, 0 increased
14. Vitamin B12 (cobalamin) metabolism (1%) — 1 decreased, 0 increased
15. Amino-sugar, galactose, and nonglucose (1%) — 1 increased, 0 decreased

*Male-only pathways (not shared with females):* serine/1-carbon metabolism, SAM/SAH/methionine/glutathione, very long chain fatty acid oxidation, propiogenic acids, threonine metabolism.

*Female-only pathways (not shared with males):* fatty acid oxidation and synthesis, collagen/hydroxyproline metabolism, bile salt metabolism, endocannabinoids, vitamin B12 metabolism, amino-sugar/galactose/nonglucose.

**3. Key metabolite-level directions and effect sizes.** Selected findings from the text:
- *Sphingolipids:* In males, >50% (16/30) of decreased sphingolipids were ceramides; 47% (14/30) were sphingomyelin species. In females, 86% (18/21) were ceramides and 14% (3/21) were sphingomyelins. Sphingolipid + glycosphingolipid abnormalities explained 55% of metabolic impact in males and 44% in females.
- *Phospholipids:* Most PC phospholipids decreased in both sexes. Exception: PC(18:1/22:6), containing omega-3 DHA and oleic acid (C18:1), was *increased* — opposite of the acute CDR pattern.
- *Purines:* Plasma uric acid decreased in males; plasma adenosine decreased in females. Both consistent with decreased ATP synthesis/turnover.
- *P5C/Arginine:* Pyrroline-5-carboxylate (P5C) and Arg were *increased* in both sexes — interpreted as a stress-response signal (P5C is produced by stress-induced oxidation of proline and hydroxyproline).
- *Riboflavin/FAD:* Plasma FAD decreased in both sexes, consistent with reduced capacity for fatty acid oxidation, sterol synthesis, and mitochondrial cofactor function.
- *Branch chain amino acids:* 2-Hydroxyisocaproic acid (HICA), a transamination product of leucine, was decreased — consistent with reduced gut absorption, increased renal excretion, or increased mitochondrial oxidation.
- *Microbiome:* Plasma 4-hydroxyphenyllactic acid (HPLA) decreased in males; plasma phenyllactic acid (PLA) decreased in females. Both are microbiome metabolites of tyrosine/phenylalanine. Opposite of what is found during acute inflammation/infection.
- *Cholesterol:* Total plasma cholesterol decreased; desmosterol, cortisol, aldosterone normal. Decreased flux through lathosterol pathway (Kandutsch–Russell), suggesting preferential use of the stress-inducible desmosterol (Bloch) pathway.
- *Bile acids (females):* Plasma chenodeoxycholic acid (CDCA) decreased in females, which can impair bile acid signaling and intestinal mucosal integrity via farnesoid X receptor (FXR).

**4. Diagnostic classifier performance (Table 4).** RF classifier with 2/3-in, 1/3-out rdCV and 1,000-permutation permutation test:
- Males (n = 18 controls, 22 CFS): 8-metabolite panel — AUROC 0.94 (95% CI 0.84–1.0), rdCV accuracy 0.84, permutation P = 0.001, 2×2 sensitivity 0.91, specificity 0.89
- Females (n = 21 controls, 23 CFS): 13-metabolite panel — AUROC 0.96 (95% CI 0.87–1.0), rdCV accuracy 0.90, permutation P = 0.001, 2×2 sensitivity 0.91, specificity 0.95

The 8-analyte male panel comprised: phosphatidyl choline PC(16:0/16:0), glucosylceramide GC(18:1/16:0), 1-PSC, FAD, pyroglutamic acid (5-oxoproline), HICA, l-serine, and lathosterol. The 13-analyte female panel comprised: THC(18:1/24:0), PC(16:0/16:0), hydroxyproline, ceramide(d18:1/22:2), lathosterol, adenosine, phosphatidylinositol PI(16:0/16:0), FAD, 2-octenoylcarnitine, phosphatidyl choline plasmalogen PC(22:6P18:0), PC(18:1/22:6), 1-PSC, and CDCA.

**5. Personalized vs. diagnostic metabolite abnormalities.** CFS patients had a mean of 10 (±1.0) metabolite abnormalities that contributed to the CFS diagnosis and 30 (±2.0) metabolites that were abnormal but noncontributory for CFS diagnosis. About 75% of the metabolic abnormalities identified were personalized; only 25% provided diagnostic group information. The authors note that personalized abnormalities may be more useful for guiding individualized treatment than the group-diagnostic signature.

**6. Convergent cellular response from heterogeneous triggers.** Possible triggering events fell into five categories: biological (viral, bacterial, fungal/mold, parasitic infections), chemical exposures, physical trauma, psychological trauma, and unknown; several patients had multiple triggers converging in the same year. Despite this heterogeneity, the cellular metabolic response was homogeneous and statistically robust, supporting the notion that the unified cellular response — not the specific trigger — lies at the root of ME/CFS metabolic features.

**7. CFS versus dauer versus CDR versus metabolic syndrome (Table 5).** The directionality of metabolite changes in CFS matches dauer and is opposite to the acute CDR and metabolic syndrome for all overlapping pathways. Specifically: sphingolipids, glycosphingolipids, phospholipids (most species), cholesterol/sterol synthesis, purines, FAD/riboflavin are all decreased in both CFS and dauer but increased in the acute CDR and metabolic syndrome. Uric acid is decreased in CFS males (N/A for dauer worms; increased in CDR and metabolic syndrome). The one exception is PC(18:1/22:6): increased in CFS (matching metabolic syndrome direction), with no dauer data.

**8. NADPH and mitochondrial redox.** The authors note that all metabolic abnormalities identified in CFS were either directly regulated by redox or by NADPH availability. ~60% of NADPH is produced by the pentose phosphate pathway at baseline; the remainder by five NADP+-dependent enzymes including mitochondrial MTHFD2. Decreased mitochondrial electron transport (when NADPH and NADP+ pools fall) leads to decreased oxygen consumption, rising dissolved oxygen, activation of NADPH oxidases (Nox4), and hydrogen peroxide production — initiating oxidative shielding rather than oxidative phosphorylation for ATP synthesis.

## Relevance

This paper is foundational for PAIS research on at least three axes:

**1. Bioenergetic/mitochondrial basis of ME/CFS (question:0011).** The 20-pathway hypometabolic profile — including mitochondrial, purine, phospholipid, FAD/riboflavin, and branch-chain amino acid metabolism — provides the strongest early quantitative metabolomics evidence that ME/CFS involves a systemic bioenergetic failure. The decreased-not-increased directionality is critical: it argues against compensatory mitochondrial upregulation as the dominant resting state and instead points to active metabolic suppression. This is the anchor for the hypometabolic pole of the direction-of-effect tension with exercise-provoked findings (Che2025), which remain to be reconciled across resting-state versus challenge study designs. The NADPH/redox framing (all abnormal metabolites linked to redox or NADPH availability) provides a mechanistic organizing principle.

**2. Convergent cellular response from heterogeneous triggers (hypothesis:0001).** The finding that metabolic profiles were homogeneous across a clinically heterogeneous ME/CFS cohort (with five trigger categories) directly supports hypothesis:0001 — that PAIS represents a shared dysregulated attractor reachable from many triggers. The paper explicitly frames this as "the unified cellular response, not the specific trigger, that lies at the root of the metabolic features of CFS."

**3. Dauer framing as evolutionary anchor.** The dauer analogy offers a biologically grounded reason why the PAIS state might be self-sustaining and resistant to spontaneous resolution: dauer is not merely a downregulated state — it is a stable alternative program maintained by active signaling. Table 5 demonstrates the directional equivalence of CFS and dauer metabolomics across all measured overlapping pathways. The paper proposes that understanding dauer entry and exit triggers (CDR/purinergic signaling, ref. 7) is the most promising path toward rational therapeutic development.

## Project Framework Mapping

| Framework element | Mapping |
|---|---|
| hypothesis:0001 (shared dysregulated attractor) | Directly supported: homogeneous metabolic attractor state reached from heterogeneous triggers (five trigger categories, one metabolic response) |
| question:0011 (mitochondrial/bioenergetic basis of PEM) | Foundational evidence: 80% decreased metabolites including mitochondrial, purine, FAD, BCAA pathways establish the hypometabolic baseline; NADPH/redox framework organizes all abnormalities |
| Direction-of-effect tension | Anchors the hypometabolic pole; must be held in tension with Che2025 exercise-provoked pathway activations |
| Convergent mechanism vs. trigger-specific | Supports convergence: chemically similar response across patients with diverse biological, chemical, physical, and psychological trigger categories |

## Limitations / Caveats

1. **Cross-sectional design.** Resting-state snapshot only; no exertional challenge, no longitudinal follow-up. Cannot establish whether hypometabolism is cause, consequence, or compensation, nor whether it precedes symptom onset.

2. **Triple-criterion case definition.** Stringent IOM + CCC + Fukuda triple requirement yields a homogeneous but likely more severe cohort (Karnofsky ~54–62). Generalizability to milder or single-criterion ME/CFS, or to other PAIS (long COVID, PTLDS), is not established in this paper.

3. **Plasma metabolomics only.** Tissue-level metabolic states may differ substantially; plasma reflects a mixture of contributions from all tissues and does not isolate the primary site(s) of metabolic failure.

4. **No pre-infection baseline.** Patients were studied in the chronic state (mean illness duration 17–21 years); it is unknown whether hypometabolism pre-existed the triggering event or emerged during or after acute illness.

5. **Sex-dimorphic panels.** The diagnostic metabolite sets differ between males (8 metabolites) and females (13 metabolites), and 11 of 20 pathways showed sex-specific differences. Studies combining sexes without stratification may dilute or obscure the signal.

6. **No independent replication cohort in this paper.** The authors explicitly call for "study of larger cohorts from diverse geographical areas" and comparison with related disorders. The AUC figures should be interpreted with caution pending external validation. (Note: subsequent publications by Naviaux's group and others have partially replicated these pathway findings, but that work is outside this paper.)

7. **Dauer framing is interpretive / mechanistic hypothesis.** The chemical similarity to dauer is an analogy supported by pathway-level directional congruence (Table 5), not a demonstrated causal mechanism. Whether CDR/purinergic signaling is causally driving the hypometabolic state requires direct experimental evidence not provided by a cross-sectional metabolomics design.

8. **Sample size.** n = 45 ME/CFS / 39 controls is modest for a 612-metabolite / 63-pathway analysis. Permutation testing and rdCV strengthen confidence in the classifier results, but external replication remains essential.

9. **Medication confounding.** ME/CFS patients took a mean of 4.1 (males) and 4.6 (females) medications vs. 0.2 and 0.3 in controls (p < 0.001 and p < 10⁻⁵, respectively); medication effects on the metabolic profile cannot be fully excluded.

## Model / Tool Availability

Data deposited in the NIH Metabolomics Data Repository and Coordinating Center (DRCC), accession no. ST000450. Analysis performed in MetaboAnalyst (ref. 56), Stata (SE12.1), Prism (6), GraphPad Software, and R. No standalone diagnostic model or code repository is described.

## Follow-up

- **Direction-of-effect reconciliation:** Compare Naviaux2016 resting-state hypometabolic pathways against Che2025 exercise-provoked pathway activations to determine whether findings are complementary (suppressed baseline + dysregulated stress response) or contradictory.
- **Cross-PAIS replication:** Has the 20-pathway or 8/13-metabolite panel been tested in long COVID or PTLDS cohorts? A positive cross-trigger replication would strongly support hypothesis:0001.
- **CDR/purinergic mechanism:** Naviaux's companion CDR publications (refs 6 and 7: Naviaux 2012, Naviaux 2014) should be reviewed to understand the proposed mechanistic link between extracellular ATP/purinergic signaling and dauer entry in ME/CFS pathophysiology.
- **Longitudinal metabolomics:** Tracking these pathways from acute infection through recovery vs. chronicity onset would test whether hypometabolism is a precursor or consequence of PAIS.
- **Sex-specific panels:** The 8-metabolite (male) and 13-metabolite (female) diagnostic panels are candidate biomarkers — have they been prospectively validated? The NIH DRCC dataset (ST000450) is publicly available for reanalysis.
- **Medication confound:** Future studies should include medication-naïve or carefully matched patients to assess whether the metabolic signature is driven by treatments rather than disease state.
