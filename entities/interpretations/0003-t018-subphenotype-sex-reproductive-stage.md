---
id: interpretation:0003-t018-subphenotype-sex-reproductive-stage
type: interpretation
title: 'Subphenotype decomposition of the PAIS female / reproductive-stage excess:
  the excess is subphenotype-dependent and tracks a measurement-channel axis, and is
  not shown to be menopausal-status-driven'
status: active
source_refs: &id001
- dataset:sylvester-2022-longcovid-sex
- dataset:dengue-postinfective-fatigue-meta
- paper:Shah2025
- paper:Costeira2021
- paper:Stewart2024
- paper:Gusinow2026
- paper:Ursini2023
- paper:Kwan2022
- paper:Eldokla2022
- paper:Wang2026c
- paper:DelgadoAlonso2023
- paper:Bland2024
- paper:Cheetham2023
related:
- question:0007-mechanism-of-female-predominance-in-pais
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold
- proposition:0005-menopause-pais-symptom-overlap-is-a-measurement-process
- proposition:0008-female-excess-concentrates-in-post-acute-persistence
- interpretation:0002-t013-cross-trigger-sex-effect-sizes
- question:0018-objective-vs-subjective-cognition-dissociation-in
- task:t018
- task:t013
created: '2026-06-22'
updated: '2026-06-22'
input: *id001
prior_interpretations:
- interpretation:0002-t013-cross-trigger-sex-effect-sizes
relations:
- predicate: "sci:amends"
  target: "interpretation:0002-t013-cross-trigger-sex-effect-sizes"
---
<!--
Conclusion chains:
- sci:amends interpretation:0002 — that interpretation found the somatic-vs-neuropsychiatric
  domain dissociation "directionally inconsistent" on 2 use-now datasets. This one, on a
  6-bucket cross-trigger literature sweep, refines that: the dissociation is not random
  inconsistency but is organized by a measurement-channel axis. It narrows/extends, it does
  not replace.
-->

# Interpretation: Subphenotype decomposition of the PAIS female / reproductive-stage excess

> **Mode: conceptual.** No new computation. This assembles published sex-stratified (and,
> where they exist, reproductive-stage-stratified) effect sizes for six PAIS subphenotypes —
> somatic fatigue/PEM, dysautonomia, vascular-thromboinflammatory, cognitive, pain, mood, and
> the recovery-time trajectory — from a targeted literature sweep (`task:t018`), and reads the
> resulting matrix against `question:0007` and `hypothesis:0005`. The two use-now anchors
> (Sylvester2022 domain ORs; the dengue fatigue meta) carry structured catalog entities; the
> remaining effect sizes are cited inline at literature-evidence grade and are candidates for
> promotion to evidence-lines (see Updated Priorities). All findings are `literature_evidence`.
>
> **Provenance.** `source_refs` lists every entity-backed input: the two use-now datasets, the
> pre-existing anchors (Shah2025, Costeira2021, Stewart2024, Gusinow2026, Ursini2023), and the six
> papers ingested under this task (Kwan2022, Eldokla2022, Wang2026c, DelgadoAlonso2023, Bland2024,
> Cheetham2023) that back the minted POTS/cognition propositions. The **held-back** cells are
> sourced from literature **not yet ingested as entities** and are therefore *not* in `source_refs`:
> the vascular reversal rests on **Abubasheer2025** (VTE meta) and **Ambrosino2021** (FMD); the
> recovery-time row on **Fischer2025** (Predi-Covid) and König2023; the reproductive-stage rows on
> **Boneva2015** (ME/CFS) and Neuhouser2024. These are cited inline only and must be ingested before
> any of those cells is promoted to an evidence-line.

## Verdict

**Verdict:** [~] Mixed, but with a sharper structure than `interpretation:0002` could see.
The female excess is **not uniform across subphenotypes**, and its variation is **not random**:
it tracks a **measurement-channel axis**. The excess is concentrated in domains captured by
**sex-differential self-report / ascertainment** (subjective cognition, fatigue, pain
self-report, mood in COVID, self-reported recovery time) and in a **baseline-female-predominant
syndrome carried through** (POTS). It is **absent** where the same construct is measured
**objectively** (neuropsychological testing) and is **reversed (male-biased)** for
**hard vascular/thrombotic endpoints** (severity-confounded). Separately, on the
reproductive-stage axis, the one study that isolates menopausal status within an age band
finds the midlife female peak is **not** menopausal-status-driven — a `disputes`-leaning signal
against a menopause-specific reading of the subphenotype excess, though not against a broader
age/immunosenescence threshold.

## Findings Summary

### Cross-trigger subphenotype × sex matrix

"Sex effect" is the female-vs-male direction of the post-acute outcome. "Channel" flags whether
the headline measure is subjective/self-reported, an objective test, or a hard clinical endpoint.

| Subphenotype | Female sex effect | Channel | Strongest evidence | Reproductive-stage data |
|---|---|---|---|---|
| **Somatic fatigue / PEM** | **Female-biased** — dengue OR 1.65 (1.27–2.14); ME/CFS ~3–4:1; recovery-time below | self-report | dengue meta (`dataset:dengue-postinfective-fatigue-meta`); MCAM ME/CFS | none usable |
| **Mood / depression** | **Mixed** — COVID mood OR 1.58 (1.37–1.82) > overall 1.22; dengue depression null (2 studies/169 pts, uninterpretable) | self-report | Sylvester2022 (`dataset:sylvester-2022-longcovid-sex`) | none |
| **Dysautonomia (POTS)** | **Female-biased ~4–5:1, but = baseline carried through** — infection *raises* POTS incidence (Kwan2022 infection→POTS odds 2.11, 1.70–2.63; vaccination→POTS 1.52, 1.36–1.71; infection-vs-vaccination RR 5.35, 5.05–5.68; meta RR 2.12, 1.71–2.62) yet Kwan's own sex-stratified analyses are "similar between sexes" (POTS subgroup 59% female ≈ 57% cohort baseline) and post-COVID POTS is ~74–80% female ≈ all-cause POTS baseline; two meta-regressions find **female-proportion does NOT predict** POTS prevalence (age does); COMPASS-31 *continuous* shows **no sex difference** (male 28.0 vs female 26.5, p=0.937) | diagnosis / self-report instrument | Kwan2022 (controlled EHR, sex-stratified); PASC POTS meta-regressions; Eldokla2022 (COMPASS-31 null) | none usable |
| **Cognitive** | **Subjective female-biased (aHR ~1.5), OBJECTIVE null** — subjective memory/executive complaints female-skewed, but objective deficit tracks **ongoing-symptom status, not sex**; subjective↔objective uncorrelated (r≈−0.07), subjective mediated by **fatigue/affect** | subjective vs objective (dissociated) | Cheetham2023 (controlled-longitudinal, n=3,335, objective null on sex); Delgado-Alonso2023; Bland2024 | none (cohorts mean age ~46–49, none stratified) |
| **Vascular-thromboinflammatory** | **MALE-biased (reversed)** for hard endpoints — VTE RR 1.43 (1.19–1.71) male; post-COVID CV mortality HR 1.33 (1.01–1.74) male; endothelial dysfunction (FMD) worse in males — opposite the overall female PAIS skew. **[RESOLVED by t042 → `interpretation:0005` / `proposition:0012`: the reversal SURVIVES acute-severity adjustment for thrombotic/CV endpoints — male VTE excess present in ambulatory patients (Xie2022 aHR 1.69) and within hospitalized patients (Kopp2024 HR 1.68); the FMD leg stays severity-confounded.]** | hard clinical endpoint | Abubasheer2025 (VTE meta); Kopp2024 (CV-mortality cohort); Xie2022 (ambulatory VTE); Ambrosino2021 (FMD) | none |
| **Pain** | **Female-biased** — persistent headache female-skewed; ME/CFS pain ~3–4:1; post-dengue somatic OR 1.65. Outlier: Ursini2023 "FibroCOVID" survey male OR 9.95 (contested, self-report, unreplicated) | self-report | headache cohort; MCAM ME/CFS; Ursini2023 (outlier) | none |
| **Recovery-time / trajectory** | **Female-biased slower resolution** — Predi-Covid LCMM persisting-trajectory female OR 1.81 (p=0.001); König2023 CIS8R OR 2.06 (0.98–4.32); duration-banded fatigue OR ~1.95–2.31 | self-report trajectory | Fischer2025 (Predi-Covid, controlled-longitudinal); Gusinow2026 (`paper:Gusinow2026`); König2023 | only age (collinear w/ stage), not menopausal status |

### Microclots — flagged separately

The fibrin-amyloid microclot construct (Pretorius/Kell) reports **no usable sex OR** and **no**
reproductive-stage stratification, and remains **corpus-dependent / replication-pending** (the
RPTH 2024 critique; Thierry2025 a partial independent corroboration). It cannot populate a
subphenotype×sex cell at present and is not read into the matrix.

### Reproductive-stage × subphenotype

| Result | What it shows | Source |
|---|---|---|
| **Within-age-band menopause null** | At ages 40–54, female long-COVID excess is **near-identical** menopausal RR **1.42** (0.99–2.03) vs nonmenopausal RR **1.45** (1.15–1.83) → the well-known 40–54 female peak is **not** explained by menopausal status per se | Shah2025 (`paper:Shah2025`, RECOVER, the only study isolating menopausal status within an age band) |
| **ME/CFS early-menopause signal (strongest true stage effect, non-COVID)** | Early menopause ≤45 adj OR **3.20** (1.21–8.49); mean age at menopause 38.5 (CFS) vs 48.6 y (controls) — but reverse causation plausible (illness → earlier menopause) | Boneva2015 (*Menopause*) |
| **Acute (not long) COVID estrogen contrast** | Postmenopausal vs premenopausal predicted-COVID OR 1.22; HRT OR 1.32 (paradoxical); **acute outcome, not long COVID** | Costeira2021 (`paper:Costeira2021`) |
| **Symptom-overlap confound** | 40–54 menopause-symptom-questionnaire load is highest within a post-COVID clinic; shared fatigue/brain-fog/sleep items mean reproductive stage biases *ascertainment* | Stewart2024 (`paper:Stewart2024`) |
| **HRT × long-COVID outcome** | **Zero** controlled data — even WHI (rich HRT data) did not analyze it | (gap) |

### What the matrix shows

1. **The female excess is subphenotype-dependent (robust).** Within a single trigger (COVID,
   Sylvester2022) it ranges from female-biased ENT 2.28 / mood 1.58 / GI 1.60 to **male-biased**
   endocrine 0.75 / renal 0.74; across the sweep it ranges from female-biased fatigue/pain/
   recovery to a **male-biased** hard-vascular domain. Uniformity is rejected.

2. **The dependence tracks a measurement-channel axis (the new structure).** Sorting the
   domains by *how the headline outcome is measured* rather than by *somatic-vs-neuropsychiatric*
   organizes them cleanly: self-reported/ascertainment-mediated domains are female-biased;
   objectively-measured cognition is sex-null; hard thrombo-cardiovascular endpoints are
   male-biased. This **resolves** `interpretation:0002`'s "directionally inconsistent" finding —
   the COVID-mood-up / dengue-fatigue-up inconsistency and the broader domain heterogeneity are
   largely a **channel** effect, not a stable biological domain map. It directly engages
   `proposition:0005` (symptom-overlap/ascertainment as a measurement process) and the
   Zhang2022 ascertainment confound flagged in `question:0007`.

3. **Dysautonomia is the cleanest "carried-through baseline" case.** Infection genuinely raises
   POTS incidence (the one controlled design, Kwan2022, orders infection→POTS in time), but the
   female skew is the pre-existing ~5:1 POTS predominance, not a PAIS-specific sex interaction;
   no study reports an infection×sex interaction above baseline.

4. **Reproductive stage is not shown to drive the subphenotype excess.** The only study breaking
   the age/menopause collinearity (Shah2025) finds menopausal status adds nothing within the
   40–54 band; the strongest genuine stage effect (Boneva2015) is in ME/CFS and is
   reverse-causation-ambiguous; HRT×long-COVID outcome data are absent. This **tempers** a
   menopause-specific reading of `hypothesis:0005` at the subphenotype level, consistent with
   `interpretation:0002`'s "weak, indirect support" and the `pre-registration:0001` framing.

## Evidence Quality

- **All literature-derived**, heterogeneous case definitions, mostly cross-sectional or
  cohort; few controlled-longitudinal designs (Cheetham2023 objective cognition; Fischer2025
  trajectory; Kwan2022 EHR are the strongest). No microdata re-analysis.
- **Ascertainment is the throughline confound, and it is now load-bearing, not incidental.**
  The measurement-channel structure means a large part of the observed subphenotype map could be
  *generated by* sex-differential care-seeking/self-report rather than biology. This is exactly
  `proposition:0005`'s mechanism operating at the subphenotype level.
- **Severity confounding** of the male-biased vascular signal was the original caveat here —
  males had more severe acute COVID, which independently raises thrombotic risk. **This was
  tested and rejected by t042 (`interpretation:0005`):** the male VTE excess is present in
  ambulatory (lowest-severity) patients and the male CV-mortality excess persists within a
  hospitalized-restricted cohort, so the thrombotic/CV reversal is severity-*independent*, not
  carryover. A distinct confound — baseline male VTE predominance at older ages — remains open.
- **Baseline-rate confounding** (dysautonomia): POTS is female-predominant regardless of trigger,
  so a female-skewed post-infectious POTS cohort is uninformative about a sex interaction.
- **Independence / contested corpora:** microclots are corpus-dependent (single dominant group);
  the dengue depression null and the Ursini FibroCOVID male-OR are single weak studies and are
  treated as such (not promoted).
- **Reverse causation** is unresolved for every cross-sectional hormone/stage finding
  (Boneva2015; Silva2024/Shahbaz2025 already in the graph): illness may suppress the HPG axis or
  advance menopause rather than the reverse.

## Data Quality Checks

No microdata involved; control-uniqueness / dimensionality checks do not apply. One structural
concern is recorded as `methodological`: across the sweep, **female-excess subphenotype cells and
self-report measurement channels are confounded** — almost every female-biased domain is
self-reported and almost every objectively-measured or hard-endpoint domain is sex-null or
male-biased, so "domain" and "channel" cannot be fully separated from the published literature
alone. Treat the measurement-channel reading as the **leading** structure but not a closed one
until an objective-endpoint, ascertainment-symmetric design tests a female-biased domain.

## Question-Level Implications

**`question:0007` (mechanism of female predominance) — sharpened; the somatic-vs-depression sub-question reframed.**
- The question asks whether the excess "genuinely tracks somatic fatigue more than post-infectious
  depression." The sweep says the more predictive cut is **not** somatic-vs-neuropsychiatric but
  **self-report/ascertainment-vs-objective/hard-endpoint**. The fatigue/depression contrast that
  `interpretation:0002` already found directionally inconsistent is subsumed by this: both fatigue
  and mood are self-report channels, which is why both can be female-biased in COVID.
- This **raises the weight** on the ascertainment/measurement-process branch of `question:0007`
  (and on `proposition:0005`) relative to the estrogen-amplification branch, without resolving
  mechanism — an objective-endpoint female-biased domain would be needed to separate them.

**`hypothesis:0005` / `proposition:0001` (reproductive-stage threshold) — tempered at the subphenotype level.**
- Shah2025's within-band menopause null is the key: the midlife female peak that `evidence-line:0001`
  reads as supporting the stage-threshold is, on the finer-grained data, **age-linked but not
  menopausal-status-linked**. This does not overturn `proposition:0001` (an age/immunosenescence
  threshold remains live) but it **disputes a menopause-specific reading** and should be recorded
  against it (see Updated Priorities).

**`proposition:0008` (persistence-concentration) — complemented, not duplicated.**
- 0008 located the excess on the *acute→post-acute phase* axis; this interpretation locates it on
  the *subphenotype × measurement-channel* axis. They are orthogonal cuts of the same female excess.

## New Questions Raised

- **Is any *objectively-measured* PAIS subphenotype female-biased?** (P2, empirical) The single
  most efficient discriminator between the ascertainment and the biological-amplification readings.
  Candidates: objective autonomic testing (tilt-confirmed POTS incidence with symmetric
  ascertainment), immune/biomarker endpoints with sex stratification.
- **Does the male-biased vascular domain survive severity adjustment?** (P2, methodological)
  **RESOLVED (t042, `interpretation:0005`): yes** — it persists within acute-severity strata
  (ambulatory and hospitalized), so it is a genuine domain reversal, not carryover. Minted as
  `proposition:0012`.
- **Is the ME/CFS early-menopause signal (Boneva2015) reverse-causation or predisposition?**
  (P3, empirical) Needs pre-infection menopausal timing — the same within-cohort design `t013`
  flagged as private/deferred.

## Limitations & Residual Uncertainty

- Domain and measurement channel are confounded in the available literature (Data Quality Checks).
- Reproductive-stage × *specific subphenotype* effect sizes are essentially absent — every
  stage-stratified result is whole-syndrome, not domain-specific.
- No pre-infection-baseline + objective-endpoint + menopausal-biomarker design exists; reverse
  causation and ascertainment remain unadjusted in most cells.
- The matrix is COVID-weighted; dengue contributes fatigue/mood only, Q-fever/PTLDS contribute
  near-nothing at the subphenotype×sex level (explicit empty cells).

## Updated Priorities

**DONE (2026-06-22, t018 disciplined-default minting):** ingested 6 papers (Kwan2022, Eldokla2022,
Cheetham2023, DelgadoAlonso2023, Bland2024, Wang2026c); minted `proposition:0009`
(dysautonomia baseline-carried; lines `evidence-line:0019`/`0020`/`0024` — Wang2026c added as a
third line so the proposition is not `fragile-single-line`) and `proposition:0010` (cognitive
self-report-only; lines `evidence-line:0021`/`0022`/`0023`); refined `evidence-line:0001` with the
Shah2025 within-band menopause-null (age-banded support stands, menopause-specific reading
disputed). Validate PASSED; neither new proposition fires `belief.fragile-single-line`. The
vascular male-reversal and the measurement-channel umbrella were **held at interpretation level**
(not minted) pending the severity-adjustment question below. **UPDATE (2026-06-23, t042): the
vascular male-reversal is now resolved and minted** as `proposition:0012` (`interpretation:0005`);
the measurement-channel umbrella remains held.

- **Promoted the two best-supported subphenotype findings to propositions + evidence-lines**
  (done above; the third — vascular — was held, and is now resolved + minted by t042 as
  `proposition:0012`, see `interpretation:0005`):
  1. *Dysautonomia female-skew is baseline-carried, not PAIS-amplified* (`empirical_regularity`;
     lines: Kwan2022 incidence, POTS meta-regression female-proportion null, Eldokla2022
     COMPASS-31 continuous null — distinct `independence_group`s).
  2. *Cognitive female-excess is self-report-only, absent in objective testing*
     (`empirical_regularity`; lines: Cheetham2023, Delgado-Alonso2023, Bland2024).
  3. *The vascular-thromboinflammatory hard-endpoint domain is male-biased (reversed)*
     (`empirical_regularity`, severity-confounded caveat; lines: Abubasheer2025, FMD).
  - and a possible umbrella `empirical_regularity` that the excess tracks a measurement-channel
    axis, bearing on `proposition:0005`.
- **Record a `disputes`-leaning evidence-line for the menopause-specific reading** (Shah2025
  within-band null) against a menopause-mechanism interpretation of `proposition:0001` — handled
  as a refinement of the existing `evidence-line:0001`, not a contradiction (the age-band support
  stands; the menopausal-status attribution does not).
- **Ingest the load-bearing new papers** (Kwan2022, Cheetham2023, Delgado-Alonso2023, Bland2024,
  Abubasheer2025, Boneva2015, Fischer2025) as `entities/papers/` so the above evidence-lines have
  valid `source:` refs.
- **Do not** mint any "somatic > neuropsychiatric" proposition (carried over from
  `interpretation:0002`) — superseded here by the measurement-channel reading.
- **Do not** promote a reproductive-stage × subphenotype proposition — the cells are empty.
