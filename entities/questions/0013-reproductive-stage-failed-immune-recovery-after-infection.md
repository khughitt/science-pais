---
id: question:0013-reproductive-stage-failed-immune-recovery-after-infection
kind: question
title: Does reproductive-stage transition change the probability of failed immune recovery after infection?
status: active
ontology_terms:
- reproductive stage
- menopause
- sex hormones
- immune recovery
- post-acute infection syndromes
datasets: []
source_refs:
- cite:Shah2025
- cite:Stewart2024
- cite:Humphreys2025
- cite:Averyanova2022
- cite:Costeira2021
- cite:Rebman2026
- cite:Kawai2025
- cite:Boneva2015
related:
- question:0007-mechanism-of-female-predominance-in-pais
- topic:menopause-sex-hormones-and-pais-risk
- topic:long-covid-immune-dysregulation
- topic:thromboinflammation-and-endothelial-dysfunction
- immunity:topic:sex-hormone-life-stage-immune-homeostasis
- immunity:topic:endocrine-immune-recovery-thresholds
- cycles:topic:menstrual-cycle-menopause-immune-modulation
required_capabilities:
- data_product: data-product:gwas-summary-statistics
  qualifiers:
    trait: sex-hormone-biomarker
- data_product: data-product:proteomics-affinity
  qualifiers:
    outcome: sex-hormone-level
created: "2026-06-19"
updated: "2026-06-26"
---
# Does reproductive-stage transition change the probability of failed immune recovery after infection?

## Summary

This question asks whether transitions in reproductive endocrine state, especially perimenopause and menopause, modify the probability that an acute infection resolves normally versus enters a persistent PAIS-like state.
It is narrower than asking whether female sex increases PAIS risk and more causal than asking whether menopausal symptoms overlap with long COVID.
The core issue is whether reproductive-stage biology changes immune, vascular, autonomic, or tissue-repair recovery thresholds after infection.

## Why It Matters

- It is the most direct bridge between the female-predominance signal in PAIS and the sex-hormone/life-stage immune mechanisms reviewed in the immunity project.
- It prevents conflating sex assigned at birth, chronological age, menopausal status, hormone therapy, pregnancy, comorbidity, and symptom reporting into one vague "women's hormones" variable.
- It shapes analysis design: menopausal transition may be a confounder, mediator, effect modifier, competing diagnosis, or downstream consequence depending on the estimand.
- If left unresolved, PAIS models may either over-attribute midlife female risk to menopause or suppress a real effect by adjusting it away as noise.

## Current Evidence

- Shah2025 provides the strongest population-level anchor: female sex was associated with higher long-COVID risk, with the clearest excess in ages 40-54 years and a smaller excess at age 55 years or older, but the study does not cleanly isolate menopausal transition from sex, age, pregnancy, comorbidity, and ascertainment [@Shah2025].
- Stewart2024 and Humphreys2025 show that perimenopause, menopause, and long COVID share fatigue, cognitive symptoms, sleep disturbance, palpitations, musculoskeletal pain, and mood symptoms, making symptom overlap a serious measurement threat [@Stewart2024; @Humphreys2025].
- Averyanova2022 summarizes plausible hormone-immune and hormone-vascular mechanisms involving cytokines, T-cell balance, B-cell response, endothelium, and hemostasis, but most of this evidence is indirect for PAIS [@Averyanova2022].
- Costeira2021 suggests estrogen-proxy associations with acute COVID outcomes can be methodologically fragile because hormone therapy route, indication, comorbidity, and healthy-user bias are hard to separate [@Costeira2021].
- Rebman2026 cautions that sex and menopausal status can affect acute infection presentation, diagnostic markers, and post-acute persistence in different directions [@Rebman2026].
- Kawai2025 supports a viral-infection-to-vascular-risk pathway that could interact with menopause-associated cardiometabolic risk without requiring menopause to be the primary PAIS cause [@Kawai2025].
- Boneva2015 reports an early/surgical-menopause signal in CFS and a limited timing clue: hysterectomy/oophorectomy preceded CFS onset in 71% of the dated-surgery subset. This weakly argues against a pure illness-causes-all-menopause-timing interpretation for the surgical component, but it does not provide pre-infection natural-menopause or confirmed post-infectious timing [@Boneva2015].

## Thoughts

- Best current interpretation: reproductive-stage transition is a plausible modifier of failed immune recovery, but it is not yet established as an independent cause of PAIS.
- The highest-value causal model should separate at least five competing explanations: hormone-mediated immune recovery threshold, X-linked immune dosage, menopause-associated vascular/metabolic risk, symptom overlap/misclassification, and care-seeking or reporting differences.
- The major remaining uncertainty is whether perimenopause, natural menopause, surgical menopause, or gynecologic disease/surgery indications are the biologically relevant exposure window. Boneva2015 makes surgical pathways salient but does not settle the natural-menopause question.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor`, `hypothesis:0004-acute-severity-threshold`, candidate `hypothesis:0005-reproductive-stage-immune-homeostatic-margin`
- Required data or analyses: longitudinal PAIS cohorts with sex, age, menopausal status, menstrual status, hormone therapy route/dose, pregnancy status, acute severity, cardiometabolic comorbidity, immune/endothelial/autonomic markers, symptom domains, and care-seeking/ascertainment proxies.
- Priority level: P2

## Related

- Topic notes: `topic:menopause-sex-hormones-and-pais-risk`, `topic:long-covid-immune-dysregulation`, `topic:thromboinflammation-and-endothelial-dysfunction`, `immunity:topic:sex-hormone-life-stage-immune-homeostasis`, `cycles:topic:menstrual-cycle-menopause-immune-modulation`
- Article notes: `paper:Shah2025`, `paper:Stewart2024`, `paper:Humphreys2025`, `paper:Averyanova2022`, `paper:Costeira2021`, `paper:Rebman2026`, `paper:Kawai2025`
- Methods/Datasets: pending hormone-measured long-COVID cohort search and causal DAG work (`task:t014`, `task:t015`)
