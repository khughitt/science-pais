# Pipeline Review: Wave-1 MR pilot — autoimmune liability → long-COVID

- **Reviews:** `plan:0007-wave1-mr-autoimmune-longcovid-pilot` (`entities/plans/0007-wave1-mr-autoimmune-longcovid-pilot.md`)
- **Date:** 2026-07-04
- **Overall:** WARN — execution-ready for its stated *mechanics* goal; four pre-execution tightenings recommended, none blocking the probe itself.
- **Resolution (2026-07-04):** all four recommendations were folded into `plan:0007` in the commit following this review — `dataset:1000g-eur-ld-panel` registered (Dim 3); weighted-median RNG seed + `renv.lock` required (Dim 5); streaming outcome-extraction with peak-memory/wall-clock recording (Dim 6); `datapackage.json` entity cross-references + provenance DAG (Dim 9); clumping-threshold default provenance noted (Dim 1). This report is retained as the point-in-time record.

## Summary

The plan is an honest, well-scoped `probe`: it is explicit that it derisks
pipeline mechanics and is *not* a scientific verdict, and the recent fixes
(corrected outcome stratum GCST90454541, ancestry mechanics-only hard-stop,
pinned GWAS-SSF→TwoSampleMR boundary, reproducible-output contract) closed the
biggest gaps. What remains are reproducibility and data-governance tightenings
that matter precisely *because* D-005's whole justification is
third-party-reproducibility: the LD reference panel is a load-bearing input with
no dataset entity (Dim 3), and the weighted-median SE bootstrap has no fixed seed
(Dim 5). Neither blocks the mechanics run, but both should be fixed before the
result is trusted or promoted into `plan:0008`.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | PASS | Clumping thresholds/`action=2` stated as TwoSampleMR defaults but not explicitly sourced; no `[UNVERIFIED]` in plan |
| Assumption audit | WARN | SLE instruments are heavily pleiotropic immune loci → exclusion-restriction non-trivial; outcome (long-COVID) is a coarse proxy for h0007's SFN/dysautonomia claim |
| Data availability | WARN | LD reference panel is a load-bearing input with **no `dataset:` entity** (rubric-letter FAIL); two sumstats otherwise pass; runtime files deferred to Task 1 (retrieval-probe exception) |
| Identifiability | PASS | Mechanics goal reachable end-to-end; scientific estimand deliberately *not* identifiable (ancestry hard-stop), and the plan says so |
| Reproducibility | WARN | No RNG seed for the weighted-median bootstrap SE; versions recorded but not pinned to an env lockfile |
| Validation criteria | WARN | Strong structural hard-stops, but no explicit **scale/resource** discipline for the multi-GB HGI outcome file |
| Scope check | PASS | Squarely within D-005's scope-limited authorization; no creep |
| Integration boundaries | PASS | SSF→TwoSampleMR and LD-build↔sumstats-build boundaries both explicitly specified with hard-stops |
| Manifest completeness | WARN | `datapackage.json` + provenance required, but entity cross-references / provenance-DAG structure not explicitly mandated |

## Detailed Findings

### Dimension 3 — Data availability (WARN; rubric-letter FAIL on the LD panel)

The two summary-statistics inputs pass cleanly: both are `origin: external`,
`access.verified: true` with `verification_method` and `last_reviewed: 2026-07-03`
(< 12 months), `source_url` populated, and `consumed_by` now includes
`plan:0007`. Their runtime files are absent, but Task 1 is the "retrieve and
verify" step and `access.verified` is already true — the retrieval-probe
exception applies, so this is PASS-with-note (deferred-to-Task-1), not FAIL.
`identity_context.assembly.label` is still `UNKNOWN` on both; the plan resolves
it in Task 1 (both harmonised files are GRCh38), which is acceptable.

The real finding: **the 1000G-EUR LD reference panel is a load-bearing data
input with no `dataset:` entity.** By the rubric letter ("a source does not
resolve to a dataset entity" → FAIL) this is a Dim-3 failure. It is not
cosmetic: the panel *determines which SNPs survive clumping*, hence the
instrument set, hence the estimate — and D-005's authorization rests on
third-party-reproducibility, which a version/build/checksum-pinned, independently
retrievable LD panel is central to. The plan's inline staging contract
(source/version/build/SHA-256/path) is good mitigation and appropriate to probe
scope, but the project's own standard is a first-class dataset entity.
**Recommendation:** register `dataset:1000g-eur-ld-panel` (reference class) with
the exact release and build before promoting any result to `plan:0008`; for the
probe itself, the inline contract is a defensible interim if the deferral is
recorded as a known risk.

### Dimension 5 — Reproducibility (WARN)

The `run_metadata.json` contract (tool + R-package versions, all parameters,
input SHA-256s, producing git commit) is strong. Two gaps:

1. **Weighted-median bootstrap seed.** TwoSampleMR computes the weighted-median
   standard error by bootstrap (default 1,000 iterations); without a fixed RNG
   seed the reported SE is not bit-reproducible run-to-run. IVW and MR-Egger are
   closed-form and need no seed. **Fix:** set and record an explicit seed for the
   weighted-median (and any bootstrapped diagnostic) in `run_metadata.json`.
2. **Environment pinning.** Versions are *recorded* but not *pinned* — a reader
   re-running later may resolve different package versions. **Fix:** commit an
   `renv.lock` (or conda/`environment.yml`) so the toolchain is reconstructable,
   not merely described.

### Dimension 6 — Validation criteria (WARN)

Structural hard-stops (required-column presence, allele coding, instrument count,
mean F, palindromic-drop count, ancestry/build reconciliation) are well
specified. The gap is **scale/resource behavior on real data**: the GCST90454541
harmonised full-p-value file is a population-control meta (N≈1.1M) spanning tens
of millions of variants — a multi-GB file. The plan should mandate **streaming /
selective extraction** of the instrument SNPs from the outcome (not a full
in-memory `fread`) and record **peak memory + wall-clock** in `qa_report`. Task 3
implies selective extraction but does not pin the memory discipline or require
the resource observation the command's Dim-6 calls for.

### Dimension 2 — Assumption audit (WARN)

Handled appropriately for a mechanics probe (relevance via mean-F>10; pleiotropy
via MR-Egger + weighted-median; MHC excluded a priori). Two caveats to carry into
`plan:0008`, both consistent with the mechanics-only framing:

- **Exclusion restriction is non-trivial for SLE.** The instrument loci (IRF5,
  STAT4, BLK, TNFAIP3, ITGAM, …) are shared, pleiotropic immune-regulatory
  variants that plausibly affect a post-infectious outcome through immune
  pathways not routed via SLE liability per se. MHC exclusion removes the largest
  pleiotropy hotspot and Egger/weighted-median partially bound the rest, but a
  clean IVW estimate should not be read as pleiotropy-free.
- **Outcome is a coarse proxy for the target hypothesis.** `hypothesis:0007` is
  specifically about an autoimmune *small-fiber-neuropathy / dysautonomia*
  substrate; the pilot outcome is broad long-COVID liability. Even a clean
  estimate evidences the general "autoimmune liability → PAIS" arrow, not h0007's
  SFN mechanism — which would need a dysautonomia/SFN-specific outcome.

### Dimension 9 — Manifest completeness (WARN, near PASS)

The Outputs contract requires `datapackage.json` (resources + SHA-256 + source)
and `run_metadata.json` (provenance + git commit) — most of a complete manifest.
Missing: an explicit requirement that the manifest carry **entity
cross-references** (`dataset:bentham-2015-sle-gwas`,
`dataset:covid19-hgi-longcovid-gwas`, `plan:0007`) and a structured
provenance-DAG linking outputs to inputs. **Fix:** add entity cross-refs to the
datapackage descriptor.

## Recommendations

1. **Register `dataset:1000g-eur-ld-panel`** (reference class, exact release +
   build + checksums) before any result feeds `plan:0008` (Dim 3). Interim inline
   contract acceptable for the probe if recorded as a known risk.
2. **Set + record a fixed RNG seed** for the weighted-median bootstrap SE, and
   commit an `renv.lock`/conda env for toolchain pinning (Dim 5).
3. **Add an explicit scale/resource discipline** — stream-extract instrument SNPs
   from the multi-GB HGI outcome, record peak memory + wall-clock in `qa_report`
   (Dim 6).
4. **Add entity cross-references** to `datapackage.json` (Dim 9). Minor: cite the
   provenance of the TwoSampleMR default clumping thresholds in `plan:0008`
   (Dim 1).

## Strengths

- Honest, disciplined `probe` framing: mechanics-only, explicitly not hypothesis
  evidence, with a self-imposed ancestry hard-stop that blocks over-claiming.
- The corrected outcome-stratum decision (GCST90454541 broad/population, verified
  against FTP `*-meta.yaml`) and the propagation fix to the handoff/dataset
  entity remove a real, load-bearing factual error.
- The GWAS-SSF→TwoSampleMR schema boundary and the LD-build↔sumstats-build
  reconciliation are specified as hard-stops, not left implicit — the two places
  this kind of pipeline usually breaks silently.
- Data-access + reproducibility gates genuinely pass on the D-005 basis
  (third-party-reproducible class clearing the `science.yaml` bar).
