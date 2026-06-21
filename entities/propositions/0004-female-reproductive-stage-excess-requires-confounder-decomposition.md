---
id: "proposition:0004-female-reproductive-stage-excess-requires-confounder-decomposition"
type: "proposition"
title: "The crude female / reproductive-stage excess in PAIS requires confounder decomposition before causal reading"
status: "active"
claim_layer: "structural_claim"
identification_strength: "structural"
proxy_directness: "direct"
supports_scope: "hypothesis_bundle"
discusses:
  - frame: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
    role: "background"
related:
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "patch-definition:menopause-pais-causal-dag"
  - "pre-registration:0001-menopause-pais-total-effect"
  - "task:t013"
  - "task:t018"
source_refs:
  - "paper:Shah2025"
  - "paper:Mishra2020"
created: "2026-06-21"
updated: "2026-06-21"
---

# Proposition: The crude female / reproductive-stage excess in PAIS requires confounder decomposition before causal reading

## Claim

The crude female / reproductive-stage excess in PAIS is **not interpretable as a reproductive-stage causal effect** without explicitly separating sex assigned at birth, chronological age, menopausal transition, hormone therapy, pregnancy, comorbidity, symptom overlap, and healthcare-seeking / reporting behaviour. This is an identification-discipline claim about the inferential structure, not a claim about the sign of any effect.

## Evidence Summary

`paper:Shah2025` reports the female long-COVID excess but does not isolate perimenopause from age, sex, pregnancy, comorbidity, and ascertainment. Acute-COVID analyses show menopausal / hormone-marker associations **attenuate after adjustment** for age, severity, comorbidity, route, and indication (`paper:Mishra2020`; corroborated by Costeira2021) — direct evidence that the crude association is confounded. The specific per-variable roles (which variables are confounders, colliders, or mediators of the menopause→PAIS effect) are **derived from the patch topology** of `patch-definition:menopause-pais-causal-dag` and its back-door query, not authored on this proposition.

## Caveats

`structural_claim` / `background` role: it informs how `hypothesis:0005` must be tested but is not a conjunctive member whose truth the conjecture stands or falls on. It is the prerequisite that the committed total-effect design (`pre-registration:0001`, `{age, smoking}` adjustment set) and the `task:t013` / `task:t018` female-excess decomposition operationalize.
