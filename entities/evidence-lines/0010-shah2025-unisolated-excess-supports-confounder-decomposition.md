---
id: "evidence-line:0010-shah2025-unisolated-excess-supports-confounder-decomposition"
kind: "evidence-line"
title: "Shah2025 non-isolation of perimenopause supports the confounder-decomposition requirement"
status: "active"
stance: "supports"
target: "proposition:0004-female-reproductive-stage-excess-requires-confounder-decomposition"
source: "paper:Shah2025"
strength: "moderate"
independence: "independent"
independence_group: "shah2025-lc-risk"
evidence_role: "background_constraint"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0004-female-reproductive-stage-excess-requires-confounder-decomposition"
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
source_refs:
  - "paper:Shah2025"
created: "2026-06-21"
updated: "2026-06-21"
---

# Evidence Line: Shah2025 non-isolation of perimenopause supports the confounder-decomposition requirement

## What this line shows

`paper:Shah2025` reports a female long-COVID excess but **cannot isolate perimenopause** from chronological age, sex, pregnancy, comorbidity, and ascertainment — a concrete instance of the crude excess being uninterpretable as a stage effect without decomposition, which is exactly what `proposition:0004` claims.

## Why it is independent

`independence_group: shah2025-lc-risk` (same study as `evidence-line:0001`, different target — here it supports the identification claim, not the threshold effect).

## Caveats / scope

`background_constraint`, moderate: it demonstrates the inferential problem rather than measuring any specific confounder's magnitude. The variable-level confounder/collider structure is derived from `patch-definition:menopause-pais-causal-dag`.
