---
id: "evidence-line:0016-sylvester2022-covid-acute-male-postacute-female-supports-persistence-concentration"
kind: "evidence-line"
title: "COVID acute-male / post-acute-female reversal supports persistence-concentration"
status: "active"
stance: "supports"
target: "proposition:0008-female-excess-concentrates-in-post-acute-persistence"
source: "dataset:sylvester-2022-longcovid-sex"
strength: "moderate"
independence: "independent"
independence_group: "sylvester2022-lc-sex"
evidence_role: "proxy_support"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0008-female-excess-concentrates-in-post-acute-persistence"
  - "question:0007-mechanism-of-female-predominance-in-pais"
source_refs:
  - "dataset:sylvester-2022-longcovid-sex"
created: "2026-06-22"
updated: "2026-06-22"
---

# Evidence Line: COVID acute-male / post-acute-female reversal supports persistence-concentration

## What this line shows

In COVID the acute phase is **male**-biased (higher mortality and severe-disease risk in men) while post-acute long COVID is **female**-biased (`dataset:sylvester-2022-longcovid-sex`: overall long-COVID OR ≈ 1.22, 95% CI 1.13–1.32, with several female-skewed symptom domains). The sex gradient therefore *reverses* between the acute and persistence phases — the pattern `proposition:0008` predicts: the female excess is a property of persistence, not a carry-over of acute female risk [@Sylvester2022].

## Why it is independent

A large COVID-specific sex-stratified meta-analysis; methodologically distinct from the dengue meta (`evidence-line:0017`) and the Q-fever natural experiment (`evidence-line:0018`). Its own `independence_group: sylvester2022-lc-sex`.

## Caveats / scope

`proxy_support`, moderate: the acute-male and post-acute-female estimates come from **different sampling frames** (acute mortality cohorts vs post-acute symptom surveys), so the phase reversal is a between-study contrast, not a within-cohort phase interaction. Sex-differential care-seeking/reporting could inflate the post-acute female OR (ascertainment confound, unquantified). Consistency with the persistence-concentration pattern is not a direct within-design test of it.
