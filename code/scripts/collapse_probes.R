#!/usr/bin/env Rscript
# =============================================================================
# collapse_probes.R — WP4 (GSE14577): probe→gene median collapse + locked
# U133A∪B dual-chip combine. (pre-reg:0002 3rd amendment; plan:0003 KD9.)
#
# Input is the WP3 harmonized table (platform, probe, ensembl_gene_id, then one
# log2 column per PATIENT, both GPL96 and GPL97 rows stacked on the shared
# patient axis). Two locked, verdict-affecting steps:
#   (1) within-platform probe→gene collapse = MEDIAN of probes mapping to the
#       same ensembl_gene_id on the same platform, per patient.
#   (2) U133A∪B combine = a gene present on BOTH GPL96 and GPL97 takes the MEAN
#       of its two platform-level collapsed log2 values per patient (15 patients,
#       not 30 arrays); single-platform genes pass through unchanged.
# Unmapped probes (empty ensembl_gene_id) are DROPPED here (they carry no gene
# identity to collapse to) and the count is logged. cohort_audit.json records
# every raw→collapsed→combined count + the dual-chip gene count.
#
# No QA SENTINEL: GSE14577 has no near-zero filter (array data inherits deposited
# log2; pre-reg), so this rule is a deterministic transform with no build-fatal
# gate of its own — its outputs (expr.gene + audit) are the gating artifacts.
# =============================================================================
suppressPackageStartupMessages({
  library(data.table)
  library(jsonlite)
})

parse_args <- function() {
  a <- commandArgs(trailingOnly = TRUE)
  out <- list(); i <- 1
  while (i <= length(a)) { out[[sub("^--", "", a[i])]] <- a[i + 1]; i <- i + 2 }
  out
}
args <- parse_args()
collapse_rule <- args[["collapse"]]
combine_rule  <- args[["dual-chip"]]
# locked, verdict-affecting rules (config preprocessing.*) — fail-early on drift.
if (is.null(collapse_rule) || collapse_rule != "median")
  stop(sprintf("probe_collapse '%s' not implemented — only 'median' (fail-early)", collapse_rule))
if (is.null(combine_rule) || combine_rule != "mean_of_platform_collapsed_log2")
  stop(sprintf("u133_dual_chip_combine '%s' not implemented — only 'mean_of_platform_collapsed_log2'", combine_rule))

# Decompress via `gzip -dc` through fread's cmd interface (the env has no R.utils,
# so fread can't open .gz directly); fread types patient columns numeric (empty→NA)
# and check.names off preserves hyphenated patient keys (e.g. "PI-CFS_2").
harm <- fread(cmd = sprintf("gzip -dc %s", shQuote(args[["harmonized"]])),
              check.names = FALSE, na.strings = c("", "NA"))
meta_cols <- c("platform", "probe", "ensembl_gene_id")
patient_cols <- setdiff(names(harm), meta_cols)

n_probes_in <- nrow(harm)
unmapped <- harm[["ensembl_gene_id"]] == "" | is.na(harm[["ensembl_gene_id"]])
n_unmapped <- sum(unmapped)
harm <- harm[!unmapped]

# (1) within-platform median collapse: one row per (platform, ensembl) ----------
collapsed <- harm[, lapply(.SD, median, na.rm = TRUE),
                  by = .(platform, ensembl_gene_id), .SDcols = patient_cols]
n_gpl96 <- collapsed[platform == "GPL96", uniqueN(ensembl_gene_id)]
n_gpl97 <- collapsed[platform == "GPL97", uniqueN(ensembl_gene_id)]

# (2) U133A∪B combine: mean across platform-collapsed rows per gene -------------
# A gene on both chips has 2 rows here → mean of the two per patient; a single-
# platform gene has 1 row → mean of one value = pass-through (the locked rule).
plat_per_gene <- collapsed[, .(n_plat = .N), by = ensembl_gene_id]
n_dual_chip <- plat_per_gene[n_plat == 2L, .N]
dual_examples <- head(sort(plat_per_gene[n_plat == 2L, ensembl_gene_id]), 10)

genes <- collapsed[, lapply(.SD, mean, na.rm = TRUE),
                   by = .(ensembl_gene_id), .SDcols = patient_cols]
# NaN can arise only if every platform value for a (gene,patient) is NA → re-mark
# as NA for the locked NA-as-NA contract (never 0).
for (cc in patient_cols)
  set(genes, which(is.nan(genes[[cc]])), cc, NA_real_)
setorder(genes, ensembl_gene_id)          # deterministic row order

# --- write expr.gene (gene × patient), deterministic gzip ---------------------
dir.create(dirname(args[["out-expr"]]), recursive = TRUE, showWarnings = FALSE)
con <- pipe(sprintf("gzip -n > %s", shQuote(args[["out-expr"]])), "w")
# fwrite would re-open the file; write through the gzip pipe with write.table so
# the `gzip -n` header (no name/mtime) makes re-runs byte-identical (KD10).
write.table(as.data.frame(genes), con, sep = "\t", quote = FALSE,
            row.names = FALSE, na = "NA")
close(con)

audit <- list(
  dataset = "GSE14577",
  canonical_axis = "ensembl_gene_id",
  independent_unit = "patient",
  n_patients = length(patient_cols),
  patients = as.list(patient_cols),
  probe_collapse = collapse_rule,
  dual_chip_combine = combine_rule,
  counts = list(
    n_probes_in = n_probes_in,
    n_probes_unmapped_dropped = n_unmapped,
    n_probes_mapped = n_probes_in - n_unmapped,
    n_genes_gpl96 = n_gpl96,
    n_genes_gpl97 = n_gpl97,
    n_genes_dual_chip = n_dual_chip,
    n_genes_total = nrow(genes)
  ),
  dual_chip_examples = as.list(dual_examples)
)
write_json(audit, args[["out-audit"]], auto_unbox = TRUE, pretty = TRUE)

message(sprintf(
  "[collapse_probes] PASS GSE14577: %d probes (%d unmapped dropped) -> GPL96 %d / GPL97 %d genes -> %d genes (%d dual-chip), %d patients",
  n_probes_in, n_unmapped, n_gpl96, n_gpl97, nrow(genes), n_dual_chip, length(patient_cols)))
