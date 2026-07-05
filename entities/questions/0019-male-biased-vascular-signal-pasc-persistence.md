---
id: question:0019-male-biased-vascular-signal-pasc-persistence
kind: question
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
- cite:Xie2022
related:
- paper:Kopp2024
- paper:Xie2022
- question:0007-mechanism-of-female-predominance-in-pais
- question:0010-vascular-microclot-subphenotype
- question:0020-male-vte-excess-post-acute-persistence
- proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
- interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment
- hypothesis:0004-acute-severity-threshold
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
created: '2026-06-22'
updated: '2026-06-23'
---

# Does the male-biased acute cardiovascular signal in COVID-19 persist into the post-acute phase, or does it reverse to a female-predominant PASC phenotype?

## Summary

> **Substantially resolved for CV mortality; narrowed for VTE (2026-06-23, t042 →
> `interpretation:0005`, `proposition:0012`).** The core CV question — does a male hard-endpoint
> signal persist post-acutely and avoid reversal to a female phenotype — is answered **yes** for
> 18-month cardiovascular mortality in Kopp2024 (hospitalized-restricted Delta-wave HR 1.68) [@Kopp2024].
> Xie2022 adds the decisive low-severity discriminator for the broader vascular direction: male
> VTE excess is present in ambulatory patients (aHR 1.69), but only in the 30-day acute window [@Xie2022].
> Therefore t042 resolves the coarse acute-severity-carryover concern, not the narrower late-VTE
> temporal-persistence gap. **Residual open threads** (carried forward, not closed): (1) is the
> excess COVID-specific amplification or carried-through baseline male vascular risk at older ages?
> (2) does it survive *within*-hospitalized severity stratification (ICU vs floor)? (3) does
> ambulatory VTE remain male-biased in the 31-180-day window (`question:0020`)?

Male sex is a well-established predictor of more severe acute COVID-19, including higher ICU admission, cardiac arrest, and in-hospital death. The question is whether this acute male cardiovascular disadvantage carries over into the post-acute phase (18+ months), or whether it reverses to the female-predominant PAIS phenotype seen in fatigue-dominant sequelae. If the male CV excess persists within a severity-restricted cohort, it implies a durable thromboinflammatory or vascular repair failure phenotype — not just the outpatient/inpatient severity mix — and represents a distinct, male-biased PAIS subphenotype alongside the more commonly discussed female-biased fatigue phenotype.

## Why It Matters

- The direction of the sex effect matters for the `hypothesis:0005` bundle: if male bias in CV outcomes is purely an acute-severity artifact, no post-acute mechanism specific to sex is required. If it survives severity restriction, a sex-modulated post-acute thromboinflammatory or vascular repair failure mechanism is implicated.
- Distinguishing CV-dominant (male-biased) from fatigue/neuroimmune-dominant (female-biased) PAIS subphenotypes would affect any sex-stratified analysis or clinical trial design.
- Leaving this unanswered risks conflating the two directional sex signals (male CV vs. female fatigue), muddying mechanism hypotheses.

## Current Evidence

**Supporting (male CV excess persists post-acutely within a severity-restricted cohort):**
- Kopp2024: In 4,509 patients all hospitalized with moderate-to-severe SARS-CoV-2 pneumonia, male sex was an independent predictor of 18-month CV death in the Delta wave (HR 1.676, 95% CI 1.005–2.796, p = 0.048) after adjustment for age, BMI, and comorbidities. CV mortality was 6.13% in men vs. 3.62% in women (p = 0.017). The combined CV endpoint was also significantly higher in men (16.87% vs. 12.61%, p = 0.017). Because all patients were hospitalized, the coarser acute-severity confound (hospitalized vs. outpatient) is controlled by design.
- The male excess was Delta-specific; Alpha and Omicron waves showed no significant sex difference — suggesting the signal interacts with variant-era context rather than being a universal fixed effect.

**Supporting the low-severity boundary test, not post-acute VTE persistence:**
- Xie2022: In 18,818 ambulatory COVID-19 outpatients, male sex independently predicted 30-day incident VTE (aHR 1.69, 95% CI 1.30-2.19). This shows the male vascular hard-endpoint direction is present below the hospitalization threshold, but it does not answer whether VTE remains male-biased after day 30.

**Complicating / mixed evidence:**
- The male excess in Kopp2024 is wave-heterogeneous, limiting generalizability; the Omicron result (no male excess, very low overall CV mortality) may reflect vaccination era, variant attenuation, or cohort changes.
- Within-hospitalized severity (ICU vs. floor) was not adjusted for in Kopp2024's Cox models; residual severity confounding within the hospitalized tier remains.
- In-hospital deaths were excluded from the analyzed sample (364 excluded: 146 Alpha, 107 Delta, 111 Omicron); if these are male-enriched, survivor-selection bias may underestimate the male long-term CV disadvantage.
- An Italian 6-month follow-up study (referenced in Kopp2024) found female sex was an independent predictor of MACCE — directionally opposite to the Delta-wave finding, suggesting the direction of sex effect may be time- and cohort-dependent.

## Thoughts

- Best current interpretation: The male acute CV disadvantage carries into the 18-month post-acute window in at least the Delta-wave hospitalized cohort (Kopp2024), consistent with a durable male-biased thromboinflammatory or vascular repair phenotype rather than purely the hospitalized-vs-ambulatory severity mix. However, this signal is wave-heterogeneous and single-center, so confidence is moderate, not high.
- Male CV mortality excess and female fatigue/neuroimmune excess may coexist as distinct PAIS subphenotypes, with the relative prevalence depending on the wave, variant, and population severity-distribution.
- The major remaining uncertainty is whether the male CV signal would survive *within-hospitalized* severity stratification (ICU vs. floor), whether it replicates in other hospitalized Delta-wave cohorts with vaccination status captured, and whether the ambulatory male VTE excess persists beyond the 30-day acute window.

## Connections to Project

- Related hypotheses: `hypothesis:0004-acute-severity-threshold` (severity gating), `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` (sex as homeostatic reserve modifier)
- Required data or analyses: Hospitalized COVID-19 cohort with ICU/severity subgroup data + sex + 12-18 month CV outcomes; ideally multi-wave with vaccination status. Separately, ambulatory sex-stratified VTE follow-up beyond 30 days is tracked in `question:0020`.
- Priority level: Medium-high — load-bearing for sex-stratified mechanism framing and any future CV subphenotype analysis.

## Related

- Topic notes: `topic:thromboinflammation-and-endothelial-dysfunction`
- Article notes: `paper:Kopp2024` (primary post-acute CV evidence); `paper:Xie2022` (acute ambulatory low-severity VTE discriminator); Abubasheer2025 (pooled hard-endpoint direction)
- Methods/Datasets: VA database studies (Cai2024, Xie2024) include sex but were predominantly male cohorts; ideally need a sex-balanced hospitalized cohort.
