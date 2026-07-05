---
id: "paper:Shankar2025"
kind: "paper"
title: "Oxidative stress is a shared characteristic of ME/CFS and Long COVID"
status: active
ontology_terms:
  - oxidative stress
  - reactive oxygen species
  - mitochondrial dysfunction
  - T cell hyperproliferation
  - glutathione
  - lipid peroxidation
  - peripheral blood mononuclear cells
  - post-acute infection syndrome
  - metformin
dataset_usage: []
datasets: []
source_refs:
  - cite:Shankar2025
related:
  - topic:mecfs-long-covid-convergence
  - topic:biomarkers-and-objective-endpoints
  - topic:shared-failure-mode-across-pais
  - question:0011-mitochondrial-basis-of-pem
  - question:0001-shared-molecular-signature-across-triggers
  - hypothesis:0001-shared-dysregulated-attractor
  - hypothesis:0003-immune-exhaustion-feedback
  - paper:Naviaux2016
  - paper:Che2025
created: "2026-06-20"
updated: "2026-06-20"
---

# Oxidative stress is a shared characteristic of ME/CFS and Long COVID

- **Authors:** Vishnu Shankar, Julie Wilhelmy, Ellis J. Curtis, Basil Michael, Layla Cervantes, Vamsee Mallajosyula, Ronald W. Davis, Michael Snyder, Shady Younis, William H. Robinson, Sadasivan Shankar, Paul S. Mischel, Hector Bonilla, and Mark M. Davis
- **Year:** 2025
- **Journal:** Proceedings of the National Academy of Sciences (PNAS), Vol. 122, No. 28, e2426564122
- **DOI/URL:** https://doi.org/10.1073/pnas.2426564122
- **BibTeX key:** Shankar2025
- **Source:** Full-text PDF (papers/pdfs/2025_Shankar_oxidative-stress-shared-mecfs-long-covid.pdf), read 2026-06-20.

## Key Contribution

This is a within-study, head-to-head molecular comparison of ME/CFS and Long COVID (LC) donors versus healthy controls (HCs), demonstrating that elevated oxidative stress in peripheral blood lymphocytes — driven by mitochondrial dysfunction and aberrant reactive oxygen species (ROS) clearance — is a shared biochemical hallmark of both conditions. The study provides direct measurement of intracellular redox properties (not serum surrogates) across both patient groups studied in parallel under the same assay pipeline at Stanford, constituting the strongest existing within-study evidence for a shared oxidative-stress signature. It further identifies robust sex-specific divergence in the oxidative pathway: females drive ROS-dependent T cell hyperproliferation, while males manifest predominantly mitochondrial lipid peroxidation, and proposes metformin as an FDA-approved candidate to attenuate this T cell hyperproliferation in ME/CFS female donors.

## Methods

**Design:** Cross-sectional, within-study comparison of three arms — 25 healthy controls (HCs), 27 ME/CFS donors, and 20 LC donors — all processed through the same assay pipeline at Stanford. This is explicitly a head-to-head comparison: both patient groups are studied together, not across separate publications.

**Case definitions:**
- ME/CFS: National Academy of Medicine (NAM) criteria (Beyond ME/CFS, 2015), diagnosed by a physician; Fukuda and Canadian Consensus criteria also applied; cohort includes patients diagnosed before and after COVID-19 pandemic onset.
- LC: CDC definition for "LC or post-COVID conditions" combined with a symptom and functional status questionnaire (Post-COVID Functional Status [PCFS] Scale); participants had symptoms assessed in the last 7 days before appointment.

**Cohort characteristics:** Mean ages balanced across the three groups; proportion of females slightly higher in LC and ME/CFS arms (reflecting the known higher female incidence).

**Assays (multi-modal):**
- **Flow cytometry** — intracellular ROS (DCFDA dye, 2',7'-dichlorofluorescein diacetate), mitochondrial Ca²⁺ (Rhod-2 AM), mitochondrial superoxide dismutase 2 (SOD2) protein levels, reduced glutathione (GSH), lipid peroxides (ratiometric sensor), and lipid droplet content; measured across CD19 B cells, CD4 T cells, and CD8 T cells in PBMCs.
- **Mass spectrometry (HILIC-MS)** — 200,000 sorted CD3⁺ T cells from ME/CFS donors and HCs; 45,507 unique m/z analytes detected, 747 identified with analytical standards; Turium systems-chemistry platform used to map 327 metabolic pathways.
- **RNA-seq reanalysis** — reanalysis of published single-cell and bulk RNA-seq datasets (GSE262861, GSE128078, GSE224615) to validate GPX4, PLA2G4A, and PLA2G6 transcript differences; longitudinal LC data from Phetsouphanh et al. (Nat. Commun. 2024) also reanalyzed.
- **Immunofluorescence** — GPX4 staining in CD3 T cells from HC, LC, and ME/CFS donors (n = 426 HC, 603 ME/CFS, 239 LC CD3 T cells quantified).
- **T cell proliferation assay** — CellTrace Violet dye with anti-CD3/CD28 and IL-2 stimulation; proportion of proliferating T cells assessed at day 5 post-stimulation under treatment with N-acetylcysteine (NAC), metformin (10 µM), and liproxstatin-1.
- **Family cohort (fPOP)** — three patients from the family population-omics profiling cohort with chronic fatigue symptoms used as a precision-medicine case study for drug testing.

## Key Findings

**1. Elevated ROS in both ME/CFS and LC lymphocytes (vs. HCs):**
- DCFDA flow cytometry identifies significantly elevated total ROS in ME/CFS and LC PBMCs across CD4 T, CD8 T, and CD19 B cells (HC vs. ME/CFS two-sided t-test CD4T P = 0.0458, CD8T P = 0.0974, CD19B P = 0.356; HC vs. LC CD4T P = 0.0076, CD8T P = 0.0182, CD19B P = 0.0842).
- A bimodal distribution in ROS levels exists among ME/CFS donors, explained by sex: 8/15 ME/CFS female donors show 2–4× higher ROS vs. controls; no significant ROS differences between male ME/CFS/LC donors and male controls.

**2. Shared mitochondrial dysfunction:**
- Mitochondrial ATP levels are decreased ~1.6× in ME/CFS (P = 0.0458 CD4T) and ~2.8× in LC (P = 0.0076 CD4T) donors vs. HCs.
- Mitochondrial Ca²⁺ (Rhod-2 AM) is 1.67× higher in ME/CFS and 1.32× higher in LC vs. HCs; elevated uniquely in female donors in both groups.
- SOD2 protein levels are significantly lower in LC CD4 and CD8 T cells vs. HCs; ME/CFS levels also lower but difference similar across sexes.
- The ratio of Ca²⁺ to SOD2 MFI is 1.75× elevated in ME/CFS and 1.67× in LC (both vs. HCs), underscoring shared mitochondrial dysfunction.

**3. Sex-specific divergence in redox pathway:**
- **Females (ME/CFS and LC):** Elevated total ROS, higher mitochondrial calcium, higher GPX4 (glutathione peroxidase 4), and higher GSH; oxidative stress drives T cell hyperproliferation (CD4 ME/CFS females show 26.5% and LC females 39.7% higher proliferation than female HCs on average; ME/CFS female CD8T 28.6% higher, LC female CD8T 42.8% higher).
- **Males (ME/CFS and LC):** No significant ROS elevation, but pronounced mitochondrial lipid peroxidation (MitoPerOx); lower lipid droplets; likely driven by PLA2G6 suppression distinct from females.
- Sex hormones hypothesized as partial explanation (estradiol regulates antioxidant enzymes and T cell redox biology; PPARα differences in CD4 T cells).

**4. Lipid oxidative damage:**
- GPX4 immunofluorescence shows 1.77× (ME/CFS) and 1.9× (LC) higher GPX4 levels in CD3 T cells vs. HCs (P < 2.2 × 10⁻¹⁶ for both).
- GPX4 elevation concentrated in central-memory CD4 T cells (not naïve), suggesting deficient adaptive immune memory formation.
- Phospholipid metabolites — lysophosphatidylethanolamine (lysoPE) species [lysoPE(22:5), lysoPE(22:4), lysoPE(22:6), lysoPE(20:4), lysoPE(16:0), lysoPE(20:3)] — significantly elevated in ME/CFS T cell mass spectrometry, consistent with phospholipid synthesis dysregulation; PLA2G4A transcript elevated in ME/CFS (GSE128078, P = 0.044).

**5. GSH elevation as compensatory antioxidant response:**
- Both ME/CFS and LC males and females show significantly higher GSH vs. HCs (ME/CFS females: HC vs. ME/CFS CD19B P = 0.00048, CD4T P = 0.00159).
- GSH positively correlates with total ROS across all lymphocyte populations (females CD19B R = 0.56, P = 0.0039; CD4T R = 0.63, P = 0.00069; CD8T R = 0.52, P = 0.0078), consistent with GSH being upregulated in response to elevated H₂O₂.
- GSH inversely correlates with lipid droplets (males CD19B R = −0.9, P = 2.5 × 10⁻⁵), linking redox homeostasis to lipid composition.

**6. T cell hyperproliferation driven by ROS and linked to fatigue:**
- Proliferation linearly scales with oxidative stress in ME/CFS and LC female donors: higher initial ROS load at day 0 predicts higher proportion of proliferating T cells at day 5 (CD8T R² = 0.9078, CD4T R² = 0.7472 for ME/CFS).
- ME/CFS male T cells exhibit relative ROS insensitivity, consistent with mitochondrial membrane integrity loss reducing capacity to increase ROS upon stimulation.
- Hyperproliferating T cells act as an "energy sink," potentially explaining post-exertional fatigue: T cell activation at elevated Ca²⁺ drives ROS → NFAT → IL-2 → further proliferation feedback loop.

**7. Metformin attenuates T cell hyperproliferation in ME/CFS:**
- 10 µM metformin (FDA-approved) significantly reduces CD4 T cell hyperproliferation in ME/CFS female donors: CD4 9.8% reduction (P = 0.041), CD8 10.5% reduction (P = 0.39), vs. no effect on HCs (HC CD4 P = 1, CD8 P = 0.69).
- NAC (N-acetylcysteine) at micromolar levels did not reduce T cell hyperproliferation in ME/CFS or LC females.
- Liproxstatin-1 showed no statistically significant effect in female ME/CFS/LC.
- Mechanism proposed: metformin inhibits mitochondrial complex I proteins, subsequently induces SOD2 expression, reducing ROS formation — consistent with the SOD2 deficit identified.
- A double-blind Phase III clinical trial (n > 1,300) showed metformin reduced LC incidence by 41% post SARS-CoV-2 infection (ref. 68), particularly among females and those with higher BMI — paralleling this study's sex-specific findings.

**8. LC vs. ME/CFS distinctions within shared signature:**
- LC T cells show a heavy-tailed GSH distribution (extreme values); ME/CFS T cells show a shifted and bounded extreme value distribution, suggesting ME/CFS captures an intermediate-but-distinct state where continuous oxidative exposure has cultivated some ROS tolerance.
- LC donors overall show lower mitochondrial SOD, ATP levels, and calcium levels vs. ME/CFS donors; symptom duration moderately correlates with ROS signatures in LC females.
- The authors interpret LC as potentially capturing an earlier or less adapted oxidative stress state, while ME/CFS represents chronic adaptation.

## Relevance

This paper is directly and strongly relevant to the core comparative question of this project (question:0001-shared-molecular-signature-across-triggers) because it provides within-study, head-to-head molecular evidence — not cross-study meta-comparison — that ME/CFS and LC share a conserved oxidative-stress biology at the level of lymphocyte bioenergetics. Key connections:

**hypothesis:0001-shared-dysregulated-attractor:** The shared mitochondrial ROS/Ca²⁺/SOD2 signature, present in both conditions using identical assays in the same cohort, provides some of the clearest evidence to date that ME/CFS and LC occupy overlapping pathophysiological attractors at the immune-metabolic level. The sex-specific divergence within this shared attractor is consistent with the idea that the attractor is traversed via different entry paths (distinct antioxidant compensation strategies), while the common endpoint (mitochondrial dysfunction, T cell hyperproliferation, fatigue) is the attractor state.

**hypothesis:0003-immune-exhaustion-feedback:** The ROS → Ca²⁺ → NFAT → IL-2 → T cell proliferation → energy drain loop identified here is a concrete mechanistic instantiation of an immune feedback that sustains symptoms. The finding that ME/CFS female T cells hyperproliferate in a ROS-dependent manner upon stimulation, yet display GPX4 elevation in memory (not naïve) cells, is consistent with a deficient adaptive immune response and constitutive immune activation driving persistent fatigue.

**question:0011-mitochondrial-basis-of-pem:** The energy-sink model proposed — where excess T cell proliferation driven by mitochondrial Ca²⁺ and ROS drains finite host energy reserves — offers a concrete mechanism for post-exertional malaise (PEM), linking immune activation directly to bioenergetic depletion. The 10× reduced slope of T cell proliferation in response to ROS in ME/CFS males vs. controls is consistent with mitochondrial membrane integrity loss reducing proliferative capacity, suggesting the bioenergetic failure is not simply a fatigue epiphenomenon but a direct mitochondrial sequela.

**paper:Naviaux2016 (dauer hypothesis / metabolic hibernation):** Naviaux's cell danger response and dauer-like metabolic suppression frame are partially complementary. Where Naviaux proposes metabolic down-regulation as a survival response to chronic danger signaling, Shankar et al. identify active ROS-driven T cell hyperproliferation consuming excess energy. These are not necessarily contradictory — the hyperproliferating immune compartment may be the source of sustained danger signaling (CDR) that triggers metabolic hibernation in non-immune tissues — but the tension is worth tracking.

**paper:Che2025:** The Che et al. paper (if it addresses immune phenotyping or bioenergetics in PAIS) may corroborate or extend the sex-specific immune dysregulation findings here. Cross-reference warranted.

**topic:shared-failure-mode-across-pais:** The study strengthens the shared-failure-mode frame by providing multi-modal (flow cytometry, mass spectrometry, RNA-seq, immunofluorescence) within-study evidence rather than cross-study inference. It does not extend to other PAIS conditions (post-Lyme, post-Q-fever, etc.), but the mitochondrial/ROS mechanism it identifies is a strong candidate for broader testing.

**topic:biomarkers-and-objective-endpoints:** The ROS-based lymphocyte flow cytometry assay (DCFDA) and T cell proliferation upon stimulation emerge as candidate quantitative biomarkers measurable from standard blood draws — directly relevant to the project's interest in objective, scalable diagnostic endpoints.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Elevated lymphocyte ROS (DCFDA) | Shared oxidative-stress signature | Within-study, head-to-head ME/CFS vs. LC |
| Mitochondrial Ca²⁺ / SOD2 imbalance | Mitochondrial dysfunction mechanism | Shared across both conditions; uniquely elevated in females |
| ROS-driven T cell hyperproliferation | Immune activation / exhaustion feedback | Specifically in female ME/CFS and LC; energy-sink model for fatigue |
| Metformin attenuation of proliferation | Therapeutic candidate (ROS-modulating) | FDA-approved; parallels Phase III LC prevention trial |
| Sex-specific redox divergence | Covariate-sensitive phenotype | Females: ROS/Ca²⁺/GPX4 path; males: lipid peroxidation path |
| GPX4 elevation in memory CD4 T cells | Adaptive immune memory defect | Consistent with deficient recall / long-term immunity |
| LysoPE metabolite elevation (mass spec) | Phospholipid dysregulation | PLA2G4A-mediated; consistent with earlier plasma metabolomics |
| T cell energy-sink model | Bioenergetic basis of PEM | Mechanistic bridge from immune activation to post-exertional fatigue |

## Limitations

1. **Small cohort sizes:** 25 HC, 27 ME/CFS, 20 LC — adequate for discovery-level findings and the multi-modal confirmation strategy, but underpowered for subgroup analyses (especially sex-stratified comparisons within each condition). Sex-stratified results for males in particular rest on small n.

2. **Cross-sectional design:** No longitudinal follow-up within the primary cohort. Duration of ME/CFS symptoms (often years) vs. LC symptoms (months to years in this cohort) differs — the authors note this confounds direct severity comparison. Causal directionality of ROS elevation cannot be established.

3. **No pre-infection baseline:** The study cannot distinguish whether oxidative stress is a consequence of infection per se, an antecedent vulnerability, or a consequence of chronic illness/inactivity. This is a fundamental limitation of all cross-sectional PAIS studies.

4. **LC case definition heterogeneity:** LC is defined by symptom persistence and functional status scale (PCFS), not by confirmed SARS-CoV-2 variant, severity of acute illness, vaccination status, or time since infection. These covariates modulate immune phenotypes and are not reported as stratification variables in the main analysis.

5. **ME/CFS case definition breadth:** The cohort spans NAM, Fukuda, and Canadian Consensus criteria-defined patients, which have different inclusion thresholds for fatigue severity and functional impairment. Mixed definitions may increase phenotypic heterogeneity within the ME/CFS arm.

6. **No controls for confounders:** No data reported on physical activity levels, BMI (except BMI correlation noted for LC), medications, sleep, or comorbidities in the HC arm. These can modulate lymphocyte ROS independently of disease status.

7. **DCFDA caveats:** DCFDA is a broad ROS indicator sensitive to H₂O₂ and other peroxides but not superoxide directly; the authors acknowledge this (noting DCFDA captures cellular H₂O₂) and cross-validate with other assays, but DCFDA can also be sensitive to non-ROS artifacts (e.g., cell viability differences).

8. **Metformin data are preliminary:** The in-vitro proliferation reduction (9.8% CD4 reduction, P = 0.041) is statistically modest and based on 6 ME/CFS female donors. The fPOP precision-medicine case study is n = 3 patients and is explicitly described as hypothesis-generating.

9. **Limited extension to other PAIS:** The study is ME/CFS and LC only. Whether the shared mitochondrial ROS signature extends to post-Lyme, post-Q-fever, post-sepsis, or other PAIS remains untested.

10. **Competing interests:** Several co-authors hold financial interests in companies related to assays or therapies studied (Turium systems chemistry; ROS-modulating therapeutics). The COI statement is fully disclosed but warrants awareness during interpretation of drug candidacy claims.

## Model / Tool Availability

No model or computational tool is released for reuse. The Turium systems chemistry platform (used for metabolic pathway mapping) is a third-party commercial tool (Material Alchemy / MA). Flow cytometry data and mass spectrometry data are included in the manuscript and/or SI Appendix. External RNA-seq datasets reanalyzed are publicly available under the GEO accessions cited (GSE262861, GSE128078, GSE224615).

## Follow-up

**Immediate reads:**
- The Phetsouphanh et al. (Nat. Commun. 2024, GSE262861) longitudinal LC dataset reanalyzed here — understanding the full single-cell landscape they built would contextualize the GPX4 and PLA2G6 reanalysis.
- Bramante et al. (RECOVER metformin trial, cited as ref. 68) for the Phase III evidence that metformin reduces LC incidence by 41%.
- Naviaux 2016 (paper:Naviaux2016) for tension/complementarity between the cell danger response frame and the ROS-hyperproliferation energy-sink model.

**Questions raised for the project:**
- Does the mitochondrial ROS / Ca²⁺ / SOD2 signature replicate in other PAIS cohorts (post-Lyme, post-Q-fever, post-sepsis)? This is the key extension needed to test question:0001 at the PAIS-wide level.
- Is female-specific T cell hyperproliferation a feature shared across PAIS triggers or specific to viral (COVID/EBV) triggers? Sex hormone modulation of PPARα and antioxidant enzymes may be a confounder specific to certain infections.
- Can the DCFDA flow cytometry assay (blood-draw based, scalable) serve as a stratification biomarker in clinical trials for ROS-modulating drugs? This directly addresses topic:biomarkers-and-objective-endpoints.
- What is the relationship between the lymphocyte ROS signature identified here and the previously reported microclot / thromboinflammation findings in LC (topic:thromboinflammation)? Endothelial and platelet ROS could parallel lymphocyte ROS as part of a systemic redox failure.
- Does metformin's effect on T cell hyperproliferation translate in vivo in ME/CFS patients (not just LC prevention)? The in-vitro signal here is modest; an ME/CFS-specific trial is warranted.
