---
id: question:0070-resistance-vs-tolerance-comorbidity-routes-pais
kind: question
title: Do comorbidities modify PAIS risk primarily through impaired pathogen resistance
  or reduced injury tolerance, and does this distinction predict PASC phenotype?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Russell2023
related:
- hypothesis:0004-acute-severity-threshold
- hypothesis:0020-host-immune-baseline-reserve-gate
- hypothesis:0001-shared-dysregulated-attractor
- question:0057-compound-boundary-conditions-co-occurring-effect-modifiers-in-pais
created: '2026-07-10'
updated: '2026-07-10'
---

# Do comorbidities modify PAIS risk primarily through impaired pathogen resistance or reduced injury tolerance, and does this distinction predict PASC phenotype?

## Summary

[@Russell2023] introduces a conceptual distinction between two mechanistic routes by which comorbidities modify COVID-19 outcomes: (a) **resistance** — capacity to control pathogen replication, impaired by specific immune defects (B-cell depletion, HIV-related CD4 T-cell loss, CMV latency effects); and (b) **tolerance** — capacity to withstand organ injury given a fixed level of immune/pathogen-mediated damage, reduced by chronic organ-function impairment (CKD, COPD, pulmonary fibrosis) and by frailty/multimorbidity. Most comorbidities act primarily through reduced tolerance (generic reserve effect), while a few act specifically through impaired resistance. The question is whether this resistance/tolerance distinction is predictive of PASC *phenotype* across PAIS triggers — not just COVID-19 severity — i.e., does impaired resistance (leading to longer antigen exposure, hypothesis:0002) produce a different PASC phenotype than impaired tolerance (leading to greater organ damage before viral clearance)?

## Why It Matters

- **Decision affected:** How to stratify PAIS comorbidity analyses — separating immune-clearance-impaired from organ-reserve-depleted patient groups will produce mechanistically distinct PASC phenotypes if the distinction is real. This has implications for which comorbidities to measure, how to adjust for them, and which PASC subtypes to expect in different patient populations.
- **Risk if unanswered:** Lumping resistance-impaired and tolerance-impaired comorbidities together in PASC analyses will reduce power to detect subgroup-specific mechanisms and may lead to incorrect conclusions about causal pathways (e.g., attributing antigen-persistence PASC features to organ-reserve effects rather than clearance defects).

## Current Evidence

- **Supporting (resistance route):** Rituximab (B-cell depletion) associated with prolonged viral shedding and relapse in COVID-19 — direct evidence that impaired resistance (antibody-mediated clearance) prolongs antigen exposure, directly connecting to h0002 (tissue reservoir / antigen persistence). HIV CD4 <350/μL independently predicts severe disease even with antiretroviral suppression. CMV seropositivity adds COVID-19 risk and severity independent of age/comorbidities, mechanism unclear but T-cell-independent.
- **Supporting (tolerance route):** Performance status / ECOG score (correlated with multimorbidity) predicts ICU mortality with effect size exceeding age [@Russell2023]; frailty clinical score similarly predictive. CKD and COPD associations more plausibly explained by reduced baseline organ reserve than by specific immune perturbation. ISARIC4C 4C score uses only multimorbidity count — consistent with tolerance/reserve being the dominant cross-comorbidity signal.
- **Evidence gap:** No study has directly compared PASC phenotype (e.g., fatigue-dominant vs dyspnea-dominant vs cognitive-dominant) by resistance-impaired vs tolerance-impaired comorbidity type. The distinction is conceptual in [@Russell2023] for acute COVID-19; its extension to PASC phenotype prediction is the gap.
- **Complication:** Many comorbidities impair both routes (e.g., advanced cancer: immune suppression + organ dysfunction). Empirical separation requires careful single-comorbidity natural experiments (rituximab cohorts, isolated CKD cohorts).

## Thoughts

- **Best current interpretation:** The resistance/tolerance distinction is plausible and maps cleanly onto existing project hypotheses: resistance impairment → antigen persistence (h0002) → sustained immune activation (h0001 attractor route A); tolerance impairment → organ damage during acute phase → inflammatory recovery failure (attractor route B, more consistent with post-intensive-care syndrome overlap). The two routes likely produce partially distinct PASC phenotypes, but this has not been tested.
- **Major uncertainty:** Whether the PASC phenotype distinction is empirically separable — most PASC cohorts lack granular pre-existing comorbidity immunophenotyping, making prospective separation difficult. Retrospective EHR approaches (e.g., rituximab users vs matched non-users followed for PASC) may offer near-term tractability.

## Connections to Project

- Related hypotheses: `hypothesis:0002-tissue-reservoir-antigen-fragment` (resistance impairment → antigen persistence); `hypothesis:0004-acute-severity-threshold` (tolerance impairment → threshold crossing at lower insult); `hypothesis:0001-shared-dysregulated-attractor` (both routes may converge on the same attractor but via mechanistically different entry paths); `hypothesis:0020-host-immune-baseline-reserve-gate` (tolerance = reserve depletion axis).
- Required data or analyses: Natural experiments in single-comorbidity populations: (1) rituximab/anti-CD20 cohort vs age-matched controls: compare PASC phenotype, viral clearance trajectory, and antigen-persistence markers. (2) Isolated CKD (without immune dysfunction) cohort: compare PASC phenotype and inflammatory trajectory as a pure tolerance/reserve test. Cross-comorbidity PASC phenotyping in a large cohort with detailed baseline immune and organ-function data.
- Priority level: P3 — the conceptual framing is important for hypotheses h0002/h0004, but empirical testing requires comorbidity-stratified PASC cohorts that are not yet available at scale.

## Related

- Topic notes: `topic:population-boundary-conditions-and-effect-modifiers-in-pais`.
- Article notes: `paper:Russell2023`; Nalbandian et al. (Nat Med 27:601, 2021) on PASC phenotypes; PHOSP-COVID (Lancet Respir Med 9:1275, 2021) on post-hospitalization comorbidity effects.
- Methods/Datasets: Rituximab registry cohorts with COVID-19 outcomes (e.g., the Calderón-Parra et al. 2022 cohort cited in [@Russell2023]); PHOSP-COVID phenotyping data; large EHR datasets with comorbidity + PASC diagnosis codes.
