---
id: evidence-line:0093-russell2023-multimorbidity-tolerance-supports-reserve-gate
kind: evidence-line
title: Russell2023 multimorbidity-tolerance model supports the reserve gate
status: active
stance: supports
target: proposition:0043-host-reserve-dominates-acute-severity-gate
source: paper:Russell2023
strength: moderate
independence: independent
independence_group: russell2023-multimorbidity-mr
evidence_role: background_constraint
related:
- hypothesis:0020-host-immune-baseline-reserve-gate
source_refs:
- paper:Russell2023
created: '2026-07-10'
updated: '2026-07-10'
evidence_type: literature_evidence
---
# Evidence Line: Russell2023 multimorbidity-tolerance model supports the reserve gate

## What this line shows

`paper:Russell2023` supplies the mechanistic vocabulary for the reserve gate: a three-phase model with an explicit *resistance-vs-tolerance* distinction in which total multimorbidity burden (not any single condition) is the dominant severity predictor and most comorbidities act via reduced tolerance/reserve, with Mendelian randomization separating causal (obesity → adipositis → pneumonitis) from confounded (T2D, not independently causal) associations [@Russell2023]. This grounds `proposition:0043`'s premise that reserve is the operative construct, as a `background_constraint` on how the reserve gate should be modeled.

## Why it is independent

This line contributes a mechanistic/causal-genetic (MR) argument across different populations and does not share the single-EHR mediation design of `evidence-line:0092` (Azhir2026). Its value is orthogonal — it constrains *why* multimorbidity gates severity (tolerance/reserve), whereas Azhir2026 quantifies *how much* reserve dominates severity.

## Caveats / scope

`background_constraint`, moderate. Russell2023 concerns acute-COVID severity, not directly the post-acute PAIS outcome, so its support for the reserve gate is by extension of the severity mechanism rather than a direct PAIS test. Reserve remains proxied by comorbidity aggregates, and the MR arm addresses only the specific exposures modeled (obesity, T2D), not reserve as a whole.
