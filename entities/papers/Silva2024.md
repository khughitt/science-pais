---
id: paper:Silva2024
type: paper
title: "Sex differences in symptomatology and immune profiles of Long COVID"
status: active
ontology_terms:
  - sex differences
  - long COVID
  - immune dysregulation
  - testosterone
  - exhausted T cells
  - herpesvirus reactivation
  - monocytes
  - NK cells
  - cytokines
  - immune-endocrine profiling
  - MY-LC cohort
dataset_usage: []
datasets: []
source_refs:
  - cite:Silva2024
related:
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0007-mechanism-of-female-predominance-in-pais
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - topic:long-covid-immune-dysregulation
  - topic:menopause-sex-hormones-and-pais-risk
  - topic:shared-failure-mode-across-pais
  - immunity:topic:sex-as-a-modifier-of-immune-homeostasis
created: '2026-06-21'
updated: '2026-06-21'
---
# Sex differences in symptomatology and immune profiles of Long COVID

- **Authors:** Julio Silva, Takehiro Takahashi, Jamie Wood, Peiwen Lu, Alexandra Tabachnikova, Jeff R. Gehlhausen, Kerrie Greene, Bornali Bhattacharjee, Valter Silva Monteiro, Carolina Lucas, Rahul M. Dhodapkar, Laura Tabacof, Mario Peña-Hernandez, Kathy Kamath, Tianyang Mao, Dayna McCarthy, Ruslan Medzhitov, David van Dijk, Harlan M. Krumholz, Leying Guan, David Putrino, Akiko Iwasaki
- **Year:** 2024 (medRxiv preprint; published form in Science Translational Medicine 2025 — see DOI note below)
- **Journal:** medRxiv (preprint DOI: 10.1101/2024.02.29.24303568, PMID: 38496502, PMCID: PMC10942502); published in Science Translational Medicine (2025) under a DOI distinct from 10.1126/scitranslmed.adr1032 — the latter resolves to Hamlin et al. (Stanford/CHAMP cohort)
- **Cohort:** MY-LC (Mount Sinai–Yale Long COVID study)
- **BibTeX key:** Silva2024
- **Source:** Full-text PDF (medRxiv preprint 10.1101/2024.02.29.24303568), read 2026-06-21

> **DOI-mismatch note for curators.** The user-supplied DOI 10.1126/scitranslmed.adr1032 resolves to a *different* paper (Hamlin, Pienkos, Blish et al., Stanford/CHAMP cohort, 45 participants, also STM 2024), confirmed via Crossref and Europe PMC. This summary describes the Silva/Takahashi/Iwasaki MY-LC paper based on its medRxiv preprint. If the published STM version of the MY-LC paper carries a different DOI, update the `source_refs` citekey, BibTeX, and related tasks accordingly.

## Key Contribution

An exploratory, cross-sectional, sex-stratified immune-endocrine profiling study of 165 participants with and without Long COVID enrolled in the MY-LC cohort (Mount Sinai Hospital, NYC). The study demonstrates that females and males with Long COVID have biologically and symptomatically distinct disease presentations, with distinct immune signatures identifiable via machine-learning-based dimensionality reduction. Most strikingly, testosterone levels were the top predictor of sex-based immune phenotype across both sexes, and lower testosterone was significantly associated with higher symptom burden regardless of sex designation — placing HPG-axis dysregulation at the center of LC's immune-endocrine pathophysiology.

## Methods

**Study design.** Exploratory, cross-sectional, single-center study. 185 participants initially enrolled at Mount Sinai Hospital; 20 excluded post-enrollment (outlier conditions n=7, oral steroid use n=4, mismatched data n=3, missing data n=6), leaving a primary analytic cohort of **n=165**: control females (CF, n=53: 27 uninfected healthy controls + 26 convalescent controls), control males (CM, n=23: 12 uninfected + 11 convalescent), females with LC (LCF, n=58), and males with LC (LCM, n=31). Sex designation from healthcare records; self-identified gender data reported separately (Extended Data Table 1). No significant age, BMI, or race/ethnicity differences across sex-based groups; vaccination status was lower in LCF.

**LC case definition.** MY-LC study enrollment criteria (reference 8 in the preprint = Takahashi et al. prior MY-LC paper); specific WHO or CDC criteria not restated in this paper. Symptom counts and organ-system involvement assessed by structured questionnaires including EQ-5D-5L and others.

**Immune-endocrine profiling.** A multi-dimensional panel was measured for each participant: (a) flow-cytometric cell-type frequencies (T cells including exhausted CD4Tex/CD8Tex and cytokine-secreting subsets, B cells, NK cells, monocytes, dendritic cells, eosinophils); (b) plasma cytokines and chemokines (IL-4, IL-6, IL-8, TGF-β1, TGF-β2, APRIL, CCL20, CCL23, CCL3, CCL28, GH, BDNF, NGF, oxytocin, insulin); (c) sex hormones and other hormones (testosterone, estradiol, cortisol, ACTH, GH, BDNF); (d) antibody levels against SARS-CoV-2 S1 and total Spike; (e) antibody reactivity against latent herpesvirus linear epitopes (EBV, CMV, HSV-1, HSV-2, HHV-6b) by Serum Epitope Repertoire Analysis (SERA) linear peptide display; (f) common autoantibodies (Smith antibody panel); (g) antibody reactivity to chronic-infection agents (Babesia microti, Helicobacter pylori, Borrelia burgdorferi).

**Statistical analysis.** Primary dimensionality reduction: Partial Least Squares Discriminant Analysis (PLS-DA) with 5-fold cross-validation, bootstrap-stabilized Variable Importance in Projection (VIP) scores. Features with 95% CI above VIP threshold 0.8 and regression coefficient not crossing zero considered significant. Confirmatory: generalized linear models (GLM; negative binomial, Poisson, ZINB depending on outcome distribution), Kruskal-Wallis with Steel-Dwass correction, Poisson regression for symptom burden, logistic regression for hormone-LC association (adjusted for age, BMI, vaccination status). Immune scores (Female-LCIS and Male-LCIS) derived from hormone-excluded models, then validated in 30% held-out testing subset. Sex-integrated model used to test testosterone as a trans-sex predictor of symptom burden. Machine learning LASSO (double LASSO with 5-fold cross-validation) used to identify hormonal predictors of the immune scores.

## Key Findings

**Symptom burden differs by sex.** Females with LC had significantly higher overall symptom burden (p<0.0001) and organ system involvement (p=0.0055) than males with LC, persisting after adjustment for age, BMI, comorbidities, and vaccination status. By PLS-DA on 42 symptoms, sex was the strongest differentiator. Females with LC more frequently reported neurological/neurocognitive symptoms, changes in body temperature, cough, and musculoskeletal/dermatological symptoms; males with LC showed higher rates of sexual dysfunction and a distinct ENT symptom cluster. On standardized quality-of-life surveys (LASSO-selected), females with LC reported higher pain, greater neurological impact, and greater health impact overall; males with LC reported higher mood impact and higher post-exertional malaise (PEM) rates on standardized instruments.

**Female-specific immune signature.** In the female sex-stratified PLS-DA (pseudo R²=0.98, 28 bootstrapped-significant features):
- Enrichment of exhausted CD4+ and CD8+ T cells (CD4Tex, CD8Tex) and a broad array of cytokine-secreting CD4 and CD8 T cells (IL-4/IL-6 double-positive; IFN-γ-secreting CD4+ T cells; IL-4, IL-6 secreting populations).
- Elevated HLA-DR+ B cells, double-negative B cells.
- Higher IL-8, C4b, growth hormone (GH), neural growth factor (NGF).
- Higher antibody levels against SARS-CoV-2 S1.
- Higher antibody reactivity to EBV (gp42 epitope PVNFNK, previously LC-associated), and subsequently confirmed higher reactivity to CMV and HSV-2 linear epitopes.
- Downregulated: cortisol, **testosterone**, and CCL28.

**Male-specific immune signature.** In the male sex-stratified PLS-DA (pseudo R²=0.98, 36 bootstrapped-significant features):
- Broad reduction in myeloid-derived lineages: total monocytes, classical monocytes, low-density neutrophils, DC1, pDC.
- Increase in low-density eosinophils and **NK cells**.
- Elevated APRIL, CCL20, **TGF-β1, TGF-β2, IL-8**.
- Higher SARS-CoV-2 S1 and total Spike antibody levels.
- Lower estradiol; higher insulin, NGF, oxytocin.

**Sex-integrated analysis and testosterone as a top predictor.** In the sex-integrated PLS-DA (7 components, pseudo R²=0.89, 57 bootstrapped features), **testosterone ranked as the single most important predictor** (above cortisol) of sex-based LC status. Females with LC had significantly lower testosterone than all other groups including control females (confirmed in regression excluding hormone-therapy users, adjusted for age, BMI). Males with LC had lower estradiol relative to control males (estradiol in males largely arises from aromatization of testosterone). Authors interpret both findings as consistent with **relative deficiency in the non-dominant sex hormone** — a shared HPG-axis dysregulation across sexes, with normal ACTH suggesting the disruption is at or below the gonadal level.

**Herpesvirus antibody reactivity is sex-differentiated.** Clustering analysis of SERA linear epitope reactivity profiles against EBV, CMV, HSV-1, and HSV-2 revealed three participant clusters; females with LC were disproportionately enriched in clusters with high reactivity to CMV and EBV epitopes simultaneously (cluster 1) and EBV alone (cluster 2), while males with LC enriched in the HSV-1-high cluster (cluster 3). HSV-2 total antibody reactivity was elevated in females with LC vs. all other groups. These differences persisted after adjusting for age, vaccination, and inferred prior herpesvirus exposure history.

**Hormone-independent immune scores validate sex-specific signatures.** PLS-DA models trained on cellular, cytokine, and non-SARS-CoV-2 antibody features (hormones excluded) produced a Female Long COVID Immune Score (Female-LCIS; AUC=0.88, 95% CI 0.70–0.96 in testing subset, p<0.0001) and a Male Long COVID Immune Score (Male-LCIS; AUC=1.0 in training and testing, p<0.0001). The two scores classified participants across sex and disease status in the sex-integrated model even without hormone data.

**Immune scores correlate with symptom burden.** Males with LC who had a higher Female-LCIS showed significantly higher symptom burden, organ system involvement, neurocognitive impact on quality of life, and greater fatigue. Females with LC who had a higher Male-LCIS showed significantly lower symptom burden, lower neurological and neurocognitive symptoms, and lower fatigue. This cross-sex immune-score-symptom relationship suggests the sex-specific immune configurations are mechanistically linked to distinct symptom phenotypes.

**Testosterone as top correlate of immune phenotypes in both sexes.** Using PLS-DA to predict testosterone levels from immune features (in LC participants, hormones excluded from predictor set):
- In females with LC: lower testosterone was predicted by higher cytokine-secreting CD4/CD8 T cells (IL-4/IL-6 double-positive) and higher EBV and CMV antibody reactivity. Higher testosterone was associated with TGF-β1, TGF-β2, APRIL, CCL3, IL-8 — the signature features of males with LC.
- In males with LC: lower testosterone was predicted by cytokine-secreting T cells (IL-4, IL-6, TNF-α, IFN-γ secreting CD4/CD8), higher herpesvirus (EBV, HHV-6b) reactivity. Higher testosterone was associated with NK cells, CCL23, ADAMTS13, IL-8, and (via bootstrap threshold) with higher estradiol, progesterone, GH, and cortisol — indicating intact HPG-axis function.
- Dividing LC participants into tertile-based lower-T (females n=24, males n=12) and higher-T (females n=33, males n=19) groups confirmed the directional reversal: lower-T females look immunologically like males with LC; lower-T males show the cytokine-secreting T cell and herpesvirus-antibody signature predominant in females with LC.

**Testosterone levels predict symptom burden over sex designation.** In a Poisson regression model including sex, testosterone levels, their interaction, BMI, age, and vaccination status as predictors of symptom burden and organ system involvement in LC participants: **testosterone was a significant negative predictor of symptom burden and organ system involvement across sex; after accounting for testosterone levels, sex designation was no longer a significant predictor.** This suggests that the biological variable driving symptom severity in this cohort is testosterone (or what it marks), not categorical sex.

## Relevance

**hypothesis:0005 (reproductive-stage immune homeostatic margin):** This paper provides a new, independent, non-UK-Biobank, author-independent clinical-cohort corroboration that gonadal steroid levels — specifically testosterone — are associated with LC symptom burden and immune phenotype. Critically: (a) it is an independent cohort from AlcaldeHerraiz2025, addressing task:t032's concern that the SHBG/sex-hormone–LC association was single-source; (b) it measures serum testosterone directly rather than SHBG, so it adds a different but related mediator-level signal; (c) the association runs across both sexes (not only females), suggesting testosterone-level rather than sex-category is the operative variable. However: this paper **does NOT** test SHBG, does not establish the pre-infection total-effect direction (it is cross-sectional, with reverse causation unresolved — LC could suppress HPG axis), and is clinical-cohort grade observational evidence, not a pre-infection longitudinal design.

**task:t032 (G2 corpus-independence gate):** This paper constitutes a non-UKB, non-Alcalde-Herraiz-network, author-independent observation of a sex-hormone × LC association in a directly measured clinical cohort. It upgrades the plausibility of gonadal steroid involvement from single-source status (though it measures testosterone, not SHBG), and narrows the corpus-independence gap. The SHBG-specific prior in AlcaldeHerraiz2025 remains single-source; the broader testosterone/gonadal steroid signal now has this independent corroboration. Note: the Hamlin/Blish STM paper (DOI 10.1126/scitranslmed.adr1032) is a separate paper from a Stanford cohort (n=45, longitudinal) and should be tracked separately if needed.

**task:t036 (hormone-panel triangulation cohorts):** The MY-LC cohort demonstrates that a directly hormone-measured clinical cohort can find testosterone associations. This is the level of evidence that t036 seeks from population cohorts (All of Us, Lifelines, Generation Scotland). The finding that testosterone predicts symptom burden independently of sex, and that the hormone-immune association holds after adjusting for hormone-therapy use, supports the triangulation hypothesis and should be cited when scoping t036 searches.

**question:0007 (mechanism of female predominance in PAIS):** Provides mechanistic candidate: testosterone-mediated immune regulation as one explanation for the female-predominance, since lower testosterone in females with LC (relative to control females) co-occurs with the heightened cytokine-secreting T cell and herpesvirus antibody phenotype. However, the testosterone mechanism cannot fully explain female excess because testosterone is also lower in males with LC (relative to control males), suggesting it is a general LC correlate not a female-specific one. The paper calls sex differences in LC "a dynamic spectrum of which hormones like testosterone may help dictate the immune landscape" rather than a biological dichotomy.

**question:0013 (reproductive stage and failed immune recovery):** This paper does not measure menopausal status, FSH, LH, AMH, or reproductive stage directly. It uses sex hormone levels (testosterone, estradiol) cross-sectionally. It cannot address whether reproductive-stage transition (perimenopause) changes the probability of entering LC — that requires longitudinal pre/peri/post-infection hormone data. It adds indirect plausibility but does not test the transition-as-exposure hypothesis.

**topic:long-covid-immune-dysregulation:** The female immune signature (exhausted T cells, herpesvirus antibody reactivity, cytokine-secreting T cells) and the male signature (monocyte/DC depletion, elevated NK cells, TGF-β, IL-8) represent two distinct dysregulated immune configurations both resulting in LC, sharing some features (low cortisol, low DC1, elevated IL-8) while differing in others.

**EBV/herpesvirus reactivation thread:** Females with LC had the highest EBV, CMV, and HSV-2 linear epitope reactivity, and lower testosterone was associated with higher EBV/CMV reactivity in both sexes. The authors suggest testosterone may help maintain herpesvirus latency, providing a mechanistic bridge between gonadal steroid suppression and latent herpesvirus reactivation as co-occurring features of LC.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| MY-LC cohort (n=165, Mount Sinai–Yale) | Independent non-UKB clinical cohort | Cross-sectional; not longitudinal; addresses t032 corpus-independence |
| Lower testosterone in females with LC vs. control females | Gonadal steroid axis suppression as LC correlate | Measured directly; cross-sectional only; reverse causation unresolved |
| Lower estradiol in males with LC vs. control males | HPG-axis dysregulation in both sexes | Authors attribute to lower aromatization from lower testosterone |
| Testosterone as top predictor of sex-based LC status | Mediator-level hormone signal (M1 of H0005) | Does NOT measure SHBG; does NOT test pre-infection causal direction |
| Testosterone predicts symptom burden over sex designation | Testosterone-mediated symptom severity pathway | Key observational finding; confounded by severity → testosterone suppression |
| Exhausted CD4Tex/CD8Tex + cytokine-secreting T cells in LCF | Immune exhaustion / failed immune homeostasis | Consistent with hypothesis:0003 (immune-exhaustion feedback) |
| Monocyte/DC depletion + NK elevation in LCM | Innate immune reconfiguration in male LC | Distinct from female phenotype; shared IL-8 elevation |
| EBV/CMV/HSV-2 antibody reactivity elevated in LCF | Latent herpesvirus reactivation (female-predominant) | Adds sex-stratified specificity to the EBV-reactivation mechanism |
| TGF-β1/TGF-β2 elevated in LCM | Profibrotic/immune-suppressive pathway in males | Also associated with higher testosterone within LC group |

## Limitations

1. **Cross-sectional design — reverse causation unresolved.** The study cannot determine whether low testosterone precedes LC (susceptibility mechanism) or is a consequence of LC physiology (e.g., LC-related HPG axis suppression by chronic inflammation, stress, or fatigue). This is the central ambiguity for interpreting the testosterone-symptom-burden finding in causal terms. The authors acknowledge it.

2. **Single time point per participant.** No longitudinal hormone-immune tracking before and after acute infection or within the LC course. Cannot test whether testosterone changes track symptom resolution or relapse.

3. **Cohort composition and selection effects.** MY-LC enrolled participants at a single tertiary center (Mount Sinai Hospital, NYC), with predominantly 30–65-year-old patients. Higher rates of women with LC may reflect care-seeking behavior as well as biology. Uninfected controls and convalescent controls are pooled as the "control" group, which may introduce heterogeneity.

4. **LC case definition not fully specified in this paper.** The paper references the prior MY-LC study (Takahashi et al.) for inclusion criteria. The specific WHO or CDC threshold for "Long COVID" duration and symptom count is not restated. Comparison to other cohorts requires checking the original MY-LC recruitment criteria.

5. **No hormone-measured pre-infection baseline.** Cannot test whether observed testosterone levels represent suppression from a normal pre-COVID baseline or represent a preexisting vulnerability.

6. **Does NOT measure SHBG.** The sex-hormone mediator most studied in relation to LC in AlcaldeHerraiz2025 and the UK Biobank analyses is SHBG, not testosterone directly. The two are correlated but distinct; this paper cannot directly confirm or refute the SHBG hypothesis.

7. **Exploratory, not pre-registered.** PLS-DA machine-learning analyses are exploratory by design; no a priori power calculations are reported; multiple testing adjustment is by bootstrapping and VIP threshold rather than pre-specified primary endpoints. Findings should be considered hypothesis-generating.

8. **Race/ethnicity and compositional diversity.** The paper notes limited race/ethnicity diversity as a limitation and notes that transgender/non-binary individuals (who showed an even higher LC rate) were not analyzed separately due to sample size.

9. **Medically excluded individuals.** Exclusion of participants on oral steroids, with outlier comorbidities, or with hormone-altering conditions reduces confounding but may reduce generalizability to typical LC clinic populations.

10. **Preprint status (at time of original posting).** The summary is based on the medRxiv preprint (March 2024); the published STM version may contain revisions to methods, analyses, or conclusions.

## Model / Tool Availability

No software model or analysis tool is released with this paper. The female-LCIS and male-LCIS scoring functions are described conceptually (PLS-DA weights from the training-set models) but are not deposited in a public repository as of the preprint. Data availability per preprint: requests to contact corresponding authors.

## Follow-up

- **Track down the published STM DOI** for the Silva/Takahashi/Iwasaki MY-LC paper (user-supplied DOI 10.1126/scitranslmed.adr1032 is the Hamlin/Blish Stanford paper — different cohort). Update this record if the STM DOI is confirmed.
- **Read the companion Hamlin2024/Blish paper** (DOI: 10.1126/scitranslmed.adr1032, Stanford CHAMP cohort, n=45, longitudinal, also STM 2024) for comparison — it finds sex-differentiated TGF-β and XIST patterns that partially overlap and partially complement the MY-LC findings.
- **Test whether testosterone-symptom association replicates in longitudinal hormone-measured cohorts** (task:t036: All of Us, Lifelines, Generation Scotland) and whether it survives pre-infection baseline control.
- **Integrate with AlcaldeHerraiz2025** (UKB SHBG–LC association): both papers find gonadal steroid axis involvement; the nature of SHBG vs. free/total testosterone as the operative variable deserves mechanistic attention.
- **Assess HPG-axis dysregulation as a potential treatment target**: the authors suggest HRT as a potential therapeutic avenue; this converges with discussion:0001-menopause-timing-pais-rival-models and should be flagged for hypothesis:0005's predictions.
- Read the SERA methodology paper for context on herpesvirus antibody quantification to evaluate the EBV/CMV elevation evidence quality.
- Assess whether the monocyte depletion signature in males with LC replicates in prior MY-LC data (ref 8 = Takahashi et al.) and in independent cohorts.
