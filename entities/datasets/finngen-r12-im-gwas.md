---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:finngen-r12-im-gwas
kind: dataset
title: FinnGen R12 AB1_EBV — infectious mononucleosis GWAS summary statistics
status: candidate
provided_capabilities:
  - modality: genetics
    assay: gwas-sumstats
    trigger: ebv
    cohort_design: summary-stats
    stratification: im-history
created: '2026-07-17'
updated: '2026-07-17'
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: custom
access:
  level: public
  availability: available
  verified: true
  source_url: https://risteys.finngen.fi/endpoints/AB1_EBV
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- infectious-mononucleosis
- ebv
- gwas-summary-statistics
- mendelian-randomization-exposure
related:
- question:0051-prior-symptomatic-ebv-mononucleosis-as-pais-risk-amplifier
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# FinnGen R12 AB1_EBV — infectious mononucleosis GWAS summary statistics

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

FinnGen R12 GWAS summary statistics for endpoint `AB1_EBV` ("Infectious mononucleosis";
ICD-10 B27, ICD-9/8 075), **3,838 cases / 486,087 controls** of Finnish ancestry. Released as
part of the FinnGen R12 public summary-statistic distribution.

## Why it fits

`question:0051` asks whether a history of **symptomatic** primary EBV infection raises later
PAIS risk *independently of current EBV reactivation markers*. That estimand is hard to attack
directly because IM history and current reactivation are entangled in any cross-sectional cohort.
A genetic instrument for IM liability breaks the entanglement structurally: genotype is fixed at
conception, so it cannot be a consequence of current reactivation. This is the **exposure** arm of
a candidate two-sample MR whose outcome arm would be `dataset:decodeme-gwas-sumstats-osf` (ME/CFS)
or the long-COVID HGI vehicle.

## Access / caveats

**Public, no login.** Verified 2026-07-17 against the R12 manifest
(`finngen-public-data-r12/summary_stats/finngen_R12_manifest.tsv`), which lists AB1_EBV with a
direct anonymous HTTPS path (`.../release/finngen_R12_AB1_EBV.gz`). Risteys reports ~3,988
genotype-QC cases against the manifest's 3,838 — a release/QC-stage difference, not a conflict;
use the manifest figure for the sumstat file.

**Caveats.**
- Registry-coded IM captures **medically-attended** mononucleosis only; mild symptomatic cases are
  misclassified as controls.
- Controls collapse **asymptomatic seroconverters with the EBV-naive** — precisely the contrast
  `question:0051` cares about. This **attenuates the SNP–IM associations and weakens the
  instrument**; confine the "toward null" intuition to that exposure-GWAS association strength — it
  does *not* cleanly bias the downstream MR ratio toward null (a weak instrument can distort the
  ratio's scale and induce weak-instrument bias).
- Finnish-only; bottlenecked population, transferability limits.
- **Underpowered as an MR exposure (power-screen 2026-07-18).** Against an HGI long-COVID outcome
  (6,450 broad-definition multi-ancestry cases, controls ≫ cases so N_eff ≈ case count), an IM
  instrument explaining even R²=1% detects only OR ≥ 1.42/SD at 80% power (≥ 1.64 at a realistic
  R²≈0.5%); power at OR 1.30 is ≈0.56. "OR/SD" here presupposes a per-SD **latent-liability**
  exposure with R² on that scale — IM is binary, so this framing must be made explicit before the
  estimate is interpretable. **Likely-uninterpretable instrument:** if the usable instrument is
  HLA-dominated (expected for medically-attended IM), the exclusion restriction is not credible.
  **Verdict: shelve** on power grounds, and on validity grounds *unless a sufficiently strong
  non-HLA instrument survives clumping* — settling that needs an acquired/clumped instrument report
  (association results), not yet in hand. `dataset:gcst005038-allergic-disease-gwas` (atopy) is the
  only surviving MR candidate.

**Scope (D-005 / D-006).** Cataloguing is unrestricted; **execution is not authorised.** D-006(c)
holds FinnGen as a *distinct measured-phenotype vehicle* requiring (i) a scope decision and (ii)
confirmation its access path clears the third-party-reproducible bar. Two clarifications, neither
of which discharges D-006 on its own:
- D-006(c) concerns FinnGen as a **long-COVID outcome**; here FinnGen is an **exposure** for a
  different question. Different role, still a distinct vehicle → still needs (i).
- On (ii): D-006 flagged the *form/email-mediated* `finngen.fi` path as unverified. The **R12 public
  bulk-download channel used here is a different channel** and was verified anonymous on
  2026-07-17. That is evidence toward (ii) for this channel; it does not substitute for (i).

Ruling (2026-07-18): independent of D-006(c), *a new exposure against the authorized HGI outcome is
a new computational line requiring a fresh D-005 decision; D-006 maintenance covers promotion of the
named Wave-1 vehicle only, not arbitrary new exposure vehicles.*

## Access verification log

- 2026-07-17 (agent (verify-access)): Risteys/FinnGen confirmed 2026-07-17: endpoint AB1_EBV = infectious mononucleosis (ICD-10 B27, ICD-9/8 075), ~3,988 genotype-QC cases; R12 public sumstats freely downloadable from the finngen-public-data-r12 GCS bucket, no login. Registry-coded IM = medically-attended only; controls collapse asymptomatic seroconverters with EBV-naive (biases toward null). SCOPE: usable as an MR EXPOSURE; D-006 restricts FinnGen as an OUTCOME vehicle -- see task note.
