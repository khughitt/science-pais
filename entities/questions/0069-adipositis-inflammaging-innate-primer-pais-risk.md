---
id: question:0069-adipositis-inflammaging-innate-primer-pais-risk
kind: question
title: Does adipositis/inflammaging as a chronic innate immune primer compound PASC
  risk independently of acute severity?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Russell2023
related:
- hypothesis:0004-acute-severity-threshold
- hypothesis:0020-host-immune-baseline-reserve-gate
- question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
created: '2026-07-10'
updated: '2026-07-10'
---

# Does adipositis/inflammaging as a chronic innate immune primer compound PASC risk independently of acute severity?

## Summary

[@Russell2023] provides Mendelian randomization evidence that obesity — via adipositis (chronic low-grade innate immune inflammation from adipose tissue) — causally increases risk of inflammatory lung injury (pneumonitis) in COVID-19, a mechanism analogous to the inflammaging pathway in older patients. Both processes represent states of tonically elevated innate immune activation that prime the lung for myeloid-driven injury when viral replication is not rapidly contained. The question is whether this same adipositis/inflammaging channel — not merely the acute-severity endpoint it produces — independently increases the probability of PASC chronicity, i.e., whether obesity and frailty confer PASC risk over and above the acute-severity pathway they share.

## Why It Matters

- **Decision affected:** Whether obesity and frailty should be modeled as PASC risk factors that act *through* acute severity (mediation only) or also *directly* via a chronic innate-immune priming mechanism. This determines how to structure the causal DAG for h0020 and whether adipositis/inflammaging is a distinct modifiable target for PASC prevention.
- **Risk if unanswered:** If adipositis/inflammaging acts solely through increasing acute severity, then PASC prevention requires only acute-severity reduction (vaccinations, antivirals). If it also operates as an independent priming channel, then metabolic/anti-inflammatory interventions targeted at adipose inflammation could reduce PASC risk even without changing acute severity — a broader intervention opportunity.

## Current Evidence

- **Supporting (indirect):** [@Russell2023] shows MR-supported causal role of obesity specifically for critical/inflammatory COVID-19 (pneumonitis phase), with adipositis proposed as the mechanism; the parallel to influenza (same group) suggests this is a general innate immune priming effect, not COVID-specific.
- **Supporting (indirect):** Inflammaging in older patients is described as analogous to adipositis, predisposing to innate immune lung damage — two independent lines of evidence pointing to tonic innate-immune elevation as a shared modifier.
- **Supporting (indirect):** Multimorbidity associated with PASC prevalence (2.8–5.5% vs 1.8%; [@Russell2023]), and most of 80 comorbidities predict 12-week symptom persistence (Subramanian et al. 2022, Nat Med) — consistent with but not mechanistically specific to an adipositis/inflammaging channel.
- **Conflicting:** T2D (often co-occurring with obesity) is NOT causally supported by MR for COVID-19 outcomes; glycemic control associations may reflect obesity rather than diabetes per se. This complicates the inference that metabolic inflammation is the causal agent vs its downstream metabolic consequences.
- **Missing:** No study has directly tested whether adipositis biomarkers (e.g., IL-6, CRP, adipokines at baseline) or inflammaging markers (e.g., p16^INK4a, senescence indices) predict PASC incidence after adjusting for acute severity. The causal chain from adipositis → PASC is hypothesized but unmeasured.

## Thoughts

- **Best current interpretation:** Adipositis/inflammaging plausibly increases PASC risk through two non-exclusive routes: (a) increasing acute inflammatory injury severity (MR-supported route), and (b) maintaining a chronically primed innate immune state that sustains post-acute inflammation. Route (b) is biologically plausible but not yet empirically grounded in PASC-specific data.
- **Major uncertainty:** Whether the adipositis/inflammaging → PASC association would survive acute-severity adjustment. If obese/older patients develop more severe COVID-19, their elevated PASC risk could be fully mediated by acute severity, and the "direct priming" channel would be absent. Separating mediation from direct effect requires designs that stratify on acute severity (hospitalized vs non-hospitalized) and measure baseline inflammatory tone prior to infection.

## Connections to Project

- Related hypotheses: `hypothesis:0020-host-immune-baseline-reserve-gate` (adipositis/inflammaging as specific instances of reserve depletion via elevated innate-immune tone); `hypothesis:0004-acute-severity-threshold` (adipositis raises risk of crossing the threshold by increasing acute inflammatory injury).
- Required data or analyses: A cohort with pre-infection adiposity/inflammatory markers (BMI, IL-6, CRP) plus post-COVID outcomes stratified by acute severity. Mediation analysis partitioning total obesity → PASC effect into severity-mediated and severity-independent components. MR analysis using obesity or adiposity instruments on PASC outcomes (vs inflammatory lung injury, which is already MR-supported).
- Priority level: P3 — mechanistically important and cross-project relevant (pan-disease, immunity), but requires a well-powered cohort with pre-infection inflammatory data; near-term tractability is moderate.

## Related

- Topic notes: `topic:population-boundary-conditions-and-effect-modifiers-in-pais`.
- Article notes: `paper:Russell2023`; Subramanian et al. (Nat Med 28:1706, 2022) on comorbidities and 12-week symptom persistence; Xie et al. (Nat Med 28:583, 2022) on post-acute CVD in VA cohort.
- Methods/Datasets: Requires either a prospective cohort with pre-infection metabolic/inflammatory phenotyping and post-COVID follow-up, or a Mendelian randomization study using BMI/obesity instruments on PASC outcomes (if GWAS of PASC is available).
