---
id: question:0080-sex-chromosome-vs-hormone-decomposition-pais
kind: question
title: Can sex-biased PAIS susceptibility be decomposed into X-chromosome dosage versus
  gonadal-steroid components in human cohort designs?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Chaulagain2026
related:
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- hypothesis:0020-host-immune-baseline-reserve-gate
- question:0007-mechanism-of-female-predominance-in-pais
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
created: '2026-07-10'
updated: '2026-07-10'
---

# Can sex-biased PAIS susceptibility be decomposed into X-chromosome dosage versus gonadal-steroid components in human cohort designs?

## Summary

Chaulagain et al. (2026) organize sex differences in immunity around two orthogonal axes: (1) sex chromosome complement — primarily X-linked gene dosage and XCI escape (TLR7, KDM6A, DDX3X, EIF2S3) — and (2) gonadal steroids (estrogen/androgen/progesterone signaling on immune cells). For PASC, the paper emphasizes the X-chromosome dosage axis (XIST upregulation, TLR7 biallelic expression) while explicitly noting "limited evidence supporting a role for gonadal steroids in PASC outcomes." However, `hypothesis:0005` (reproductive-stage immune homeostatic margin) centers on the hormone axis as the mechanism by which menopausal-stage transition modifies PAIS risk. This question asks whether the sex-chromosome and hormone axes can be empirically separated in human PAIS cohort designs — specifically, whether they make independent, distinguishable contributions to PAIS susceptibility and phenotype, or whether they are so entangled as to be practically inseparable in observational data.

## Why It Matters

- **Directly affects `hypothesis:0005` and `hypothesis:0020`:** If the chromosome-dosage and hormone axes cannot be decomposed in observational data, the core mechanistic claim of h0005 (that reproductive-stage hormone transitions specifically modify PAIS risk above and beyond sex itself) cannot be tested without genetic instruments (e.g., Mendelian randomization with sex-hormone GWAS instruments). If they can be separated, the design requirements for h0005 become more tractable.
- **Affects interpretation of female PAIS excess:** If the chromosome axis fully explains female-biased PASC (because it is fixed across life) and the hormone axis adds no independent contribution, then menopausal-stage effects on PASC are epiphenomenal. If the hormone axis modifies the chromosome axis dynamically (e.g., estrogen induces TLR7, amplifying an already-elevated biallelic dose), both must be measured simultaneously.
- **Risk if unanswered:** The field may attribute female PAIS excess entirely to one axis (usually hormones, since they're more easily modifiable) while the chromosome-dosage axis is ignored in study design and therapeutic targeting — leaving a key mechanistic lever uninstrumented.

## Current Evidence

- **Chromosome axis evidence in PAIS:** XIST upregulation and Y-chromosome gene loss in PASC immune cells (Chaulagain2026) are sex-chromosome-specific findings not driven by hormonal levels. Klinefelter syndrome (XXY) immune phenotype (biallelic TLR7) provides a genetic natural experiment showing chromosome dosage effects independent of androgen suppression.
- **Hormone axis evidence:** Estradiol levels positively correlate with COVID-19 vaccine immune responses in mice. Age-related attenuation of sex differences in vaccine responses corresponds to reproductive senescence (lower estradiol) in women. Menopause hormone therapy reverses age-associated inflammatory monocyte expansion in women (De Maeyer et al. 2025, cited in Chaulagain2026 ref 41). Testosterone treatment of transgender men reduces TLR7-driven IFN responses and class-switched B cells.
- **Conflicting / confounding:** XX sex (chromosome) and estrogen levels are highly correlated across most of the lifespan — both vary together with menopause, making observational decomposition extremely difficult without genetic or pharmacological instruments. Turner syndrome (X0) and Klinefelter syndrome (XXY) provide natural variation in chromosome dosage independent of typical hormone trajectories, but PAIS outcomes in these populations are rarely studied.
- **Formal mediation analysis gap:** No PAIS cohort study has formally decomposed total sex effect → chromosome-mediated pathway versus hormone-mediated pathway using measured hormone levels, genetic sex (XX/XY), and PAIS outcomes simultaneously.

## Thoughts

- **Best current interpretation:** The two axes are partially entangled in observational human data (because XX sex co-occurs with female hormone levels) but are conceptually and mechanistically distinct and can in principle be empirically separated using: (1) genetic natural experiments (Turner, Klinefelter, gender-diverse populations on hormone therapy); (2) Mendelian randomization with sex-hormone GWAS instruments; (3) longitudinal designs where hormone levels vary (perimenopause, pregnancy, hormone therapy) while chromosome complement is fixed. The review's framing — chromosome axis is the "structural" baseline; hormone axis modulates it dynamically — is mechanistically plausible and not yet falsified.
- **Major uncertainty:** Whether hormone effects (if real) are primarily via amplification of chromosome-axis effects (e.g., estrogen induces TLR7 → amplifies the biallelic-dose advantage in XX) or act via entirely separate immune targets (ILC2s, Treg induction, inflammasome) that are independent of XCI-escape. The former predicts interaction (synergy) between the two axes; the latter predicts additive independent effects.

## Connections to Project

- Related hypotheses: `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` (the primary hypothesis whose mechanism depends on separability of the hormone axis); `hypothesis:0020-host-immune-baseline-reserve-gate` (the chromosome axis is one fixed component of the reserve; the hormone axis is a dynamic, life-stage-dependent modifier)
- Required data or analyses: (1) PAIS cohort with measured sex chromosomes (genetic), measured hormone levels (estradiol, testosterone, FSH, LH), and PAIS outcomes — allowing formal causal mediation or IV analysis; (2) Klinefelter and Turner syndrome natural experiments with PASC follow-up; (3) transgender cohort with longitudinal hormone data and infection/PAIS outcomes.
- Priority level: High for `hypothesis:0005` — this question must be answered (or the gap formally acknowledged) before the hypothesis can be promoted to active. Currently no admissible human PAIS vehicle exists for this decomposition.

## Related

- Topic notes: `topic:menopause-sex-hormones-and-pais-risk`; `immunity:topic:sex-hormone-life-stage-immune-homeostasis`; `immunity:topic:sex-as-a-modifier-of-immune-homeostasis`
- Article notes: `paper:Chaulagain2026` (source); `paper:Averyanova2022` (indirect mechanistic plausibility); `paper:Shahbaz2025` (reduced non-dominant sex hormone in LC patients, cross-sectional)
- Methods/Datasets: `dataset:ruth-2020-shbg-testosterone-gwas` (MR instrument for SHBG/testosterone); `dataset:covid19-hgi-longcovid-gwas` (outcome for MR); gender-affirming hormone therapy cohorts (e.g., Lakshmikanth2024 Nature).
