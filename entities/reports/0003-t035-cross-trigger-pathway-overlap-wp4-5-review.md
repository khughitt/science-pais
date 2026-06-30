---
id: "report:0003-t035-cross-trigger-pathway-overlap-wp4-5-review"
type: "report"
title: "t035 WP4-5 implementation review: preprocessing + DE/enrichment (cross-trigger pathway-overlap)"
status: "proposed"
source_refs:
  - plan:0003-cross-trigger-pathway-overlap-pipeline
  - pre-registration:0002-cross-trigger-pathway-overlap
  - task:t035
related:
  - hypothesis:0001-shared-dysregulated-attractor
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
created: "2026-06-20"
updated: "2026-06-20"
---

# Pipeline Review: cross-trigger pathway-overlap pipeline (WP4–WP5)

- **Plan:** plan:0003-cross-trigger-pathway-overlap-pipeline
- **Pre-reg:** pre-registration:0002-cross-trigger-pathway-overlap
- **Scope:** WP4 (preprocessing + gene-set prep) and WP5 (limma DE + fgsea enrichment)
- **Date:** 2026-06-20
- **Overall:** WARN → **all findings resolved** (fixes committed; see Resolution)

## Summary

WP4–WP5 are functionally correct and the science framing is sound: the near-zero
filter's "derive, don't guess" bimodality guard did real work (derived τ=−5.567,
not the superseded fixed `-7.0`), and the DE stage correctly treats per-gene limma
as *rank input* for GSEA rather than as a verdict — appropriate given the
pilot-grade RNA-seq power. One **High** correctness bug (rounding the verdict-
bearing moderated-t before fgsea) plus a **Medium** staleness risk and a **Low**
doc drift were found and fixed before WP6.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | N/A — inherited from parent plan/pre-reg | params sourced in config↔pre-reg mirror |
| Assumption audit | N/A — inherited | causal claims held at pre-reg evidence level |
| Data availability | PASS | GSE14577 + GSE130353 provisioned/hashed (G1); GMTs pinned/hashed |
| Identifiability | PASS | raw → ranked → NES chain fully connected; 63-job DAG resolves |
| Reproducibility | PASS (after fix) | seed/RNGkind pinned, envs hash-built; full-precision intermediates now byte-deterministic |
| Validation criteria | PASS | two-severity QA gates; bimodality build-fatal; hash asserts; size filter |
| Scope check | PASS | within `specs/scope-boundaries.md` (public, bounded, 2-cohort) |
| Integration boundaries | WARN → PASS | io_contract schema verified; `t`-precision boundary bug fixed (see High) |
| Manifest completeness | deferred to WP8 (finding 5) | datapackage emitted at terminal target |

## Detailed Findings

### High — moderated-t rounded before the verdict-bearing fgsea rank (Integration boundary)

`limma_de.R` applied `signif(t, 7)` to the `t` column written to `ranked.tsv`, and
`fgsea_enrich.R` consumed that rounded column as its ranking statistic. This is
not serialization: it altered the statistic entering fgsea and manufactured ties
(duplicate rounded `t` in all five ranked lists). The original rationale
(byte-determinism vs. BLAS ulp jitter) was the wrong trade — precision of the
analysis input was sacrificed for a guarantee that lmFit already provides here.

**Recommendation (done):** keep full-precision `t` for the analysis input; round
only the diagnostics sidecar / final serialized verdict.

### Medium — `theme_spec.json` can go stale after a theme-map/config amendment (Reproducibility)

`emit_theme_spec` took `config=ancient(CONFIGFILE)`; `ancient()` suppresses the
config input's freshness, so a future amendment to the verdict-relevant
`theme_map` or `compartment_marker_regex` could leave `theme_spec.json` (and
downstream `theme_map.tsv`) stale.

**Recommendation (done):** drop `ancient()` on the config input so a config edit
reruns this path. (The `ancient()` on `fetch_url.py`/`acquire_common.py` in
`download_genesets` is unaffected — those payloads are content-addressed by a
locked sha256, a distinct and justified use.)

### Low — stale harmonization-reference wording (doc)

`genesets_reference.R`'s `ensembl_lift_note` still said off-universe rel68 ids are
"logged, not dropped," but the fixed `harmonize_gse130353.py` now drops
off-universe ids (KD5 finding-1 fix: a dropped gene can never be a gene-set
member, so keeping it would only inflate the fgsea ranked-walk denominator).

**Recommendation (done):** update the note to state the drop-on-off-universe
contract so future reviewers do not misread G3.

## Resolution

All three findings addressed in the WP5 review-fix commit:

- **High:** `limma_de.R` / `fgsea_enrich.R` now write full-precision doubles via
  `data.table::fwrite` (round-trip exact); no rounding on any analysis column.
  Verified: 0 tied `t` across all 5 ranked lists (was the artificial-tie source),
  the fgsea "ties in preranked stats" warning is gone, and outputs remain
  byte-identical across forced re-runs (incl. stochastic fgsea-multilevel on
  GO:BP) — full precision **and** KD10 determinism both hold.
- **Medium:** `ancient()` removed from `emit_theme_spec`'s config input.
- **Low:** `ensembl_lift_note` corrected.

Post-fix gate: `snakemake --lint` clean (only the known `common.smk`
rules/functions false-positive), full DAG resolves (63 jobs), `science validate`
PASSED.

## Strengths

- The bimodality guard is genuinely load-bearing: it derived τ from the data and
  would have build-halted on a non-bimodal density rather than silently using a
  fixed constant.
- Verdict-affecting decisions live in the pre-reg with an amendment audit trail
  (multimap policy, near-zero procedure), not in config/code drift — no HARKing.
- Two-severity QA (structural=build-fatal, distribution=surfaced) is applied
  consistently; evidence is always written even on a halt.
- The DE→GSEA framing correctly subordinates underpowered per-gene RNA-seq DE to
  the pathway-rank estimand the pre-reg actually commits to.
