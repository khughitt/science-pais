---
id: paper:Broderick2012
kind: paper
title: 'Cytokine expression profiles of immune imbalance in post-mononucleosis chronic
  fatigue'
status: active
ontology_terms:
- chronic fatigue syndrome
- post-mononucleosis fatigue
- Epstein-Barr virus
- cytokine network
- Th17 immune dysregulation
- IL-8
- IL-23
- immune signaling
- post-infectious CFS
source_refs:
- cite:Broderick2012
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0001-shared-molecular-signature-across-triggers
created: '2026-06-20'
updated: '2026-07-26'
---
# Cytokine expression profiles of immune imbalance in post-mononucleosis chronic fatigue

<!--
- **Authors:** Gordon Broderick, Ben Z. Katz, Henrique Fernandes, Mary Ann Fletcher, Nancy Klimas, Frederick A. Smith, Maurice R.G. O'Gorman, Suzanne D. Vernon, Renee Taylor
- **Year:** 2012
- **Journal:** Journal of Translational Medicine, 10:191
- **DOI:** 10.1186/1479-5876-10-191
- **PMID:** 22973830
- **PMCID:** PMC3480896
- **BibTeX key:** Broderick2012
- **Tier:** Core now
- **Source:** Full-text XML via Europe PMC (PMC3480896), read 2026-07-26.
-->

## Key Contribution

This paper provides a cytokine-level characterization of post-infectious CFS (PI-CFS) arising specifically after Epstein-Barr virus (EBV)-associated infectious mononucleosis in adolescents — the most thoroughly studied and largest incidence pathway to PI-CFS in prospective literature. Using archived plasma from a subset of a well-characterized 301-person prospective cohort, the authors identify a discriminating 5-cytokine signature (IL-2, IL-6, IL-8, IL-23, IFN-γ) and interpret the pattern as disrupted innate priming of the Th17 adaptive response: elevated IL-8 and IL-2 (a Th17 antagonist), decreased IL-23 (required for Th17 maintenance), with IFN-γ and IL-6 providing co-expression context. The paper's primary contribution is the analytical framework (cytokine co-expression rather than single-analyte comparisons) rather than the specific analytes, and it is the load-bearing citation for the EBV/ME/CFS arm of the cytokine axis in the project's cross-pathogen signature matrix.

## Methods

**Study design:** Secondary analysis of banked plasma from the Katz et al. 2009 prospective adolescent infectious mononucleosis cohort (R01 HD043301, PI Taylor). Cross-sectional comparison of PI-CFS versus fully-recovered controls at the 24-month post-IM timepoint.

**Cohort:** 301 adolescents recruited from the greater Chicago metropolitan area upon diagnosis of monospot-positive acute infectious mononucleosis (IM), presumed to reflect EBV infection in the large majority. Recruited through school nurses (middle school, high school, university), pediatric practices, and the Virology Laboratory of Children's Memorial Hospital. All prescribed treatments were recorded.

**Case definition — Fukuda 1994 CDC CFS criteria:** At 6 months post-IM diagnosis, 286 (95%) subjects completed the Jason et al. 1999 CFS Screening Questionnaire (telephone); 70 (24%) were assessed as not fully recovered and 53 (76%) of these completed a full clinical evaluation. Of those, 39/53 were classified as CFS (13% of original 301). CFS classification was based on the 1994 CDC (Fukuda) CFS criteria, with reference to the pediatric adaptation (Jason et al. 2006). Those with an alternative explanatory diagnosis were classified as "CFS-explained" and excluded. The cohort was then reassessed at 12 months (22 CFS, 7% of 301; all female) and 24 months (13 CFS, 4% of 301; all female). Of the 13 PI-CFS subjects at 24 months, 9 had banked plasma samples available; all 9 were female. Twelve recovered controls had banked plasma available at 24 months and served as the comparison group (sex composition of the control group not explicitly stated).

**Cytokine assay:** Morning fasting blood samples collected in EDTA tubes; plasma separated within 2 hours and stored at −80°C. Cytokine concentrations measured using Quansys Biosciences Q-Plex Human Cytokine Screen (16-plex), a 96-well plate chemiluminescent imaging ELISA. The panel measured: IL-1α, IL-1β, IL-2, IL-4, IL-5, IL-6, IL-8, IL-10, IL-12(p70), IL-13, IL-15, IL-17, IL-23, IFN-γ, TNF-α, and TNF-β. Each sample was run in duplicate; concentrations were estimated from second-order polynomial calibration curves.

**Statistical analysis (two stages):**
1. *Comparative statistics:* Log-transformed values compared by parametric t-test (mean expression) and nonparametric Wilcoxon rank-sum test (median expression). Subject-to-subject variation was confirmed to exceed replicate error by n-way ANOVA and Kruskal-Wallis; values below detection limit replaced with the lowest detected concentration for each cytokine within each group.
2. *Classification analysis:* Cytokines ranked as individual biomarkers by ROC AUC and Wilcoxon U-statistic, with cross-correlation-adjusted reweighting (alpha=0 and alpha=1) to penalize redundant candidates. Multivariate linear discriminant models were constructed iteratively across all possible cytokine subsets; only models achieving <20% overall error rate and posterior classification probability ≥0.95 were accepted. An independent stepwise regression approach (partial-F criterion: entry p<0.05, exit p>0.10) was run in parallel. Collinearity was corrected using a diagonal covariance matrix estimate.

**Covariates:** All subjects shared the same acute infection trigger (monospot-positive IM). Timepoint is fixed (24 months). Age: adolescent cohort (specific age range reported in the primary cohort paper, Katz et al. Pediatrics 2009, PMID 19564299). Sex: 90% of 6-month CFS cases were female (vs 68% of full cohort, p=0.01 Fisher's exact); all 24-month PI-CFS subjects are female. No covariate adjustment for sex or acute-illness severity was performed in the cytokine analysis (because the final comparison groups are too small). Socioeconomic status and race did not differ between CFS and full cohort.

## Key Findings

**CFS incidence in the post-IM prospective cohort:**
- 13% at 6 months (n=39/301)
- 7% at 12 months (n=22/301)
- 4% at 24 months (n=13/301), all female

This is consistent with prospective data from Buchwald et al. 2000 (~12% at 6 months), the Australian Dubbo cohort (11-14% at 6 months, various triggers), and other post-IM CFS studies (collectively the ~10% rule documented in the background literature).

**Cytokine univariate comparisons (PI-CFS n=9 vs recovered controls n=12, at 24 months):**
- **IL-8:** significantly elevated in PI-CFS by both t-test and Wilcoxon (p≤0.05); strongest individual discriminator (ROC AUC 0.34 above 0.50)
- **IL-23:** significantly decreased in PI-CFS by both tests (p≤0.05); second-best discriminator by Wilcoxon U-statistic
- **IL-2:** elevated in PI-CFS; significant by t-test only
- **IL-5:** decreased in PI-CFS; significant by Wilcoxon only
- **IL-13:** trend toward increased expression (p~0.07)
- IL-1α, IL-1β, IL-4, IL-6, IL-10, IL-12(p70), IL-15, IL-17, IFN-γ, TNF-α, TNF-β: not individually significant

**Optimal multi-cytokine classifier:**
- Minimum set of 5 cytokines satisfying >80% accuracy at 95% confidence: **IL-2, IL-6, IL-8, IL-23, and IFN-γ**
- Performance on training data: sensitivity 94%, specificity 88%, PPV=0.85, NPV=0.95
- Only 7 of 42 individual duplicate-sample pairs received an inconclusive classification at the 0.95 confidence threshold with this model, versus 22–29 inconclusives from alternative cytokine sets ranked by individual AUC or U-statistic — demonstrating that redundancy-penalized co-expression outperforms individually-ranked cytokines
- Both all-possible-subsets and stepwise regression approaches independently converged on IL-6, IL-8, and IL-23 as the core discriminating cytokines; IL-1α, IL-2, and IFN-γ were each selected in one approach

**Biological interpretation — Th17 dysregulation:**
- IL-6, IL-8, and IL-23 are the key drivers. IL-23 (produced by dendritic cells and macrophages) is essential for sustained Th17 differentiation. The authors note that **IL-23 is decreased despite comparable IFN-γ levels** (which normally co-stimulates IL-23 production) and that IL-17 is not significantly elevated despite elevated IL-2 (a known Th17 antagonist). This pattern is internally consistent with blunted IL-23-driven Th17 priming: the innate system fails to sustain the Th17 arm of adaptive immunity, while IL-2 provides an additional brake. Elevated IL-8 (a downstream effector of the NF-κB pathway that links IL-1, IL-23, IL-6, and IL-8 production in fibroblasts) is part of the same dysregulated loop. The interpretation is that the *pattern of co-expression* (innate-Th17 context) — not individual cytokine levels — defines the immune imbalance.
- This Th17 axis interpretation is corroborated by the authors' prior adult CFS study (Fletcher et al., J Transl Med 2009, PMID 19909538) and a formal network analysis of CFS cytokines (Broderick et al., Brain Behav Immun 2010, PMID 20447453) from the same group, which showed a similar subdued IL-23/Th17/IL-17 response in adult CFS of unknown etiology.

## Relevance

**Post-EBV cytokine anchor for `hypothesis:0001`:** This paper fills the EBV/post-mononucleosis cytokine cell in the project's cross-pathogen signature matrix (`search:0002`, `discussion:0002`). It is the primary evidence supporting "cytokine dysregulation in ME/CFS (post-EBV)" as a populated matrix cell. This is a legitimate contribution given the design: a prospective cohort with known trigger, matched controls from the same cohort, and a 24-month post-IM timepoint that rules out the acute-infection confound.

**Weight assessment — does the paper support the cross-trigger claim placed on it?**
The paper occupies a modest but honest position in the evidence hierarchy:
1. It is a **single-trigger study** (EBV/IM only): it contributes exactly one cell to the cross-trigger matrix, consistent with the project's labeling of it as "single-trigger longitudinal." It does **not** demonstrate cross-trigger convergence on its own; it is one data point in an assembled convergence argument.
2. The cytokine pattern is **different from the QFS pattern** (Keijmel2016, Raijmakers2018) which shows elevated IFN-γ/CXCL10/IL-6/TNFα in active Coxiella infection contexts, and from the post-infective fatigue absence-of-cytokine-differences finding in the Dubbo cohort (Vollmer-Conna et al., Clin Infect Dis 2007, PMID 17712757). The Dubbo study measured serum rather than plasma cytokines in a combined EBV/RRV/Q-fever post-infective cohort and found no consistent cytokine differences. The two papers are not directly contradictory (different methods, different timepoints, different case definitions) but they are in tension — this paper's positive signal and the Dubbo negative together suggest the cytokine signal in post-EBV fatigue is not robust to method and cohort variation.
3. The sample size is **very small** (n=9 PI-CFS, n=12 controls), the classifier is **trained and tested on the same dataset** with no external validation, and the paper explicitly notes the sensitivity analysis on the 4 missing PI-CFS plasma samples. These are substantial caveats.
4. The Th17 dysregulation interpretation is **mechanistically coherent but speculative**: the key marker is decreased IL-23 rather than direct measurement of Th17 cells or IL-17, and the authors themselves frame this as a "possible dysregulation" and candidate biomarker, not an established mechanism.
5. **The within-group cytokine consistency across the adult and adolescent post-EBV/idiopathic CFS papers from the same group (Fletcher et al. 2009, Broderick et al. 2010, and this paper) is a signal worth noting** — these are the same collaborating group using similar assays, which limits independence.

In sum: the paper appropriately anchors the post-EBV cytokine cell with a specific Th17-associated pattern, but the cross-trigger weight is carried by assembled convergence (multiple single-trigger papers) rather than head-to-head design. The Th17 dysregulation pattern has not been independently replicated in post-EBV CFS by an external group, so the EBV cytokine cell should be read as "one small study suggests" rather than "established." The project's existing grading ("single-trigger longitudinal, Core now") correctly characterizes its role.

**Connection to `question:0001` (shared molecular signature):** Contributes the EBV cytokine term to the question but does not answer it. The decisive test — a harmonized, controlled multi-omics study across ≥3 fatigue-phenotype triggers — remains absent.

**Connection to `hypothesis:0001` (shared attractor):** Supports the immune-activation domain of the attractor claim for the post-EBV arm. But the Th17 pattern (particularly the decreased IL-23) is not a generic "immune activation" signal; it is a specific pattern that may or may not be shared with other PAIS. Given that QFS shows elevated IFN-γ/CXCL10, not decreased IL-23, the cross-trigger cytokine picture is pattern-heterogeneous even where cells are nominally both "supported."

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| PI-CFS after IM (post-EBV) | Post-acute infection syndrome (PAIS); EBV trigger | Trigger = confirmed monospot-positive IM; EBV presumed causal but not serologically confirmed beyond monospot |
| 4% CFS incidence at 24 months | ~10% chronic fraction across PAIS triggers | Consistent with the cross-pathogen ~10% rule; here 4% reflects progressive natural recovery from the 13% at 6 months |
| Fukuda 1994 CFS case definition | ME/CFS Fukuda criteria arm | Not the CCC or ICC criteria; implications for clinical heterogeneity vs stricter ME/CFS criteria cohorts |
| Th17 dysregulation (decreased IL-23; elevated IL-8, IL-2) | Cytokine axis of the shared-attractor hypothesis | Trigger-specific pattern; differs from QFS cytokine profile; not head-to-head comparable |
| 5-cytokine co-expression classifier | Candidate biomarker panel | Training=testing set (n=21 total); no external validation; not clinically deployable |
| Adolescent cohort, all-female PI-CFS at 24 months | Sex as PAIS risk modifier | 100% female PI-CFS cases at 24 months; consistent with the general female preponderance of ME/CFS; no male-comparator control arm |
| Plasma cytokines (16-plex ELISA) | Circulating immune markers | No cellular or transcriptomic data; Quansys-specific platform |

## Limitations

1. **Very small biomarker sample (n=9 PI-CFS, n=12 recovered controls).** Only 9 of 13 PI-CFS subjects at 24 months had available banked plasma, and the recovered control comparison group is also small. The sensitivity analysis (Supplementary Table S6) simulating the 4 missing PI-CFS profiles shows variability in which cytokines are selected, suggesting the specific panel is sensitive to the small sample.

2. **No external validation.** The 5-cytokine classifier is trained and evaluated on the same 21-subject dataset. The reported performance (sensitivity 94%, specificity 88%) is an optimistic within-sample estimate. Given n=21, overfitting is a serious concern even with the stepwise and all-subsets approaches used. The paper does not include a held-out test set or cross-validation; the "better than 80% accuracy at 95% confidence" figure should be treated as provisional.

3. **Case definition (Fukuda 1994) lacks specificity for PEM-positive ME/CFS.** The Fukuda criteria do not require post-exertional malaise (PEM), the cardinal feature of the stricter CCC and ICC definitions. This means the PI-CFS cases here may include a heterogeneous group. In a project that distinguishes PEM-positive from PEM-absent phenotypes (D-002), the Fukuda case definition limits how directly these findings apply to the PEM-defined ME/CFS phenotype.

4. **No stratification by sex within the controls.** All 13 PI-CFS cases at 24 months are female, but the sex distribution of the 12 recovered controls is not specified. If controls include males, the cytokine comparison conflates sex effects with CFS effects — relevant given that sex strongly modulates cytokine patterns.

5. **No acute-severity adjustment.** While all subjects share the same trigger (monospot-positive IM), there is no stratification by severity of acute illness. Acute illness severity is a known predictor of persistent fatigue (D-002 context).

6. **Single platform, same research group.** The Th17 cytokine pattern is consistent across the Fletcher et al. 2009, Broderick et al. 2010, and this paper — all from the same collaborating group using the Quansys Q-Plex assay. The platform- and group-specific nature limits independence.

7. **Tension with the Dubbo cohort negative.** Vollmer-Conna et al. 2007 (Clin Infect Dis) — the Dubbo Infective Outcomes Study, which includes post-EBV fatigue — explicitly found that post-infective fatigue syndrome is not associated with altered cytokine production. The methods differ (serum vs plasma; different assay; different timepoints; combined EBV/RRV/Q-fever group), but this head-to-head-period negative is material context for the single-trigger positive signal here.

8. **EBV confirmed only by monospot.** "Monospot-positive IM" is presumed to be EBV in the majority of cases but not universally confirmed by EBV-specific serology. CMV, HHV-6, adenovirus, and hepatitis A can also cause monospot-positive IM. This is a minor qualification: the cohort is well-characterized overall and EBV causes the great majority of monospot-positive IM in adolescents.

9. **Pre-2012; 16-plex ELISA only.** This is a targeted cytokine panel with 16 analytes, not a multi-omic or proteomic study. Many relevant markers (T-cell subsets, type I interferon signature, complement, autoantibodies, metabolomics) were not assessed. The study predates the long-COVID literature and the current generation of multi-omic post-infectious fatigue studies by over a decade.

## Model / Tool Availability

No software or computational model released. The Quansys Q-Plex 16-plex assay is a commercial platform. The statistical methods (linear discriminant analysis with collinearity correction) are described in sufficient detail to reimplement. No raw data repository is cited; data are available from the corresponding author (per journal policy, but "author request" is treated as dead/non-viable by project convention).

## Follow-up

- **Replication in independent post-EBV cohort.** The 5-cytokine Th17-associated pattern (IL-2, IL-6, IL-8, IL-23, IFN-γ) has not been independently validated in a distinct post-EBV CFS cohort or across adolescent ME/CFS more broadly. This is the primary gap before treating the EBV cytokine cell as established.
- **Cross-trigger comparison of cytokine patterns.** Does the decreased-IL-23 / elevated-IL-8 pattern differ from the QFS/Coxiella profile (elevated IFN-γ/CXCL10, Keijmel2016 / Raijmakers2018)? A within-study head-to-head would directly test whether post-EBV and post-bacterial cytokine patterns overlap or diverge — this is the data that would sharpen `question:0001`.
- **Fletcher et al. 2009 (J Transl Med) and Broderick et al. 2010 (Brain Behav Immun).** These companion papers from the same group characterize cytokines in adult CFS of unknown etiology and in network analysis, respectively, and support the Th17 interpretation. Reading them would assess whether the EBV-specific pattern differs from idiopathic adult CFS.
- **Katz et al. 2009 (Pediatrics, PMID 19564299).** The primary cohort paper; includes clinical characterization, autonomic data, and exercise tolerance findings from the same cohort — relevant to D-002 (pacing over GET for PEM-positive phenotypes) since this cohort overlaps with a study of exercise tolerance in PI-CFS adolescents (Katz et al. 2010, J Pediatr).
- **Vollmer-Conna et al. 2007 (Clin Infect Dis) — the Dubbo cytokine negative.** A head-to-head negative from the cross-trigger Dubbo cohort (EBV/RRV/Q-fever). Methodological reconciliation of the Broderick positive and Dubbo negative would clarify whether the cytokine signal is robust or platform/sample-specific.
