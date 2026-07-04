# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Harmonise exposure<->outcome and run the MR estimators (Wave-1 pilot).
#
# plan:0007 Tasks 3-4. STREAM/selective-extract the instrument SNPs from the
# multi-GB outcome file by hm_rsid (NOT a full in-memory load); record peak
# memory + wall-clock. Run TwoSampleMR::harmonise_data(action = config.harmonise
# .action = 2) — infer palindromic by EAF, drop ambiguous; log every dropped SNP
# (no silent drops). Effects are log-OR (both binary). Then IVW (primary),
# MR-Egger, weighted-median; the WM bootstrap SE uses config.estimate
# .weighted_median_seed (set.seed) for bit-reproducibility. Emit harmonised
# table + mr_results.json (estimates, SEs, Egger intercept, concordance) with the
# ancestry/mechanics-only label.
#
# STUB — not yet implemented (WP0 skeleton).

args <- commandArgs(trailingOnly = TRUE)
# expected: --config <yaml> --instrument <tsv> --outcome <file>
#           --harmonised-out <tsv> --results-out <json>
stop("harmonize_estimate.R: STUB not implemented (plan:0007 Tasks 3-4)")
