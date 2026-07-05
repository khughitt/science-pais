---
id: paper:Germain2022
kind: paper
title: Plasma metabolomics reveals disrupted response and recovery following maximal
  exercise in myalgic encephalomyelitis/chronic fatigue syndrome
status: active
ontology_terms:
  - ME/CFS
  - metabolomics
  - post-exertional malaise
  - maximal exercise
  - bioenergetics
  - recovery
  - CPET
  - glutamate metabolism
  - carnitine metabolism
  - lipid metabolism
dataset_usage: []
datasets: []
source_refs:
  - cite:Germain2022
related:
  - question:0011-mitochondrial-basis-of-pem
  - topic:mecfs-long-covid-convergence
  - topic:biomarkers-and-objective-endpoints
  - hypothesis:0001-shared-dysregulated-attractor
created: '2026-06-20'
updated: '2026-06-20'
---
# Plasma metabolomics reveals disrupted response and recovery following maximal exercise in myalgic encephalomyelitis/chronic fatigue syndrome

- **Authors:** Arnaud Germain, Ludovic Giloteaux, Geoffrey E. Moore, Susan M. Levine, John K. Chia, Betsy A. Keller, Jared Stevens, Carl J. Franconi, Xiangling Mao, Dikoma C. Shungu, Andrew Grimson, Maureen R. Hanson
- **Year:** 2022
- **Journal:** JCI Insight
- **DOI:** 10.1172/jci.insight.157621
- **PMCID:** PMC9090259
- **BibTeX key:** Germain2022
- **Source:** XML full text via Europe PMC (open access)

## Key Contribution

This study establishes that ME/CFS patients show a fundamentally abnormal metabolomic trajectory in the hours and days after maximal exercise, with the most striking disruption occurring during the 24-hour recovery window rather than during or immediately after exertion. Using the largest provoked-metabolomics cohort reported for ME/CFS to date (60 patients, 45 controls, 1157 plasma metabolites, four time points around two CPET challenges), the authors demonstrate that metabolic divergence between patients and controls *escalates* across the exercise-recovery timeline — the opposite of the normalization expected in healthy subjects. The critical insight is that PEM biology is most visible in the provoked state: the 24-hour recovery period exposes disruptions in energy, amino acid, and lipid pathways invisible at rest.

## Methods

**Design.** Two-day maximal cardiopulmonary exercise test (CPET) provocation protocol. Participants underwent two maximal-effort exercise tests on a stationary cycle at a 24-hour interval, with the explicit aim of provoking PEM. Blood was drawn at four time points: 15–20 min before exercise day 1 (D1PRE), 15–20 min after exercise day 1 (D1POST), before exercise day 2 (D2PRE; i.e., 24-hour recovery point), and 15–20 min after exercise day 2 (D2POST).

**Cohort.** N = 105 total: 60 ME/CFS (45 female, 15 male) and 45 healthy sedentary controls (30 female, 15 male), ages 18–69, similar BMI. ME/CFS diagnosis required fulfillment of the **Canadian Consensus Criteria (CCC)**. All patients were ambulatory (able to travel to testing sites and complete two CPETs) and therefore represent a mild-to-moderate severity range; very few scored in the mild category on the Bell scale or SF-36. Sites: Ithaca College, Weill Cornell Medicine, Workwell Foundation.

**Platform.** Metabolon Precision Metabolomics LC-MS global untargeted platform; 1157 plasma features total — 933 identified metabolites spanning 9 superpathways and 108 subpathways, plus 224 metabolites of unknown identity (19% of the dataset).

**Analysis pipeline.** Missing values imputed per-metabolite (minimum detected value). Wilcoxon rank-sum tests with Benjamini-Hochberg FDR correction (q-values reported at three thresholds: q < 0.05, q < 0.15, P < 0.05). Pathway enrichment via MetaboAnalyst 5.0 (KEGG and SMPDB libraries; pathway impact topology analysis). Chemical cluster enrichment via ChemRICH (chemical-similarity-based enrichment, not pathway-knowledge-dependent). Multivariate time-series analysis via MEBA (Multivariate Empirical Bayes Analysis of Variance, Hotelling T² test for temporal consistency). t-SNE for global dimensionality reduction. Linear model analysis comparing fold-changes between cohorts across all pairwise time-point combinations. Sex-stratified analyses throughout (female and male cohorts reported separately).

## Key Findings

**No global hypometabolism at rest.** At baseline (D1PRE), roughly half of metabolites were lower in ME/CFS vs. controls for any individual; the distribution of fold-changes was symmetric around zero for women, making global resting hypometabolism (as reported in Naviaux 2016 using a different platform and sex-balanced design) non-apparent in this female-dominant cohort. The male cohort showed a mild asymmetry toward lower metabolites, consistent with sex-specific effects.

**Escalating metabolic divergence across the protocol.** The number of metabolites significantly different between patients and controls increased monotonically across the four time points. In women at q < 0.05, there were 8-fold more differentially abundant metabolites at D2POST compared with D1PRE. Pathway analysis corroborated this: 11 significantly different pathways at D1PRE, 19 at D1POST, 17 at D2PRE, and 28 at D2POST. This is the principal finding: exertion and especially the recovery period unmasked patient-control differences that were largely invisible at rest.

**The 24-hour recovery period is maximally abnormal.** Recovery metabolomics (D1POST → D2PRE) identified 61 metabolites with significantly different trajectories between patients and controls (q < 0.15), more than any other pairwise time-point comparison. Over a quarter of identified SMPDB pathways (28 total at P < 0.05, 20 at q < 0.05) were statistically different during recovery. Key abnormal recovery pathways included: citric acid cycle (TCA), pyruvate metabolism, malate-aspartate shuttle, glucose-alanine cycle, glycolysis, amino sugar metabolism, and urea cycle / ammonia recycling. Lipid pathways were notably less prominent in recovery than during exercise.

**Glutamate metabolism as a central disrupted node.** Many of the pathways most disrupted in the ME/CFS recovery period converge on glutamate metabolism. Pathways dependent on glutamate include butyrate metabolism, arginine and proline metabolism, lysine and alanine metabolism, and nucleic acid / protein synthesis. Glutamate is also the primary CNS excitatory neurotransmitter and plays roles in neuronal plasticity. The authors flag glutamate dysfunction as a "common denominator" linking energy, nitrogen, and neuro-related pathway disruptions, though the directionality and causal role remain uncharacterized.

**Exercise on day 1 vs. day 2 produces divergent effects in patients, not controls.** Comparing the metabolomic response to day-1 exercise (ΔD1) versus day-2 exercise (ΔD2), healthy controls showed no significantly different pathways between days (same exercise response profile both days). ME/CFS patients showed 14 significantly different pathways (P < 0.05) between ΔD1 and ΔD2, including butyrate metabolism, carnitine synthesis, malate-aspartate shuttle, glucose-alanine cycle, branched-chain fatty acid oxidation, and related lipid/energy pathways. This asymmetry — a normal, reproducible exercise response in controls vs. a disrupted, non-reproducible response in patients — is a hallmark of PEM biology.

**Specific metabolite classes driving recovery abnormalities.** During the D1POST → D2PRE recovery window in patients: (a) short- and medium-chain acylcarnitines (chains < 12 C) were heavily over-represented among significant metabolites (53% of significant lipids were carnitine-containing, vs. 20% of all lipids in the dataset), suggesting abnormal fatty acid beta-oxidation and mitochondrial import; (b) branched-chain and aromatic amino acids (leucine/isoleucine/valine, arginine, proline subpathways) were differentially distributed; (c) TCA cycle intermediates including alpha-ketoglutarate decreased in patients but increased in controls after exercise (opposite directionality); (d) lactate showed similar absolute kinetics in both groups across the protocol, but the maximum Hotelling T² for patients was lactate ranked fifth behind malate, 3-methyl-2-oxobutyrate, 4-methyl-2-oxopentanoate, 3-methyl-2-oxovalerate, and pantothenate (vitamin B5), pointing to branched-chain amino acid catabolism and CoA metabolism as more strained.

**Unknown metabolites are enriched among the most significantly different features.** At baseline (D1PRE) in women, 3 of 7 metabolites significant at q < 0.05 were of unknown identity (43%). The proportion of unknowns among the most statistically different features remained elevated across time points, reaching 25% of metabolites with high Hotelling T² scores. At D2POST the most time-varying unknown in controls/patients (16397) showed a 24-hour recovery divergence: 84% of patients' plasma levels of this compound declined during recovery vs. 50% of controls. This enrichment of unknowns among top discriminating features highlights an interpretive gap.

**Sex differences.** Female patients drove most significant findings (the male subcohort was underpowered at N = 15 ME/CFS men for FDR-corrected tests). Male patients showed recovery-period changes only at P < 0.05, including phosphatidylcholine/phosphatidylethanolamine biosynthesis differences. The overall pattern of sex differences is consistent with prior studies; the authors report distinct but qualitatively related metabolic patterns in men vs. women.

**1,5-anhydroglucitol (1,5-AG).** The only highly significant baseline metabolite with a catalogued HMDB entry was 1,5-AG (HMDB0002712), a validated proxy for short-term glycemic control. Its reduction in patients at baseline directs attention to carbohydrate/glycemic dysregulation as a resting feature, independent of exercise provocation.

## Relevance

This paper is directly relevant to `question:0011-mitochondrial-basis-of-pem` and a key resource for the project's PEM biomarker and mechanistic goals. Its primary contribution is demonstrating that **provocation reveals what rest conceals**: the metabolomic differences between ME/CFS patients and matched sedentary controls are small at rest but expand dramatically — up to 8-fold in number — after maximal exercise and especially during the 24-hour recovery period. This makes the recovery trajectory itself a candidate **objective PEM biomarker**: a measurable disruption in metabolic recovery that is not visible in resting blood draws and that distinguishes patients from controls who perform the same exercise.

Relation to the project framework:

- **Complements Naviaux2016 (resting hypometabolism):** Naviaux et al. found a global resting hypometabolic signature; Germain et al. do not reproduce this in their larger, female-dominant cohort at rest (D1PRE), but reveal a profound *dynamic* deficit visible only under provocation. The two findings are compatible if resting hypometabolism is sex- or cohort-dependent and if the recovery-trajectory deficit is the more robust and specific signal. Together they suggest ME/CFS occupies a constrained metabolic operating range with poor reserve under stress.

- **Relates to `hypothesis:0001-shared-dysregulated-attractor`:** The disrupted recovery trajectory — where patients fail to return to metabolic baseline after exercise while controls do — is a functional signature of a system unable to restore homeostasis after perturbation. This is precisely the phenomenology predicted by an attractor-basin model: the system is displaced by exercise but lacks sufficient restoring forces to recover, falling instead into a PEM basin. The metabolic data provide a quantitative, pathway-level correlate of this attractor dynamic.

- **Grounds `question:0011` (mitochondrial/bioenergetic basis of PEM):** The abnormal recovery pathways (TCA, pyruvate, malate-aspartate shuttle, carnitine acylation, branched-chain amino acid catabolism) collectively point to impaired mitochondrial substrate flux and recovery of oxidative metabolism as central to PEM. Alpha-ketoglutarate's inverse response (increases in controls, decreases in patients after exercise) is a particularly interpretable TCA-cycle disruption signal.

- **PEM biomarker operationalization:** The study demonstrates that a two-day CPET protocol with four-timepoint plasma metabolomics can generate a reproducible patient-vs-control separation, and that the 24-hour recovery window (D1POST → D2PRE comparison) is the most discriminating epoch. This supports using the provoked metabolomic recovery trajectory as an objective outcome measure for future intervention trials, though validation across cohorts and replication with targeted assays are needed.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Post-exertional malaise (PEM) | `topic:biomarkers-and-objective-endpoints` | PEM as measurable endpoint via CPET-provoked metabolomics |
| Recovery-trajectory deficit (D1POST→D2PRE) | Candidate provoked PEM biomarker | The key novel signal; resting metabolomics misses it |
| Two-day CPET provocation design | Provoked-challenge paradigm | Generates 4-timepoint longitudinal metabolomics window |
| Glutamate-dependent pathway disruptions | Metabolic / mitochondrial dysfunction node | Bridges energetics to CNS effects |
| Failed metabolic recovery | `hypothesis:0001-shared-dysregulated-attractor` | Operational signature of attractor-basin dynamics |
| Acylcarnitine overrepresentation in recovery | Mitochondrial beta-oxidation failure | Accumulation of incompletely oxidized fatty-acid intermediates |
| Canadian Consensus Criteria (CCC) | PAIS case definition | CCC is more stringent than Fukuda criteria; captures PEM as required |

## Limitations

1. **No replication cohort.** Single study; the provoked metabolomic recovery trajectory has not been independently validated in an external ME/CFS cohort.

2. **Platform-dependent metabolite coverage.** Metabolon's Precision Metabolomics platform covers 933 identified metabolites; the identity of 224 features (19%) remains unknown, and several of these unknowns are among the most discriminating features. Results cannot be directly mapped to prior studies using different platforms.

3. **Sedentary control design.** Controls were matched for sedentary behavior, not fitness level. This is appropriate for comparing PEM-related responses to maximal effort, but exercise-experienced controls would clarify whether recovery disruptions reflect deconditioning vs. disease-specific biology.

4. **Mild-to-moderate severity selection bias.** All ME/CFS participants had to be ambulatory enough to travel and complete two CPETs. The most severely affected patients — those most likely to have the largest PEM responses — are entirely absent from this cohort, which likely *underestimates* the recovery-trajectory deficit.

5. **Underpowered male subcohort.** N = 15 male ME/CFS participants is insufficient for FDR-corrected metabolomics; male results are only interpretable at P < 0.05. Sex-stratified conclusions for men should be considered preliminary.

6. **Cross-sectional within-timepoint comparisons.** The primary within-cohort trajectory analyses (recovery deficit) are computed as fold-changes per participant across time points; but the comparison between patient and control *recovery trajectories* is still cross-sectional in that the two groups are not the same individuals. Randomized crossover or paired designs would be stronger.

7. **No causal mechanistic validation.** The metabolomic differences are associative; whether disrupted glutamate or carnitine metabolism *causes* PEM vs. co-occurs with it is not established. Orthogonal measurements (e.g., muscle biopsy, 31P-MRS, functional immune assays) would be needed to establish mechanism.

8. **No long COVID or cross-trigger comparison.** This paper is ME/CFS-specific; whether the same provoked recovery trajectory is present in long COVID or other PAIS is unknown, leaving the shared-mechanism question (central to this project) open.

9. **Potential confound from 1,5-AG and glucose fluctuations.** Carbohydrate intake and hydration status can affect 1,5-AG and metabolite levels; dietary standardization prior to blood draws is not described in detail.

## Model / Tool Availability

None. Metabolon data and R analysis scripts are not publicly deposited. The complete Metabolon metabolomics spreadsheet is provided as Supplemental Data File 1 within the paper's supplemental materials at the JCI Insight DOI. MetaboAnalyst 5.0 and ChemRICH are publicly accessible online tools used for analysis.

## Follow-up

**Papers to read in context:**
- Naviaux2016 (resting hypometabolism in ME/CFS; direct comparison study)
- Che2025 (provoked CPET + multi-omics; innate-immune coupling to metabolic failure; already in project)
- Fluge2016 (JCI Insight; impaired pyruvate dehydrogenase function in ME/CFS; directly relevant to TCA disruption found here)
- Contrepois2020 (Cell; "molecular choreography" of healthy exercise response; the comparator the authors cite for their t-SNE design)
- McGregor2019 (PEM association with glycolysis, acetylation, hypermetabolism in urine/serum; partially overlapping design)

**Questions this raises:**
- Does the provoked metabolomic recovery trajectory replicate in an independent ME/CFS cohort, and does it transfer to long COVID patients (a cross-PAIS validation)?
- Which of the significantly disrupted recovery metabolites (especially unknowns 16397 and 15245) can be identified and targeted for follow-up assay development?
- Is the alpha-ketoglutarate response (inverted kinetics after exercise in patients vs. controls) detectable via 31P-MRS or stable isotope tracing, and does it correlate with PEM severity?
- Do the acylcarnitine accumulation patterns in recovery indicate a specific beta-oxidation enzymatic bottleneck that could be targeted pharmacologically?
- Would including bedbound or severely affected ME/CFS patients (via home-based, lower-intensity provocation protocols) reveal an even more pronounced recovery deficit, or qualitatively different pathways?
