---
id: "evidence-line:0029-xie2022-ambulatory-male-vte-excess-survives-low-severity-stratum"
type: "evidence-line"
title: "Xie2022 male VTE excess in ambulatory (lowest-severity) COVID-19 patients is the decisive severity-discriminating line"
status: "active"
stance: "supports"
target: "proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment"
source: "paper:Xie2022"
strength: "strong"
independence: "independent"
independence_group: "xie2022-ukbb-ambulatory-vte"
evidence_role: "direct_test"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment"
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "hypothesis:0004-acute-severity-threshold"
source_refs:
  - "paper:Xie2022"
created: "2026-06-23"
updated: "2026-06-23"
---

# Evidence Line: Xie2022 — male VTE excess is present in the lowest acute-severity stratum

## What this line shows

Xie2022 is the **decisive severity-discriminating test** for `proposition:0012`. It is a UKBB population cohort of **18,818 strictly ambulatory (non-hospitalized) COVID-19 outpatients** — patients hospitalized at the time of testing were excluded — propensity-matched 1:5 to 93,179 uninfected participants, with prior VTE and antithrombotic users excluded (incident VTE). In this **lowest acute-severity stratum**, **male sex is an independent risk factor for incident VTE, adjusted HR 1.69 (95% CI 1.30–2.19)**, after adjustment for age, race/ethnicity, socioeconomic status, obesity, vaccination status, cancer, fall, fracture, and number of comorbidities. A male thrombotic excess that is already present *below* the hospitalization threshold cannot be explained as acute-severity (hospitalization/ICU) carryover — which is exactly the alternative `proposition:0012` must exclude.

## Why it is independent

A single large population cohort with its own `independence_group: xie2022-ukbb-ambulatory-vte`, methodologically distinct from the hospitalized CV-mortality cohort (`evidence-line:0030`) and the cross-study meta (`evidence-line:0031`). It is the only line restricted to ambulatory patients, which is what makes it the severity discriminator rather than a redundant direction line.

## Caveats / scope

`direct_test`, strong-for-its-design but bounded: (1) the cohort mean age is ~64, and VTE is male-predominant at older baseline ages, so this line establishes that the male excess **survives severity adjustment** but does **not** establish that it is COVID-*specific* amplification rather than carried-through baseline male vascular risk (the mechanism caveat on `proposition:0012`). (2) A published correction exists (JAMA Intern Med 2022;182(11):1234); confirm it does not alter the sex HR before quantitative reuse. (3) Observational; male sex enters as an adjusted covariate, not a formal infection×sex interaction term.
