---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gcst005038-allergic-disease-gwas
kind: dataset
title: GCST005038 — Shared genetic origin of asthma, hay fever and eczema (Ferreira
  2017) GWAS summary statistics
status: candidate
provided_capabilities:
  - modality: genetics
    assay: gwas-sumstats
    trigger: not-applicable
    cohort_design: summary-stats
    stratification: atopy
created: '2026-07-17'
updated: '2026-07-17'
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ebi.ac.uk/gwas/studies/GCST005038
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- atopy
- allergic-disease
- gwas-summary-statistics
- mendelian-randomization-exposure
related:
- question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GCST005038 — Shared genetic origin of asthma, hay fever and eczema (PMID 29083406) GWAS summary statistics

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

GWAS Catalog study GCST005038 — "Allergic disease (asthma, hay fever or eczema)",
**180,129 European-ancestry cases / 180,709 controls** (PMID 29083406). Full summary statistics
released (`fullPvalueSet: true`).

## Why it fits

The only well-powered **open** atopy exposure instrument located, and therefore the only
third-party-reproducible way into `question:0034` today. Intended as the exposure arm of an
atopy → PAIS MR, paired with `dataset:covid19-hgi-longcovid-gwas` (infected-control long-COVID
outcome) or `dataset:decodeme-gwas-sumstats-osf`.

## Access / caveats

**Public, no DUA.** GWAS Catalog REST confirmed 2026-07-17; full sumstats on the EBI FTP.

**Caveats.**
- The released file **excludes 23andMe samples**, i.e. the best-powered stratum is withheld.
- The phenotype is a **broad any-allergic-disease composite**; it cannot separate atopy from MCAS.
  MCAS specifically has essentially no genetic or omics footprint (see this entity's sibling
  search residue) — hereditary alpha-tryptasemia (TPSAB1 copy number) is **not capturable** from
  standard GWAS arrays or sumstats, so it cannot be recovered through this vehicle.
- **Power is the live risk**, not availability — power-**screened** 2026-07-18. Status: a
  **provisional power-screen survivor**, *not* "conditionally viable" and not a committed line.
  Model: against an HGI long-COVID outcome the control pool (~1.09M) ≫ cases, so N_eff ≈ case
  count and power ≈ N_cases·R²·(lnOR)². Minimum detectable effects (80% power, α=0.05):
  - R²≈3.7% / 6,450 cases → OR **1.20/SD**; R²≈2% / 3,500 cases → floor OR **~1.40** (power at
    OR 1.20 there is only ≈**0.33** — the ≈0.54 figure belongs to 6,450 cases at R²=2%, or 3,500
    at R²=3.7%, not 3,500 at R²=2%).

  Four unresolved issues keep this provisional, and none is discharged yet:
  - **No EUR-only outcome exists.** The 6,450-case file (`GCST90454541`) is the European-*dominant*
    **multi-ancestry** meta (6,450 broad-definition cases / 1,093,995 population controls); the
    project has established there is no EUR-only HGI long-COVID file. This **fails D-006's
    ancestry-matched-primary gate**, so any run here is **mechanics / sensitivity only, never
    reportable primary MR**. "Pull the actual EUR-arm case count" is therefore not a real step.
  - **Exposure scale unresolved.** Atopy is *binary*; "OR/SD" is meaningful only as an effect per
    SD of **latent liability**, with the instrument R² transformed onto that same liability scale.
    Standard binary-outcome MR power assumes a standardized continuous exposure — without the
    liability framing the estimand is a different quantity.
  - **The 3.7% R² is not the composite instrument's empirical liability R².** Ferreira's supplement
    reports *disease-specific* variance for the lead loci (~3.2% asthma, ~3.8% hay fever, ~1.2%
    eczema), not a transferable broad-composite liability R². The empirical liability-scale R² must
    be computed from these public sumstats before any power claim stands.
  - **Sample overlap.** UKB plausibly contributes to both an atopy instrument and the HGI outcome;
    the two-sample overlap must be checked and handled, or it biases toward the confounded
    observational estimate.

  Scope of the estimand: even if all four resolve, this vehicle speaks only to **broad
  allergic-disease liability**, not q0034's stronger "mechanistically distinct atopy/MCAS subgroup"
  question (MCAS has no capturable footprint here — see the sibling caveat above). It is
  nonetheless the **only surviving MR candidate** after IM was shelved (see
  `dataset:finngen-r12-im-gwas`).

**Feasibility result (t137, 2026-07-18): NO-GO.** The D-007 feasibility packet ran on public
sumstats and shelved the line. The instrument is **strong** — 63 independent instruments after MHC
exclusion, mean F = 62 — but its **liability-scale R² is only ~2–2.5%** (logit-latent 1.96%;
Lee-2011 normal-liability 2.14–2.53% across K∈{0.20,0.30,0.40}; the naïve Σ2p(1−p)β²=6.56% overstates
and is excluded). Against the ancestry-capped ~6,450-case HGI outcome that gives only **0.57–0.64
power at OR 1.20/SD** (minimum detectable OR ≈ 1.25), below the pre-registered 80%/OR-1.20 floor. The
limit is the outcome's case count, not the exposure. **D-007b is not raised**; atopy joins IM as
shelved; no boundary-strata MR line survives. Revisit only if a EUR-matched or larger long-COVID
outcome appears (the built instrument would be reusable). Full packet:
`doc/plans/2026-07-18-t137-atopy-feasibility-result.md`.

**Scope (D-005 / D-006 / D-007).** The 2026-07-18 ruling — *a new exposure against the authorized
HGI outcome is a new computational line requiring a fresh D-005 decision; D-006 maintenance covers
promotion of the named Wave-1 vehicle, not arbitrary new exposure vehicles* — was taken up as
**D-007 (2026-07-18)**: the **feasibility packet only** is authorised (instrument construction +
clumping, empirical liability-scale R², UKB↔HGI overlap, binary-exposure scale; public sumstats,
no gated data — `task:t137`). MR **execution is still not authorised** — it is gated on a follow-up
ratification (**D-007b**) once the packet clears pre-registered thresholds (detectable floor
OR≳1.2). The ancestry-matched-primary gate remains an independent D-006 bar: if no EUR-specific HGI
stratum exists, any estimate is mechanics/robustness-only, not reportable-primary.

## Access verification log

- 2026-07-17 (agent (verify-access)): GWAS Catalog REST confirmed 2026-07-17: trait 'Allergic disease (asthma, hay fever or eczema)', 180,129 EUR cases / 180,709 EUR controls, PMID 29083406, fullPvalueSet=true (full sumstats on FTP, no DUA). NOTE: the released file excludes 23andMe samples; broad any-allergic-disease phenotype cannot separate atopy from MCAS.
