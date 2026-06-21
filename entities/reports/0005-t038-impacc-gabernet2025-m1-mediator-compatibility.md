---
id: "report:0005-t038-impacc-gabernet2025-m1-mediator-compatibility"
type: "report"
title: "t038: IMPACC (Gabernet2025) androgen-metabolite signal vs h0005 M1 — directionally concordant but underdetermined (no belief update)"
status: "proposed"
source_refs:
  - task:t038
  - paper:Gabernet2025
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways
related:
  - plan:0004-impacc-m1-mediator-compatible-corroboration
  - report:0004-t036-hormone-panel-cohort-feasibility-m1-positive-test
  - proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold
  - proposition:0003-infection-pais-perturbs-the-reproductive-axis-and-menopausal-timing
  - discussion:0001-menopause-timing-pais-rival-models
  - paper:Ozonoff2024
  - paper:Shahbaz2025
  - paper:Silva2024
created: "2026-06-21"
updated: "2026-06-21"
---

# t038: IMPACC (Gabernet2025) androgen-metabolite signal vs h0005 M1

## Scope and verdict

This report executes the **in-scope literature-synthesis portion** of `task:t038` as scoped by
`plan:0004` — assessing whether IMPACC's *already-published* steroid-axis + immune/metabolic mediator
findings are *directionally compatible with* M1's prediction (`proposition:0002`: reproductive-stage /
sex-hormone state modifies immune-regulatory pathways governing post-infectious recovery). It is a
**literature read of a published result; no data were downloaded and no re-analysis was run** (the
fresh SDY1760 / dbGaP phs002686 re-analysis remains post-seed-stage).

> **Verdict: `underdetermined` → no belief update.** The IMPACC signal is **directionally concordant**
> with M1 (androgens lower in long COVID, inflammatory mediators higher), and it is a genuinely
> **independent, subject-disjoint third cohort**. But the androgen and mediator signals **co-load on a
> single *outcome-supervised* latent factor (SPEAR)**, which is co-association *with long COVID* by
> construction, not a demonstrated **within-subject / within-cluster androgen↔mediator relationship**.
> Reading `plan:0004`'s co-variation gate **conservatively given that model class** (see § gate
> interpretation), this is `underdetermined`, recorded as **navigation-only** — and the call is
> **robust to the gate reading**: even taken as a literal *weak-concordant* line, the severity /
> staging / baseline confounders independently withhold the update. `proposition:0002` stays
> single-line fragile; `proposition:0001` and `proposition:0003` are untouched.

## The paper (identity correction)

**`paper:Gabernet2025`** — Gabernet et al. 2025, *J. Clin. Invest.* 135(21):e193698
(DOI 10.1172/JCI193698; **PMC12582403**), "A multiomics recovery factor predicts long COVID in the
IMPACC study." IMPACC convalescent cohort, **n=513** hospitalized COVID-19 survivors (subset of 1,164
enrolled at 20 US hospitals, May 2020–March 2021; pre-Omicron, largely unvaccinated). Multiomics
(plasma metabolomics, PBMC transcriptomics, Olink proteomics, CyTOF) reduced via **SPEAR**, a
*supervised* dimensionality reduction, into a "recovery factor" discriminating minimal-deficit (MIN)
from long-COVID (LC) participants.

> **Provenance fix:** `report:0004` cited the "androgen-metabolite paper" as *"PMC12582403;
> Nat. Commun. s41467-023-44090-5."* That DOI (`10.1038/s41467-023-44090-5`) actually belongs to
> **`paper:Ozonoff2024`** (the IMPACC PRO-phenotype paper, which reports FGF21 / B-cells /
> methylhistidine-acylcarnitine modules — **no androgen metabolites**). PMC12582403 is a **distinct**
> JCI 2025 paper. `report:0004`'s Sources line is corrected accordingly.

## Compatibility comparison

| Axis | M1 prediction (`proposition:0002` / Shahbaz2025 grounding) | Gabernet2025 (IMPACC) finding | Compatible? |
|---|---|---|---|
| Androgen direction | Lower androgen → worse recovery | Androgenic steroids (DHEA-S, epiandrosterone-S, androsterone-S, 5α-androstanediol sulfates) **lower in LC**; 7/12 leading-edge androgenic-steroid metabolites among 26 significant SPEAR analytes | **Yes, directionally** |
| Mediator direction | Lower androgen ↔ higher inflammatory tone | Inflammatory proteins (LRG1, CXCL9, FGF21, CSF1, MMP10, TNFRSF9/11B, IL10RB) **higher in LC** on the same factor | **Yes, directionally** |
| **Androgen↔mediator co-variation (the decisive test)** | Hormone acts **through** immune mediators (mediation / within-unit linkage) | Both sets **co-load on the supervised SPEAR factor**, i.e. both co-associate with the LC outcome. **No mediation, no within-subject androgen-vs-mediator correlation, no within-cluster linkage.** Authors call the mechanistic link "speculative." | **No — co-tracks the outcome, not each other** |
| Reproductive staging | Signal indexed to menopausal transition | **No menopausal-status data;** androgen signal **attenuates when sex-stratified** | **Cannot assess** |
| Reverse-causation control | Pre→post-infection within-person anchor | **No pre-infection baseline;** cross-sectional/convalescent | **Cannot break P3** |

## Why this is `underdetermined`, not a weak supporting line

### Gate interpretation (stated honestly — not back-dated)

`plan:0004`'s `concordant` criterion, **read literally**, admits co-variation "within the *same*
phenotype / module / **model** / subject-stratum," and explicitly disqualifies only *two separate*
long-COVID-association statements. Gabernet's SPEAR recovery factor **is a single model**, so a literal
reading would admit this as a *weak* concordant line. The stricter reading applied here — that
**co-loading on an *outcome-supervised* factor is co-association with the long-COVID outcome by
construction, not the within-unit mutual androgen↔mediator relationship M1's mediation requires** — is
a **conservative execution-time clarification of the gate, made after seeing the model class**, *not* a
criterion literally locked in the plan text. It is recorded as such, not presented as pre-registered.
(The "within-subject / within-cluster" phrasing came from the plan-review discussion, not the committed
plan body, so it is treated here as interpretive guidance, not a locked threshold.)

Why the conservative reading is the right one: a supervised factor selects features *because they
jointly discriminate the outcome*, so two features can co-load without co-varying with *each other*
(they are conditionally associated *through* the outcome). The paper presents **no** bivariate
androgen↔mediator correlation, **no** mediation model, and **no** within-cluster linkage — so the
within-unit relationship M1 needs is not demonstrated; the SPEAR co-loading is a more sophisticated
form of two parallel outcome-associations.

### The verdict does not hinge on that interpretation

Even under the **literal weak-concordant** reading, `plan:0004`'s **genuinely pre-committed cap** holds
— a qualifying line is `weak` and **may not be scored above `evidence-line:0007` (Shahbaz)** — and
three confounders, each independently sufficient to withhold the update, erode even that floor:

- **Hospitalized-severity HPG suppression** — the entire cohort is hospitalized; low androgens are a
  textbook feature of acute critical illness. The authors themselves note testosterone "is often
  reduced in patients with other critical illnesses." This is the rival explanation for the androgen
  signal, unaddressed for the androgen subset specifically.
- **No menopausal status** + **sex-stratified attenuation** — female sex strongly predicts low recovery
  scores; post-menopausal women have physiologically lower DHEA-S, so the LC androgen-low signal could
  be a menopausal-composition confound, and the individual androgenic-steroid score lost significance
  in one or both sexes when split.
- **No pre-infection baseline** — cannot order androgen change relative to infection, so the signal is
  reverse-causation-symmetric (equally consistent with `proposition:0003`).

So under **either** gate reading the disposition is the same: `underdetermined`, **no belief update** —
the strict reading rejects the co-loading as outcome-co-association, and the lenient reading admits at
most a capped `weak` line that the confounders then erode to no usable update.

## Graph disposition

- **`proposition:0002`** — **no evidence-line added.** Caveat updated to record the realized
  triangulation: an independent, subject-disjoint IMPACC cohort is *directionally* concordant but
  **mediator-compatible-only / non-corroborating** for the reasons above; fragility is unchanged and,
  as `report:0004` argued structurally, unfixable from existing data.
- **`proposition:0001` / `proposition:0003`** — untouched (all cross-sectional lines remain
  reverse-causation-symmetric; concordance does not confirm forward direction or refute the reverse
  rival).
- **Independence note (for any future line):** IMPACC subjects are disjoint from Silva2024/Shahbaz2025,
  so a *qualifying* future IMPACC analysis would earn its own independence group — but this read does
  not qualify.

## What would change this verdict

- An IMPACC (or other) analysis demonstrating **within-subject or within-cluster** androgen↔mediator
  co-variation *independent of the LC outcome axis* (e.g. a mediation model, or an androgen-stratified
  mediator contrast within LC) — would convert this from `underdetermined` to a weak supporting line.
- Severity-adjusted re-analysis of the **androgen subset specifically**, showing the androgen-low signal
  survives acute-severity / critical-illness adjustment.
- Menopausal-status or sex-hormone-panel data on the IMPACC biospecimens (an assay step, post-seed-stage
  — overlaps the RECOVER path `task:t040`, not t038).

## Sources

- `paper:Gabernet2025` (PMC12582403; JCI 2025;135(21):e193698) — full text via Europe PMC, 2026-06-21.
- `paper:Ozonoff2024` (Nat. Commun. 2024, s41467-023-44090-5) — the DOI `report:0004` conflated.
- `report:0004` (t036 feasibility, Tier-3 IMPACC assessment) — the path this executes.
- `proposition:0002` / `discussion:0001` §M1 / `paper:Shahbaz2025` — the M1 predictions compared against.
