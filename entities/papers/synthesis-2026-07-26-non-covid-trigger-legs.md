---
id: paper:synthesis-2026-07-26-non-covid-trigger-legs
kind: paper
title: 'Cross-paper synthesis (2026-07-26): the four non-COVID trigger legs of the cross-trigger
  convergence claim are weaker and more phenotype-heterogeneous than the signature matrix records'
status: active
paper_kind: review
ontology_terms:
- post-acute infection syndrome
- cross-trigger convergence
- post-mononucleosis fatigue
- post-chikungunya chronic inflammatory joint disease
- post-Ebola syndrome
- myalgic encephalomyelitis/chronic fatigue syndrome
- phenotype heterogeneity
- evidence provenance
- head-to-head design
dataset_usage: []
source_refs:
- cite:Broderick2012
- cite:Ramundo2025
- cite:Sanford2026
- cite:Watton2026
related:
- paper:Broderick2012
- paper:Ramundo2025
- paper:Sanford2026
- paper:Watton2026
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune
- spec:0001-scope-boundaries-for-health-post-acute-infection
- question:0001-shared-molecular-signature-across-triggers
- question:0091-post-ebola-metabolic-signature-hc-controlled
- question:0092-arthralgia-vs-fatigue-pais-phenotype-attractor
- search:0002-cross-pathogen-pais-signatures
- discussion:0002-cross-pathogen-pais-signature-convergence
created: '2026-07-26'
updated: '2026-07-26'
---
# Cross-paper synthesis (2026-07-26): the four non-COVID trigger legs are weaker than the matrix records

## Scope of this synthesis

These four papers were promoted from `status: stub` to full summaries under `task:t130`. They were
seeded together for one reason: `search:0002` and `discussion:0002` cite them to grade the
**non-COVID trigger legs** of the cross-trigger convergence claim that feeds
`hypothesis:0001-shared-dysregulated-attractor`. Until now those gradings rested on entities with
no summary body — the papers had been catalogued, not read.

Each paper was read independently and in isolation. This synthesis records what only becomes
visible with all four in view at once.

## Headline

**Two of the four legs are materially weaker than the signature matrix currently states — but for
different reasons, and only one of the two is a comparator problem.** The matrix grades cells by
*whether a molecular signature exists*. It records neither the study-level provenance of that
signature (analytic N, validation type, confounding) nor which phenotype was ascertained. This is
adjudicated by **D-010**: primary scope follows infection × persistence, while evidential
admissibility for convergence additionally follows **phenotype × comparator × measurement**.

| Leg | Matrix grading | What reading the paper shows | Net |
|---|---|---|---|
| Post-EBV cytokine (`Broderick2012`) | `supported` | Comparator is **appropriate**; analytic n=9 vs n=12, resubstitution classifier, no external validation, all-female cases vs unstated-sex controls | **weaker than recorded — power/validation/confounding** |
| Post-Ebola metabolomic (`Sanford2026`) | Thin-but-present | Healthy contacts **were** tested; the signature **did not survive** that contrast | **weaker than recorded — comparator** |
| Post-chikungunya (`Ramundo2025`) | Moderate, arthralgia-dominant | Accurate; strong prospective design, joint-specific downstream biology | confirms |
| Convergence claim (`Watton2026`) | CLAIM, not evidence | Confirmed: assembled single-disease synthesis, no head-to-head design | confirms |

## Finding 1 — Only one leg has a comparator problem, and it is not the one with the small N

An earlier draft of this synthesis grouped `Broderick2012` and `Sanford2026` together as "not
contrasted against healthy controls". That conflation is wrong and is corrected here.

**Recovered same-trigger controls are not intrinsically a weak comparator.** `question:0001` asks
for a signature that is *simultaneously* shared across triggers **and** specific to failed recovery
versus full recovery. For that second conjunct, `Broderick2012`'s recovered post-mononucleosis
controls are **exactly the right comparison group** — arguably better than healthy controls, since
they hold the trigger, the timepoint, and the cohort constant. Scoring this design as
comparator-deficient would penalize the very contrast the project needs.

`Broderick2012`'s weaknesses lie elsewhere, and they are substantial:

- The 301-adolescent figure is the **cohort**; the cytokine comparison is **n=9 PI-CFS vs n=12
  recovered** (only 9 of 13 24-month cases had banked plasma).
- The 5-cytokine classifier's 94% / 88% performance is a **resubstitution estimate** — trained and
  evaluated on the same 21 samples, no held-out set, no cross-validation.
- **Possible sex confounding**: all 9 PI-CFS cases are female; the sex composition of the 12
  recovered controls is not stated. If the controls include males, sex effects and CFS effects are
  entangled in a cytokine panel that sex is known to modulate.
- Standing tension with the Dubbo negative (Vollmer-Conna 2007).

**`Sanford2026` is the sharper case, and the distinction matters.** Healthy uninfected household
contacts *were* enrolled and tested (n=20). The 34-metabolite signature separates PES survivors
(n=37) from asymptomatic EVD survivors (n=20), but **did not reach significance against the healthy
contacts**. This is not a missing comparator — it is a positive signature that disappeared in the
contrast that would have made it a post-infectious-versus-healthy finding. The authors attribute
the null to sample size; the alternative reading — that all EVD survivors carry a metabolic
alteration, with PES an amplification — is not excluded.

## Finding 2 — The phenotype drifts leg by leg, which bears on h0012, not h0001

Per **D-010**, this must be routed to the right hypothesis. `hypothesis:0001` is a broad,
**heterogeneously realized** immune-state-displacement claim that explicitly does *not* require
every PAIS subtype to share one analyte, gene module, or cytokine hub. The explicitly
fatigue/cognitive common-path claim is `hypothesis:0012`. A phenotype mismatch is therefore
evidence about **h0012**, and reporting it as weakening **h0001** would misstate what h0001 claims.

What was actually ascertained:

- `Broderick2012` — Fukuda 1994 CFS. Fatigue phenotype; **PEM not required** by the case definition.
- `Ramundo2025` — persistent joint symptoms **plus ultrasound-confirmed synovitis** at Day 90.
  Arthralgia phenotype, objectively verified.
- `Sanford2026` — exam-confirmed **musculoskeletal/GI or cardiopulmonary** sequelae. No fatigue,
  cognitive, or PEM instrument administered.

So of the three primary-data legs, exactly one ascertains a fatigue phenotype, and that one does
not require PEM. Note carefully: for Ramundo and Sanford the fatigue phenotype is
**unmeasured, not absent** — D-010 holds those cells *indeterminate*, not negative. Neither paper
licenses a claim that post-chikungunya or post-Ebola patients lack fatigue; both merely fail to
supply fatigue/PEM convergence evidence.

The asymmetry in rigor runs *opposite* to the phenotype match: `Ramundo2025` has by far the
strongest design of the three (prospective, pre-outcome sampling, objective endpoint) and the
weakest phenotype match, while the fatigue-phenotype leg is the smallest and least validated.
`question:0092` carries this forward.

## Finding 3 — The convergence review is confirmed as assembled, not head-to-head

`search:0002` already classified `Watton2026` as a convergence *claim* rather than *evidence*,
alongside Komaroff2023/2025 and Trautmann2025. Reading it confirms that classification rather than
revising it: the unified model is built on ME/CFS-specific primary data with long COVID adduced by
pattern-matching, and no section presents patients from two or more triggers measured on a common
platform. Its scope does not reach PTLDS, post-dengue, QFS, or post-Ebola at all.

This is a case where the project's prior suspicion was correct and is now verified rather than
merely suspected. `Watton2026` also aligns with **D-002** — it endorses the evidence base behind
the 2021 NICE reversal on GET and recommends individualised pacing, so there is no tension to
manage there.

## Finding 4 — Ramundo2025 supplies genuine upstream read-across

The one leg that strengthens on reading does so on an axis the matrix does not have a column for.
`Ramundo2025` finds that *early antiviral immune impairment* — down-regulated LIFR and ZBTB16,
suppressed neutrophil degranulation and MHC-class-I antigen presentation, sampled **before** the
Day-90 outcome — predicts who becomes chronic. That upstream mechanism (immune failure permitting
viral persistence) is directly relevant to `hypothesis:0002`'s antigen-persistence axis, even
though the downstream failure mode is joint tissue rather than neuro-immune-autonomic.

The paper also proposes an estradiol-responsive `miR-98-5p → LIFR` axis as a mechanism for female
predominance (86% female in the chronic group), which touches the project's sex-modifier line
without being derived from it.

## Disposition under D-010

| Paper | Primary scope | Admissible as | Not admissible as |
|---|---|---|---|
| `Ramundo2025` | **In** (infection × persistence pass) | Upstream immune-clearance / viral-persistence read-across | Fatigue/PEM convergence evidence; `h0012` support; discriminating evidence for `h0001` |
| `Sanford2026` | **In** (infection × persistence pass) | Post-Ebola molecular presence, survivor-internal | Fatigue/PEM convergence evidence; `h0012` support; discriminating evidence for `h0001` |
| `Broderick2012` | **In** | Failed-vs-full-recovery contrast within the EBV trigger | A validated biomarker panel; a strong cell on its own |
| `Watton2026` | n/a (review) | Convergence **claim**; mechanistic map; D-002-aligned pacing position | Independent convergence **evidence** |

For the broad `hypothesis:0001`, Ramundo and Sanford are **contextual but non-discriminating**
until a shared state is actually measured across an arthralgia-dominant and a fatigue-dominant
trigger on one platform.

## What this does and does not change

**Does not change:** `hypothesis:0001` is not refuted, nor is it narrowed to a fatigue-only claim.
Nothing here is a head-to-head test, so nothing here can refute a convergence claim any more than
it can establish one. Ramundo's upstream finding is genuinely valuable — it simply cannot be
promoted to evidence of a shared *downstream* attractor (D-010).

**Does change:** the honest statement of the *breadth* of support. The project's own summary in
`search:0002` — "convergence is robust at the level of biological domains but the molecular cells
that prove it are overwhelmingly assembled from separate single-trigger studies" — survives intact,
but the assembled cells are individually thinner than their labels imply, and one of them
(post-Ebola) failed the healthy-control contrast it actually ran.

The decisive test named in `search:0002` — harmonized multi-omics across ≥3 fatigue-phenotype
triggers with full-recovery controls — remains non-existent, and this reading makes the "≥3
fatigue-phenotype" qualifier harder to satisfy than the trigger count suggests: post-chikungunya
and post-Ebola supply no *measured* fatigue-phenotype cells.

## Follow-ups raised

- `question:0091` — does the post-Ebola metabolic signature extend to a fatigue-phenotype PES
  cohort and replicate against uninfected controls?
- `question:0092` — do arthralgia-dominant and fatigue-dominant post-infectious phenotypes converge
  on one attractor, or share only an upstream cause?
- **`task:t145`** — the matrix cannot express study-level provenance. A companion **provenance
  ledger** (phenotype/case definition, comparator, assay, analytic N, validation type, design
  provenance) fits better than one extra column, because these dimensions vary independently per
  cell. t145 also carries a **stale contradiction**: `search:0002` still describes `Galbraith2011`
  as partial/shared in several places, while `discussion:0002`, `question:0001`, and
  `hypothesis:0001` all correctly record it as a head-to-head **negative** with no genes consistent
  across all three triggers.
