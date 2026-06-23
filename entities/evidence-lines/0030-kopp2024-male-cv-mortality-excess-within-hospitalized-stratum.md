---
id: "evidence-line:0030-kopp2024-male-cv-mortality-excess-within-hospitalized-stratum"
type: "evidence-line"
title: "Kopp2024 male CV-mortality excess persists within a hospitalized (severity-restricted) cohort"
status: "active"
stance: "supports"
target: "proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment"
source: "paper:Kopp2024"
strength: "moderate"
independence: "independent"
independence_group: "kopp2024-hospitalized-cv-mortality"
evidence_role: "direct_test"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment"
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "hypothesis:0004-acute-severity-threshold"
source_refs:
  - "paper:Kopp2024"
created: "2026-06-23"
updated: "2026-06-23"
---

# Evidence Line: Kopp2024 — male CV-mortality excess holds within hospitalized patients

## What this line shows

Kopp2024 follows **4,509 patients all hospitalized with moderate-to-severe SARS-CoV-2 pneumonia** for 18 months — a **severity-restricted (high-severity) stratum**. Within this stratum, men have higher 18-month cardiovascular mortality (Delta wave **6.13% vs 3.62%**, p=0.017) and a higher combined CV endpoint (16.87% vs 12.61%), and **male sex remains an independent predictor of 18-month CV death in multivariable Cox regression, HR 1.68 (95% CI 1.005–2.796), p=0.048**, after adjustment for age, BMI, and comorbidities. Because every patient is already hospitalized, the male excess here is *within* a controlled high-severity band — the complement to the ambulatory line (`evidence-line:0029`): the two together bracket the reversal across the low and high ends of the acute-severity range.

## Why it is independent

A single-cohort multi-wave hospitalized registry with its own `independence_group: kopp2024-hospitalized-cv-mortality`, distinct in population (hospitalized), endpoint (CV mortality/MACE), and design from the ambulatory VTE cohort and the meta.

## Caveats / scope

`direct_test`, moderate: (1) **wave-heterogeneous** — the male excess is significant in the Delta wave only; Alpha and Omicron are null, so the effect is not stable across variants/eras. (2) The model did **not** adjust for within-hospital severity (ICU vs floor), so residual severity confounding inside the hospitalized band remains, though the cohort restriction already removes the ambulatory-vs-hospitalized contrast. (3) Single cohort, modest event counts (CI lower bound ~1.0); observational with sex as an adjusted covariate.
