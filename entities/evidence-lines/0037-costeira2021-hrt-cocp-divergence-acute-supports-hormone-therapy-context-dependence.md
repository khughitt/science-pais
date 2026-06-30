---
id: "evidence-line:0037-costeira2021-hrt-cocp-divergence-acute-supports-hormone-therapy-context-dependence"
type: "evidence-line"
title: "Costeira2021 within-study HRT↑ / COCP↓ divergence (acute COVID, predicted outcome) weakly supports hormone-therapy context-dependence"
status: "active"
stance: "supports"
target: "proposition:0006-hormone-therapy-effects-on-pais-are-context-dependent"
source: "paper:Costeira2021"
strength: "weak"
independence: "independent"
independence_group: "costeira2021-css-cohort"
evidence_role: "proxy_support"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0006-hormone-therapy-effects-on-pais-are-context-dependent"
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "topic:menopause-sex-hormones-and-pais-risk"
  - "task:t019"
source_refs:
  - "paper:Costeira2021"
created: "2026-06-23"
updated: "2026-06-23"
---

# Evidence Line: Costeira2021 — HRT/COCP divergence (acute, predicted) weakly supports hormone-therapy context-dependence

## What this line shows

In one large within-study comparison (UK COVID Symptom Study app: n=151,193 menopausal women for
HRT, n=295,689 for combined oral contraceptive pill), the two exogenous-estrogen exposures point in
**opposite directions** on the same outcome: HRT use was associated with **higher** predicted COVID-19
(OR 1.32, 95% CI 1.16–1.49) while COCP use was associated with **lower** predicted COVID-19 (OR 0.87,
0.81–0.93) and lower hospitalization (OR 0.79, 0.64–0.97). The HRT signal did **not** carry through to
hospitalization, and tested-positivity / respiratory-support endpoints trended negative but were
non-significant. That two estrogen-containing therapies diverge in sign — and that the HRT signal is
endpoint-dependent — is a concrete instance of `proposition:0006`'s claim that exogenous-hormone-therapy
effects are **not uniformly protective or harmful** but contingent on the exposure's route, dose,
timing, indication, and the population it is prescribed to [@Costeira2021].

## Why it is independent

`independence_group: costeira2021-css-cohort` — the COVID Symptom Study app cohort, distinct from the
mechanism-review line (`evidence-line:0014`, `averyanova-mech`). These are the only two lines on
`proposition:0006`; no shared-cohort double-count arises.

## Caveats / scope

`proxy_support`, **weak**, and load-bearing-confounded. This is an **acute-COVID** observation on a
**symptom-predicted** (not tested) outcome, so it is at best a proxy for any post-acute / PAIS hormone-
therapy effect — the transport gap to PAIS is unbridged. The HRT↑ signal is **consistent with** the
artifact the proposition warns about: HRT users are, by indication, symptomatic menopausal women, so a
symptom-model–predicted outcome is **vulnerable to** inflation from the menopause↔COVID symptom overlap
in precisely that group (indication + ascertainment confounding) — a bias pathway Costeira2021 does not
itself identify, measure, or rule out. HRT **type, route, dose, duration, and indication were
unavailable**, so the within-study divergence demonstrates heterogeneity *exists* without identifying
which dimension drives it. The line therefore supports the **non-uniformity / context-dependence**
content of `proposition:0006` only; it provides **no** admissible estimate of an HRT→PAIS effect's
sign or magnitude [@Costeira2021]. See `interpretation:0008` (t019 audit) for the full disposition.
