# science:code
# status: exploratory
# task_ids: [t035]
# science:end

#!/usr/bin/env Rscript
# =============================================================================
# limma_de.R — WP5: per-contrast moderated-t ranked gene list (one contrast).
#
# MMSEQ estimate is log_mu (continuous, natural-log posterior mean) and the
# array matrix is log2 intensity — both continuous → limma moderated-t only;
# DESeq2/edgeR are INADMISSIBLE (pre-reg:0002 G2 lock). The output is the gene
# ranking that fgsea consumes: each gene's limma moderated **t-statistic** for
# the case-vs-control coefficient (BH-FDR is recorded but is descriptive only —
# verdict significance comes from the downstream sample-label permutation null).
#
# The two-group design is `~ group` with the CONTROL level as reference, so
# coefficient 2 is the case effect; topTable(coef = 2) gives logFC / t / p.
# A diagnostics sidecar (design rank, residual df, eBayes hyperparameters,
# FDR tally) is emitted for the WP8 admissibility step (model_inadequate),
# which owns its own thresholds — this script only measures, never adjudicates.
#
# Determinism (KD10): limma has no RNG and lmFit is bit-reproducible here, so the
# FULL-PRECISION ranked list (fwrite emits the round-trip-exact decimal for each
# double) is itself byte-identical across runs. The `t` column is the verdict-
# bearing statistic fgsea ranks on, so it is NEVER rounded here — rounding it
# would alter the NES rank and manufacture ties (review WP4-5, High). The only
# rounding is in the diagnostics sidecar (reporting); the KD10 verdict-rounding
# happens at the END of the chain, not on this intermediate.
# =============================================================================
suppressPackageStartupMessages({
  library(limma)
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

dataset    <- args[["dataset"]]
case       <- args[["case"]]
control    <- args[["control"]]
sample_col <- args[["sample-col"]]
group_col  <- args[["group-col"]]
contrast   <- args[["contrast"]]
seed       <- as.integer(args[["seed"]])

SIGDIG <- 7L
rnd <- function(x) signif(x, SIGDIG)

# limma is deterministic; seeding is a harmless no-op kept for parity with the
# locked determinism config (and to fail loudly if a seed is ever omitted).
if (is.na(seed)) stop("[limma_de] --seed required (determinism lock)")
set.seed(seed)

read_matrix <- function(path) {
  # env has no R.utils → fread cannot open .gz directly; pipe through gzip.
  dt <- fread(cmd = sprintf("gzip -dc %s", shQuote(path)),
              check.names = FALSE, na.strings = c("", "NA"))
  ids <- as.character(dt[[1]])
  m <- as.matrix(dt[, -1L, with = FALSE])
  rownames(m) <- ids
  m
}

m <- read_matrix(args[["expr"]])

# sample → group map (deduplicated: GSE14577 metadata has one row per chip, two
# per patient, but the expr matrix is per-patient — collapse to a single group).
sheet <- fread(args[["sheet"]], check.names = FALSE, na.strings = c("", "NA"))
if (!all(c(sample_col, group_col) %in% names(sheet)))
  stop(sprintf("[limma_de] sheet missing column(s): %s / %s", sample_col, group_col))
map <- unique(data.table(
  sample = as.character(sheet[[sample_col]]),
  group  = as.character(sheet[[group_col]])))
dup <- map[, .N, by = sample][N > 1L]
if (nrow(dup) > 0L)
  stop(sprintf("[limma_de] sample(s) map to >1 group: %s",
               paste(dup$sample, collapse = ", ")))

map <- map[group %in% c(case, control)]
grp_of <- setNames(map$group, map$sample)

# preserve expr-matrix column order for stability
samples <- colnames(m)[colnames(m) %in% map$sample]
missing <- setdiff(map$sample, colnames(m))
if (length(missing) > 0L)
  stop(sprintf("[limma_de] %d sheet sample(s) absent from expr matrix: %s",
               length(missing), paste(missing, collapse = ", ")))
n_case <- sum(grp_of[samples] == case)
n_control <- sum(grp_of[samples] == control)
if (n_case < 1L || n_control < 1L)
  stop(sprintf("[limma_de] %s: need both arms, got case=%d control=%d",
               contrast, n_case, n_control))

M <- m[, samples, drop = FALSE]
n_genes_in <- nrow(M)
ok <- rowSums(!is.finite(M)) == 0L          # drop genes with any NA/Inf/NaN
n_dropped_na <- sum(!ok)
M <- M[ok, , drop = FALSE]
if (nrow(M) == 0L)
  stop(sprintf("[limma_de] %s: no genes survive finite-value filter", contrast))

# two-group moderated-t: reference = control → coef 2 is the case effect.
g <- factor(grp_of[samples], levels = c(control, case))
design <- model.matrix(~ g)
design_rank <- qr(design)$rank
fit <- lmFit(M, design)
fit <- eBayes(fit)
tt <- topTable(fit, coef = 2L, number = Inf, sort.by = "none")

# FULL precision — no rounding on any analysis column. `t` is the verdict-bearing
# ranking statistic; fwrite writes the minimal decimal that restores each double
# exactly, so fgsea ranks on the unrounded moderated-t (review WP4-5, High).
ranked <- data.table(
  gene_id   = rownames(tt),
  logFC     = tt$logFC,
  t         = tt$t,
  P.Value   = tt$P.Value,
  adj.P.Val = tt$adj.P.Val)
# rank by moderated-t (desc), gene_id tiebreak → deterministic file order.
ranked <- ranked[order(-t, gene_id)]
data.table::fwrite(ranked, args[["out-ranked"]], sep = "\t",
                   quote = FALSE, na = "NA")

# diagnostics for WP8 admissibility (model_inadequate) — measured, not judged.
n_sig <- sum(tt$adj.P.Val < 0.05, na.rm = TRUE)
diag <- list(
  contrast        = contrast,
  dataset         = dataset,
  case            = case,
  control         = control,
  n_case          = n_case,
  n_control       = n_control,
  n_samples       = length(samples),
  design_cols     = ncol(design),
  design_rank     = design_rank,
  full_rank       = identical(as.integer(design_rank), ncol(design)),
  residual_df     = as.numeric(unique(fit$df.residual))[1],
  n_genes_in      = n_genes_in,
  n_genes_dropped_na = n_dropped_na,
  n_genes_tested  = nrow(M),
  n_sig_adj_p05   = n_sig,
  prop_sig_adj_p05 = rnd(n_sig / nrow(M)),
  sigma_median    = rnd(median(fit$sigma)),
  df_prior        = rnd(as.numeric(fit$df.prior)[1]),
  s2_prior        = rnd(as.numeric(fit$s2.prior)[1]),
  seed            = seed)
writeLines(toJSON(diag, auto_unbox = TRUE, pretty = TRUE, digits = SIGDIG,
                  na = "null"), args[["out-diag"]])

message(sprintf(
  "[limma_de] %s (%s): %d vs %d samples, %d genes tested (%d dropped NA), %d BH<0.05",
  contrast, dataset, n_case, n_control, nrow(M), n_dropped_na, n_sig))
