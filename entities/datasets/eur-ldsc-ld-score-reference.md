---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:eur-ldsc-ld-score-reference
kind: dataset
title: European LDSC LD-score reference (eur_w_ld_chr) + HapMap3 SNP list (MRlap
  cross-trait LDSC infrastructure)
status: candidate
created: '2026-07-04'
updated: '2026-07-04'
origin: external
dataset_class: reference
source_class: reference
tier: use-now
license: CC-BY-4.0
update_cadence: static
access:
  level: public
  availability: available
  verified: true
  source_url: https://doi.org/10.5281/zenodo.8182036
  verification_method: metadata-confirmed
  last_reviewed: '2026-07-04'
  verified_by: agent (plan:0009 Task 1)
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "MRlap's internal cross-trait LDSC needs two reference inputs: the European LD-score set (eur_w_ld_chr, the `ld` argument) and the HapMap3 SNP list (w_hm3.snplist, the `hm3` argument). BOTH are pinned to DOI-archival, checksummed Zenodo mirrors — eur_w_ld_chr: record 8182036 (eur_w_ld_chr.tar.gz, md5 e2f16343c4cfaa76caa7d0c03d26b489, CC-BY-4.0); w_hm3.snplist: record 7773502 (w_hm3.snplist.gz, md5 153ecc2bcfa740afafe656e6a384d769, CC-BY-4.0) — deliberately NOT the non-archival UT-Austin Box share link MRlap's README points at nor the Broad GCS bucket (404 at staging), mirroring the plan:0007 1000G Zenodo-hardening. Third-party-reproducible (top class)."
accessions:
- DOI:10.5281/zenodo.8182036
- DOI:10.5281/zenodo.7773502
- PMID:25642630
- GitHub:bulik/ldsc
ontology_terms:
- ld-score-reference
- ldsc
- hapmap3
- european-ancestry
- mr-infrastructure
- homo-sapiens
consumed_by:
- plan:0009-wave1-mr-hormone-pilot
- task:t089
related:
- plan:0009-wave1-mr-hormone-pilot
- dataset:ruth-2020-shbg-testosterone-gwas
- dataset:covid19-hgi-longcovid-gwas
- task:t089
identity_context:
  taxon: 9606
  assembly:
    label: GRCh37
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# European LDSC LD-score reference (eur_w_ld_chr) + HapMap3 SNP list

**Candidate dataset.** `status: candidate` — catalogued with an archival source
pinned; per-file SHA-256 and the extracted per-chromosome contents are recorded at
staging (plan:0009 Task 1 retrieval-probe exception).

## What it is

The two reference inputs **MRlap** requires to run its internal cross-trait LD-score
regression (it builds on GenomicSEM and munges/LDSC-regresses internally — there is no
separate Python-`ldsc` stage):

- **`eur_w_ld_chr`** — the European-ancestry LD scores by chromosome (the classic
  Bulik-Sullivan / Alkes-group LDSC reference, derived from 1000 Genomes Phase 3 EUR;
  LDSC method: Bulik-Sullivan et al., *Nat Genet* 2015, PMID 25642630). Passed to MRlap
  as the `ld` argument (a folder path).
- **`w_hm3.snplist`** — the HapMap3 SNP list (~1.2M well-imputed SNPs) MRlap uses to
  restrict/munge both traits. Passed as the `hm3` argument.

It is **analysis infrastructure**, not a measured-phenotype dataset: it satisfies no
question/hypothesis capability target. Classed in-scope per **D-006** (same class as the
1000G-EUR LD panel — reference infrastructure, not a new measured-phenotype vehicle).

## Why it fits

`plan:0009` (Arm-B hormone pilot) corrects the structural Ruth↔HGI UK-Biobank sample
overlap with **MRlap**, whose cross-trait LDSC intercept — hence the estimated overlap
fraction, hence the corrected estimate — is computed against these references. Because
the LD-score reference determines the correction, it is a **load-bearing input** and is
tracked as a first-class dataset per the project's reproducibility standard (the same
finding that promoted `dataset:1000g-eur-ld-panel` in the `plan:0007` pipeline review,
and the `plan:0009` pipeline-review Dim-3 finding).

## Access / caveats

- **eur_w_ld_chr — openly downloadable from a DOI-archival, checksummed source.**
  Zenodo record 8182036 (DOI 10.5281/zenodo.8182036, `eur_w_ld_chr.tar.gz`, 33.4 MB,
  md5 `e2f16343c4cfaa76caa7d0c03d26b489`, CC-BY-4.0), no credentials/gating →
  third-party-reproducible (top class). Chosen over the non-archival UT-Austin Box share
  link MRlap's README points at (kept as provenance only), for transport security +
  archival permanence — the same hardening `plan:0007` applied to the 1000G panel
  (plain-http MRC-IEU → Zenodo DOI). The published md5 is verified on download; the
  extracted per-chromosome `.l2.ldscore.gz` / `.l2.M_5_50` set is checksummed and
  row-counted into the run manifest.
- **w_hm3.snplist — openly downloadable from a DOI-archival, checksummed source.**
  Zenodo record 7773502 (DOI 10.5281/zenodo.7773502, `w_hm3.snplist.gz`, 5.2 MB, md5
  `153ecc2bcfa740afafe656e6a384d769`, CC-BY-4.0). The Broad Alkes-group GCS bucket
  (`storage.googleapis.com/broad-alkesgroup-public/LDSCORE/w_hm3.snplist.bz2`) **404'd at
  staging** and the historical `data.broadinstitute.org/alkesgroup` path is gone, so the
  Zenodo mirror is the pinned source — md5 verified on download.
- **Build = GRCh37 (native, rsID-keyed).** The LD scores are keyed by rsID (not
  coordinates), so alignment to the GRCh37-native Ruth exposures and the GRCh38 outcome
  is by **rsID**, matching the `plan:0007`/`plan:0009` reconciliation policy. Task 1
  confirms the rsID-key reconciliation before Task 4. `identity_context.assembly` records
  the underlying build label but is left `declared_unresolved` (no seqcol digest pinned).
- **EUR only** — matched to the European Ruth exposures and the European-dominant HGI
  outcome; do not use for non-European ancestry work.

## Access verification log

- 2026-07-04 (agent, plan:0009 Task 1): registered as the tracked MRlap cross-trait
  LDSC reference (plan:0009 pipeline-review Dim-3 finding — parallel to the 1000G-panel
  promotion in the plan:0007 review). eur_w_ld_chr source pinned to the DOI-archival,
  checksummed Zenodo record 8182036 (md5 `e2f16343c4cfaa76caa7d0c03d26b489`, CC-BY-4.0),
  replacing MRlap's non-archival UT-Austin Box link (provenance only).
- 2026-07-04 (agent, plan:0009 Task 1 staging run): **eur_w_ld_chr retrieved + md5-verified**
  from Zenodo 8182036 (md5 `e2f16343c4cf…` matched); tar extracted to `data/raw/ldsc/eur_w_ld_chr/`
  with 23 per-chromosome `*.l2.ldscore.gz` files (+ `*.l2.M_5_50`). The initial w_hm3
  source (Broad GCS `w_hm3.snplist.bz2`) **404'd**; the stager hard-stopped (no silent
  fallback). **w_hm3.snplist re-pinned to the DOI-archival Zenodo record 7773502**
  (`w_hm3.snplist.gz`, md5 `153ecc2bcfa740afafe656e6a384d769`, CC-BY-4.0) — so both
  MRlap references now clear the third-party-reproducible top bar. Recorded SHA-256s:
  eur_w_ld_chr.tar.gz `9537f00e…6060b069` (23 per-chromosome `*.l2.ldscore.gz` extracted);
  w_hm3.snplist.gz `3c876903…14d45a48` → `w_hm3.snplist` with **1,217,312** SNPs (the
  expected HapMap3 count). Staged off-Dropbox at `/data/proj/post-acute-infection/raw/ldsc/`
  (repo `data/raw` symlink); `ldsc_ref_manifest.json` written by rule `stage_ldsc_ref`.
