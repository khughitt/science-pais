---
id: proposition:0013-immune-domain-partial-hormone-mediated-objective-exception
type: proposition
title: The immune/inflammatory domain is a partial, testosterone-conditioned objective exception
  to the self-report-channeled female PAIS excess
status: active
claim_layer: empirical_regularity
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- frame: hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  role: background
related:
- question:0007-mechanism-of-female-predominance-in-pais
- interpretation:0003-t018-subphenotype-sex-reproductive-stage
- interpretation:0006-t041-objective-female-biased-subphenotype-search
- proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified
- proposition:0010-cognitive-female-excess-is-self-report-only-absent-in-objective-testing
- proposition:0005-menopause-pais-symptom-overlap-is-a-measurement-process
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- task:t041
source_refs:
- paper:Aid2025
- paper:Shahbaz2025
- paper:Silva2024
created: '2026-06-23'
updated: '2026-06-23'
---
# Proposition: The immune/inflammatory domain is a partial, testosterone-conditioned objective exception to the self-report-channeled female PAIS excess

## Claim

Across PAIS subphenotypes the female excess is overwhelmingly carried by **self-report /
ascertainment channels** (fatigue, pain, mood, subjective cognition, recovery-time) and is
**absent or reversed** in objectively-measured domains (objective cognition sex-null; hard
vascular/thrombotic endpoints male-biased). The **immune/inflammatory domain is the one objective
exception**: a sex-symmetrically-assayed endpoint — **persistent post-acute pro-inflammatory
activation** — is **female-amplified**, i.e. elevated in long-COVID **females relative to recovered
females** by *more* than the corresponding male contrast, with the female excess **absent within
the recovered control group at detectable levels** (the discriminating interaction control). This makes the domain a
genuine `empirical_regularity`-level exception to a *strong universal* "every objective domain is
sex-null or male-biased" reading. **However**, the signal is **strongly testosterone-conditioned
rather than cleanly categorical-sex-driven** (in the best-powered cohort, after adjusting for
testosterone, sex is no longer a significant predictor of symptom burden or organ-system
involvement), so it points to a **hormone-linked biological channel**, not a categorical-sex
amplification — and it is
**reverse-causation-ambiguous** (cross-sectional; chronic inflammation may suppress the HPG axis).
The claim is therefore a **weak-to-moderate** objective exception, not a clean positive.

## Evidence Summary

All `literature_evidence`; the discriminating design is **within-sex case-control** (LC-females vs
recovered-females, LC-males vs recovered-males), not LC-females-vs-LC-males (which would confound the
higher female baseline antibody/Th2/T-activation immunity).

- **Within-sex interaction control (the strongest available design)** — Aid2025 (multi-omic, two cohorts
  n≈142+38) finds stronger inflammatory-pathway enrichment (JAK-STAT/IL-6/IFN/complement) in
  LC-females-vs-recovered-females than in the male contrast, and — critically — reports **no
  significant sex difference within the recovered control group**. The within-recovered null is the
  control that argues against simple carried-through baseline female immunity, while remaining
  underpowered for excluding all baseline-carry explanations.
  See `evidence-line:0033`.
- **Directly-measured cytokines, within-sex design** — Shahbaz2025 (long COVID meeting CCC ME/CFS
  criteria, n=140, ~74% female) finds broad multiplex pro-inflammatory cytokine, gut-barrier
  (I-FABP, LPS-BP, sCD14), and Treg-depletion elevations in the LC-female-vs-recovered-female
  contrast that are weaker or not seen in the male contrast, while both sexes share the cortisol drop
  and terminal-effector T expansion. A second, independent cohort corroborating the female-amplified
  inflammatory direction with directly assayed analytes (not only pathway enrichment). See
  `evidence-line:0034`.
- **Female immune signature + the testosterone bound** — Silva2024 (MY-LC, n=165) identifies a
  distinct female LC immune signature (exhausted/cytokine-secreting T cells, EBV/CMV/HSV-2 antibody
  reactivity; Female-LCIS AUC 0.88) — supporting the female *direction* — **but** shows the operative
  variable is **testosterone level**: lower-testosterone females look immunologically like LC-males,
  and in a model including sex × testosterone, **after accounting for testosterone, sex designation
  is no longer a significant predictor** of symptom burden. This line simultaneously supports the
  female-biased objective immune signal and supplies the testosterone-conditioning caveat that bounds it
  (and ties the exception to the `hypothesis:0005` HPG-axis story and the testosterone work in
  `paper:Silva2024` / t032 / t036). See `evidence-line:0035`.

## Caveats

`empirical_regularity` / `background` role for `hypothesis:0005`: this locates the **one objective
domain where the female excess is not confined to self-report**, and reframes it as a candidate
**hormone-linked** rather than purely ascertainment-driven channel. Bounding conditions:

1. **Testosterone conditioning collapses the categorical-sex reading.** Silva2024's testosterone-adjusted
   null means the "female-biased objective immune endpoint" is better read as a **low-testosterone /
   HPG-dysregulation endpoint** that is *partly* sex-linked (women have lower baseline testosterone),
   not a categorical-sex amplification. This is consistent with — not a refutation of — a mechanism
   in which sex acts *through* gonadal steroids.
2. **Reverse causation is unresolved.** Every line is cross-sectional ~12 months post-infection;
   chronic inflammation can suppress the HPG axis, so low testosterone + high inflammation in
   LC-females may be a *consequence* of the post-acute state rather than a sex-amplification of it.
   No pre-infection-baseline longitudinal design exists.
3. **Secondary-analysis power.** The within-sex sex stratification is a secondary analysis in each
   cohort (e.g. Aid2025 female-LC n≈29 / recovered-F n≈14); the authors themselves flag the need for
   confirmation in larger studies. The reduced-cytotoxicity (NK/CD8) female pattern that points the
   same direction (Silva2024; bioRxiv 2024) is largely **non-significant**.
4. **The classic objective ME/CFS endpoint is a GAP, not a null.** NK-cell cytotoxicity — the
   best-replicated objective ME/CFS functional deficit — is essentially **never sex-stratified**;
   muscle-OXPHOS day-2 worsening (Appelman2024) likewise. These are the highest-value untested
   endpoints; the "objective immune domain is female-biased" reading rests on inflammatory-activation
   analytes, not on the functional-cytotoxicity endpoint.
5. **Walitt2024 shows the immune biology is sex-*dimorphic*, not simply female-amplified** (female
   LC = B-cell-proliferation enrichment; male = T-cell/NF-κB; <5% gene overlap), complicating any
   one-dimensional "more disease in females" reading and cautioning that the exception is
   qualitative as much as quantitative.
6. **Scope of what this disputes.** It does **not** dispute `proposition:0009` (dysautonomia
   baseline-carried — the autonomic/exercise domain was re-checked sex-null) or `proposition:0010`
   (cognitive self-report-only). It disputes only the *strong universal* form of the
   measurement-channel umbrella, which was deliberately **held back unminted** in
   `interpretation:0003`; t041 prevents that strong form from being minted and substitutes this
   bounded, hormone-linked exception (`interpretation:0006`).
