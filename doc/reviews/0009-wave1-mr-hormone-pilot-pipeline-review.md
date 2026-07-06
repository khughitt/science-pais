---
reviews: "plan:0009-wave1-mr-hormone-pilot"
target_path: "entities/plans/0009-wave1-mr-hormone-pilot.md"
date: "2026-07-04"
overall: "WARN"
---

# Pipeline Review: Wave-1 MR Arm-B hormone pilot — sex-hormone liability → long-COVID

- **Reviews:** `plan:0009-wave1-mr-hormone-pilot` (`entities/plans/0009-wave1-mr-hormone-pilot.md`)
- **Date:** 2026-07-04
- **Overall:** WARN — execution-ready for its stated *exploratory-probe* goal; several pre-execution tightenings, none blocking the probe, but two should land before code is written (Dim 8: MRlap tooling reality) and before any result promotes (Dim 3: register the LDSC reference from an archival source; fix `consumed_by`).
- **Resolution (2026-07-04):** all findings folded into `plan:0009` in the commit following this review — the separate Python-`ldsc` munge stage / `ldsc.yaml` env dropped and MRlap documented as running LDSC+munge internally on raw sumstats + `ld`/`hm3` paths (Dim 8/5); `r-genomicsem` pinned by commit alongside `r-mrlap` (Dim 5); `MR_threshold`/`MR_pruning_dist`/`MR_pruning_LD` pinned and the naive↔MRlap instrument-set non-identity stated (Dim 8/1); the LDSC/HapMap3 reference required from an archival, checksummed source (not the Box link) with the entity + gate rerun before Task 4, and `plan:0009` added to `consumed_by` on the three datasets at Task 1 (Dim 3); the SHBG↔testosterone-coupling and weak-female-testosterone caveats added to Background + Task 5 (Dim 2). This report is retained as the point-in-time record.
- **Re-review (2026-07-04, revised plan):** original findings are materially addressed; **Overall remains WARN** because two narrow pre-execution issues remain: the plan now says MRlap receives "raw canonical-schema" sumstats, but it does not define the adapter/N-injection step that creates those files; and it pins most, but not all, MRlap instrument-selection parameters (`MR_reverse` is omitted).
- **Re-review resolution (2026-07-04):** both remaining issues folded in — a **hard-stop canonicalization adapter** (before the MRlap call) is now defined in Approach + Task 4, mapping each source family to MRlap-ready columns and injecting **total `N`** (case + control for the binary outcome, not effective N), with Task 1 recording the outcome's case/control N; and **`MR_reverse`** is added to the pinned instrument-selection params in Approach, Task 4, and Validation. Overall now WARN→clear for execution.

## Summary

`plan:0009` is a disciplined, honestly-caveated `probe` — it inherits `plan:0008`'s
two hard ceilings (ancestry flag KD1, bounded-sex read KD3) verbatim, carries the
KD-scale MRlap contract, and — unlike its predecessor — already mandates the
genome-wide MRlap **scale/resource run on real data** the pipeline rubric demands
(Dim 6 PASS). The material findings are not about the MR logic but about the MRlap
integration: the plan's mental model of the LDSC step (a separate Python-`ldsc`
munge stage feeding MRlap) does not match how MRlap actually works — it runs
cross-trait LDSC internally in R (via GenomicSEM), munges raw sumstats itself, and
selects its own instruments by internal distance-pruning. That has three concrete
consequences (a redundant/misspecified `ldsc.yaml` env, an unpinned GenomicSEM
dependency, and a naive-vs-MRlap instrument-set non-identity) that should be
reconciled before WP1 builds the infrastructure. Separately, the `eur_w_ld_chr` /
HapMap3 reference is a load-bearing input with no dataset entity yet, and its
canonical source is a fragile Box share link — the same archival hazard the 1000G
panel had to be hardened away from in `plan:0007`.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | PASS | Params inherited from `plan:0007`/`0008` conventions; no `[UNVERIFIED]`. MRlap internal pruning params (`MR_pruning_dist`/`MR_pruning_LD`) not pinned in the plan |
| Assumption audit | WARN | SHBG and total-testosterone instruments overlap heavily and are mechanistically coupled → not two independent exposures; the female-testosterone stratum (the arm most relevant to female-predominance) is the one most likely to be weak/sparse |
| Data availability | WARN | LDSC/HapMap3 reference is a load-bearing MRlap input with **no `dataset:` entity** (rubric-letter FAIL, deferred to Task 1); canonical source is a Box share link (not archival/checksummed); the three existing datasets pass verification but their `consumed_by` omit `plan:0009` |
| Identifiability | PASS | Mechanics reachable end-to-end; scientific estimand deliberately non-primary (ancestry flag), and the plan says so |
| Reproducibility | WARN | Seeds + conda-lock + MRlap-pinned-by-commit specified; but GenomicSEM (MRlap's LDSC engine, GitHub-only) not pinned, and the `ldsc.yaml` python env is likely the wrong dependency (see Dim 8) |
| Validation criteria | PASS | Task 4 explicitly mandates the genome-wide munge+MRlap real-data run with peak-memory + wall-clock recorded — exactly the Dim-6 scale/resource requirement |
| Scope check | PASS | Within D-005 (Ruth vehicle) + D-006 (LDSC/HapMap3 infra; same HGI outcome vehicle; no FinnGen); within `specs/scope-boundaries.md` |
| Integration boundaries | WARN | MRlap runs LDSC+munge internally and takes raw sumstats + `ld`/`hm3` paths → the separate munge stage is redundant; MRlap prunes instruments internally by distance → naive-arm and MRlap-arm are **not** on the same instrument set |
| Manifest completeness | PASS | Task 5 requires `datapackage.json` + entity cross-refs + provenance DAG, `qa_report.{json,md}`, `run_metadata.json` (seeds/versions/pinned-MRlap-commit/SHA-256), env locks |

## Detailed Findings

### Dimension 8 — Integration boundaries (WARN) — the load-bearing finding

I verified MRlap's actual interface against its README (n-mounier/MRlap). Two boundary
mismatches with how the plan describes the step:

1. **MRlap does cross-trait LDSC and munging internally; there is no separate
   Python-`ldsc` stage.** MRlap "builds up on the GenomicSEM R-package to perform
   cross-trait LDSC," accepts **raw** summary statistics (data frame or gz file with
   `rsid/chr/pos/a1/a2/Z or beta+se/N`), and takes two file-path arguments — `ld`
   (the `eur_w_ld_chr` folder) and `hm3` (the HapMap3 snplist). It munges and runs
   LDSC itself. The plan's Task 4 ("**Munge** each exposure + the outcome genome-wide
   to HapMap3, run MRlap …") and the `ldsc.yaml` "LDSC / munge infra env" (inherited
   from `plan:0008`'s architecture) describe a Python-`ldsc` munge pipeline that MRlap
   does not need. **Recommendation:** drop the separate munge stage and the Python
   `ldsc.yaml` env; the real new dependency is **R GenomicSEM** (+ MRlap), fed raw
   canonical-schema sumstats plus the `ld`/`hm3` paths. If a Python `ldsc` env is kept
   for anything, name what actually uses it — otherwise it is dead infrastructure that
   will be built and locked for nothing.

2. **MRlap selects its own instruments by internal distance-pruning — so the
   "MRlap beside naive IVW" comparison is not on a shared instrument set.** MRlap
   parameters: `MR_threshold` (default 5e-8), `MR_pruning_dist` (default 500 kb),
   `MR_pruning_LD` (default off → distance-only), plus an automatic Steiger-like
   exclusion of IVs more strongly associated with the outcome (p < 1e-3). The naive
   arm, by contrast, clumps against the staged **1000G-EUR panel at r² < 0.001 / 10 Mb**
   (Task 2). The two arms therefore instrument differently, and MRlap does **not** use
   the 1000G panel at all under defaults. The consequence: the naive-vs-corrected delta
   conflates the overlap/weak-instrument correction (what you want to read) with a
   change of pruning scheme (a nuisance). **Recommendation:** pin `MR_pruning_dist` /
   `MR_pruning_LD` explicitly in `config.yaml`, and in the write-up state that the
   MRlap correction and the naive IVW are on different instrument sets — do not read
   the whole difference as "overlap bias." (This does not break the plan; the two are
   already correctly kept on different *scales* per KD-scale — this adds the parallel
   instrument-set caveat.)

The one boundary the plan already handles well: the **effect-scale** boundary (log-OR
TwoSampleMR vs standardised/observed MRlap) is explicitly not-merged (KD-scale), and
the assembly/rsID boundary (Ruth GRCh37-native, outcome GRCh38, `ld`/`hm3` keyed by
rsID) is reconciled at Task 1.

### Dimension 3 — Data availability (WARN; rubric-letter FAIL on the LDSC reference)

The three declared datasets verify cleanly (all `origin: external`,
`access.verified: true`, `verification_method` set, `last_reviewed` 2026-07-03/04,
`source_url` populated). Findings:

- **The `eur_w_ld_chr` + HapMap3 LDSC reference is a load-bearing input with no
  `dataset:` entity.** By the rubric letter ("a source does not resolve to a dataset
  entity" → FAIL). This is the exact parallel of `plan:0007`'s 1000G-panel finding: the
  LD-score reference *determines the cross-trait LDSC intercept, hence the overlap
  fraction, hence the corrected estimate* — it is not cosmetic infrastructure. The plan
  makes Task 1 create the entity, which is the retrieval-probe exception and is
  acceptable **provided** (a) the entity is created and the data-access gate reruns
  green *before* Task 4 consumes it, and (b) it pins an **archival, checksummed** source.
  MRlap's README points at a **UT Austin Box share link** for `eur_w_ld_chr`/`hm3` —
  a non-archival, non-checksummed, single-host URL, precisely the fragility that forced
  `plan:0007` to move the 1000G panel from the plain-http MRC-IEU fileserve to a Zenodo
  DOI. **Recommendation:** source `eur_w_ld_chr` + `w_hm3.snplist` from a DOI-archival,
  checksummed mirror (record SHA-256), not the Box link; treat the Box link as
  provenance only.
- **`consumed_by` drift.** `ruth-2020-shbg-testosterone-gwas`,
  `covid19-hgi-longcovid-gwas`, and `1000g-eur-ld-panel` all list `plan:0008` (and
  `plan:0007` where relevant) but **not** `plan:0009`. WARN (missing canonical
  `plan:<stem>` backlink). Fix as part of Task 1's entity pass (the plan already says it
  will, but list it explicitly so the gate closes).

### Dimension 2 — Assumption audit (WARN)

Ceilings are handled correctly (ancestry flag, bounded-sex read carried verbatim; the
no-MHC-exclusion call is right — hormone architecture is not HLA-dominated, and the
*cis*-SHBG signal on chr17 is a legitimate instrument, not an MHC concern). Two caveats
to carry into the write-up:

- **SHBG and total-testosterone are not two independent exposures.** SHBG genetically
  and physiologically determines bioavailable testosterone; their instrument sets
  overlap and the traits are mechanistically coupled (Ruth 2020 [@Ruth2020] itself foregrounds
  this). Running them as two arms risks double-counting a shared signal, and horizontal
  pleiotropy via the broader steroid axis (estradiol, bioavailable T) is plausible.
  MR-Egger + weighted-median partially bound it; state that a "clean" IVW is not
  pleiotropy-free here, mirroring the `plan:0007` SLE caveat.
- **The scientifically most-relevant stratum is the weakest-instrumented one.** The
  female-only **testosterone** GWAS has far fewer genome-wide-significant loci and
  smaller effects than the male stratum — yet the female hormone arm is exactly the one
  bearing on `question:0007`/`hypothesis:0005` (female predominance). The mean-F > 10
  halt (Task 2) will catch collapse, but flag up front that a NO-GO or a wide,
  uninformative female-testosterone estimate is a likely — and itself informative —
  outcome, not a pipeline failure.

### Dimension 5 — Reproducibility (WARN, near PASS)

Fixed weighted-median RNG seed, conda-lock env, MRlap pinned by git commit, Snakemake
`--use-conda` — all specified and good. Gap tied to Dim 8: **GenomicSEM is MRlap's
LDSC engine and is GitHub-only (no CRAN release)** — it must be pinned by commit in the
env alongside MRlap, or the "reconstructable toolchain" has an unpinned transitive
dependency. And if the `ldsc.yaml` Python env survives Dim-8 triage, justify it; if not,
removing it *improves* reproducibility (one fewer locked env to drift).

## Re-review After Revision (2026-07-04)

The revised `plan:0009` closes the original review's material findings: MRlap is now
modeled as an R/GenomicSEM-internal LDSC+munge step; GenomicSEM is pinned; the
naive-vs-MRlap instrument-set non-identity is explicit; LDSC/HapMap3 is hardened to
an archival/checksummed source; and the SHBG↔testosterone plus weak-female-testosterone
caveats are carried into the plan. Two residual execution-contract findings remain.

### R1 — MRlap input canonicalization and total-N injection are not yet an explicit task (WARN)

`plan:0009` now correctly says MRlap should receive **raw canonical-schema genome-wide
sumstats** plus `ld`/`hm3` paths (`entities/plans/0009...` lines 83-87 and 146-149).
But the plan does not define how the GWAS Catalog SSF/Ruth/HGI files become that
canonical MRlap schema, nor where the required total-`N` column is verified or injected.

This matters because MRlap is not schema-free. Its documented input columns include
rsID, chr, pos, effect/ref alleles, Z or beta+SE, and `N`; for case-control GWAS the
sample-size column must be total sample size, not effective N. The existing
`plan:0007` code resolves SSF columns only for the SLE pilot path, and `plan:0009`
does not carry forward `plan:0008`'s explicit `source_adapters.yaml` /
`adapt_sumstats.py` contract. A future Task 4 can therefore be "correct" about MRlap
while still failing at runtime or silently using the wrong N/allele columns.

**Recommendation:** add a Task 1/Task 4 precondition that creates canonical
MRlap-ready files for each Ruth stratum and the HGI outcome, with a per-source adapter
contract and row-level smoke tests. Hard-stop if rsID/chr/pos/alleles/beta/SE-or-Z/p
or total `N` cannot be constructed; for `GCST90454541`, explicitly inject or verify
case+control total N from the source metadata, not effective N.

### R2 — Pin `MR_reverse` along with the other MRlap pruning parameters (WARN, small)

The revision now pins `MR_threshold`, `MR_pruning_dist`, and `MR_pruning_LD` in
`config.yaml` (`entities/plans/0009...` lines 90-97 and 146-155). That closes the
main instrument-set caveat. One MRlap instrument-selection parameter is still missing:
`MR_reverse` (default `1e-3`), which excludes instruments more strongly associated
with the outcome than the exposure. It affects the final MRlap instrument set just as
surely as the pruning parameters.

**Recommendation:** pin and record `MR_reverse: 0.001` in `config.yaml` and
`run_metadata.json` (or explicitly choose another value). Also record `do_pruning=TRUE`
and the fact that `MR_plink`/`MR_bfile` are unused when `MR_pruning_LD=0`, so the
MRlap instrument-selection surface is fully auditable.

### Dimension 6 — Validation criteria (PASS)

Notable strength: Task 4 explicitly requires running "the full genome-wide munge +
MRlap on the staged sumstats with **peak memory + wall-clock recorded**." This is the
real-data scale/resource discipline the rubric calls for, and it is the one MRlap step
where it genuinely bites (genome-wide LDSC over HapMap3 is the resource-heavy operation,
unlike the pilot's instrument-only streaming). Retain it as a hard gate.

## Recommendations

1. **Reconcile the MRlap tooling model before WP1 builds infrastructure (Dim 8/5).**
   MRlap munges + runs cross-trait LDSC internally from raw sumstats given `ld`/`hm3`
   paths; drop the separate Python-`ldsc` munge stage and `ldsc.yaml` env unless
   something else uses it, and pin **GenomicSEM** (GitHub, by commit) alongside MRlap.
2. **Register the LDSC/HapMap3 reference as a first-class dataset from an archival,
   checksummed source (Dim 3)** — not the UT Austin Box link — before Task 4 consumes
   it, and rerun the data-access gate. Mirror the 1000G Zenodo-hardening precedent.
3. **Pin MRlap's internal pruning (`MR_pruning_dist`, `MR_pruning_LD`) in `config.yaml`
   and state the instrument-set non-identity (Dim 8/1)** — the naive IVW and MRlap
   estimates are on different instrument sets *and* different scales; report both
   caveats so the delta is not over-read as pure overlap bias.
4. **Add `plan:0009` to `consumed_by`** on the three existing datasets during Task 1
   (Dim 3), and carry the two assumption caveats — SHBG↔testosterone coupling, and the
   weak female-testosterone stratum — into the Task 5 write-up (Dim 2).

## Strengths

- Correctly proportioned `probe`: one arm, both `plan:0008` ceilings carried verbatim,
  explicitly exploratory/non-primary — no over-expansion back toward the banked design.
- Already satisfies the Dim-6 real-data scale/resource requirement that `plan:0007` only
  got as a review recommendation — the plan internalised the prior review's lesson.
- The scale discipline (KD-scale: log-OR vs standardised, not-merged) and the
  no-MHC-exclusion reasoning are both correct and explicitly defended.
- Cleanly in D-005/D-006 authorisation and project scope; FinnGen correctly absent.
