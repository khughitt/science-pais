---
title: 'Wave-1 MR pilot — execution result + go/no-go'
status: active
created: '2026-07-04'
see_also:
- plan:0007-wave1-mr-autoimmune-longcovid-pilot
- doc:2026-07-03-gwas-mr-ingestion-handoff
- task:t089
---

# Wave-1 MR pilot — execution result + go/no-go

`plan:0007` Task 5. The pilot pipeline
(`code/workflows/wave1-mr/`) ran **end to end** on 2026-07-04 via
`snakemake --use-conda` (env materialised from `r-mr.conda-lock.yml`; TwoSampleMR
`v0.7.9` pinned). This records the **mechanics** outcome. **It is not a scientific
verdict** — see the mechanics-only scope below.

## What ran (all real data, third-party-reproducible sources)

- **Exposure:** `dataset:bentham-2015-sle-gwas` GCST003156 harmonised
  fullPvalueSet (474 MB, 7,914,824 rows, GRCh38), from the GWAS Catalog FTP.
- **Outcome:** `dataset:covid19-hgi-longcovid-gwas` **GCST90454541**
  (broad cases / population controls; 303 MB, 9,442,353 rows, GRCh38).
- **LD panel:** `dataset:1000g-eur-ld-panel` — Zenodo 6614170 (https, DOI-archival,
  md5-verified, GRCh37 EUR), reconciled to the GRCh38 sumstats **by rsID**.

## Mechanics outcome — every GO criterion met

- Instrument: 32 independent SLE variants after p<5×10⁻⁸ + extended-MHC exclusion
  + local plink clumping (r²<0.001, 10 Mb); **mean F = 76.4** (≫ weak-instrument
  floor of 10).
- Harmonisation `action=2`: 31/32 retained; 1 palindromic SNP (rs5029939) dropped,
  logged (no silent drops).
- Outcome extraction streamed by rsID: **5.0 s, peak ~31 MB** (from the 303 MB
  file — the scale discipline held).
- Estimators (all finite, concordant in sign, all null):

  | Method | β (log-OR) | SE | p | OR |
  |---|---|---|---|---|
  | IVW (primary) | −0.017 | 0.015 | 0.24 | 0.98 |
  | MR-Egger | −0.039 | 0.034 | 0.26 | 0.96 |
  | Weighted median (seed 20260704) | −0.023 | 0.020 | 0.25 | 0.98 |

- MR-Egger intercept = 0.0077 (p=0.48) → no directional-pleiotropy signal.
- Output bundle QA: **overall PASS** (all 7 structural checks) —
  `results/wave1-mr-pilot/{datapackage.json, mr_results.json, qa_report.*,
  run_metadata.json}` (gitignored; provenance incl. git commit + input SHA-256s +
  tool versions).

## Scope — MECHANICS-ONLY (not hypothesis evidence)

The estimate is **not** interpreted as evidence for or against
`hypothesis:0007`/`hypothesis:0009`/`question:0022`. Two independent bars stop
that: (1) the **ancestry hard-stop** — the only retrievable outcome file is a
European-dominant *multi-ancestry* meta (no EUR-only sibling), so this is not a
valid ancestry-matched primary estimate; (2) the full **acceptance gate**
(handoff §4) — sample-overlap correction, strict-stratum sensitivity, HLA-inclusive
run, and a EUR-matched outcome — is deliberately out of pilot scope. The null IVW
point estimate is reported as a *pipeline output*, nothing more.

## Go/no-go → **GO** to the full design plan (`plan:0008`)

The pipeline mechanics are proven: retrieval, MHC-aware instrument construction,
local reproducible clumping, streamed harmonisation, seeded estimators, and the
reproducible output/QA bundle all work on real data. Proceed to `plan:0008` (the
`design` plan) to add: a EUR-matched outcome (lift the ancestry hard-stop),
Ruth sex-hormone exposure + sex-modifier targets, sample-overlap correction
(Ruth↔HGI), broad/strict + HLA-inclusive sensitivities, and the full acceptance
gate before any result is reportable as hypothesis/question evidence.

## Reproducibility note

The committed `r-mr.conda-lock.yml` + pinned TwoSampleMR tag reproduce the
environment from scratch. During this run, `r-r.utils` (fread gz) and `gzip`
(zcat streaming) were found missing from the first env build and added to the
env spec + lock; a from-scratch `snakemake --use-conda` now builds a complete
working env. The back-half rules were executed against the (patched) already-built
env to avoid a redundant full rebuild in a disk-constrained sandbox; the DAG and
env definition are unchanged and reproduce identically elsewhere.
