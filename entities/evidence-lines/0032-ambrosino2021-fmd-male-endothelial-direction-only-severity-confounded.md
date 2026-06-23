---
id: "evidence-line:0032-ambrosino2021-fmd-male-endothelial-direction-only-severity-confounded"
type: "evidence-line"
title: "Ambrosino2021 male endothelial dysfunction (FMD) supports the male direction only — severity-confounded, not a discriminating line"
status: "active"
stance: "supports"
target: "proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment"
source: "paper:Ambrosino2021"
strength: "weak"
independence: "independent"
independence_group: "ambrosino2021-fmd-casecontrol"
evidence_role: "proxy_support"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment"
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "hypothesis:0004-acute-severity-threshold"
source_refs:
  - "paper:Ambrosino2021"
created: "2026-06-23"
updated: "2026-06-23"
---

# Evidence Line: Ambrosino2021 — male endothelial dysfunction (direction only, severity-confounded)

## What this line shows

Ambrosino2021 (case-control, 133 convalescent COVID-19 vs 133 matched controls) finds persistent
endothelial dysfunction concentrated in males: male convalescent FMD **2.5%±1.9 vs female 6.1%±2.9
(p<0.001)**, and female cases vs female controls show **no difference** (6.1 vs 5.3%, p=0.362) — i.e.
the COVID-associated endothelial deficit is essentially male-only. This supports the **male
direction** (sub-claim A) of `proposition:0012`.

## Why it is independent

A distinct case-control cohort with an objective endothelial-function readout (FMD), its own
`independence_group: ambrosino2021-fmd-casecontrol`, methodologically separate from the VTE and
CV-mortality lines.

## Caveats / scope

`proxy_support`, **weak** — deliberately **not** a severity-discriminating line, and it must not be
read as supporting sub-claim (B) (survival of severity adjustment). FMD **correlates with
pulmonary-impairment severity** within cases (FEV1% rho=0.436; FVC% rho=0.406; PaO2 rho=0.247;
DLCO% rho=0.280), the cohort is 81% male, and the male-vs-female contrast was **not** adjusted for
or stratified by acute severity — so this line cannot separate a sex effect from acute-severity
confounding. It contributes only to the reproducibility of the male *direction*; the severity-
survival claim rests entirely on `evidence-line:0029` (ambulatory) and `evidence-line:0030`
(within-hospitalized).
