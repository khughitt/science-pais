# t137 — Atopy → long-COVID MR feasibility packet: frozen pre-registration

- **Date frozen:** 2026-07-18
- **Task:** `task:t137` · **Authorized by:** D-007 (feasibility packet only; MR **execution** gated on a later D-007b ratification)
- **Status:** Step 1 (freeze) — this document. Steps 2–5 execute against it and may not silently amend the frozen choices below.

This freezes the analysis specification **before** any data is touched, so that instrument
strength, scale, and power cannot become researcher-degrees-of-freedom after the numbers are seen.
Ordering (per the 2026-07-18 directive): **(1) freeze [this doc] → (2) construct + clump → (3)
empirical liability-scale R² + power → (4) UKB↔HGI overlap → (5) emit GO/NO-GO packet; draft D-007b
only on GO.**

## Estimand (frozen)

The causal effect of **genetic liability to allergic disease** (asthma/hay-fever/eczema composite)
on **liability to long COVID**, as a two-sample MR germline-liability IV effect — the same estimand
*class* as the D-005 Wave-1 pilot. Reported as **log-OR long-COVID per 1 SD of allergic-disease
liability** (primary scale). This speaks to **broad allergic-disease liability only** — *not*
q0034's stronger atopy/MCAS-subgroup question; MCAS has no capturable footprint in this vehicle.

## Vehicles (frozen)

- **Exposure:** `dataset:gcst005038-allergic-disease-gwas` (Ferreira 2017; 180,129 EUR cases /
  180,709 EUR controls; full sumstats, 23andMe stratum excluded from the public file). Sample
  case-fraction **P = 180129 / 360838 = 0.4992**.
- **Outcome:** `dataset:covid19-hgi-longcovid-gwas` (HGI long COVID; European-*dominant*
  multi-ancestry, ~6,450 broad-definition cases). **Ancestry status is settled: WP1 previously
  found no public EUR-specific HGI stratum**, so this outcome is treated as **mechanics /
  robustness-only** from the outset — *not* re-investigated here. Step-2 does a **release-freshness
  check only** (confirm the current freeze/accession is the one used; record hash).
- **LD panel:** `dataset:1000g-eur-ld-panel` (Zenodo 6614170), EUR — ancestry-matched to the EUR
  exposure. Outcome is multi-ancestry, which is one reason the estimate is mechanics-grade.

## Frozen parameters

1. **Instrument scale (binary exposure).** Primary scale = **per-SD of latent liability**. Per-allele
   observed-scale log-ORs are converted to SD-liability units, and the instrument R² is transformed
   from the observed (ascertained case/control) scale to the **liability scale** via the Lee et al.
   2011 transformation, using threshold `T = Φ⁻¹(1−K)` and `z = φ(T)` with sample fraction P above.
   A per-log-OR-of-exposure scale is reported as a secondary/interpretation alternative, never
   swapped in as primary post-hoc.
2. **Prevalence sensitivity grid (frozen).** The liability transform depends on population prevalence
   K of the any-allergic-disease composite, which is high and uncertain. Report the full packet
   across **K ∈ {0.20, 0.30, 0.40}**, central **K = 0.30**. No single K is chosen post-hoc.
3. **Clumping (frozen, matches the Wave-1 pilot).** Genome-wide-significant lead variants at
   **p < 5×10⁻⁸**, local PLINK clumping **r² < 0.001**, **10 Mb** window, against the 1000G-EUR panel.
4. **HLA / MHC rule (a priori, frozen).** **Primary analysis excludes the extended MHC,
   chr6:25–34 Mb (GRCh37);** an HLA-inclusive run is reported only as a sensitivity contrast. (Atopy
   is far less HLA-driven than the autoimmune Wave-1 exposures, but the exclusion is fixed a priori
   for consistency and to keep the exclusion restriction defensible.)
5. **Detectable-effect floor (frozen).** Power is evaluated against the pre-registered floor
   **OR ≥ 1.20 per SD liability**, using `NCP = N_cases · R²_liability · (ln OR)²` with N_cases from
   the actual outcome file (controls ≫ cases ⇒ N_eff ≈ N_cases; two-sided α = 0.05). A null **below**
   this floor is uninformative, not evidence of no effect.
6. **Instrument strength (frozen).** Report per-instrument and mean **F-statistic**; F < 10 flags a
   weak instrument.

## GO / NO-GO decision rule (frozen, evaluated at Step 5)

**GO** (→ draft D-007b for execution) **iff all** hold:
- (i) **≥ 5** independent genome-wide-significant instruments survive clumping **and** MHC exclusion
  (enough to run IVW + MR-Egger + weighted-median pleiotropy-robust set);
- (ii) **mean F ≥ 10** (target ≫ 10, as the pilot's 76.4);
- (iii) empirical **liability-scale R²** yields **≥ 80% power at OR 1.20/SD** at the outcome case
  count, holding at least at central **K = 0.30** (report the full grid);
- (iv) exposure↔outcome (chiefly **UKB↔HGI**) **sample overlap is negligible (<~10%)** *or*
  **correctable** via the established MRlap route used in Wave-1 Task 4.

**NO-GO** (→ shelve atopy, mirroring the IM outcome) if: power < 80% at OR 1.20 even at the most
favorable K; **or** < 3 instruments survive MHC exclusion; **or** overlap is large **and**
uncorrectable.

**Inconclusive** (report as underpowered mechanics-only; do **not** draft D-007b) for anything
between. Even a GO yields a **mechanics/robustness-grade** result while the outcome lacks a EUR
stratum — D-007b would authorize execution at that grade, not reportable-primary MR.

## Deliverables (Step 5 packet)

A single GO/NO-GO record carrying: instrument table (rsID, chr:pos, EA/OA, β_logOR, SE, per-SNP
F); n instruments pre/post MHC exclusion; mean F; empirical R²_observed and R²_liability across the
K-grid; power at OR 1.20 across the K-grid; UKB↔HGI overlap estimate and whether MRlap-correctable;
outcome freshness/hash; and the GO/NO-GO/inconclusive verdict with the triggering criterion.
