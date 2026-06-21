---
id: paper:Gabernet2025
type: paper
title: 'A multiomics recovery factor predicts long COVID in the IMPACC study'
status: active
ontology_terms:
  - post-acute sequelae of SARS-CoV-2 (PASC)
  - long COVID (LC)
  - androgenic steroids
  - DHEA-S (dehydroepiandrosterone sulfate)
  - androsterone sulfate
  - heme metabolism
  - stress erythropoiesis
  - anemia of inflammation
  - multiomics factor analysis (MOFA)
  - SPEAR (Supervised Principal components via Expectation-maximization and Augmented Regression)
  - immune dysregulation
  - plasma metabolomics
  - PBMC transcriptomics
  - Olink proteomics
  - CyTOF mass cytometry
  - IMPACC cohort
dataset_usage: []
datasets: []
source_refs:
  - cite:Gabernet2025
related:
  - paper:Ozonoff2024
  - paper:Talla2023
created: '2026-06-21'
updated: '2026-06-21'
---
# A multiomics recovery factor predicts long COVID in the IMPACC study

<!--
- **Authors:** Gisela Gabernet, Jessica Maciuch, Jeremy P. Gygi, John F. Moore, et al. (IMPACC Network); co-senior authors: Seunghee Kim-Schulze, Leying Guan, Lauren I.R. Ehrlich
- **Year:** 2025
- **Journal:** Journal of Clinical Investigation, Vol. 135, No. 21, e193698
- **DOI:** 10.1172/JCI193698
- **PMC:** PMC12582403
- **BibTeX key:** Gabernet2025
- **Source:** XML full text (Europe PMC)
-->

## Key Contribution

Using the IMPACC hospitalized COVID-19 cohort (n=513 convalescent participants followed longitudinally for 12 months post-discharge), this study applies supervised multiomics integration — specifically SPEAR (Supervised Principal components via Expectation-maximization and Augmented Regression) trained on PROMIS Physical function scores — to derive a single "recovery factor" that discriminates long COVID (LC) from minimal-deficit (MIN) recovery. The key finding is that three co-varying biological signatures compose the recovery factor: (1) **decreased androgenic steroid metabolites** (DHEA-S, androsterone sulfate, epiandrosterone sulfate, and related pregnenolone-pathway intermediates) in LC; (2) **elevated heme metabolism transcriptomic signature** (stress erythropoiesis/inflammation-driven anemia) in LC; and (3) **persistent elevation of inflammation-associated serum proteins** (LRG1, CXCL9, FGF21, CSF1, FGF23, and others) in LC. Crucially, all three signatures are features of a **single SPEAR factor**, meaning they co-vary within the same statistical construct — not as separate independent associations. Acute-phase recovery factor scores predicted eventual LC status as early as hospital admission (visit 1, within 72 hours), independent of acute COVID-19 severity. The androgenic steroid metabolite signature is highly reproducible and overlaps with a published ME/CFS versus healthy-control comparison.

## Methods

**Design:** Longitudinal prospective multiomics study within the IMPACC (Immunophenotyping Assessment in a COVID-19 Cohort) observational cohort. Enrolled 1,164 participants hospitalized with COVID-19 at 20 US hospitals (15 academic institutions), May 2020 – March 2021. 513 convalescent participants met inclusion criteria (survived ≥28 days hospitalization, completed ≥1 PRO survey, provided ≥1 biosample during convalescent period). NCT04378777.

**Cohort (convalescent):** n=513; 310 men (60%), 213 women (40%). Median age and IQR: [UNVERIFIED — not stated explicitly in text portion accessed; cohort demographics inherit from Ozonoff2024 baseline: median age ~57, IQR ~19]. Pre-Omicron, largely unvaccinated at enrollment (vaccines became available during follow-up; ~75% received a vaccine post-discharge, but vaccination did not significantly affect recovery factor scores).

**Omics modalities (acute and convalescent phases):**
- Serum Olink inflammatory proteomics (SO) — 92-protein panel
- Global plasma metabolomics (PMG) — liquid chromatography-mass spectrometry
- Global and targeted plasma proteomics (PPG and PPT)
- PBMC transcriptomics (PGX) — RNA-seq
- CyTOF — whole blood immune cell frequencies and mean marker signal intensities (BCT)

**Timepoints:** Acute phase — within 72 h of admission and at days 4, 7, 14, 21, 28 (visits 1–6). Convalescent phase — 3, 6, 9, 12 months post-discharge (visits 7–10).

**Factor construction:** SPEAR (Supervised PCA via EM and Augmented Regression) using the MOFA framework (Multiomics Factor Analysis v2). Training response variable: PROMIS Physical function PRO score. Model trained on convalescent phase data (train/test split). Multiple SPEAR models evaluated (Physical, Cognitive, Mental, Impact, Dyspnea, binary LC label); SPEAR Physical performed best (AUROC 0.69 in test cohort, P=0.00098 for LC vs. MIN association, effect size 0.44, adjusted for sex and age). Analyte significance defined by SPEAR Bayesian posterior selection probability ≥0.95 (yielded 26 significant analytes across 4 assays).

**Pathway enrichment:** Gene set enrichment analysis (GSEA) on SPEAR model internal feature rankings. Pathways assessed: MSigDB Hallmark sets (transcriptomics), metabolite sub-pathway sets (metabolomics).

**Statistical methods:** Linear mixed-effects models for differential analysis (fixed effects: sex, age, visit number; random effect: enrollment site). Generalized mixed-effects models for longitudinal variation. Benjamini-Hochberg correction; adjusted P<0.05 considered significant.

**LC definition:** Binary LC label based on PRO cluster assignment from Ozonoff2024 (PHY, COG, or MLT clusters = LC; MIN cluster = recovered). LC is operationalized as patient-reported physical, cognitive, or multidomain functional deficit persisting through the convalescent period — not as self-reported symptom presence.

## Key Findings

### Recovery factor and long COVID

The SPEAR Physical recovery factor was significantly lower in LC participants vs. MIN in the test cohort (P=0.00098, effect size 0.44), adjusting for sex and age. AUROC for predicting LC vs. MIN was 0.69. The recovery factor also significantly discriminated MIN vs. individual PRO subgroups (MIN vs. COG, MIN vs. PHY, MIN vs. MLT in sex-adjusted comparisons).

### Androgenic steroid metabolites — direction and specific analytes

The androgenic steroids metabolite sub-pathway was **positively associated with the recovery factor**, meaning **lower in LC participants and higher in MIN (recovered) participants**. This association held in both the convalescent and acute phases.

Five androgenic steroid metabolites were individually significant after multiple-comparison adjustment (Figure 3B, adj. P<0.05 for LC vs. MIN):
1. **DHEA-S** (dehydroepiandrosterone sulfate)
2. **Epiandrosterone sulfate**
3. **Androsterone sulfate**
4. **5α-androstan-3β,17β-diol monosulfate (2)**
5. **5α-androstan-3β,17α-diol disulfate**

Seven of 12 leading-edge androgenic steroid metabolites were also among the 26 significant SPEAR analytes (Bayesian posterior selection probability ≥0.95). Additional significant analytes included five pregnenolone-related metabolites (pregnenolone is the upstream steroid hormone biosynthesis precursor).

In addition, the Discussion notes that: "Several intermediate metabolites in the canonical steroid hormone biosynthesis pathway were associated with the recovery factor and were decreased in participants with LC, including sulfated forms of testosterone precursors (pregnenolone and DHEA) and downstream metabolites (androsterone, epiandrosterone, and 5α-androstan-3β,17β-diol)."

**Effect size for metabolite sub-pathway geometric mean:** The combined geometric mean score of leading-edge androgenic steroid pathway metabolites significantly differentiated MIN vs. LC at all convalescent visits (Figure 3C) and also during the acute phase (Figure 5C). Exact fold-changes and confidence intervals for individual metabolites are presented in figures only [UNVERIFIED — not quantified in text].

No sex-stratified effect sizes for the androgenic metabolites are reported separately by sex in the main text. When the cohort was split by sex, the geometric mean score of leading-edge analytes from the heme metabolism and androgenic steroid pathways "lost significance in 1 or both sexes" individually, but "their combined score remained significantly associated with LC in both sexes" (Supplemental Figure 7D).

### Inflammation and immune cell composition — in the same factor

Alongside the androgenic steroid signal, the same SPEAR recovery factor incorporates inflammation-associated signals. The 26 significant SPEAR analytes across 4 assays include:

**Serum Olink proteins negatively associated with the recovery factor (higher in LC):**
- LRG1 (IL-6/STAT3–activated; vascular/angiopathic)
- CXCL9 (interferon-gamma–induced chemokine; chronic inflammation marker)
- FGF21 (elevated in COG and MLT clusters in Ozonoff2024; ME/CFS biomarker)
- FGF23
- TNFRSF11B (osteoprotegerin; inflammatory)
- TNFRSF9 (CD137; co-stimulatory; inflammatory activation)
- MMP10 (myeloid regulator)
- CSF1 (macrophage colony-stimulating factor; myeloid expansion)
- IL10RB (worse acute outcomes marker)

**Serum Olink protein positively associated with the recovery factor (higher in MIN):**
- DNER (noncanonical Notch ligand; wound healing; lower in LC participants, consistent with prior LC proteomics)

**Plasma metabolomics negatively associated with recovery factor (higher in LC):**
- Phenylacetylglutamate and phenylacetylglutamine (gut microbiota–derived; vascular inflammation / thrombosis association)
- OSBP2 transcript (oxysterol binding; heme metabolism)

**CyTOF immune cell frequencies:** Higher recovery factor scores (better recovery, MIN group) were associated with increased lymphocyte frequencies and decreased myeloid cell frequencies. Specifically, monocytes were negatively associated and B cells were positively associated with the recovery factor (Figure 3D).

**Heme metabolism transcriptomic pathway (PBMC transcriptomics, hallmark gene set):** Negatively associated with recovery factor — i.e., **upregulated in LC** at convalescent and acute timepoints. The paper interprets this as inflammation-driven stress erythropoiesis (IL-6 → hepcidin → iron restriction → anemia → lymphocyte impairment → sustained inflammation loop). Anemia at hospital discharge was negatively associated with the recovery factor (adj. P<0.05).

### Co-variation structure (critical question)

**Both signals co-load on a single *outcome-supervised* unit — the SPEAR recovery factor — but this is NOT qualifying within-subject / within-cluster androgen↔mediator co-variation.** They co-associate with the long-COVID outcome by construction of the supervised factor, which is weaker than a demonstrated mutual androgen↔mediator relationship.

Both the androgenic steroid metabolite sub-pathway and the inflammation-associated serum proteins (LRG1, CXCL9, FGF21, CSF1, MMP10, etc.) are features of the same multiomics factor (SPEAR Physical). The factor is a single latent variable trained simultaneously on all omics modalities. The GSEA result (Figure 3A) identified the androgenic steroids pathway and heme metabolism pathway as the two most significantly enriched pathway-level signals within the same factor. The 26 significant individual SPEAR analytes (Figure 3B) span both metabolites from the androgenic steroids pathway and proteins from the inflammatory proteomics panel — within the same model. Furthermore, the combined geometric mean score of analytes from heme metabolism, androgenic steroids, and the 26 SPEAR analytes (which includes inflammatory proteins) is reported as a single composite score in Figures 3C and 5C, and this combined score most significantly discriminated MIN vs. LC across both convalescent and acute phases.

The paper does not present a mediation or regression model in which androgens → inflammation → LC is tested as a causal chain. It does not explicitly show that the androgen-low and inflammation-high signals are mutually dependent within subjects (e.g., a within-subject correlation between DHEA-S and LRG1). What it shows is that both contribute to the same factor that predicts LC — they load on the same latent variable. The paper states: "Androgens can suppress inflammation (60), suggesting that higher levels of androgenic steroids in MIN participants could reflect better control of chronic inflammation" — this is interpretive/speculative framing, not a demonstrated mediation within the paper itself.

**Summary for co-variation decision:** Both androgenic steroids (low in LC) and inflammatory mediators (high in LC) co-load on the **same outcome-supervised latent factor** (SPEAR) — i.e. both co-associate with the LC outcome by construction — but **no** mediation analysis and **no** bivariate within-subject correlation between the two feature groups is presented. This is therefore **not** qualifying within-subject / within-cluster androgen↔mediator co-variation. See `report:0005` for why this is classified `underdetermined` (mediator-compatible but non-corroborating) for the h0005 M1 positive test.

### Predictive power across disease phase

Acute-phase recovery factor scores (computed from the convalescent-trained model applied to acute-phase data) were significantly lower in LC vs. MIN as early as visit 1 (within 72 hours of hospital admission). This association persisted after controlling for acute disease severity trajectory group (co-variate), demonstrating that the LC-predictive signal is not simply a proxy for acute illness severity.

### Sex differences

- Female sex was significantly associated with lower recovery factor scores (P=3.6×10⁻⁷).
- ~50% of women in the cohort presented with long-term deficits vs. ~30% of men.
- Recovery factor scores significantly discriminated LC vs. MIN in women but not in men individually after P-value adjustment (though the trend persisted in men).
- The androgenic steroid geometric mean score lost significance when the cohort was split by sex (Supplemental Figure 7D), but the combined score (heme metabolism + androgenic steroids + 26 SPEAR analytes) remained significant in both sexes.
- The paper did not stratify by menopausal status or report menopausal status data.

### Overlap with ME/CFS

The six androgenic steroid metabolites elevated in healthy controls vs. ME/CFS patients in an independent all-female ME/CFS cohort [DHEA-S, androstenediol (3α,17α) monosulfate (2), androstenediol (3β,17β) disulfate (2), 5α-androstan-3β,17α-diol disulfate, androsterone sulfate, epiandrosterone sulfate] were all among the 26 significant SPEAR analytes in this IMPACC LC study — a direct cross-syndrome convergence.

## Relevance

This study directly addresses the project's core question of why some individuals fail to recover after acute infection by identifying a multiomics LC "recovery factor" with three co-varying hallmarks: reduced androgenic steroids, elevated heme metabolism signatures (stress erythropoiesis/anemia of inflammation), and persistent inflammatory serum protein elevation. Key connections to the project framework:

1. **Androgen-inflammatory co-variation in a single factor:** The SPEAR recovery factor simultaneously incorporates lower androgenic steroid levels and higher inflammatory mediators as features of poor physical recovery. This is the most direct available evidence that these two biological channels track together in LC — though not a demonstrated causal link. For a downstream hypothesis that "sex hormones modify post-infectious recovery through immune mediators," this provides supportive co-occurrence evidence within one cohort and one model, but not a mediation pathway estimate.

2. **Stress erythropoiesis as a candidate PAIS mechanism:** The heme metabolism / anemia-of-inflammation signature places iron restriction and anemia at the center of LC biology. This connects to IL-6 → hepcidin → iron restriction → lymphocyte dysfunction → persistent viral failure resolution — a mechanistic chain consistent with the project's interest in failed immune homeostasis.

3. **Predictive from acute phase:** The recovery factor can be scored from acute-phase data and predicts LC irrespective of acute severity. This is relevant to the project's interest in identifying the initiating events of failed recovery, as the biological signature is already present at hospital admission.

4. **Cross-PAIS convergence (LC and ME/CFS):** The exact same 6 androgenic steroid metabolite signature appears in LC and in ME/CFS vs. healthy controls, reinforcing the project's working frame that LC and ME/CFS share overlapping failed-recovery biology.

5. **IMPACC cohort overlap:** n=513 convalescent participants from the same IMPACC hospitalized enrollment (n=1,164 total). Subject overlap with Ozonoff2024 is high and direct: Ozonoff2024 reports the PRO cluster assignments (MIN/PHY/COG/MLT) on which Gabernet2025 depends. IMPACC subjects are disjoint from Silva2024 (cross-sectional outpatient cohort) and Shahbaz2025 (separate clinical cohort).

## Confounders and Interpretation Caveats

1. **Hospitalized, pre-Omicron, unvaccinated cohort:** All participants were hospitalized for COVID-19 between May 2020 and March 2021 — i.e., severe end of the acute severity spectrum. The androgenic steroid depression may reflect acute critical illness–driven HPG (hypothalamic-pituitary-gonadal) axis suppression. This cohort does not capture the non-hospitalized LC majority and may overweight the androgen-low signal via severity confounding.

2. **No pre-infection baseline for androgens:** Androgen levels at hospital admission may already be depressed by acute illness. The paper acknowledges that "testosterone can play an immunomodulatory role and is often reduced in patients with other critical illnesses." There is no pre-infection androgen measurement in the IMPACC design, so it is impossible to determine whether LC participants started with lower androgens or whether illness drove them lower.

3. **No menopausal status recorded:** Sex significantly modified the recovery factor association, yet menopausal status was not captured. This is a major gap: if female LC participants are predominantly post-menopausal, their androgen levels would be expected to be lower at baseline, independently of LC. Without this adjustment, the sex×androgen interaction is uninterpretable as a reproductive-stage signal.

4. **Sex-stratified analysis showed attenuation:** When split by sex, the androgenic steroid geometric mean score lost significance in one or both sexes. This suggests the effect may be partly driven by the sex composition of LC vs. MIN groups rather than a within-sex effect of androgens.

5. **Acute severity co-variate:** The paper shows that LC vs. MIN discrimination by the recovery factor persists after controlling for acute trajectory group — so the factor is not simply a severity proxy. However, this does not rule out that the androgen-low signal specifically (among the 26 analytes) is severity-driven rather than LC-specific.

6. **LC definition is functional (PRO-based), not symptom-checklist:** LC here = assignment to PHY, COG, or MLT PRO clusters (Ozonoff2024 method). This operationalization may miss LC patients who recover physical function but have other symptoms, and may include patients with non-LC functional deficits (e.g., deconditioning post-hospitalization).

7. **No independent cohort validation of the androgenic steroid signal within IMPACC:** The heme metabolism signature was externally validated in two independent cohorts (Hanson et al.; and a nonhospitalized LC cohort). The androgenic steroid signature was validated only by comparison to the ME/CFS metabolomics study — not replicated in an independent LC cohort.

## Limitations

1. **All-hospitalized cohort** — not generalizable to non-hospitalized LC (the numerical majority).
2. **No pre-infection androgen baseline** — cannot disentangle LC-specific androgen depression from acute critical-illness HPG suppression.
3. **No menopausal status** — critical gap given the sex effect on the recovery factor and androgen levels.
4. **Train/test split within the same cohort** — no external validation cohort for the recovery factor itself (though the heme metabolism component was externally validated).
5. **PRO-based LC definition depends on Ozonoff2024 cluster assignments** — inherits that paper's limitations (no pre-COVID symptom baseline, hospitalization-enriched).
6. **Pre-Omicron, pre-vaccine cohort (2020–2021)** — unclear generalizability to post-vaccine or Omicron-era LC.
7. **No mediation analysis** for the androgen–inflammation link — co-variation in the same factor does not imply that androgen deficiency causes persistent inflammation or vice versa.
8. **Analyte-level sex stratification was underpowered** — splitting the cohort by sex reduced N substantially; the fact that the androgenic steroid score lost significance in one or both sexes may reflect power loss rather than effect absence.

## Model / Tool Availability

- Code: https://bitbucket.org/kleinstein/impacc-public-code/src/master/multiomics-longcovid/
- Data: ImmPort repository, accession SDY1760; dbGaP, accession phs002686
- Raw data for all figures: Supporting Data Values file (supplemental)

## Follow-up

- **Ozonoff2024 (this project):** The PRO cluster assignments (MIN/PHY/COG/MLT) used here as the LC definition depend on Ozonoff2024. Ozonoff2024's metabolomics module 3 (methylhistidine) and module 18 (acylcarnitine) are distinct from the androgenic steroid metabolites described here; the two papers are complementary within the same cohort.
- **ME/CFS androgenic steroid paper (cited as ref 72):** The all-female ME/CFS cohort study that reported the overlapping 6-metabolite signature should be identified and ingested for direct comparison. The overlap is strong and mechanistically important for the cross-PAIS claim.
- **Hanson et al. (cited ref 29):** Independently identified the heme metabolism / stress erythropoiesis signature in LC (102 participants, mixed hospitalized/non-hospitalized, 1–3 months post-infection). This is the external validation paper for the heme metabolism component.
- **Mediation gap:** A formal mediation model testing whether androgen depression → altered immune regulation → LC would require a dataset with pre-infection androgen levels and longitudinal immune tracking. IMPACC does not provide this; it is a gap for future study.
- **Testosterone in LC (cited as ref 31):** The paper cites a study showing lower testosterone in both men and women with LC symptoms. This should be identified and ingested as it is the closest published evidence for the androgen–LC association in non-hospitalized patients.
