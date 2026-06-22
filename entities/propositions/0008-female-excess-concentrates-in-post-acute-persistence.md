---
id: "proposition:0008-female-excess-concentrates-in-post-acute-persistence"
type: "proposition"
title: "The PAIS female excess concentrates in the post-acute persistence phase rather than being inherited from an acute female skew"
status: "active"
claim_layer: "empirical_regularity"
identification_strength: "observational"
proxy_directness: "direct"
supports_scope: "hypothesis_bundle"
discusses:
  - frame: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
    role: "background"
related:
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "question:0013-reproductive-stage-failed-immune-recovery-after-infection"
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "interpretation:0002-t013-cross-trigger-sex-effect-sizes"
  - "task:t013"
  - "task:t018"
source_refs:
  - "dataset:sylvester-2022-longcovid-sex"
  - "dataset:dengue-postinfective-fatigue-meta"
  - "dataset:dutch-qfever-qfs-cohort"
created: "2026-06-22"
updated: "2026-06-22"
---

# Proposition: The PAIS female excess concentrates in the post-acute persistence phase rather than being inherited from an acute female skew

## Claim

Across post-acute infection syndromes, the well-documented female excess is **a property of the persistence phase**, not a carry-over of an acute-phase female skew. In the triggers with usable sex-stratified data the acute phase is *sex-neutral or male*-biased while the *post-acute* phase is female-biased: the female excess therefore **emerges in (or is amplified by) persistence** rather than being inherited from acute disease. This is an `empirical_regularity` about the *phase location* of the sex gradient — it is deliberately agnostic about mechanism (hormonal, X-dosage, immune-setpoint, or ascertainment), which `question:0007` holds open.

## Evidence Summary

Three methodologically distinct triggers show the same acute→post-acute reversal:

- **COVID** — the acute phase is *male*-biased (mortality/severity) yet post-acute long COVID is female-biased (overall OR ≈ 1.22; `dataset:sylvester-2022-longcovid-sex`). See `evidence-line:0016`.
- **Dengue** — acute severe-dengue/DHF risk is **not** female-predominant, yet post-dengue fatigue carries female OR ≈ 1.65–1.69 (`dataset:dengue-postinfective-fatigue-meta`, Hertanti2025 ⊕ Conde2026; corroborated within-trigger by the Colombo cohort aOR ≈ 2). See `evidence-line:0017`.
- **Q-fever** — acute exposure is *male*-skewed (occupational/farming) yet QFS persistence is not male-skewed (`dataset:dutch-qfever-qfs-cohort`, the Dutch QFS cohorts — a qualitative natural experiment, no published female OR). See `evidence-line:0018`.

The convergence rests on **between-study** comparison of separately-measured acute and post-acute sex gradients, not a within-design phase interaction, so it is `suggestive` rather than decisive.

## Caveats

`empirical_regularity` / `background` role for `hypothesis:0005`: this frames *where* the female excess sits, which any reproductive-stage / immune-setpoint account must explain, but it is not a conjunctive member of `hypothesis:0005` and does not by itself favour a reproductive-stage mechanism over an ascertainment or immune-setpoint one. Two confounds remain unquantified and are not separable from this evidence: (1) **ascertainment** — sex-differential care-seeking/reporting could inflate apparent post-acute female excess uniformly (Zhang2022, per `question:0007`); (2) **between-study heterogeneity** — acute and post-acute estimates come from different cohorts, designs, and case definitions, so the phase contrast is not held within one sampling frame. The decisive design (within-cohort acute-male-skew → post-acute-female-skew, e.g. Dubbo/Dutch-QFS) requires microdata that are currently private. This proposition records the cross-trigger pattern; it does **not** assert a fatigue-vs-neuropsychiatric domain boundary, which `interpretation:0002` found directionally inconsistent.
