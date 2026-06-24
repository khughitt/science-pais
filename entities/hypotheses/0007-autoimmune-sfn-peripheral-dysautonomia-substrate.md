---
id: hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
type: hypothesis
title: Non-length-dependent autoimmune small-fiber neuropathy as a shared peripheral
  substrate of PAIS dysautonomia
status: proposed
phase: candidate
source_refs:
- cite:Oaklander2022
- cite:Joseph2021
- cite:Kharraziha2020
- cite:Hall2022
- cite:Novak2026
related:
- question:0004-convergent-small-fiber-neuropathy-substrate
- question:0009-functional-autoantibodies-drive-dysautonomia
- topic:post-infectious-dysautonomia-and-autoimmunity
- topic:measurement-ascertainment-artifacts-in-pais
- paper:Novak2026
- evidence-line:0063-novak2026-largest-paired-biopsy-pais-sfn-supports-p1
- evidence-line:0064-novak2026-single-protocol-two-trigger-convergence-supports-p4
- evidence-line:0065-novak2026-proximal-sgnfd-not-lesser-weakly-supports-p2
- interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat
- proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified
- proposition:0014-pais-small-fiber-structural-lesion-ienfd
- proposition:0015-pais-sfn-non-length-dependent-pattern
- proposition:0016-pais-sfn-autoimmune-causation
- proposition:0017-pais-sfn-cross-trigger-convergence
- proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity
- proposition:0019-pais-sfn-immunomodulation-modifies-lesion-trajectory
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
- pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls
- interpretation:0010-t006-functional-gpcr-autoantibody-ingestion
created: '2026-06-24'
updated: '2026-06-24'
---
# Hypothesis: Non-length-dependent autoimmune small-fiber neuropathy as a shared peripheral substrate of PAIS dysautonomia

## Organizing Conjecture

A **non-length-dependent small-fiber neuropathy (SFN) of autoimmune origin**, affecting autonomic
and sensory small fibers (and plausibly their dorsal-root-ganglion / autonomic-ganglion cell bodies),
is a **shared peripheral structural substrate** for the dysautonomia seen across post-acute infection
syndromes — PTLDS, long COVID, and ME/CFS. The conjecture operates at a level no current project
hypothesis occupies: not the system-level attractor (`hypothesis:0001-shared-dysregulated-attractor`),
not the immune-maintenance engine (`hypothesis:0003-immune-exhaustion-feedback`), but the **end-organ
lesion** that those upstream processes would produce and that would, in turn, generate orthostatic
intolerance, POTS-like physiology, sudomotor failure, and GI dysmotility. The frame is deliberately
*structural and localizing*: it predicts a measurable peripheral lesion with a characteristic
non-length-dependent distribution, distinct from primary/idiopathic dysautonomia and from
mast-cell-mediated or purely central explanations.

This is a **candidate** frame: it is assembled from individually plausible but not yet
project-verified observations (skin-biopsy SFN reports across syndromes; functional GPCR
autoantibodies), and the decisive cross-syndrome controlled comparison does not yet exist in the
corpus.

## Proposition Bundle

### Core Propositions

*Formalized into the graph as durable propositions (`/science:specify-model`, 2026-06-24):
P1 → `proposition:0014-pais-small-fiber-structural-lesion-ienfd`,
P2 → `proposition:0015-pais-sfn-non-length-dependent-pattern`,
P3 → `proposition:0016-pais-sfn-autoimmune-causation` (the bare immune-mediation claim),
P4 → `proposition:0017-pais-sfn-cross-trigger-convergence`. P3's two evidential routes are carried as
separate, individually falsifiable auxiliary propositions —
`proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity` and
`proposition:0019-pais-sfn-immunomodulation-modifies-lesion-trajectory` (background members of the
bundle) — so the core causal claim is not made elastic by an "and/or". All are now coded against
literature evidence-lines via `task:t049` (`interpretation:0009-t049-sfn-cross-syndrome-ingestion`):
P1/P4 supported, P2 and the anti-GPCR route (0018) the thinnest legs. The anti-GPCR route was then
deepened by `task:t006` (`interpretation:0010-t006-functional-gpcr-autoantibody-ingestion`), which
ingested the primary functional-autoantibody literature and rendered `proposition:0018` **contested**:
one functional-assay correlation (Kharraziha2020, α1-AR-activity↔orthostatic-severity) against a
binding-ELISA specificity null (Hall2022), with **no study linking any anti-GPCR antibody to the
small-fiber lesion**.*

- **P1 (structural lesion → `proposition:0014`).** A substantial subset of PAIS patients with autonomic symptoms have
  objectively reduced intraepidermal nerve-fiber density (IENFD) or autonomic small-fiber loss on
  standardized skin biopsy / autonomic testing — i.e. a real peripheral lesion, not only a functional
  state. *(structural_claim; measurement_model: IENFD on distal+proximal skin biopsy, QSART, autonomic
  reflex screen.)*
- **P2 (non-length-dependent pattern).** The lesion is disproportionately **non-length-dependent**
  (proximal involvement comparable to or exceeding distal), distinguishing it from the
  length-dependent pattern of metabolic/idiopathic SFN and implicating a ganglionopathy / immune-
  mediated mechanism. *(structural_claim.)*
- **P3 (autoimmune causation → `proposition:0016`).** The lesion is immune-mediated — caused or
  sustained by an autoimmune process — rather than degenerative, metabolic, or deconditioning-driven.
  The two evidential routes are split out so the causal claim is not made elastic: *anti-GPCR
  autoantibody pathogenicity* (`proposition:0018`; β-adrenergic / muscarinic, the `question:0009`
  thread) and *immunomodulation modifies the lesion trajectory* (`proposition:0019`). *(causal_effect;
  the autoantibody → fiber-dysfunction link is the weakest leg — a hypothesis, not an established
  pathogenic mechanism.)*
- **P4 (cross-trigger convergence).** The same peripheral SFN substrate recurs across distinct
  triggers (Borrelia/PTLDS, SARS-CoV-2/long COVID, and ME/CFS), supporting a shared end-organ
  failure mode reachable from many infections. *(empirical_regularity.)*

### Supporting Or Auxiliary Propositions

- **A1 (subtype distinctness).** This autoimmune-SFN subtype is mechanistically distinct from
  mast-cell-activation-driven and from central/baroreflex dysautonomia, and the subtypes may
  co-occur — so the substrate accounts for *a fraction*, not all, of PAIS dysautonomia.
- **A2 (sex-skew is baseline-carried).** Any female predominance of this substrate should track the
  pre-existing POTS/dysautonomia female baseline rather than a PAIS-specific amplification, consistent
  with `proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified`.

## Current Uncertainty

The frame is now **literature-coded** but only **partially supported**:
`interpretation:0009-t049-sfn-cross-syndrome-ingestion` deposited 11 evidence-lines (`evidence-line:0038`–
`0048`) across P1–P4 and the autoantibody routes, and `interpretation:0010-t006-functional-gpcr-autoantibody-ingestion`
added 4 more (`evidence-line:0049`–`0052`) on the anti-GPCR route. P1 (lesion) and P4 (cross-trigger
breadth) are supported; P2 (non-length-dependent) and the anti-GPCR route (`proposition:0018`) remain the
thinnest legs. Key fragilities: SFN prevalence estimates in long COVID/ME/CFS vary
widely by biopsy protocol and case definition (a `topic:measurement-ascertainment-artifacts-in-pais`
concern); the **non-length-dependent** claim (P2) requires proximal-plus-distal sampling that many
studies omit; the autoantibody→neuropathy causal link (P3) is the weakest leg and now formally
**contested** — t006 found one functional-assay correlation (Kharraziha2020) against a binding-ELISA
specificity null (Hall2022), and crucially **no study links any anti-GPCR antibody to the small-fiber
lesion** (only to autonomic *function*), so the antibody→*lesion* bridge is untested; and no study
in the corpus compares PAIS SFN head-to-head against **primary-dysautonomia controls** using one
standardized protocol, which is exactly what P2/A1 need.

## Predictions

- **Strong/discriminating:** In a standardized multi-site skin-biopsy study, PAIS patients with
  autonomic symptoms show non-length-dependent IENFD reduction at a higher rate than length-dependent
  reduction, and at a higher rate than matched primary-dysautonomia controls.
- **Strong/discriminating:** Functional anti-GPCR autoantibody titer (or seropositivity) correlates
  with autonomic small-fiber dysfunction severity within PAIS, and immunomodulation (e.g. IVIG in
  seropositive subsets) improves both autonomic measures and IENFD trajectory.
- **Weaker corollary:** SFN markers recur across ≥2 distinct triggers (e.g. PTLDS and long COVID) with
  a comparable non-length-dependent signature.

## Falsifiability

- If standardized biopsy shows PAIS autonomic-symptom patients have IENFD indistinguishable from
  symptom-matched controls, **P1** fails and the structural-lesion frame collapses into a functional
  account.
- If the lesion, when present, is **length-dependent** and indistinguishable in pattern from
  metabolic/idiopathic SFN, **P2** fails and the "distinct ganglionopathy" claim is lost.
- If well-powered immunomodulation trials in autoantibody-positive subsets show no autonomic or IENFD
  benefit, **P3** is materially weakened.
- If SFN is present in one trigger but reliably absent in others under one protocol, **P4** (shared
  substrate) fails and the finding becomes trigger-specific.

## Promotion criteria

Promote from **candidate** to **active** when **both**: (1) at least one cross-syndrome study using a
**standardized skin-biopsy / autonomic protocol with primary-dysautonomia controls** reports the
non-length-dependent pattern in PAIS (resolving `question:0004`); and (2) at least one independent line
links the functional-autoantibody thread (`question:0009`) to the structural lesion — either a
titer↔IENFD/autonomic-severity correlation or an immunomodulation response in a seropositive subset.
Absent (1), this remains a candidate organizing frame for the dysautonomia/autoimmunity work rather
than a committed hypothesis.

**Status of the criteria (2026-06-24):**
- *Criterion #1* is operationalized as the data-gated `pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls` — **not yet met** (no admissible vehicle exists; tracked by `task:t050`).
- *Criterion #2* is **not cleanly met** after `task:t006` (`interpretation:0010`). Note its wording links the autoantibody thread *to the structural lesion*: that strict reading is **unmet** — no ingested study correlates any anti-GPCR antibody with IENFD/SGNFD; all endpoints are autonomic *function*. A weaker titer↔autonomic-*severity* reading is only **partially and contestedly** met (Kharraziha2020 functional α1-AR↔OHQ, against the Hall2022 binding-ELISA specificity null). The decisive missing measurement — functional anti-GPCR activity *and* IENFD in the same subjects — is co-measurable in the pre-reg:0003 **G5 serology arm**, which would discharge both criteria in one design. Future criterion-#2 evidence should be gated on **functional** (not binding-ELISA) assays.

## Supporting Evidence

- **`cite:Oaklander2022` (ingested 2026-06-24):** Earliest prospective long-COVID referral cohort
  using paired distal+proximal skin biopsies (n=17; 63% distal / ~50% proximal SFN). The paired-site
  design demonstrates widespread proximal involvement alongside distal SFN — consistent with P2's
  non-length-dependent claim — though per-patient NLD classification is not formally reported.
  65% received immunotherapy; apparent IVIg/corticosteroid benefit is the best current evidence for
  P3/`proposition:0019`. **No controls of any kind** (neither healthy nor primary-dysautonomia) and
  no functional GPCR autoantibody serology. Referral bias limits prevalence inference. See
  `paper:Oaklander2022` for full detail. Supports P1, P2 (partially), P4 (SARS-CoV-2 arm), and
  P3-auxiliary (`proposition:0019`).
- **`cite:Joseph2021` (ingested 2026-06-24):** Largest ME/CFS skin-biopsy cohort (n=160; NAM 2015
  criteria). 31% had lower-leg SFN (PGP9.5 punch biopsy, ≤5th percentile). Alongside iCPET,
  identified two hemodynamic subtypes — preload failure and peripheral O2 extraction failure —
  proposed to reflect autonomic small-fiber dysregulation. 24% had documented preceding infection
  (no SFN sub-analysis by onset type). **Distal-only biopsy** (single lower-leg site): P2
  (non-length-dependent pattern) CANNOT be assessed. No primary-dysautonomia controls; no
  autoantibody serology. See `paper:Joseph2021`. **Supports P1 and P4 (ME/CFS arm); does NOT
  address P2, P3.**
- **`cite:Adler2024`:** PTLDS leg of P4 — narrative review citing a series in which 10/10 well-defined
  PTLDS patients had abnormal IENFD/SGNFD, plus explicit PTLDS↔long COVID↔ME/CFS cross-syndrome framing.
  Coded as `evidence-line:0044` (weak; narrative review, no controls). Supports P4 (PTLDS arm).
- **`cite:deSa2026`:** the causal anchor for P3/`proposition:0016` — long-COVID IgG passive transfer
  reduces intraepidermal nerve fibers in mice (`evidence-line:0045`, strong/interventional). Note its
  autoantigens were **non-GPCR** (MED20/USP5) and it did not recapitulate the autonomic axis.
- **`cite:Stein2025`:** β2-AR-autoantibody-selected immunoadsorption improves autonomic symptoms
  (`evidence-line:0047` → `proposition:0019`; `evidence-line:0048` weak → `proposition:0018`).
- **`cite:Novak2026` (ingested 2026-06-24; the largest paired-site PAIS biopsy series):** single-center
  retrospective comparison with **paired thigh + calf** ENFD/SGNFD across **long COVID (n=143) and ME/CFS
  (n=170)** vs hEDS (n=290) and healthy controls (n=73). Biopsy SFN 67%/53% vs **0% controls**
  (`evidence-line:0063` → P1, moderate). First **single-protocol two-trigger** convergence — answering the
  prior "convergence of finding, not of protocol" caveat (`evidence-line:0064` → P4, moderate). Group-level
  proximal SGNFD not lesser than distal weakly supports the NLD pattern but is **not per-subject classified**
  (`evidence-line:0065` → P2, weak). Screened as a candidate `pre-registration:0003` vehicle but
  **inadmissible** (fails G2: hEDS is not a clean primary-dysautonomia comparator; QASAT grading, not the
  ≤5th-percentile cutoff). **Key new caveat → Disputing Evidence (specificity).**
- **`cite:Walitt2024` (disputing):** rigorously adjudicated PI-ME/CFS with *no* small-fiber-density
  difference and *no* uniform autoantibody (`evidence-line:0040` → P1; `evidence-line:0046` → 0016).
- *(literature, indirect)* The broader functional anti-GPCR autoantibody literature (the `question:0009` /
  `task:t006` thread) supplies the candidate immune mechanism for P3.
- *(project)* `proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified`
  supports A2's framing of the sex distribution as baseline-carried.

## Disputing Evidence

- The deflationary/deconditioning account of PAIS autonomic symptoms (see
  `question:0017-deflationary-alternatives-vs-shared-pathophysiology`) competes with P1/P3: orthostatic
  intolerance can arise from deconditioning and hypovolemia without a fixed peripheral lesion.
- Reported SFN prevalence in long COVID is heterogeneous and protocol-sensitive; some cohorts find
  limited or length-dependent changes, pressuring P2.
- **Specificity pressure (Novak2026, `evidence-line:0064`).** A non-infectious heritable dysautonomia
  (hEDS, n=290) shows SFN **comparable to or greater than** the PAIS arms (63% biopsy; "more pronounced
  peripheral neurodegeneration"). This is the first corpus data point indicating the small-fiber substrate
  is **not specific to post-infectious syndromes** — it does not dispute P1 (the lesion exists) or P4 (it
  recurs across PAIS triggers), but it pressures `question:0004`'s "**distinguishes from primary
  dysautonomia**" clause and A1 (subtype distinctness). It is exactly why the locked discriminating test
  (`pre-registration:0003`) requires a *clean primary-dysautonomia control arm*: lesion existence is now
  well-supported, but PAIS-specificity of the *pattern* remains unproven and may be the harder contrast.

## Evidence Needed To Shift Belief

The single most discriminating test is a **standardized, multi-trigger skin-biopsy + autonomic-function
study** (proximal *and* distal IENFD, QSART, autonomic reflex screen) in PAIS patients with autonomic
symptoms, against both healthy and **primary-dysautonomia** controls, with parallel functional-
autoantibody serology — directly addressing P1, P2, P4, and (via the serology arm) P3 in one design.

## Related Work

- Questions: `question:0004-convergent-small-fiber-neuropathy-substrate` (primary),
  `question:0009-functional-autoantibodies-drive-dysautonomia`.
- Topics: `topic:post-infectious-dysautonomia-and-autoimmunity`,
  `topic:measurement-ascertainment-artifacts-in-pais`.
- Hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (this is the end-organ instantiation of
  the shared attractor at the peripheral-lesion level), `hypothesis:0003-immune-exhaustion-feedback`
  (a candidate upstream driver of the autoimmune lesion).
- Propositions: `proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified`.
- Tasks: `task:t006` (functional-autoantibody lit-search), `task:t049` (SFN cross-syndrome ingestion).
