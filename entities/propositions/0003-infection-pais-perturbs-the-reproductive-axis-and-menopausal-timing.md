---
id: "proposition:0003-infection-pais-perturbs-the-reproductive-axis-and-menopausal-timing"
type: "proposition"
title: "Infection / PAIS perturbs the reproductive (HPG) axis state (reverse direction)"
status: "active"
claim_layer: "causal_effect"
identification_strength: "observational"
proxy_directness: "indirect"
supports_scope: "hypothesis_bundle"
measurement_model:
  observed_entity: "cross-sectional gonadal-steroid levels in PAIS cases vs controls"
  latent_construct: "infection/PAIS-driven perturbation of the reproductive (HPG) axis"
  measurement_relation: "a case-control hormone difference is consistent with axis perturbation but does not time-order it relative to infection"
  known_failure_modes:
    - "cannot distinguish reverse (axis←PAIS) from forward without temporal data"
    - "menopausal status often uncollected, confounding the steroid reading"
    - "surgery-before-CFS timing constrains only surgical menopause, not natural menopause or infection timing"
discusses:
  - frame: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
    role: "rival"
related:
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "question:0013-reproductive-stage-failed-immune-recovery-after-infection"
  - "proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold"
  - "patch-definition:menopause-pais-causal-dag"
source_refs:
  - "paper:Silva2024"
  - "paper:Shahbaz2025"
  - "paper:Boneva2015"
created: "2026-06-21"
updated: "2026-06-26"
---

# Proposition: Infection / PAIS perturbs the reproductive axis and menopausal timing (reverse direction)

## Claim

Acute infection and/or the established PAIS state **perturbs the reproductive (HPG) axis state** — e.g. HPG-axis suppression or altered gonadal-steroid levels. This is the reverse-causal direction (P←) relative to `proposition:0001`. A stronger version — that infection shifts menstrual / menopausal **timing** — remains plausible, but Boneva2015 now constrains a simple blanket version: surgical menopause often preceded CFS onset in the dated subset (`evidence-line:0082`). (The entity slug retains "menopausal-timing" as the eventual scope; the asserted claim is still primarily axis-state.) It is a first-class, evidence-evaluated proposition in its own right; relative to the forward hypothesis `hypothesis:0005` it carries `membership_role: rival` — a competing reading a forward-only model must rule out, not a conjunctive member of that bundle.

## Evidence Summary

The same cross-sectional associations that weakly support `proposition:0001` are **equally consistent with this reverse reading**: lower testosterone in female long-COVID (`paper:Silva2024`, `paper:Shahbaz2025`) could reflect LC-driven HPG-axis suppression rather than low pre-infection hormone predisposing to LC. `paper:Boneva2015` is a weak counterweight only for the surgical-timing subset: hysterectomy/oophorectomy preceded CFS onset in 71% of women with both dates, disputing a simple illness-driven account of that component (`evidence-line:0082`). It does not rule out PAIS-driven hormone-axis perturbation or natural-menopause timing shifts.

## Caveats

Thin and mostly **undistinguished from the forward direction**: the hormone lines do not separate P← from `proposition:0001`, and Boneva2015's temporal handle is surgical rather than natural menopause or infection-indexed. The principled DAG encoding is time-indexed (`menopause_t0 → PAIS`, `PAIS → menopause_t1`) — two ordinary propositions over related endpoints, not a literal cycle (a strict DAG forbids one). The discriminating evidence is temporal: pre-infection hormone/stage measurement (rules toward forward) versus within-person post-infection axis change (rules toward reverse).

## Related Propositions

- `proposition:0001` — the forward effect this is the reverse of; "truth in the middle" is both edges carrying moderate support.
