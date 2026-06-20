---
id: paper:Sommen2026
type: paper
title: "Long COVID: Deep single-cell immunophenotyping and machine learning reveal a general signature for fatigue"
status: active
ontology_terms:
  - long COVID
  - post-infective fatigue syndrome
  - mass cytometry CyTOF
  - natural killer cell dysregulation
  - terminal NK cells
  - CD4+ T cell exhaustion
  - machine learning immune biomarker
  - adolescent SARS-CoV-2 cohort
  - cross-condition fatigue immune signature
dataset_usage: []
datasets: []
source_refs:
  - cite:Sommen2026
related:
  - topic:long-covid-immune-dysregulation
  - topic:mecfs-long-covid-convergence
  - topic:biomarkers-and-objective-endpoints
  - topic:shared-failure-mode-across-pais
  - question:0001-shared-molecular-signature-across-triggers
  - hypothesis:0001-shared-dysregulated-attractor
  - hypothesis:0003-immune-exhaustion-feedback
  - paper:Klein2023
created: '2026-06-20'
updated: '2026-06-20'
---
# Long COVID: Deep single-cell immunophenotyping and machine learning reveal a general signature for fatigue

- **Authors:** Silke Lauren Sommen, Sunniva Segtnan, Joel Selvakumar, Lise Beier Havdal, Tonje Stiansen-Sonerud, Johannes Gjerstad, Siri Mjaaland, Unni Cecilie Nygaard, Vegard Bruun Bratholm Wyller, Ratnadeep Mukherjee, Lise Lund Berven (co-senior: Mukherjee and Berven)
- **Year:** 2026
- **Journal:** Journal of Translational Medicine, vol. 24, p. 736
- **DOI:** 10.1186/s12967-026-08149-3
- **BibTeX key:** Sommen2026
- **Source:** Full-text PDF (papers/pdfs/2026_Sommen_single-cell-immunophenotyping-ml-fatigue-signature.pdf), read 2026-06-20.

## Key Contribution

Using 41-marker CyTOF mass cytometry on PBMCs from a 2x2 factorial adolescent cohort (SARS-CoV-2+/− crossed with fatigue+/−; n = 20 per group, all female), this study shows that Long COVID shares its peripheral blood immune signature with a non-infectious fatigued control group — and that no immune alterations are unique to Long COVID relative to other post-infective fatigue states. Machine learning classifiers trained to predict fatigue (regardless of SARS-CoV-2 exposure) identified elevated terminal NK cell frequencies as the single most important predictive feature across all three models (Logistic Regression, Linear SVC, Random Forest), supporting the hypothesis that Long COVID is a specific example of a broader post-infective fatigue syndrome rather than a SARS-CoV-2-specific immune disease.

## Methods

**Cohort:** The LoTECA (Long-Term Effects of COVID-19 in Adolescents and Young Adults) prospective observational cohort (ClinicalTrials.gov NCT04686734), recruited December 2020–May 2021 in Norway during the B.1.1.7 (alpha) dominant period. For the CyTOF sub-study, n = 80 participants were selected (n = 20 per group): Long COVID (LC, SARS-CoV-2 PCR-positive, WHO/Fukuda criteria-positive at 6 months, CFQ ≥ 14), Recovered Convalescents (RC, SARS-CoV-2 PCR-positive, CFQ < 14, LC/PIFS criteria-negative), Fatigued Controls (FC, SARS-CoV-2-negative with fatigue, CFQ ≥ 14), and Healthy Controls (HC, SARS-CoV-2-negative, asymptomatic). All participants were female, median age 18.5 years; samples collected at the 6-month follow-up visit (median ~210 days post-infection/enrollment). Classification was performed blinded to initial SARS-CoV-2 status.

**Immunophenotyping:** PBMCs were isolated and split into two stimulation conditions: unstimulated and PMA/ionomycin-stimulated (4 h) with protein transport inhibitor for intracellular cytokine detection. CyTOF acquisition on a Helios mass cytometer using a 41-antibody panel (Table S2). ~3×10^6 events per multiplexed sample.

**Analysis pipeline:**
- Bead-based normalization; PeacoQC quality filtering; premessa debarcoding; CyTOFClean doublet removal.
- Unsupervised clustering: FlowSOM (30 initial metaclusters per major lineage), UMAP visualization. Manual cluster merging by marker heatmaps/histograms.
- Four major lineages resolved: T cells (CD3+), B cells (CD19+), NK cells (CD3−CD19−CD56+), myeloid cells (CD56−CD11b+).
- NK cells further sub-clustered into: early NK (CD56hi CD16lo), effector NK (CD56hi CD16hi), terminal NK (CD56lo CD16hi), CD56lo CD16lo NK — 20 metaclusters each.
- CD4+ T cells: Naive, Central Memory, Effector Memory, Effector, Naive Treg, Memory Treg, Activated Treg (7 subsets).
- CD8+ T cells: Naive, Central Memory, Effector Memory, Effector, CD8 Treg (5 subsets).
- B cells: Naive, Transitional, Founder, IgM Memory, IgD Memory, CSM (class-switched memory), Marginal Zone (MZ), Double Negative (DN) — 8 subsets.
- γδ T cells also examined (NKG2A+/− subsets).
- Differential abundance: diffcyt package (edgeR negative binomial), FDR-adjusted p < 0.05 threshold.
- Polyfunctionality (stimulated cells): COMPASS algorithm; Kruskal-Wallis + Dunn post-hoc.
- Machine learning (unstimulated frequencies): Logistic Regression (L1), Linear SVC (L1), Random Forest; 75/25 train/test split; 5-fold cross-validation, 500 iterations hyperparameter tuning; final accuracy averaged over 40 repeated train-test runs (scikit-learn 1.4.2). Target: fatigue (FC + LC) vs. non-fatigued (HC + RC) — pooling infection strata.

## Key Findings

**NK cell subsets (primary finding):**
- Terminal NK cells (CD56lo CD16hi) significantly elevated in both LC and FC versus HC; effector NK cells reduced in both fatigue groups versus HC.
- Early NK cells significantly lower in FC versus HC (trend in LC not reaching significance).
- CD56lo CD16lo NK cells significantly increased in FC vs. HC, trend in LC.
- The RC (recovered convalescent) group showed an intermediate NK subset distribution between HC and LC/FC groups, suggesting incomplete normalization at 6 months post-infection.
- PCA of terminal NK cell markers showed PC2 (24% variance) discriminated LC/FC from HC/RC, driven positively by HLA-DR and negatively by CD161 — indicating a more activated, less regulatory terminal NK phenotype in fatigued groups.
- COMPASS polyfunctionality in terminal NK cells: significantly higher in FC and LC vs. HC (Kruskal-Wallis p = 0.018); LC and FC had enhanced multi-cytokine production (Granzyme B, TNF-α, MIP-1β, IFN-γ combinations) upon PMA/iono stimulation.

**CD4+ T cells:**
- Elevated Naive Treg frequencies in LC vs. RC (significant); decreased Memory Treg and CD4+ Central Memory cells in LC vs. RC.
- Increased CD4+ Effector cells in both fatigue groups (FC vs. RC, p < 0.05).
- RC showed significantly higher COMPASS polyfunctionality scores in CD4+ T cells vs. HC, while both fatigue groups were comparable to HC — potentially reflecting better viral clearance capacity in RC.

**CD8+ T cells:**
- RC individuals showed significantly higher CD8+ Treg frequencies compared to FC and LC.
- No significant differences in CD8+ T cell COMPASS polyfunctionality across groups (Kruskal-Wallis p = 0.51).
- γδ T cell subset analysis revealed no statistically significant group differences.

**B cells:**
- Marginal Zone B cells (CD27+ IgM+ IgD+) significantly decreased in LC and FC vs. HC.
- Double Negative B cells (IgD− CD27− CD24− CD38−) significantly increased in FC vs. HC (trend in LC).
- Trend toward decreased Transitional B cells in fatigue groups (not significant after FDR correction).
- No differences in Naive B, IgD Memory B, or CSM B cells between groups.

**Machine learning — cross-condition fatigue signature:**
- Initial Random Forest (HC + RC vs. FC + LC): 80.8% accuracy on fatigued cases but poor specificity (only 46% HC correctly classified); Terminal NK identified as most important feature.
- After L1 penalization to reduce noise features: Linear SVC achieved 67.75% (non-fatigued) / 67.0% (fatigued); Logistic Regression 69.75% / 67.5%; Random Forest 68.0% / 74.5%.
- Top five features shared across all three models (Venn diagram, Fig. 6G): Early NK, Memory Treg, DN B cells, DN NK cells, and Terminal NK cells.
- Top positive features (associated with fatigue): Early NK, Memory Treg, CD4 Central Memory, IgD Mem B, DN B.
- Top negative features (associated with non-fatigued state): DN NK, Naive Treg, Terminal NK, NKG2a(−) γδT, IgM Mem B.

**Key negative result:** No immune alterations were unique to the LC group relative to FC; none of the cell-subset frequency differences survived FDR correction as LC-specific versus FC.

## Relevance

This paper bears directly on **question:0001** (shared molecular signature across PAIS triggers) and **hypothesis:0001** (shared dysregulated attractor): the explicit finding is that LC and a non-COVID fatigue group share the same peripheral immune perturbations, with no SARS-CoV-2-specific immune fingerprint detectable at 6 months. The elevated terminal NK cell signature is proposed as a general fatigue biomarker candidate.

The terminal NK hyperresponsiveness finding connects to **hypothesis:0003** (immune exhaustion feedback): the shift from early/effector NK to terminal NK, combined with enhanced polyfunctionality in terminal NKs, suggests a paradox of subset depletion alongside heightened per-cell cytokine output — consistent with the exhaustion-reactivation loop framing. The absent normalization of NK homeostasis in both fatigued groups (LC and FC) relative to RC echoes the disrupted homeostatic recovery logic of hypothesis:0001.

The CD4+ T cell findings (elevated Naive Tregs, reduced Memory Tregs, increased Effector T cells in LC) resonate with **topic:long-covid-immune-dysregulation** and with the Klein2023 Nature paper's report of CD4+ exhaustion/dysregulation in LC, though the populations studied and age groups differ (adolescents here vs. adults in Klein2023).

The B cell changes (decreased MZ B, increased DN B) overlap with alterations reported in other PAIS and autoimmune conditions (SLE), reinforcing **topic:mecfs-long-covid-convergence**.

Limitation for **question:0006** (JAK-STAT/IL-6): the 41-marker CyTOF panel did not include intracellular signaling markers or cytokine receptors probing JAK-STAT pathway activity directly; no plasma cytokine measures are reported here.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Terminal NK cells (CD56lo CD16hi) elevated in LC and FC | Immune dysregulation — innate arm | Proposed as general fatigue marker, not LC-specific |
| Early NK cells depleted in fatigue groups | NK homeostasis disruption | Consistent with incomplete homeostatic recovery |
| Enhanced polyfunctionality of terminal NK | Hyperresponsive innate effectors | Per-cell cytokine output elevated despite subset redistribution |
| LC = FC immune phenotype (no unique LC immune changes) | Shared failure mode across PAIS | Strong empirical support for PAIS convergence hypothesis |
| Recovered convalescents (RC) as immunological intermediate | Partial homeostatic recovery | NK subsets between HC and fatigued groups at 6 months |
| Naive Treg increase in LC vs. RC | Regulatory T cell rebalancing attempt | May reflect attempt to suppress chronic inflammation |
| DN B cell increase, MZ B cell decrease | B cell compartment dysregulation | Seen in other PAIS and autoimmune conditions |
| ML predicts fatigue (LC+FC) vs. non-fatigue (HC+RC) | Cross-condition biomarker discovery | Terminal NK most important feature; accuracy ~67–75% |

## Limitations

**Sample size and power:** n = 20 per group (n = 80 total) is small for a high-dimensional CyTOF + ML study. Multiple comparisons across dozens of immune subsets with FDR correction at this N yields low power for secondary comparisons; many trends noted in the paper do not reach significance. The authors note this is mitigated by prospective, well-characterized design.

**ML overfitting risk (critical concern):** The ML setup has structural weaknesses. The total feature set (~30+ immune subsets) is large relative to n = 80. The 75/25 train/test split yields only n = 10 per class in the test set — far too small for stable performance estimates. The reported "40 runs averaged" addresses variability in split randomization but does not cure the fundamental small-N problem. The confusion matrices show poor discrimination of non-fatigued individuals (HC + RC classified correctly at only ~67–70%), meaning the models are not reliably distinguishing fatigue from non-fatigue; they identify fatigued cases better, likely because the fatigued groups are less heterogeneous in immune subset frequencies than the non-fatigued groups. The terminal NK result is convergent across three model types and with the differential abundance analysis, lending some robustness — but the quantitative accuracy figures should not be taken as clinically meaningful.

**Female-only adolescent cohort:** All 80 participants are female, aged 12–25 years. The sex specificity and developmental stage limit generalizability to males and older adults. The authors explicitly acknowledge this.

**PBMC-only, single timepoint:** Granulocytes, tissue-resident cells, and myeloid cells are unreliable in frozen PBMCs and were not assessed. Only a single timepoint (6-month follow-up) is available; no longitudinal immune trajectory data. Whether terminal NK elevation precedes or follows symptom onset is unknown.

**PMA/ionomycin as stimulant:** PMA/iono is a very strong, non-physiological activator. It reveals maximal polyfunctional potential rather than antigen-specific or physiological-level responses. This limits interpretation of the COMPASS polyfunctionality findings as disease-relevant.

**Case definition mix in FC group:** The Fatigued Control group includes individuals whose fatigue was attributed to adverse life events or psychiatric comorbidity (Table S1). If psychiatric/psychosocial fatigue has a distinct immune profile from post-infectious fatigue, lumping them with LC in the ML target confounds the "general fatigue signature" claim.

**Lack of LC-specific immune changes may reflect statistical power, not biology:** With n = 20 per group, differences that are real but modest would not survive FDR correction. The absence of LC-specific findings is a true negative result conditional on this sample size and assay sensitivity.

**No plasma cytokines, no transcriptomics:** The study does not measure soluble mediators (plasma cytokines, chemokines) or gene expression, limiting mechanistic inference about why NK and T cell subset distributions differ.

**Variant and vaccination context:** Recruitment was during the alpha-dominant wave; vaccine uptake was 55% in LC and RC groups. Effects of vaccination and variant on immune phenotype cannot be separated from PAIS pathophysiology at this N.

## Model / Tool Availability

Raw FCS files without attached metadata can be made available upon request to the corresponding author (ratnadeep.mukherjee@fhi.no). All computer code (R and Python scripts for all analyses, citing publicly available packages: FlowSOM, CATALYST, PeacoQC, premessa, CyTOFClean, diffcyt, COMPASS, scikit-learn 1.4.2) is available upon request. The study does not release a standalone tool or pre-trained classifier. No public repository accession is cited in the paper.

## Follow-up

**Key questions raised:**

1. Does the terminal NK cell frequency elevation persist beyond 6 months, and does it normalize upon clinical recovery in longitudinal follow-up?
2. Is the terminal NK signature replicable in adult PAIS cohorts (ME/CFS, PTLDS) with larger n and both sexes? This is the central test of the "general fatigue marker" claim.
3. What drives terminal NK cell accumulation — impaired NK maturation, reduced NK cell clearance, or antigen-driven differentiation from early/effector pools? Is this linked to viral reactivation (EBV) or persistent antigen?
4. The Klein2023 (Nature) immune profiling study of adult long COVID found distinct features (cortisol, EBV reactivation, non-classical monocytes); how do the NK cell findings map between the two cohorts given age, sex, and variant differences?
5. Could the FC group contain individuals with undiagnosed post-infectious fatigue (from non-COVID agents) — in which case the "non-specific fatigue" comparison is less cleanly separating etiologies than the design implies?

**Papers to read next:**
- Galan et al. (ref 30): NK cell overactivation in Long COVID (Spanish cohort) — directly parallels the terminal NK finding
- Ryan et al. 2022 (ref 40): Long-term perturbation of peripheral immune system months after SARS-CoV-2 — NK cell trajectory paper
- Brenu et al. (refs 35–38): NK cell cytotoxicity in ME/CFS — context for whether the terminal NK signature is ME/CFS-specific or broader
- Walitt et al. 2024 (paper:Walitt2024): deep phenotyping of ME/CFS including immunophenotyping — cross-comparison opportunity
