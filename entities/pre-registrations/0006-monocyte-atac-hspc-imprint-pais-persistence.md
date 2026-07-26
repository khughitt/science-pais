---
id: pre-registration:0006-monocyte-atac-hspc-imprint-pais-persistence
kind: pre-registration
title: "Monocyte-progeny (CD14+) ATAC-seq imprint-depth vs PAIS persistence — data-gated, severity-stratified within-trigger test of the transmitted HSPC imprint (q0055/q0026), with LIINC banked-marrow HSPC ATAC as the source-localization fidelity check"
status: committed
committed: '2026-07-10'
mode: data-gated
spec: ''
related:
- question:0055-hspc-epigenomic-imprinting-depth-predicts-pais-persistence
- question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
- hypothesis:0001-shared-dysregulated-attractor
- topic:innate-immune-memory-trained-immunity-in-pais
- interpretation:0040-t107-hspc-epigenomics-feasibility-banked-pbmc
- interpretation:0039-t108-cross-pais-il6-peak-vs-pais-risk
- task:t120
- task:t107
commits_to:
- question:0055-hspc-epigenomic-imprinting-depth-predicts-pais-persistence
- question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
- hypothesis:0001-shared-dysregulated-attractor
created: '2026-07-10'
updated: '2026-07-10'
---
# Pre-registration: monocyte-progeny (CD14+) ATAC-seq imprint-depth vs PAIS persistence

> **Mode: data-gated. SCOPE — design + interpretation rule committed now; execution deferred.** The vehicle
> (CD14+ monocyte ATAC-seq on banked PAIS-cohort PBMC) does not yet exist in the corpus — no specimens are in
> hand and no assay has run. This pre-registration commits the *estimand, contrast, and belief-update rule*
> now and defers execution until specimens are obtained and the readout clears the Vehicle-Admissibility Gate
> (G1–G6 below). Until then the standing verdict is **`[?]` inconclusive-for-coverage** — it produces **no
> `bears_on` belief update** on any commitment target. Load-bearing parameters that require an
> access decision — final assay platform (bulk vs single-cell), per-arm N, and power — are **deliberately
> left open** here and are the first execution step, gated on confirming per-aliquot viable-cell counts with
> the biorepositories (the `[UNVERIFIED]` number flagged in `interpretation:0040`). This pre-reg
> operationalizes the **t107 target pivot** (`interpretation:0040`): the feasible, high-leverage readout of
> the HSPC-imprint hypothesis on already-banked blood is the **monocyte progeny**, not rare circulating
> CD34+ HSPCs. Tracked by an `active` task (**t120**) whose blocker is specimen access.

## Hypotheses Under Test

The single most discriminating *opportunistic* test named in `question:0055` (as revised by
`interpretation:0040`) and in `question:0026`. It commits how a severity-stratified monocyte-ATAC imprint-
depth analysis will update the following targets:

| Target | Role | Test | Class |
|---|---|---|---|
| `question:0026` (acute imprinting → **hyperreactive monocytes** sustaining PAIS inflammation, antigen-independent) | the effector-state prediction | does monocyte imprint-depth track PAIS persistence *independent of acute severity*? | **confirmatory — headline** |
| `question:0055` (does imprint depth predict PAIS persistence?) | the open question | same, as the feasible monocyte readout | **confirmatory** |
| `hypothesis:0001` (shared dysregulated attractor; HSPC-imprint as a candidate maintenance mechanism) | the candidate frame | is a durable innate-epigenomic set-point associated with non-recovery? | **confirmatory — weak prior** |

The upstream **HSPC-source localization** (whether a monocyte difference *originates* in the marrow HSPC
compartment) is **not** a commitment target of the monocyte arm — it is the job of the LIINC banked-marrow
fidelity check (Exploratory/Tier-2 below), because the monocyte epigenome reports the *transmitted* imprint,
not its origin.

## Estimand & Design

- **Estimand:** the association between **CD14+ monocyte chromatin-accessibility imprint-depth** at a
  defined post-acute timepoint and **PAIS persistence at 12+ months**, **conditional on acute-illness
  severity** (severity as a modeled covariate/effect-modifier, not a post-hoc adjustment).
- **Substrate:** CD14+ monocytes gated/sorted from banked cryopreserved PBMC (abundant, ~10–20% of PBMC).
- **Primary contrast:** **within-trigger, PAIS-persistent vs infected-recovered**, both arms spanning the
  **mild→severe** acute-severity spectrum. The within-trigger, both-infected framing estimates imprint-depth
  orthogonal to trigger identity and to infection-vs-not (mirroring the control-frame correction in
  `interpretation:0036`).
- **Imprint-depth score (pre-specified loci):** ATAC-seq accessibility at innate-immune / trained-immunity
  loci — **NLRP3, TNF, IL6, CXCL8/IL8, and an IFN-stimulated-gene panel** — i.e. the `question:0026` /
  Cheong2023 effector loci, summarized as a single a-priori score plus per-locus reporting.
- **Cohorts (per `interpretation:0040`):** **RECOVER** (long-COVID arm; open BAC application; viable PBMC;
  longitudinal to ~4 y; **full acute-severity spectrum** — the design-critical property) and the **UK ME/CFS
  Biobank** (ME/CFS arm; open cost-reimbursement; ~20 PBMC vials/contact). Cross-trigger concordance
  (COVID vs ME/CFS) is a secondary, `hypothesis:0001`-relevant readout.
- **Fidelity check (Tier-2, source localization):** the same accessibility contrast in **sorted marrow
  HSPCs from LIINC's banked bone marrow** (consortium/LCRC access) — the only *identified* same-compartment
  substrate matching Cheong2023.

## Expected Outcomes

Prior (weak, from Cheong2023's transmitted-imprint finding and the `question:0026` corollary): monocyte
imprint-depth will be **higher in PAIS-persistent than in recovered** within trigger, with an effect that
**partly but not wholly** reduces after conditioning on acute severity (a purely severity-explained signal
is the key competing reading — the same severity-through-line that defeated the serum-IL-6 proxy in
`interpretation:0039`). The prior is held weakly: a severity-explained or null result is genuinely
informative, and the multi-mechanism view (`hypothesis:0001`: HSPC-imprint is one of several maintenance
routes, not the sole one) predicts at most a partial association.

## Decision Criteria

Epistemic (belief-updating) criteria for the commitment targets:

- **SUPPORT (imprint-as-persistence-predictor; `question:0026` effector prediction gains a supporting line,
  `question:0055` → "predicts," `hypothesis:0001` updates upward):** monocyte imprint-depth is **higher in
  PAIS-persistent vs recovered within trigger, and the association survives conditioning on acute
  severity** (severity as covariate/effect-modifier). Strength scales with **cross-trigger concordance**
  (present in both COVID and ME/CFS arms) and with **directional agreement in the LIINC marrow HSPC arm**.
- **WEAKEN → SEVERITY-CORRELATE (disputing line on the `question:0026` effector prediction; `question:0055`
  → "does not predict independent of severity"):** an imprint-depth difference that is present marginally
  but **fully attenuates after conditioning on acute severity** — the imprint tracks how sick the acute
  illness was, not who stays sick. This is the pre-committed "it's a severity marker" reading.
- **REFUTE (disputing line; downward for the antigen-independent-effector framing):** **no imprint-depth
  difference** between persistent and recovered within trigger even before severity adjustment, in an
  adequately powered, QC-passing assay.
- **INCONCLUSIVE (no update):** effect seen only pooled-across-severity with no severity model; monocyte
  purity / ATAC QC failure; underpowered per-arm N; or PAIS/recovery misclassification. → exploratory,
  await a powered/QC-clean replication.

## Null Result Plan

A **clean severity-conditioned null is evidence** (disputing the `question:0026` effector prediction and
weakening the HSPC-imprint maintenance route in `hypothesis:0001`), but its weight is gated on **adequacy**:
adequate per-arm N (execution parameter, deferred), demonstrated monocyte purity + dead-cell/granulocyte
depletion (Desoutter2019 hazard), passing ATAC QC, and a severity spectrum wide enough to *separate*
severity from persistence. A **flat null in a narrow-severity or hospitalized-only cohort** (e.g. if only
PHOSP-style specimens were reachable) is **weak** disconfirmation — confounded with the severity-selection
trap that `interpretation:0040` flagged — and routes to replication in a full-spectrum cohort, not to a
belief update.

## Suspicious/Unexpected Result Plan

A surprisingly large or purely-cross-trigger-uniform effect would prompt checks for **batch/processing
confounding** (freeze-thaw date, biobank site, sort batch — the dominant error class per the t035 lesson in
`interpretation:0038`/`interpretation:0001`), **monocyte-subset composition shift** (classical/intermediate/
non-classical proportions differing by group can masquerade as an accessibility difference — must be modeled
or sorted), **ambient/granulocyte-debris contamination** (Desoutter2019), and **PAIS-definition leakage**
(case status correlating with a processing covariate) before acceptance.

## Known Limitations

Even a perfectly executed monocyte-ATAC analysis cannot: **localize** whether an imprint originates in the
marrow HSPC compartment vs peripheral monocyte reprogramming (needs the LIINC marrow arm); establish
**symptom causation** (association only — an interventional/epigenetic-reversal test is a separate vehicle);
or fully **eliminate** residual confounding by acute severity (it is modeled and spanned, not randomized).
Cross-sectional post-acute sampling also cannot separate "imprint precedes non-recovery" from "chronic
disease sustains the imprint" without the longitudinal (3→12 mo) design the RECOVER banking supports.

## Exploratory vs. Confirmatory

- **Confirmatory:** the severity-conditioned, within-trigger monocyte imprint-depth → persistence test above.
- **Exploratory:** cross-trigger (COVID vs ME/CFS) concordance of the imprint signature; per-locus vs
  composite-score behavior; monocyte-subset-specific effects (single-cell arm, if cell counts allow);
  longitudinal imprint trajectory (3→12 mo) as a predictor vs a correlate; and the **LIINC marrow HSPC**
  source-localization check.

## Vehicle-Admissibility Gate (G1–G6)

The readout activates the belief-update rule only if it satisfies:

- **G1 — viable substrate:** cryopreserved *viable* PBMC obtained, with **confirmed per-aliquot cell
  counts** sufficient for the chosen ATAC platform (the deferred parameter; single-cell requires pooling or
  large aliquots).
- **G2 — severity spectrum:** both arms span mild→severe acute severity (else severity is not separable from
  persistence — the pre-committed confound).
- **G3 — control frame:** **infected-recovered** within-trigger controls (not uninfected-only).
- **G4 — case definition locked:** an explicit PAIS case definition with **12+ month persistence** (WHO/CDC
  for long COVID; CCC/ICC for ME/CFS), recorded before analysis.
- **G5 — cell-purity + composition QC:** demonstrated CD14+ monocyte purity, dead-cell/granulocyte depletion
  (Desoutter2019), and **monocyte-subset composition** measured/modeled.
- **G6 — ATAC QC:** frozen-input Omni-ATAC library metrics passing (TSS enrichment, FRiP, fragment-size
  periodicity), per Corces2017.

Spent/partial datasets failing G1/G2/G3 (no viable cells, narrow severity, or uninfected-only controls) do
**not** activate the rule.

## Standing verdict

`[?]` inconclusive-for-coverage until an admissible readout exists — **no `bears_on` update** on
`question:0055`, `question:0026`, or `hypothesis:0001`. Tracked by **task:t120**; blocker = specimen access +
finalization of the deferred platform/N/power parameters.
