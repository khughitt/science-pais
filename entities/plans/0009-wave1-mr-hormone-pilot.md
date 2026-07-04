---
id: "plan:0009-wave1-mr-hormone-pilot"
type: "plan"
plan_kind: "pipeline"
title: "Wave-1 MR Arm-B hormone pilot: sex-hormone liability → long-COVID (overlap-corrected, ancestry-flagged exploratory)"
status: "active"
created: "2026-07-04"
updated: "2026-07-04"
related:
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "question:0013-reproductive-stage-failed-immune-recovery-after-infection"
  - "plan:0008-wave1-mr-autoimmune-hormone-longcovid-design"
  - "plan:0007-wave1-mr-autoimmune-longcovid-pilot"
  - "task:t089"
  - "dataset:ruth-2020-shbg-testosterone-gwas"
  - "dataset:covid19-hgi-longcovid-gwas"
  - "dataset:1000g-eur-ld-panel"
  - "dataset:eur-ldsc-ld-score-reference"
---

# Wave-1 MR Arm-B hormone pilot: sex-hormone liability → long-COVID

## Goal

Run the **sex-hormone arm** of the Wave-1 MR line end to end — genetic liability to
SHBG and total testosterone (sex-combined **and** sex-specific) as exposures,
long-COVID liability as outcome — with **MRlap sample-overlap correction**, as a
scoped, explicitly **ancestry-flagged, exploratory** probe. It derisks the new
mechanics the SLE pilot (`plan:0007`) did not exercise (sex-stratified hormone
instruments, the LDSC/MRlap overlap-correction stack) and returns a first,
honestly-caveated read on whether germline hormone liability moves long-COVID risk.

## Background

`plan:0008` (the full reportable design) is **banked**: WP1 proved no matched EUR
long-COVID outcome is publicly downloadable, so nothing can be a reportable
*primary* estimate until a matched outcome appears (see `plan:0008` status banner +
WP1 finding). The re-scope decision (2026-07-04) is to pursue the single novel,
high-value line now — the hormone arm — as an exploratory probe, because it targets
the project's central sex/female-predominance question (`hypothesis:0005`,
`question:0007`, `question:0013`) and is informative **even ancestry-flagged**. This
is the hormone analogue of `plan:0007`: mechanics-derisk plus a first exploratory
signal, **not** a reportable scientific verdict. It runs within D-005/D-006
authorisation (Ruth exposure + LDSC/HapMap3 infrastructure are both in-scope per
D-006; the outcome is the same authorised HGI vehicle).

**Two hard caveats carried from `plan:0008`, load-bearing here:**
- **Ancestry flag (KD1 demotion).** The outcome is the European-dominant (~85–90%)
  *multi-ancestry* HGI broad/population meta (`GCST90454541`); no EUR-only file
  exists. Every estimate is flagged and **non-primary** — exploratory/robustness
  only, never reported as primary hypothesis evidence.
- **Bounded sex read (KD3).** With a mixed-sex outcome, male-only and female-only
  hormone instruments give a **bounded exposure-architecture** probe (concordant vs
  discordant hormone-predictor associations with a common outcome) — **not** a
  genotype × sex effect-modification test. No sex-modification claim is made.

**Two exposure-side assumption caveats (interpretation, not ceilings):**
- **SHBG and total testosterone are not independent exposures.** SHBG sets
  bioavailable testosterone and the two share instrument loci (Ruth 2020), so a shared
  signal can be double-counted and steroid-axis horizontal pleiotropy is plausible —
  MR-Egger + weighted-median partially bound it; a "clean" IVW is not pleiotropy-free.
- **The most decision-relevant stratum is the weakest-instrumented.** The female-only
  testosterone GWAS has the fewest genome-wide hits and smallest effects, yet the female
  hormone arm is exactly the one bearing on the female-predominance question — a NO-GO or
  a wide female-testosterone estimate is a likely, itself-informative outcome, not a
  pipeline failure.

## Approach

Two-sample MR on the pilot's proven `TwoSampleMR` toolchain (`plan:0007` harness,
extended). Exposures: Ruth 2020 SHBG and total testosterone, three strata each
(sex-combined, male-only, female-only), instrumented by genome-wide-significant
SNPs, LD-clumped locally against the staged 1000G-EUR panel (r² < 0.001, 10 Mb).
Unlike the SLE instrument, hormone GWAS are **not** HLA-dominated, so **no extended-
MHC exclusion** is pre-committed (standard clumping suffices; the strong *cis*-SHBG
signal is retained as a legitimate instrument). Outcome effects extracted by rsID
streaming from `GCST90454541` (the pilot's scale discipline).

Estimators: **naive IVW / MR-Egger / weighted-median** (log-OR outcome), instrumented
by the 1000G-EUR-clumped set above, as the uncorrected comparator; then **MRlap**
(Mounier & Kutalik 2023) for joint sample-overlap + weak-instrument + winner's-curse
correction — **mandatory here** because Ruth is 100% UK Biobank and the HGI outcome
pools UKB (structural overlap). **MRlap runs cross-trait LDSC and munging internally
in R** (it builds on GenomicSEM): it is handed **raw canonical-schema genome-wide
sumstats** for each trait plus the `eur_w_ld_chr` LD-score folder (`ld`) and the
HapMap3 snplist (`hm3`) as path arguments — there is **no separate Python-`ldsc` munge
stage**. Those "raw canonical-schema" files are produced by a **hard-stop
canonicalization adapter** (before the MRlap call) that maps each source family
(GWAS Catalog harmonised SSF, Ruth strata, HGI outcome) to MRlap's required columns —
rsID, chr, pos, effect/other allele, `Z` **or** `beta`+`SE`, and **`N`** — failing loud
on any missing column or unresolved `N`. It applies the `plan:0008` **KD-scale
contract**: `N` is **total sample size** (for the binary long-COVID outcome, total =
case + control from the recorded counts, observed scale, **not** effective N; Ruth
carries its continuous-trait N); effect reported in its **native standardised/observed
scale beside** the naive log-OR IVW — the two are **not** merged as one like-for-like
estimate. **Instrument-set caveat:** MRlap selects and prunes its own instruments
internally by distance (`MR_pruning_dist`, default 500 kb; `MR_pruning_LD` off by
default → distance-only; `MR_reverse` outcome-exclusion default 1e-3) and does not use
the 1000G-EUR panel, so the MRlap and naive arms are **not on the same instrument set**;
the instrument-selection params (`MR_threshold`, `MR_pruning_dist`, `MR_pruning_LD`,
`MR_reverse`) are pinned in `config.yaml` and the non-identity is stated in the write-up
so the naive↔corrected delta is not read as pure overlap bias. MRlap **and GenomicSEM** (its
internal LDSC engine; both GitHub-only, no CRAN/tagged release) are **pinned by git
commit**. Weighted-median SE is bootstrapped → **fixed RNG seed** recorded.
Reproducibility: extend the `plan:0007` conda-lock env with `r-mrlap` + `r-genomicsem`
(both pinned by commit) — **no Python-`ldsc` env is needed**; run under Snakemake
`--use-conda`. Payloads gitignored under `data/`; outputs + manifest under
`results/wave1-mr-hormone-pilot/`.

## Inputs

- **Exposures** — `dataset:ruth-2020-shbg-testosterone-gwas`: SHBG (male
  GCST90012109 / female GCST90012107 / combined GCST90012111) and total testosterone
  (male GCST90012113 / female GCST90012112 / combined GCST90012114) harmonised
  `fullPvalueSet` files (European UKB; continuous traits, SD-scaled effects; native
  GRCh37, harmonised GRCh38 served — resolve the entity's UNKNOWN assembly at Task 1).
- **Outcome** — `dataset:covid19-hgi-longcovid-gwas` `GCST90454541` (broad/population;
  binary, log-OR; **European-dominant multi-ancestry** — the ancestry flag).
- **LD panel** — `dataset:1000g-eur-ld-panel` (Zenodo 6614170; local plink clumping),
  reconciled to GRCh38 by rsID as in `plan:0007`.
- **MRlap infrastructure (new, in-scope per D-006)** — `dataset:eur-ldsc-ld-score-reference`:
  `eur_w_ld_chr` EUR LD-score reference (pinned to the **DOI-archival, checksummed**
  Zenodo record 8182036, md5 `e2f16343…`, CC-BY-4.0 — **not** the UT-Austin Box share
  link, mirroring the `plan:0007` 1000G Zenodo-hardening) + the HapMap3 (`w_hm3.snplist`)
  list (archival source confirmed at staging). Entity created; per-file SHA-256 +
  extracted contents recorded at Task 1 under the retrieval-probe exception; the
  data-access gate reruns before Task 4 consumes it.
- `TwoSampleMR`, `MRlap` + `GenomicSEM` (MRlap's internal cross-trait LDSC engine),
  `MendelianRandomization`, local `plink` (naive-arm clumping only).
- Scale/overlap contract: `plan:0008` KD2 + KD-scale; bounded-sex framing: `plan:0008` KD3.

## Tasks

1. **Stage inputs + infrastructure.** Retrieve the six Ruth strata + `GCST90454541`
   (harmonised `fullPvalueSet`) into `data/raw/gwas/`; stage `eur_w_ld_chr` + HapMap3
   (from an **archival, checksummed source — not the Box link**) and the 1000G-EUR
   panel. Record SHA-256 / build / rows for each **plus the outcome's case/control N**
   (needed for MRlap total-N injection at Task 4); resolve the Ruth entity's assembly
   label and upgrade its `verification_method`; create the LDSC-reference dataset entity
   (archival source, SHA-256, build/ancestry, rsID-key policy); **add `plan:0009` to
   `consumed_by`** on `ruth-2020-shbg-testosterone-gwas`, `covid19-hgi-longcovid-gwas`,
   and `1000g-eur-ld-panel`; rerun the data-access gate (**must pass before Task 4**).
   Confirm the LD-score / HapMap3 build+ancestry reconcile (rsID) with the GRCh37-native
   Ruth and the GRCh38 outcome.
2. **Build hormone instruments.** Per trait × stratum (SHBG/testosterone ×
   combined/male/female), filter to p < 5×10⁻⁸, LD-clump locally (r² < 0.001, 10 Mb;
   **no MHC exclusion** — hormones are not HLA-dominated), compute per-instrument +
   mean F = (beta/se)². Halt loud if a stratum's mean F < 10.
3. **Naive MR (comparator).** Harmonise (`action = 2`) and run IVW / MR-Egger /
   weighted-median (log-OR outcome; seeded weighted-median) on the **1000G-EUR-clumped**
   instruments for each trait × stratum; report per/mean F, Egger intercept, and
   IVW/Egger/WM concordance. Stream the outcome extraction by rsID (record peak memory +
   wall-clock).
4. **Canonicalize + MRlap overlap correction.** First run the **hard-stop
   canonicalization adapter**: map each source family (GWAS Catalog harmonised SSF,
   Ruth strata, HGI outcome) to MRlap-ready columns — rsID, chr, pos, effect/other
   allele, `Z` or `beta`+`SE`, and **total `N`** (inject total = case + control for the
   binary outcome, **not** effective N; Ruth carries its continuous-trait N) — failing
   loud on any missing column or unresolved `N`. Then pass each exposure + the outcome
   as **raw canonical-schema genome-wide sumstats** to MRlap with the `eur_w_ld_chr`
   (`ld`) and HapMap3 (`hm3`) paths — MRlap munges and runs cross-trait LDSC internally;
   pin `MR_threshold` / `MR_pruning_dist` / `MR_pruning_LD` / `MR_reverse` in
   `config.yaml`. Record the
   **estimated UKB overlap fraction** and the corrected effect in its **native scale**,
   beside the naive IVW, **noting that MRlap's internally distance-pruned instrument set
   differs from the naive 1000G-clumped set**. **Scale/resource validation on real
   data:** run the full genome-wide MRlap (internal munge + LDSC) on the staged sumstats
   with **peak memory + wall-clock recorded** (the new, untested resource step). Label
   the scale of every estimate.
5. **Write-up + go/no-go.** One results note: the mechanics outcome, the exploratory
   (ancestry-flagged, non-primary) hormone→long-COVID signal, and the **bounded**
   male-vs-female exposure-architecture concordance/discordance (KD3 — no
   sex-modification claim). State the two exposure-side caveats explicitly: the
   naive↔MRlap **instrument-set non-identity** (the delta is not pure overlap bias) and
   the **SHBG↔testosterone coupling** (shared instruments / steroid-axis pleiotropy);
   flag any female-testosterone weak-instrument outcome as informative, not a failure.
   Recommend whether the deferred `plan:0008` full design is worth resuming if/when a
   matched EUR outcome appears, and whether the MRlap stack is sound. Emit the
   reproducible bundle under `results/wave1-mr-hormone-pilot/` (datapackage.json with
   entity cross-refs + provenance DAG; qa_report.{json,md} with structural hard-stops
   incl. overlap fraction + scale labels + resource; run_metadata.json with
   seeds/versions/**pinned MRlap + GenomicSEM commits**/SHA-256s; env locks).

## Decision criteria

Mechanics **GO** (the deferred design's hormone stack is proven) if all hold:

- All six Ruth strata + the outcome retrieve, parse, and yield sane row counts;
  LD-score/HapMap3 reconcile with the sumstats.
- Each hormone stratum retains a workable independent instrument set (target ≳ 10)
  with **mean F > 10**.
- Naive IVW/Egger/weighted-median return finite, sane estimates with computable Egger
  intercept and reported concordance.
- **MRlap runs** (internal munge + cross-trait LDSC), records the UKB overlap fraction,
  and returns a corrected estimate in a **clearly labelled native scale** (not merged
  with the log-OR IVW); the genome-wide MRlap resource cost is recorded.

**Interpretation ceiling (both bars hold, always).** Every estimate is
**ancestry-flagged and non-primary** (KD1) and any sex read is a **bounded
exposure-architecture** probe (KD3). No result is reported as primary hypothesis
evidence for `hypothesis:0005` / `question:0007` / `question:0013`, or as any
sex-modification claim — that awaits a matched EUR outcome (+ the `plan:0008`
acceptance gate) and, for sex-modification, a sex-stratified outcome that does not
yet exist.

**NO-GO / fix-first** if a hormone stratum collapses below the weak-instrument floor,
MRlap cannot run or reconcile scales, or the LD-score reference cannot be matched —
surface and repair before any hormone result is quoted even as exploratory.

## Validation

- Per-file SHA-256 / build / row counts recorded; Ruth assembly resolved; LDSC-ref
  entity created from an **archival, checksummed source** and gate-passing; `plan:0009`
  added to `consumed_by` on the three consumed datasets.
- Every instrument SNP p < 5×10⁻⁸ in its exposure stratum; per/mean F reported.
- Harmonisation `action = 2` drop-log present and non-silent; weighted-median RNG
  seed recorded.
- Canonicalization adapter ran with a **non-silent hard-stop** on missing columns /
  unresolved `N`; MRlap `N` is **total** (case + control for the outcome), not effective.
- MRlap overlap fraction, corrected estimate, and its **native scale label** present;
  no cross-scale comparison presented as like-for-like; **MRlap instrument-selection
  params (`MR_threshold`/`MR_pruning_dist`/`MR_pruning_LD`/`MR_reverse`) pinned and the
  naive↔MRlap instrument-set non-identity stated**; genome-wide resource (peak mem +
  wall-clock) recorded.
- MRlap **and GenomicSEM** commits pinned; no Python-`ldsc` env in the lock set.
- Every output carries the **ancestry-flag** and **non-primary / bounded-sex** labels.
- Full bundle under `results/wave1-mr-hormone-pilot/`; `git status` shows nothing
  under `data/`.

## Out of scope

- **Arm A (SLE → long-COVID) sensitivity matrix**, **bidirectional MR**, **formal
  pre-registration**, and the **acceptance-gate-for-primary** — all deferred with the
  banked `plan:0008`.
- **Any reportable-primary or sex-modification claim** — barred by the two ceilings.
- **A EUR-matched / EUR-only outcome and FinnGen** — none downloadable / held (D-006).
- **BMI-adjusted hormone strata and bioavailable-testosterone / estradiol** — the
  combined/male/female SHBG + total-testosterone strata are the pilot's scope;
  additional hormone traits are a later increment.

## Notes on plan scope

A deliberate one-arm `probe`, not a re-expansion of `plan:0008`: the point is to
derisk the hormone/MRlap mechanics and get a first honest (flagged) signal on the
project's central sex question, proportionate to what a demoted line can deliver now.
It is sized like `plan:0007` — plus the MRlap/LDSC stack, which is the one genuinely
new mechanism it exists to prove. Grow back to `plan:0008` only when a matched EUR
outcome lifts the ancestry ceiling.
