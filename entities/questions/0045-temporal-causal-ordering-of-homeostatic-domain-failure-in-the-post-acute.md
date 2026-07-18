---
id: question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute
kind: question
title: Temporal causal ordering of homeostatic domain failure in the post-acute period
status: active
ontology_terms: []
datasets: []
source_refs:
- paper:Walitt2024
- paper:Peluso2024b
- cite:Su2022
- cite:DirayArce2023
- cite:Gabernet2025
- cite:Talla2021
- cite:Klein2023
- cite:PerezChacon2026
- cite:Faghy2026
origins:
- type: assistant
  ref: explore-ideas-temporal
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0008-formalize-vicious-cycle-attractor-model
- question:0001-shared-molecular-signature-across-triggers
- theme:0002-temporal-ordering-and-causal-kinetics
created: '2026-07-04'
updated: '2026-07-18'
added_by: explore-ideas:claude-opus-4-8:cand-temporal-domain-failure-sequence
lens_views:
- lens: temporal
  rationale: "Sharpens question:0008 and the causal-priority open question already\
    \ noted in topic:shared-failure-mode-across-pais (which domain deviates first\
    \ is unresolved). Dense longitudinal multi-omics from the first weeks could establish\
    \ causal order — the primary intervention target — and explain cross-trigger\
    \ convergence as different sequence-entry points into a similar cascade. Orthogonal\
    \ to the severity-magnitude and late-divergence framings.\n"
  origin_ref: explore-ideas-temporal
---
# Temporal causal ordering of homeostatic domain failure in the post-acute period

## Summary

The candidate PAIS mechanisms span several homeostatic **domains** — immune activation/inflammation,
autonomic function, metabolic/mitochondrial, gut microbiome, autoimmunity/autoantibody, viral persistence,
endothelial/coagulation. This question asks **which domain deviates *first*** after acute infection, and
whether **dense longitudinal multi-omics sampled from the first weeks** could establish the **causal
sequence** — identifying the primary (most upstream) intervention target and reframing cross-trigger
convergence as **different entry points into a shared cascade** rather than a single fixed origin. It is the
temporal sharpening of `question:0008` and of the "which domain is causally primary" open question in the
shared-failure-mode frame.

The decisive obstacle is a **design mismatch**: the richest PAIS characterizations are **cross-sectional**
(a single snapshot cannot order domains, however deep), while the true longitudinal cohorts are **sparse
(2–3 timepoints), acute-window-only, or single-domain**, and are framed as **prediction** (which early
feature forecasts later PASC) rather than **lead/lag among domains**. No existing dataset combines
early-start + dense sampling + parallel-domain coverage + a formal ordering estimator — which is precisely
the unfilled niche.

## Why It Matters

- **Decision it affects:** *what to intervene on.* If one domain reliably fails first and drives the
  others, it is the primary therapeutic target and the natural anchor for the acute-window prevention
  question (`question:0046`). Ordering is the handle on **driver-vs-consequence** that a cross-sectional
  snapshot cannot provide (`theme:0002`).
- **It could explain cross-trigger convergence mechanistically.** Different pathogens might enter the same
  cascade at **different domains** yet converge on a similar attractor — a concrete, testable reading of
  `hypothesis:0001` / `question:0001` that ordering data could confirm or refute.
- **Risk if unanswered:** the field keeps cataloguing co-occurring abnormalities from single blood draws
  and inferring cascades that are actually **hypothetical** (see Walitt below). Without ordering, every
  domain looks equally "involved," and intervention targeting stays guesswork.

## Current Evidence

**Rich deep-phenotyping of established PAIS is cross-sectional and CANNOT order domains.**

- **PI-ME/CFS deep phenotyping (`paper:Walitt2024`).** The single deepest multi-system characterization
  (50+ modalities). **Estimand:** **cross-sectional**, single deep-phenotyping visit, small N — its
  proposed cascade (infection → immune/microbiome → CNS catecholamine → autonomic → deconditioning) is
  **explicitly hypothetical**, a sequence *inferred from a static snapshot*, not a measured lead/lag. This
  is the exact "however rich, cross-sectional cannot order" case.
- **Long-COVID immune profiling (`cite:Klein2023`).** 275 participants, multidimensional immune phenotyping
  + ML. **Estimand:** **single-timepoint case/control**; associations only, no time axis — cannot order.

**True longitudinal cohorts exist but are sparse, acute-window-only, or single-domain — and framed as
prediction, not domain ordering.**

- **Early acute-phase predictors (`cite:Su2022`).** 309 patients, deep multi-omics at **3 discrete
  timepoints** (diagnosis, acute, 2–3 mo convalescent); four acute-phase factors (type 2 diabetes,
  SARS-CoV-2 RNAemia, EBV viremia, autoantibodies) **anticipate** specific PASC phenotypes. **Estimand:**
  predictor→outcome *association*; sampling is too sparse and stops at 2–3 mo, so it **cannot resolve
  lead/lag among mechanism domains** — it tells us *which early features forecast* PASC, not *which domain
  deviates first*.
- **IMPACC acute trajectories (`cite:DirayArce2023`, `cite:Gabernet2025`).** Serial multi-omic sampling
  across the **first 28 days** from admission (>15,000 samples), and a derived "recovery factor" predicting
  long COVID to 12 months. **Estimand:** genuine within-person **acute** trajectory, but **hospitalized-
  only**, severity-focused, and dense in the acute phase / **sparse post-acute** — predictive, not a
  post-acute domain-ordering design, and generalizability to mild/outpatient PAIS is a caveat.
- **Within-person mild-COVID immune trajectory (`cite:Talla2021`, preprint).** 1–15 d through >100 d.
  **Estimand:** genuine within-person longitudinal, but profiles the **immune compartment only**, so it
  cannot rank *which domain* leads. Preprint — cite cautiously.

**The nearest formal ordering attempt, and the review consensus that ordering is unresolved.**

- **Dynamic Bayesian network on long-COVID data (`cite:PerezChacon2026`).** Applies the *class* of method
  this question calls for (a formal temporal/causal-ordering estimator). **Estimand:** models
  **symptom → organ-dysfunction** structure across timepoints, **not** the multi-omic mechanism domains —
  a framework/proof-of-concept, so it does not itself resolve which molecular domain deviates first. (2026;
  verify at source.)
- **Review framing (`cite:Faghy2026`, `paper:Peluso2024b`).** Mechanisms are catalogued but their
  **temporal/causal sequence is explicitly unresolved**; both call for dense longitudinal, omics-integrated
  sampling. `paper:Peluso2024b`'s upstream/downstream two-tier map is a *conceptual* ordering, not a
  measured one.

**Honest negative.** No published study runs a cross-lagged-panel / Granger / mediation analysis across
**longitudinal PAIS mechanism-domain time series** (immune ↔ autonomic ↔ metabolic ↔ microbiome ↔
endothelial) to infer lead/lag. `cite:PerezChacon2026` is the closest real ordering method but on
symptoms/organ dysfunction, not multi-omic domains. This gap is real and strengthens the question's novelty.

## Thoughts

- **Best current interpretation:** *which homeostatic domain fails first is genuinely unresolved.* Every
  rich characterization of established PAIS is cross-sectional (`paper:Walitt2024`, `cite:Klein2023`) and
  cannot order; the real longitudinal cohorts (`cite:Su2022`; IMPACC `cite:DirayArce2023`/`cite:Gabernet2025`;
  `cite:Talla2021`) are sparse, acute-window-only, or single-domain and answer *prediction*, not *ordering*.
  The methods to do it exist (`cite:PerezChacon2026`) but have not been applied to multi-omic domain data.
- **The discriminating design:** a cohort sampled **from the first weeks**, **densely**, across **all
  candidate domains in parallel**, analyzed with a **formal ordering estimator** (cross-lagged panel /
  dynamic Bayesian network / Granger-type), with severity co-modeled (acute severity co-varies with several
  domains and confounds naive ordering — see `theme:0002` guardrail). That single dataset would serve this
  question **and** the CSD test (`question:0036`).
- **Major remaining uncertainty:** whether a **single** stereotyped domain-failure order exists at all, or
  whether triggers/phenotypes enter the cascade at different domains (the cross-trigger-entry reading) —
  which itself would be a substantive finding, not a failure to find an order.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (cross-trigger convergence as shared
  cascade); `question:0008-formalize-vicious-cycle-attractor-model` (formalizing the cascade makes the
  ordering prediction); `question:0001-shared-molecular-signature-across-triggers` (the cross-trigger
  signature whose *entry point* ordering would explain).
- Required datasets: dense, early-start, parallel-domain longitudinal multi-omics with post-acute follow-up.
  None currently held — list in frontmatter `datasets:` when identified.
- Required analyses: cross-lagged panel / dynamic Bayesian network / Granger-type ordering across domains,
  with acute-severity confounding controlled; mediation of downstream domains by the earliest-deviating one.
- Priority level: **P3** — foundational for intervention targeting but gated behind a dense longitudinal
  multi-domain cohort that does not yet exist.

## Related

- Topic notes: `theme:0002-temporal-ordering-and-causal-kinetics` (ordering hub);
  `topic:shared-failure-mode-across-pais` (the causal-priority open question this sharpens).
- Article notes: `paper:Walitt2024`, `cite:Klein2023` (cross-sectional — cannot order); `cite:Su2022`,
  `cite:DirayArce2023`, `cite:Gabernet2025`, `cite:Talla2021` (longitudinal but sparse/acute/single-domain,
  predictive); `cite:PerezChacon2026` (nearest formal ordering method, on symptoms not domains);
  `cite:Faghy2026`, `paper:Peluso2024b` (order unresolved; dense longitudinal omics needed).
- Methods/Datasets: cross-lagged / dynamic-Bayesian-network domain-ordering on dense longitudinal
  multi-omics — the missing design.
