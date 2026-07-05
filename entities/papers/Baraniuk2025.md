---
id: paper:Baraniuk2025
kind: paper
title: "Cerebrospinal fluid metabolomics, lipidomics and serine pathway dysfunction in myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS)"
status: active
ontology_terms:
  - cerebrospinal fluid metabolomics
  - lipidomics
  - serine pathway
  - one-carbon metabolism
  - post-exertional malaise
  - bioenergetics
  - sphingomyelin
  - myalgic encephalomyelitis/chronic fatigue syndrome
  - exercise provocation
dataset_usage: []
datasets: []
source_refs:
  - cite:Baraniuk2025
related:
  - question:0011-mitochondrial-basis-of-pem
  - question:0001-shared-molecular-signature-across-triggers
  - topic:mecfs-long-covid-convergence
  - topic:biomarkers-and-objective-endpoints
  - hypothesis:0001-shared-dysregulated-attractor
created: '2026-06-20'
updated: '2026-06-20'
---
# Cerebrospinal fluid metabolomics, lipidomics and serine pathway dysfunction in myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS)

- **Authors:** James N. Baraniuk
- **Year:** 2025
- **Journal:** Scientific Reports, vol. 15, article 7381
- **DOI:** 10.1038/s41598-025-91324-1
- **BibTeX key:** Baraniuk2025
- **Source:** Full-text PDF (papers/pdfs/2025_Baraniuk_csf-metabolomics-serine-pathway-mecfs.pdf), read 2026-06-20.

## Key Contribution

This study provides the first targeted mass-spectrometry-based metabolomic and lipidomic profile of cerebrospinal fluid (CSF) from ME/CFS subjects under two conditions — resting baseline and after submaximal bicycle exercise designed to provoke postexertional malaise (PEM) — compared with sedentary healthy controls. The central finding is that serine is persistently elevated in ME/CFS CSF while 5-methyltetrahydrofolate (5MTHF) is reciprocally reduced, indicating a functional block in the serine → glycine → one-carbon (folate) methylation axis. Serine's roles as a phospholipid and sphingomyelin precursor explain a parallel elevation of multiple sphingomyelins and phosphatidylglycerols, pointing to disrupted myelin-related lipid biology in the central nervous system. The CSF metabolomic profile in ME/CFS is dominated by this serine/folate/lipid axis and is largely distinct from prior plasma hypometabolic findings, reinforcing the CNS compartment as an independent locus of metabolic disruption.

## Methods

**Study design.** Cross-sectional case-control with exercise provocation arm. Two independent cohorts: (1) nonexercise cohort — lumbar puncture without prior exercise; (2) postexercise cohort — submaximal bicycle stress test (70% → 85% predicted heart rate for 25 min) followed by CSF collection 1–5 h later. Subjects could only appear in one cohort; cohorts were reconciled with MetaboAnalyst batch-correction tools (COMBAT).

**Cohort sizes.**
- Nonexercise: 45 ME/CFS (36 female), 20 sedentary controls (SC; 9 female).
- Postexercise: 15 ME/CFS (9 female), 12 SC (2 female).
- Total: 60 ME/CFS, 32 SC (Table 3 reports N = 60 and 32 for CSF chemistry; Table 2 gives N = 45 + 15 = 60 ME/CFS and 20 + 12 = 32 SC).

**Case definition.** ME/CFS diagnosed using 1994 CDC "Fukuda" criteria plus Canadian Consensus Criteria (CCC). PEM was a required feature per CCC. Subjects were not retrospectively assessed for 2015 IOM/SEID criteria. Sedentary controls had < 40 min aerobic exercise per week and did not meet ME/CFS criteria.

**Institution.** Georgetown University, Georgetown Howard Universities Clinical and Translational Science Clinical Research Unit (IRB 2006–481, 2009–229, 2013–0943, 2015–0579; ClinicalTrials.gov NCT03567811, NCT00810329).

**Metabolomics platform.** Targeted LC-MS/MS (QTRAP 5500, Sciex/Biocrates) measuring up to 179 endogenous metabolites. Targeted lipidomics (Xbridge amide column, QTRAP 5500) covering 21 lipid classes (FFA, DAG, TAG, PG, PC, PE, PI, PS, PA, LPC, LPE, LPI, LPA, ceramides, DCER, HCER, LCER, SM, acylcarnitines, CE) — 220 lipid targets. Data log-transformed, normalized, and standardized; zeros imputed at half the class minimum.

**Statistical analysis.** Two-tailed Student's t-test for initial screening with Hedges' g effect sizes; primary analysis by multivariate general linear model (GLM) in SPSS v29 with ME/CFS vs. SC as the primary factor and gender, exercise status (nonexercise vs. postexercise), age, and BMI as covariates or independent variables. Sidak correction for multiple comparisons (p < 0.05). Pathway enrichment in MetaboAnalyst 6.0 using SMPDB, KEGG, and RaMP-DB. Simultaneous Component ANOVA for 2×2 disease × exercise interaction. Spearman correlation matrix for analyte–questionnaire associations (|R| > 0.3, p < 0.015).

**Questionnaires and clinical measures.** CFS Symptom Severity Questionnaire (CFSQ), SF-36, Chalder Fatigue, Multidimensional Fatigue Inventory (MFI), McGill Pain Questionnaire, CMSI (interoception), COMPASS-31 (autonomic function), dolorimetry (central sensitization).

## Key Findings

**Serine / one-carbon axis (primary finding).**
- Serine was persistently and markedly elevated in ME/CFS CSF (Hedges' g = 0.962, 95% CI [1.412–0.527]; p = 0.000017 by t-test; also significant in multivariate GLM). This was the largest effect size among all metabolites tested.
- 5-Methyltetrahydrofolate (5MTHF) was significantly reduced in ME/CFS, indicating impaired folate-dependent methylation despite adequate serine supply.
- Sarcosine (N-methylglycine), a product of glycine methylation, was elevated; dimethylglycine and choline were reduced — consistent with incomplete flux through the serine → glycine → sarcosine → dimethylglycine → choline methylation cascade.
- Creatine and creatinine (methyl-group consumers downstream of the methionine cycle) were elevated. 5-Methylthioadenosine (MTA), a methionine pathway intermediate, was also elevated.
- Interpretation: serine metabolism is shunted toward sarcosine and creatine end products rather than completing folate-cycle methylation, creating a functional 5MTHF deficiency.

**Sphingomyelin and phospholipid elevation.**
- Six sphingomyelins (SM) were significantly elevated in ME/CFS (Hedges' g 0.46–0.75; p < 0.05). Serine is the precursor for sphinganine and hence ceramides → hexylceramides → sphingomyelins.
- Phosphatidylglycerols (PG; 11 of 17 mass spec targets, p = 0.000085 by Fisher Exact Test) and phosphatidylcholines (PC) and phosphatidylethanolamines (PE) were also elevated. 3-Phosphoglycerate (a serine precursor) links glycolysis to PG synthesis.
- Elevated sphingomyelins in the context of reduced choline may be compatible with CNS white matter pathology (demyelination or impaired remyelination), contrasting with the reduced serine, tyrosine, and choline pattern seen in multiple sclerosis CSF.

**TCA cycle and energy metabolism disruption.**
- Transaconitate (a TCA intermediate) was elevated in ME/CFS, suggesting diversion of citrate away from acetyl-CoA and toward aconitate/transaconitate, potentially short-circuiting the TCA cycle similarly to the Warburg effect in cancer.
- Glucose-1-phosphate and glucose-6-phosphate were elevated in the nonexercise cohort (consumed during exercise in both groups).
- Pantothenate and cysteamine (CoA metabolism) were elevated, further implicating mitochondrial energy pathway disruption.
- Citrate and glutamine were elevated, consistent with anaplerotic TCA disruption.

**Aromatic amino acids and neurotransmitter precursors.**
- Phenylalanine, tyrosine, and dopamine were elevated in ME/CFS; these are metabolized to acetyl-CoA via aromatic amino acid pathways.
- Dopamine elevation was unexpected and not explained by the primary pathway analysis.

**Purine and pyrimidine metabolism.**
- Hypoxanthine, xanthosine, purines, 1-methyladenosine, AMP, and 7-methylguanosine were elevated in ME/CFS, indicating disrupted purine catabolism or nucleotide turnover.

**Exercise (PEM provocation) effects on CSF.**
- In controls, exercise consumed lipids (phosphatidylglycerols, phosphatidylcholines, TAGs) while generating folate metabolites, glycine, thiamine, riboflavin, and phosphorylcholine (serine/phosphocholine synthesis).
- In ME/CFS, exercise consumed metabolites that were elevated at baseline; metabolites generated in controls were not equivalently produced in ME/CFS, suggesting a blunted or inverted metabolic response to exertion.
- 5MTHF, hexoses, phospholipids, and sphingomyelins were in the nonexercise > postexercise set for both groups, suggesting exercise-driven CNS uptake of these compounds.
- The nonexercise > postexercise contrast in ME/CFS included choline, creatinine, dopamine, and purine metabolites. Postexercise additions were glutathione (reduced), thiamine, riboflavin, butyrate metabolites, glycine, dimethylglycine, and phosphorylcholine.
- Notably, exercise did NOT trigger the severe PEM expected from maximal CPET; this was submaximal exercise (70–85% pHR), which produced only modest orthostatic symptom worsening. Maximal two-day CPET protocols may be needed to fully capture PEM-related CSF changes.

**Vitamins and cofactors.**
- SC had elevated 5MTHF, riboflavin, and flavin mononucleotide relative to ME/CFS, suggesting a relative vitamin B2 and B9 deficiency in ME/CFS. These vitamins are cofactors for enzymatic steps disrupted in the serine/one-carbon and TCA pathways.

**Correlations with symptoms.**
- Serine had the most correlations with questionnaire items (34 interactions, |R| > 0.3), notably with fatigue (CFS questionnaire total), Physical Fatigue, Permanance, and CPSS. Elevated serine and related metabolites were correlated with ME/CFS diagnostic hallmarks.
- A second correlation pattern linked 5MTHF and seven phosphatidylglycerols with exercise status, gender, and internal locus of control.
- A third pattern linked sphingomyelins and hexylceramides with age, transaconitate, citrate, dimethylglycine, riboflavin, glucose phosphates, and TCA/lipid metabolites.

**Metabolites higher in SC than ME/CFS (i.e., relatively depleted in ME/CFS):**
- 5MTHF, riboflavin, flavin mononucleotide, choline, dimethylglycine, 1-methylhistidine, N-acetylglutamine, FFA(16:1), 2,3-butanediol, indoleacrylic acid, FFA(20:0).

**Pathway enrichment (MetaboAnalyst; Fig. 3).**
- SMPDB top enrichments: Methionine Metabolism, Phenylacetate Metabolism, Pantothenate and CoA Biosynthesis, Pyrimidine Metabolism, Glycine and Serine Metabolism, Arginine and Proline Metabolism, Riboflavin Metabolism, Betaine Metabolism.
- KEGG top enrichments: Glycine/serine/threonine metabolism, Pyrimidine metabolism, Phenylalanine/tyrosine/tryptophan biosynthesis, Riboflavin metabolism, Purine metabolism, Glyoxylate/dicarboxylate metabolism, Arginine biosynthesis.
- RaMP-DB top enrichments: Oligodendrocyte specification/differentiation leading to myelin components; Immunoregulatory interactions between lymphoid and non-lymphoid cells; Kennedy pathway from sphingolipids; MTHFR deficiency; Sphingolipid pathway; Glycerolipids and glycerophospholipids.

## Relevance

**To question:0011 (mitochondrial basis of PEM).** This is the primary CNS-compartment data point for the bioenergetic-PEM question. The TCA disruption (elevated transaconitate, citrate diversion, pantothenate/CoA elevation), vitamin cofactor deficiency (relative B2/B9 insufficiency), and inverted exercise-metabolite response in ME/CFS all point toward mitochondrial and one-carbon metabolic failure under exertional demand. Critically, the serine → 5MTHF blockade could impair methylation-dependent mitochondrial function (e.g., folate-dependent one-carbon units needed for complex I assembly and mitochondrial translation). The finding that exercise consumes rather than generates folate metabolites in ME/CFS, while generating them in controls, is a CNS-level correlate of the metabolic incompetence hypothesis for PEM.

**To question:0001 (shared molecular signature across PAIS triggers).** The serine/one-carbon/sphingomyelin signature in CSF is distinct from, and not fully congruent with, plasma hypometabolic signatures in ME/CFS (Naviaux et al., Germain et al.) — suggesting the CNS compartment has a disease-specific perturbation that plasma alone cannot capture. Whether this pattern generalises to post-COVID or other PAIS remains untested.

**To topic:mecfs-long-covid-convergence.** Reference 11 (Volberding 2024 National Academies long COVID report) is cited for the ME/CFS–long COVID overlap, and CSF metabolomics of neuro-post-acute COVID sequelae (Chen 2022 in the discussion) showed a different profile (elevated sphinganine, ST1A1, disordered sphingolipid metabolism) — convergent at the sphingolipid level but divergent in specifics. This paper provides a pre-COVID ME/CFS CSF baseline against which neuro-long-COVID CSF profiles can be compared.

**To topic:biomarkers-and-objective-endpoints.** Serine (g = 0.962) and sphingomyelins (g 0.46–0.75) in CSF are objective, quantitative biomarker candidates for ME/CFS diagnosis and stratification, with the caveat that lumbar puncture limits clinical translation. The Spearman correlation between serine and fatigue questionnaire scores supports construct validity.

**To hypothesis:0001 (shared dysregulated attractor).** The CSF data suggest the CNS is locked in a metabolic state characterised by serine accumulation (blocked downstream flux), folate insufficiency, and compensatory sphingolipid build-up. This is consistent with a stable but pathological attractor state that does not self-correct with rest or mild exertion — a CNS-level analogue of the dysregulated homeostasis frame.

**To paper:Naviaux2016.** Naviaux et al. reported a hypometabolic plasma profile in ME/CFS with disrupted sphingolipid metabolism; the present study finds the opposite direction for some sphingomyelins in CSF (elevated, not reduced), consistent with the hypothesis that serine accumulation drives upstream sphingomyelin overproduction in the CNS while plasma sphingolipids reflect downstream depletion. Direct comparison is complicated by compartment, platform, and cohort differences.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Serine ↑ / 5MTHF ↓ in CSF | Metabolic/mitochondrial dysfunction | CNS-compartment one-carbon deficiency |
| Sarcosine ↑, dimethylglycine ↓, choline ↓ | Methylation impairment | Downstream of serine → glycine → methyl cascade |
| Sphingomyelins ↑ in CSF | CNS white matter / myelin pathology | RaMP-DB enrichment: oligodendrocyte differentiation pathways |
| Transaconitate ↑, citrate diversion | Mitochondrial TCA disruption | Warburg-like short-circuiting of TCA in CNS |
| Submaximal exercise → blunted metabolite generation in ME/CFS | Post-exertional malaise (PEM) | CNS metabolic incompetence under exertion; links to bioenergetic-PEM hypothesis |
| Riboflavin/5MTHF depletion relative to SC | Cofactor insufficiency | Mechanistic entry point for vitamin supplementation trials |
| CSF vs. plasma divergence | Compartment-specific pathophysiology | CNS not mirroring plasma; lumbar puncture required for full picture |
| Fukuda + CCC case definition | ME/CFS (stringent phenotype) | CCC requires PEM; SEID criteria not applied |

## Limitations

1. **Small sample, especially postexercise arm.** Postexercise cohort: 15 ME/CFS, 12 SC — too small to reliably interpret triple cross-products (Disease × Gender × Exercise); the authors acknowledge the smallest subgroup had 30 subjects and effects sizes from these cross-products should be considered preliminary.

2. **Two separate cohorts, not a within-person crossover.** Nonexercise and postexercise cohorts were recruited and sampled at different times; batch effects addressed with COMBAT but temporal confounding cannot be fully excluded.

3. **Submaximal exercise — PEM not fully induced.** The 70–85% pHR bicycle protocol caused only modest orthostatic worsening in ME/CFS; maximal two-day CPET (the standard provocation for severe PEM) was not performed. The CSF exercise signature may therefore underrepresent the true PEM metabolic signature.

4. **Biocrates targeted panel — not discovery metabolomics.** 179 metabolites and 220 lipids measured; formate (a key one-carbon metabolite) was not detected. Many secondary metabolites, microbiome-derived compounds, and novel analytes not in the Biocrates kit were invisible. This restricts pathway coverage and may miss important co-factors.

5. **Case definition: Fukuda + CCC, not SEID/IOM 2015.** Subjects were not retrospectively assessed for 2015 IOM criteria. Prevalence of key features (orthostatic intolerance) was not systematically captured. Cohort may not represent the broadest PAIS/ME/CFS phenotype.

6. **Sex imbalance and gender effects.** ME/CFS cohort is 80% female; SC nonexercise cohort is 45% female. Gender has large effects on CSF metabolome (57 analytes differed by sex in univariate analysis); the multivariate correction partially addresses this but residual confounding is possible.

7. **Dopamine elevation unexplained.** Elevated CSF dopamine in ME/CFS was an unanticipated finding not well accounted for by the primary serine/folate/TCA framework; may reflect catecholamine dysregulation, dysautonomia, or analytical artefact.

8. **Thiamine elevation flagged as possible artefact.** Authors note that lumbar puncture–associated erythrocyte lysis could elevate thiamine; absence of the expected accompanying amino acid changes argues against widespread contamination but cannot be fully excluded.

9. **No longitudinal or recovery data.** All measurements are cross-sectional within the exercise protocol timeframe; no follow-up CSF after PEM resolution to assess metabolite trajectory.

10. **Cohort from a single US academic centre (Georgetown).** Racial/ethnic and geographic representativeness is limited; the Discussion notes that African Americans have significantly different metabolomic profiles for several relevant analytes.

11. **CSF invasiveness limits biomarker translation.** Lumbar puncture is not a viable clinical screening tool; the CSF signature would need plasma or urine proxy markers for practical diagnostic use.

## Model / Tool Availability

No computational model, software tool, or processed dataset is released separately. Raw mass spectrometry abundances and supplementary tables (SOM S1–S4) are included as supplementary online material with the published article. MetaboAnalyst 6.0 (publicly available) was used for pathway enrichment and ANOVA simultaneous component analysis.

## Follow-up

- **Maximal two-day CPET + CSF protocol.** The authors explicitly call for maximal CPET (two consecutive days) followed by lumbar puncture to capture the full PEM-state CSF metabolome; this would close the key gap left by the submaximal provocation used here.
- **Plasma–CSF paired sampling.** Concurrent plasma and CSF in the same subjects would allow direct compartment comparison and resolve the apparent divergence from Naviaux2016's plasma hypometabolic findings.
- **Replication in post-COVID / neuro-long-COVID cohorts.** Chen et al. (2022) CSF data in neuro-COVID showed overlapping sphingolipid themes; a direct head-to-head comparison using the same Biocrates platform would test whether the serine/5MTHF axis is ME/CFS-specific or shared across PAIS.
- **Vitamin B2/B9 supplementation trial.** The relative cofactor deficiency (5MTHF, riboflavin) provides a mechanistic rationale for a targeted supplementation RCT; serine and sphingomyelin normalization could serve as surrogate endpoints.
- **Folate imaging.** CSF 5MTHF reduction combined with elevated serine raises the question of cerebral folate deficiency syndrome; anti-folate receptor antibodies (FOLR1 autoantibodies) should be measured in this cohort.
- **White matter imaging linkage.** The RaMP-DB oligodendrocyte pathway enrichment and sphingomyelin elevation justify paired MRI white matter analysis (DTI, myelin water imaging) in the same subjects.
- **Microbiome metabolite overlap.** Several ME/CFS-elevated metabolites were flagged as having possible microbial origins (indoleacrylic acid elevated in SC > ME/CFS; others not in KEGG). Gut–brain axis metabolite tracking would complement the CNS data.
- **Connection to question:0011:** Does the serine/one-carbon blockade explain impaired mitochondrial complex assembly or NAD+ cycling during exertion? One-carbon units from the serine → glycine → formate pathway feed the mitochondrial folate cycle required for complex I assembly factors.
