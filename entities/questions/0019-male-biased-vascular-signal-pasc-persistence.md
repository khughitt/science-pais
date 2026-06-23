---
id: question:0019-male-biased-vascular-signal-pasc-persistence
type: question
title: Does the male-biased acute cardiovascular signal in COVID-19 persist into the
  post-acute phase, or does it reverse to a female-predominant PASC phenotype?
status: active
ontology_terms:
  - sex differences
  - thromboinflammation
  - cardiovascular outcomes
  - PASC subphenotype
  - vascular long COVID
datasets: []
source_refs:
- cite:Abubasheer2025
- cite:Kopp2024
related:
- paper:Kopp2024
- question:0007-mechanism-of-female-predominance-in-pais
- question:0010-vascular-microclot-subphenotype
- hypothesis:0004-acute-severity-threshold
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
created: '2026-06-22'
updated: '2026-06-22'
---

# Does the male-biased acute cardiovascular signal in COVID-19 persist into the post-acute phase, or does it reverse to a female-predominant PASC phenotype?

## Summary

Male sex is a well-established predictor of more severe acute COVID-19, including higher ICU admission, cardiac arrest, and in-hospital death. The question is whether this acute male cardiovascular disadvantage carries over into the post-acute phase (18+ months), or whether it reverses to the female-predominant PAIS phenotype seen in fatigue-dominant sequelae. If the male CV excess persists after severity adjustment, it implies a durable thromboinflammatory or vascular mechanism — not just more acute injury — and represents a distinct, male-biased PAIS subphenotype alongside the more commonly discussed female-biased fatigue phenotype.

## Why It Matters

- The direction of the sex effect matters for the `hypothesis:0005` bundle: if male bias in CV outcomes is purely an acute-severity artifact, no post-acute mechanism specific to sex is required. If it survives severity restriction, a sex-modulated post-acute thromboinflammatory or vascular repair failure mechanism is implicated.
- Distinguishing CV-dominant (male-biased) from fatigue/neuroimmune-dominant (female-biased) PAIS subphenotypes would affect any sex-stratified analysis or clinical trial design.
- Leaving this unanswered risks conflating the two directional sex signals (male CV vs. female fatigue), muddying mechanism hypotheses.

## Current Evidence

**Supporting (male CV excess persists post-acutely within a severity-restricted cohort):**
- Kopp2024: In 4,509 patients all hospitalized with moderate-to-severe SARS-CoV-2 pneumonia, male sex was an independent predictor of 18-month CV death in the Delta wave (HR 1.676, 95% CI 1.005–2.796, p = 0.048) after adjustment for age, BMI, and comorbidities. CV mortality was 6.13% in men vs. 3.62% in women (p = 0.017). The combined CV endpoint was also significantly higher in men (16.87% vs. 12.61%, p = 0.017). Because all patients were hospitalized, the coarser acute-severity confound (hospitalized vs. outpatient) is controlled by design.
- The male excess was Delta-specific; Alpha and Omicron waves showed no significant sex difference — suggesting the signal interacts with variant-era context rather than being a universal fixed effect.

**Complicating / mixed evidence:**
- The male excess in Kopp2024 is wave-heterogeneous, limiting generalizability; the Omicron result (no male excess, very low overall CV mortality) may reflect vaccination era, variant attenuation, or cohort changes.
- Within-hospitalized severity (ICU vs. floor) was not adjusted for in Kopp2024's Cox models; residual severity confounding within the hospitalized tier remains.
- In-hospital deaths were excluded from the analyzed sample (364 excluded: 146 Alpha, 107 Delta, 111 Omicron); if these are male-enriched, survivor-selection bias may underestimate the male long-term CV disadvantage.
- An Italian 6-month follow-up study (referenced in Kopp2024) found female sex was an independent predictor of MACCE — directionally opposite to the Delta-wave finding, suggesting the direction of sex effect may be time- and cohort-dependent.

## Thoughts

- Best current interpretation: The male acute CV advantage does carry into the 18-month post-acute window in at least the Delta-wave hospitalized cohort (Kopp2024), consistent with a durable male-biased thromboinflammatory or vascular repair mechanism rather than purely acute-severity confounding. However, this signal is wave-heterogeneous and single-center, so confidence is moderate, not high.
- Male CV mortality excess and female fatigue/neuroimmune excess may coexist as distinct PAIS subphenotypes, with the relative prevalence depending on the wave, variant, and population severity-distribution.
- The major remaining uncertainty is whether the male CV signal would survive *within-hospitalized* severity stratification (ICU vs. floor), and whether it replicates in other hospitalized Delta-wave cohorts with vaccination status captured.

## Connections to Project

- Related hypotheses: `hypothesis:0004-acute-severity-threshold` (severity gating), `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` (sex as homeostatic reserve modifier)
- Required data or analyses: Hospitalized COVID-19 cohort with ICU/severity subgroup data + sex + 12-18 month CV outcomes; ideally multi-wave with vaccination status.
- Priority level: Medium-high — load-bearing for sex-stratified mechanism framing and any future CV subphenotype analysis.

## Related

- Topic notes: `topic:thromboinflammation-and-endothelial-dysfunction`
- Article notes: `paper:Kopp2024` (primary evidence); Abubasheer2025 (acute-phase sex CV signal)
- Methods/Datasets: VA database studies (Cai2024, Xie2024) include sex but were predominantly male cohorts; ideally need a sex-balanced hospitalized cohort.
