---
reviews: "plan:0009-wave1-mr-hormone-pilot"
review_scope: "Task 1 implementation, staging results, and interpretation"
date: "2026-07-04"
overall: "WARN"
---

# Pipeline Review: plan:0009 Task 1 Staging

- **Reviews:** `plan:0009-wave1-mr-hormone-pilot` (`entities/plans/0009-wave1-mr-hormone-pilot.md`)
- **Scope:** Task 1 implementation/results only (`code/workflows/wave1-mr-hormone/`, staged manifests, touched dataset entities)
- **Date:** 2026-07-04
- **Overall:** WARN

## Summary

Task 1 materially succeeds as an input-staging increment: all expected raw sumstats and references are present on disk, the main payloads are checksummed, the 1000G and LDSC archives are md5-verified, and the new MRlap reference source is now DOI-archival rather than Box/GCS-dependent.
I would not block Task 2, because Task 2 uses the Ruth exposure files and 1000G panel rather than MRlap total-N injection.
Before Task 4/MRlap, however, the outcome total-N handoff must be made machine-readable and the LDSC reference/file-set assertions should be tightened.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | PASS | Task 1 source choices are named and recorded. |
| Assumption audit | WARN | Build/rsID reconciliation is directionally right but Ruth build language drifted in the LDSC manifest/comments. |
| Data availability | PASS | Runtime files exist and manifests record source URLs/checksums. |
| Identifiability | N/A | No estimand execution in Task 1. |
| Reproducibility | WARN | Raw payload checksums are present; no Task-1 datapackage/env lock yet, and total N is not machine-extracted. |
| Validation criteria | WARN | Downloads/checksums/row counts run, but nested HGI sample-size parsing and exact LDSC file-set checks are incomplete. |
| Scope check | PASS | D-005/D-006 boundary respected; no gated-data line reopened. |
| Integration boundaries | WARN | Staged files are raw GWAS-SSF, not yet MRlap-ready; acceptable for Task 1 only if Task 4 canonicalization remains a hard gate. |
| Manifest completeness | WARN | `staging_manifest.json` exists, but no full datapackage/provenance bundle yet. |

## Findings

### F1. Outcome total N is prose-recorded but not manifest-recorded (WARN)

`plan:0009` Task 1 requires recording the outcome's case/control or total N for later MRlap observed-scale correction.
The staged HGI `*-meta.yaml` contains nested ancestry-level `samples[*].sample_size` values that sum to 1,100,445, and the dataset entity records that total in prose.
But `acquire_sumstats.py` only scans top-level metadata keys for sample-size-like names, so the generated `acquire_manifest.json` records `"sample_size_fields": {}`.

This leaves the Task 4 total-N injection dependent on a manual/entity-prose value rather than the reproducible staging manifest.
Before MRlap runs, extend `capture_meta_n()` to parse nested `samples`, write `sample_size_total`, per-ancestry components, and `sample_size_policy: total_observed_n`, then hard-stop if the outcome total cannot be constructed.
If case/control splits are absent, say that explicitly: MRlap needs total N, not case/control split, but the missing split should not be implied to exist.

### F2. LDSC reference file-set validation accepts 23 ldscore files without declaring the intended set (WARN)

`stage_ldsc_ref.py` treats `len(ldscore_files) >= 22` as success and the manifest reports 23 `*.l2.ldscore.gz` files.
The staged folder includes the usual chromosomes plus `6_old.l2.ldscore.gz`.
That may be harmless if MRlap/GenomicSEM address files by chromosome prefix, but the task result should not read as "23 chromosomes", and the validation should distinguish the exact required `1..22` files from archival extras.

Before Task 4, validate that `1.l2.ldscore.gz` through `22.l2.ldscore.gz` and their matching `*.l2.M_5_50` files exist exactly, record extras separately as ignored, and pass MRlap the standard `eur_w_ld_chr` folder/prefix expected by LDSC-style tooling.

### F3. Build-reconciliation prose drifted: Ruth is staged as GRCh38, not GRCh37-native (WARN-small)

The Ruth entity correctly says Task 1 used harmonised GRCh38 GWAS Catalog files and reconciles them to GRCh37 LD/LDSC references by rsID.
But `stage_ldsc_ref.py` and the generated LDSC manifest say "GRCh37 Ruth + GRCh38 outcome".
That does not appear to break execution, because rsID is the intended join key, but it is misleading in exactly the place downstream MRlap interpretation will look for the build contract.

Update the script/manifest wording to: Ruth and HGI staged sumstats are GRCh38 harmonised files; LDSC/1000G references are GRCh37; reconciliation is by rsID/hm_rsid, with a hard stop later if rsIDs are missing.

### F4. Entity status text and provenance bundle are slightly behind the implementation (INFO/WARN)

The HGI dataset body still says "catalogued but not yet acquired" near the top, even though the verification log now records both plan:0007 and plan:0009 acquisition.
The Task 1 workflow also emits `staging_manifest.json`, not the final `datapackage.json`/QA/run-metadata bundle; that is acceptable for this increment, but should be stated as "Task 1 staging manifest complete" rather than "full bundle complete."

## Recommendation

Proceed to Task 2 if desired, because these findings do not affect exposure instrument construction.
Before Task 4, close F1/F2/F3 in code and regenerate the staging manifest so MRlap receives machine-checked total N and an explicit LDSC reference file-set contract.

## Resolution (2026-07-04)

All four findings closed in code and the staging manifests regenerated
deterministically from the local, checksummed payloads (no 4.1 GB download again —
the byte-stable checksums recorded at staging are preserved; only the
fix-touched fields were recomputed from the local `meta.yaml` / `eur_w_ld_chr`
folder using the workflow's own functions).

- **F1 (total N machine-recorded).** `acquire_sumstats.py` now factors a pure
  `extract_total_n(meta)` (unit-testable, no I/O) out of `capture_meta_n()`. It
  sums the nested `samples[*].sample_size` to `sample_size_total`, records
  per-ancestry `sample_size_components`, sets `sample_size_policy:
  total_observed_n`, and **hard-stops** if no total can be constructed. It also
  records `case_control_split_available: false` with an explicit note that this
  HGI release carries per-cohort totals only (no `n_cases`/`n_controls`), so a
  split must not be implied. Verified against the staged meta:
  `179 + 5,725 + 3,536 + 1,090,649 + 356 = 1,100,445`. The regenerated
  `acquire_manifest.json` / `staging_manifest.json` now carry
  `sample_size_total: 1100445`.
- **F2 (exact LDSC file-set).** `stage_ldsc_ref.py` now validates chromosomes
  **1..22 exactly**, each with its matching `.l2.M_5_50` sidecar (hard-stop on any
  gap), and records archival extras separately as
  `extra_ldscore_files_ignored` (here `["6_old.l2.ldscore.gz"]`) — the result
  no longer reads as "23 chromosomes". Manifest now:
  `n_required_ldscore_files: 22`, `required_chromosomes: "1..22"`.
- **F3 (build-reconciliation prose).** The `stage_ldsc_ref.py` docstring and the
  manifest `build_reconciliation` now state the correct contract: **staged Ruth
  exposures and the HGI outcome are GRCh38 harmonised sumstats; the LDSC and
  1000G references are GRCh37; the join is by rsID/hm_rsid** (build-independent),
  with a hard stop later if rsIDs are missing. The stale `hm3`-source comment in
  `config.yaml` (which still named the Broad GCS bucket) was corrected to the
  DOI-archival Zenodo mirror actually used.
- **F4 (entity status text).** The HGI dataset entity's opening line no longer
  says "catalogued but not yet acquired"; it now reflects acquired+checksummed
  status. The Task-1 artifact remains the staging manifest (not the final
  datapackage bundle), which is correct for this increment.

Net: WARN → resolved. The LDSC/total-N contracts MRlap consumes at Task 4 are
now machine-checked in the manifest rather than dependent on entity prose.
