---
id: interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis
type: interpretation
title: "Metric-harmonization re-analysis of cross-PAIS skin-biopsy SFN prevalence — the QASAT-vs-≤5th-percentile cutoff explains LESS of the Oaklander/Joseph/Walitt/Novak scatter than assumed; modality breadth (sensory→autonomic→functional), trigger (LC>ME/CFS), and cohort referral-enrichment are the dominant drivers, and within-trigger the corpus is more concordant than the raw range suggests"
status: active
source_refs: []
related:
- proposition:0014-pais-small-fiber-structural-lesion-ienfd
- proposition:0017-pais-sfn-cross-trigger-convergence
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- question:0004-convergent-small-fiber-neuropathy-substrate
- pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls
- topic:measurement-ascertainment-artifacts-in-pais
- paper:Oaklander2022
- paper:Joseph2021
- paper:Walitt2024
- paper:Novak2026
- interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat
- task:t050
created: '2026-06-24'
updated: '2026-06-24'
input: []
prior_interpretations: []
relations:
- predicate: "sci:amends"
  target: interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat
---

# Interpretation: Metric-harmonization re-analysis of cross-PAIS skin-biopsy SFN prevalence

## Verdict

**Verdict:** [~] Partial and reframed. The premise — that **QASAT-vs-≤5th-percentile scoring** explains
the heterogeneous skin-biopsy SFN prevalence across Oaklander2022 / Joseph2021 / Walitt2024 / Novak2026
(`interpretation:0013` New Question 3) — is **only weakly supported, and is not the dominant driver**.
Re-reading the four studies' methods against their reported rates shows the *cutoff rule* contributes
surprisingly little: Novak2026's QASAT-graded **ENFD-only** rates (LC 48.3%, ME/CFS 33.5%) sit right
next to Joseph2021's strict **≤5th-percentile distal** rate (ME/CFS 31%). The large prevalence
inflation comes instead from **modality breadth** (counting sweat-gland SGNFD and functional ESC, not
just sensory ENFD), from **trigger** (LC > ME/CFS), and from **cohort referral-enrichment** (the most
parsimonious explanation for the Walitt2024 null). Critically, **the referral/enriched biopsy cohorts are
far more concordant within trigger than the raw 0%→91% range implies** — much of the apparent
"heterogeneity" is an artifact of pooling different triggers and different abnormality definitions into
one number. This does **not** weaken `proposition:0014` (lesion existence) in enriched/autonomic PAIS
cohorts, but it preserves Walitt2024 as a real counterexample to universality: the *presence of a
substantial lesion-positive subset* is supported, while the *magnitude and generality* are
metric/trigger/cohort-sensitive.

## Findings Summary

A re-analysis (no new external evidence; a methods-vs-rates re-reading of four corpus papers). The
SFN-biopsy prevalence figures, decomposed by **trigger × cohort × site × scoring rule**:

| Study | Trigger | Cohort selection | Site(s) | Scoring rule | SFN prevalence | n |
|---|---|---|---|---|---|---|
| Oaklander2022 | Long COVID | neuropathy-referral (enriched) | paired distal + proximal | clinical "pathologically confirmed" (lab/cutoff unspecified) | 62.5% distal / 50% proximal | 17 |
| Novak2026 (LC arm) | Long COVID | autonomic-lab referral | paired calf + thigh | QASAT > 0 (age/sex-adjusted) | 48.3% ENFD / 67.2% any-morphological / 91.4% +functional ESC | 143 |
| Joseph2021 | ME/CFS | iCPET referral | distal-only | ≤5th-percentile (sex/age/race-adjusted) | 31% | 160 |
| Novak2026 (ME/CFS arm) | ME/CFS | autonomic-lab referral | paired calf + thigh | QASAT > 0 | 33.5% ENFD / 52.6% any-morphological / 82.9% +functional ESC | 170 |
| Walitt2024 | PI-ME/CFS | adjudicated, **not** neuropathy-referred | distal (NIH protocol) | nerve-fiber-density group difference vs HC | **null** (no difference) | 17 |

Three findings fall out:

1. **The cutoff rule (QASAT > 0 vs ≤5th-percentile) is a *minor* driver.** Novak's QASAT-graded
   ENFD-only rate for ME/CFS (33.5%) is within noise of Joseph's strict ≤5th-percentile distal rate
   (31%), despite different metric, site protocol, and cohort. Whatever the field assumed about QASAT
   inflating prevalence relative to the percentile cutoff, *for the sensory-ENFD channel it barely
   moves the number.*

2. **Modality breadth is the *large* within-cohort driver — demonstrated on identical patients.**
   Within Novak2026's single LC cohort, the SFN rate climbs **48.3% → 67.2% → 91.4%** purely by
   widening the abnormality definition from sensory ENFD only → any morphological (ENFD *or*
   sweat-gland SGNFD) → including functional ESC. Same patients, same biopsy, same lab: a >40-point
   swing generated entirely by *what you count as SFN*. This is the cleanest possible demonstration of
   the measurement-channel thesis, and it isolates the driver as **modality breadth, not percentile
   cutoff.**

3. **Within trigger the enriched-biopsy corpus is concordant; the raw scatter is partly a pooling artifact.** For **Long
   COVID**, Oaklander (50–63%) and Novak's morphological rate (67%) agree closely. For **ME/CFS**,
   Joseph (31%) and Novak's ENFD rate (33.5%) agree closely within referral/enriched cohorts, while
   Walitt2024 remains an adjudicated non-neuropathy-referred counterexample. The "0%→91%" spread that
   looked like irreconcilable heterogeneity is mostly (a) lumping LC with ME/CFS — Novak's own single
   protocol shows LC > ME/CFS for ENFD (48.3% vs 33.5%, p = 0.021), a *genuine trigger effect* — (b)
   comparing a sensory-ENFD number from one study to a sensory+autonomic+functional composite from
   another, and (c) mixing referral-enriched cohorts with an adjudicated deep-phenotyping cohort not
   selected for neuropathy.

## Evidence Quality

- **Re-analysis, not new data.** This is a methods-harmonization read of four existing summaries; it
  introduces no new evidence-line and changes no belief band. Its force is in re-partitioning variance
  the corpus already contains.
- **Strongest internal evidence is within-cohort** (Novak's 48→67→91 ladder) — immune to between-study
  confounds, since it is one cohort re-scored under three definitions.
- **The cross-study near-identities** (Joseph 31% ≈ Novak ENFD 33.5%; Oaklander 50–63% ≈ Novak morph
  67%) are *suggestive but confounded* — different cohorts, sites, and labs. QASAT > 0 is in principle
  more inclusive than a strict ≤5th-percentile count, so the near-identity with Joseph could be partly
  coincidental; only individual-patient-data re-scoring at a common cutoff and site could confirm the
  cutoff rule's small contribution. The *direction* (cutoff contributes less than modality breadth) is
  nonetheless well-supported by the within-Novak ladder alone.

## Data Quality Checks

No data quality concerns identified in the re-analysis itself. Two ascertainment hazards are *the
subject* of the analysis rather than defects in it: (a) **referral enrichment** — Oaklander, Joseph,
and Novak all draw from neuropathy/autonomic referral streams that enrich for SFN, whereas Walitt's
adjudicated cohort was not neuropathy-referred, which is the most parsimonious explanation for its
null; (b) **trigger pooling** — three of the four studies mix or differ in trigger, so any single
"PAIS SFN prevalence" figure silently averages a real LC>ME/CFS gradient. Novak and Joseph's controls
are clean 0% comparators by design/selection; Oaklander lacks controls; and Walitt is the important
exception, showing that the direction-vs-control inference is not universal outside neuropathy/autonomic
referral streams.

## Proposition-Level Updates

- **`proposition:0014` (P1, structural lesion) — unweakened; precision added.** The lesion is present
  above control rates under *every* metric in *every* PAIS arm; the re-analysis converts the alarming
  prevalence scatter into an orderly trigger × modality table. The supporting evidence-lines
  (`0038` Oaklander, `0063` Novak) carry their metric caveats correctly; this interpretation records
  that the caveat is specifically about **absolute magnitude under modality breadth**, not about
  whether the lesion exists.
- **`proposition:0017` (P4, cross-trigger convergence) — refined.** Convergence survives, but the
  re-analysis quantifies a *real, non-artifactual trigger gradient* riding on top of it: LC > ME/CFS
  for sensory ENFD within Novak's single protocol (48.3% vs 33.5%, p = 0.021). Cross-trigger
  convergence is therefore "same substrate, trigger-graded severity," not "identical rates."
- **`proposition:0015` (P2, non-length-dependent pattern) — untouched here**, but see Updated
  Priorities: the re-analysis *validates the pre-reg's design choice* of a within-subject pattern
  metric, which sidesteps exactly the absolute-prevalence confound this analysis exposes.

## Hypothesis-Level Implications

For **`hypothesis:0007`** (candidate): the re-analysis is net-stabilizing. It defuses what could have
read as a credibility problem (wildly inconsistent SFN prevalence) by showing much of the inconsistency
is definitional and trigger-pooling, not a fatal contradiction in the bounded subset lesion claim. P1's
evidence base is more coherent after harmonization, while Walitt remains the adjudicated non-referral
counterweight that prevents a universal-lesion reading. No promotion implication — criterion
#1 still requires the `pre-registration:0003` G2 vehicle. The substantive lesson for the hypothesis is
methodological: **all future SFN-prevalence claims must state trigger, biopsy modality counted
(ENFD / SGNFD / functional), site protocol, and cutoff rule**, because absolute prevalence is
dominated by those four choices.

## Evidence vs. Open Questions

- **Addresses `interpretation:0013` New Question 3** ("Does QASAT-vs-percentile scoring reconcile the
  heterogeneous LC SFN prevalence?") — **answered, with a reframe**: the cutoff rule is a minor
  contributor; the heterogeneity is reconciled instead by modality breadth + trigger + cohort
  selection, and for LC specifically the two corpus studies already agree (~50–67%).
- **Sharpens `question:0004`** (convergent SFN substrate, distinctness from primary dysautonomia): the
  discriminating study must hold trigger, biopsy modality, site, *and* cutoff fixed across arms, or
  any PAIS-vs-comparator prevalence gap is confounded by these four axes before biology enters.
- **Does not touch** the autoimmune-causation leg (P3/`0016`/`0018`) or the anti-GPCR route.

## New Questions Raised

1. **(P2, methods)** Does the QASAT > 0 rule actually diverge from a ≤5th-percentile count when applied
   to the *same* ENFD distribution, or do they coincide for sensory ENFD? Resolvable only by IPD
   re-scoring of one cohort under both rules — would confirm or refute Finding 1's "cutoff contributes
   little" claim. Priority: medium; type: measurement-harmonization.
2. **(P4, biology)** Is the LC > ME/CFS ENFD gradient (Novak p = 0.021) a trigger effect or a
   chronicity/duration effect (Novak's ME/CFS arm had ~10 yr symptom duration vs LC ~1.9 yr)? Severity
   could regress, or denervation could accrue, with time-since-onset. Priority: medium.
3. **(ascertainment)** Would Walitt2024's null survive a neuropathy-symptom-enriched re-sampling of the
   same adjudicated cohort, or is the null purely a referral-stream artifact? This is the decisive test
   of whether the Walitt outlier is biology or ascertainment. Priority: low (no access to re-sample).

## User Questions

The user directed this thread ("look into the first suggested follow-up: a metric-harmonization
re-analysis"). The substantive answer returned: **the QASAT-vs-≤5th-percentile cutoff is *not* the main
explanation** — modality breadth (decisively, within Novak: 48→67→91% on identical patients), trigger
(LC>ME/CFS), and cohort referral-enrichment (the Walitt null) are; and within trigger the corpus is
already concordant.

## Limitations & Residual Uncertainty

- The harmonization rests on **summarized prevalence figures and methods descriptions**, not on
  individual-patient densities. The strongest claim (cutoff rule contributes little) is anchored by one
  within-cohort ladder (Novak) plus one confounded cross-study near-identity (Joseph≈Novak-ENFD); a
  true IPD re-scoring at a common cutoff/site is not available in the corpus.
- **Walitt2024's biopsy site and exact cutoff** are reported in the entity as a null on "nerve-fiber
  density" without a stated per-site/percentile breakdown; its placement as "distal, strict, group
  difference" is inferred from the NIH deep-phenotyping protocol, not verified line-by-line. The null's
  attribution to cohort selection is the most parsimonious reading but not the only one.
- Trigger, site, cutoff, and cohort are **collinear across these four studies** — the re-analysis can
  show modality breadth is a large driver (within-cohort) and that within-trigger concordance is high,
  but it cannot fully orthogonalize the between-study axes. That orthogonalization is exactly what
  `pre-registration:0003`'s single-protocol multi-arm design exists to deliver.

## Updated Priorities

1. **Adopt a corpus convention** (extend `topic:measurement-ascertainment-artifacts-in-pais`): every
   SFN-prevalence claim states *trigger + modality counted + site protocol + cutoff rule*. Absolute SFN
   prevalence without these four is uninterpretable.
2. **Record a design-validation note on `pre-registration:0003`:** its headline P2 test is a
   *within-subject proximal:distal pattern* contrast, which is structurally **less vulnerable to the
   absolute-prevalence confound** this re-analysis exposes because it fixes site, modality, norms, and
   arm protocol before classifying each lesion-positive subject's distribution. This is a positive
   reason the pre-reg's per-subject NLD-classification design is the right instrument — stronger than a
   between-study prevalence comparison could ever be — but it still depends on pre-specifying which
   structural modalities enter the lesion-positive set.
3. **Carry the LC>ME/CFS trigger gradient** (Novak p = 0.021) forward as a *real* signal, not noise, in
   any future cross-trigger convergence claim (P4).
4. No new task required; this closes `interpretation:0013` NQ3. t050 remains blocked on the G2 vehicle.
