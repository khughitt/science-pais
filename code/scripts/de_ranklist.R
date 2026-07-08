# science:code
# status: workflow-owned
# task_ids: [t117, t119]
# science:end

#!/usr/bin/env Rscript
# =============================================================================
# de_ranklist.R — WP2 (plan:0010): per-contrast moderated-t ranked gene list for
# the cross-PAIS rank matrix. ONE ranking statistic (limma moderated-t) for EVERY
# deposit, so the downstream NES vectors are commensurable across the 5 expression
# scales in the corpus — the NES-comparability precondition of the rank estimand.
#
# This is NOT the stock t035 limma_de.R (which lmFits the matrix DIRECTLY and only
# fits `~ group`). That is correct only for already-log data; the t117 corpus adds
# raw/estimated COUNTS and FPKM, which must be normalized before a linear model.
# review Finding F: "reuse plan:0003 verbatim understates this." So this t117-owned
# script (composition, not a mutation of the shared t035 script) makes the DE path
# SCALE-AWARE, and adds the three per-contrast model extensions the `de_models`
# contract declares (platform covariate, twin-pair block, longitudinal collapse):
#
#   scale-aware gene-level statistic (config parse.expression_scale):
#     counts | estimated_counts  -> limma::voom (logCPM + precision weights, on
#                                   library-size normalization) -> lmFit  [RNA-seq
#                                   counts]. voom is used standalone (no edgeR/TMM):
#                                   edgeR is NOT in the pinned r-bioc env and adding
#                                   it would force a re-solve of the NES-sensitive
#                                   limma/fgsea stack; library-size voom is standard
#                                   and, since each deposit's NES is computed
#                                   independently, the cross-deposit rank estimand is
#                                   insensitive to the within-deposit TMM-vs-libsize
#                                   choice. A manual low-expression CPM filter stands
#                                   in for filterByExpr.
#     fpkm | cpm                 -> log2(x + 1) -> lmFit         [already lib-size
#                                   normalized; just put on the log scale]
#     log_mu | log2_intensity    -> lmFit DIRECTLY               [already log]
#   ALL paths end in eBayes moderated-t on the case coefficient -> the SAME
#   statistic fgsea ranks on (never rounded; full-precision fwrite).
#
#   model extensions (config de_models):
#     --collapse-col <col>  longitudinal: average each subject's timepoints to ONE
#                           pseudo-sample on the model-ready (post-voom/post-log)
#                           scale, THEN fit `~ group` across subjects. unit = subject
#                           (no pseudo-replication). plan:0010 "collapse BEFORE limma,
#                           stock_ok AFTER collapse". (gse226260, gse128078)
#     --design-covariates   extra design terms, e.g. platform batch (gse251872 ->
#                           `~ platform + group`); the case coef is read by NAME.
#     --block <col>         duplicateCorrelation block, e.g. twin pair (gse16059 ->
#                           `~ group` with within-pair correlation).
#   collapse is mutually exclusive with block/covariates in this corpus (the two
#   longitudinal deposits need neither); asserted below.
#
# Determinism (KD10, matches t035): limma/edgeR have no RNG here; the full-precision
# ranked list is byte-reproducible. --seed is required for parity and fails loud if
# omitted. The `t` column is NEVER rounded (it sets the fgsea rank); only the
# diagnostics sidecar is rounded (reporting).
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
contrast   <- args[["contrast"]]
scale      <- args[["scale"]]
case       <- if (is.null(args[["case"]])) "case" else args[["case"]]
control    <- if (is.null(args[["control"]])) "control" else args[["control"]]
sample_col <- if (is.null(args[["sample-col"]])) "sample" else args[["sample-col"]]
group_col  <- if (is.null(args[["group-col"]])) "group" else args[["group-col"]]
seed       <- as.integer(args[["seed"]])

# "NONE" is the Snakefile's absent-value token (a missing config key), kept explicit
# so a typo'd column name fails loud rather than silently disabling an extension.
none_or <- function(x) if (is.null(x) || x == "NONE" || x == "") NULL else x
collapse_col  <- none_or(args[["collapse-col"]])
block_col     <- none_or(args[["block"]])
cov_arg       <- none_or(args[["design-covariates"]])
design_covs   <- if (is.null(cov_arg)) character(0) else strsplit(cov_arg, ",")[[1]]

SIGDIG <- 7L
rnd <- function(x) signif(x, SIGDIG)
if (is.na(seed)) stop("[de_ranklist] --seed required (determinism lock)")
set.seed(seed)

COUNT_SCALES  <- c("counts", "estimated_counts")   # -> voom
LOG_XFORM     <- c("fpkm", "cpm")                  # -> log2(x + 1)
ALREADY_LOG   <- c("log_mu", "log2_intensity")     # -> direct
if (!scale %in% c(COUNT_SCALES, LOG_XFORM, ALREADY_LOG))
  stop(sprintf("[de_ranklist] %s: unknown expression_scale '%s'", contrast, scale))

# collapse in this corpus is only ever on the two plain-two-arm longitudinal deposits
# (gse226260, gse128078); it does not co-occur with a design covariate or a block.
if (!is.null(collapse_col) && (length(design_covs) > 0L || !is.null(block_col)))
  stop(sprintf("[de_ranklist] %s: collapse is mutually exclusive with covariates/block (got covs=%s block=%s)",
               contrast, paste(design_covs, collapse = "+"), block_col))

read_matrix <- function(path) {
  # env has no R.utils -> fread cannot open .gz directly; pipe through gzip.
  dt <- fread(cmd = sprintf("gzip -dc %s", shQuote(path)),
              check.names = FALSE, na.strings = c("", "NA"))
  ids <- as.character(dt[[1]])
  m <- as.matrix(dt[, -1L, with = FALSE])
  rownames(m) <- ids
  m
}
m <- read_matrix(args[["expr"]])

# --- sample -> group (+ covariate / collapse / block columns) ----------------
sheet <- fread(args[["sheet"]], check.names = FALSE, na.strings = c("", "NA"))
need_cols <- c(sample_col, group_col, design_covs, collapse_col, block_col)
miss_cols <- setdiff(need_cols, names(sheet))
if (length(miss_cols) > 0L)
  stop(sprintf("[de_ranklist] %s: sheet missing column(s): %s",
               contrast, paste(miss_cols, collapse = ", ")))

sheet[[sample_col]] <- as.character(sheet[[sample_col]])
sheet[[group_col]]  <- as.character(sheet[[group_col]])
sheet <- sheet[sheet[[group_col]] %in% c(case, control)]
if (nrow(sheet) == 0L)
  stop(sprintf("[de_ranklist] %s: no samples in arms {%s,%s}", contrast, case, control))

# preserve expr-matrix column order; every sheet sample must exist in the matrix.
samples <- colnames(m)[colnames(m) %in% sheet[[sample_col]]]
missing <- setdiff(sheet[[sample_col]], colnames(m))
if (length(missing) > 0L)
  stop(sprintf("[de_ranklist] %s: %d sheet sample(s) absent from expr matrix: %s",
               contrast, length(missing), paste(head(missing, 10), collapse = ", ")))
srow <- match(samples, sheet[[sample_col]])
grp  <- sheet[[group_col]][srow]
M    <- m[, samples, drop = FALSE]

n_case <- sum(grp == case); n_control <- sum(grp == control)
if (n_case < 1L || n_control < 1L)
  stop(sprintf("[de_ranklist] %s: need both arms, got case=%d control=%d",
               contrast, n_case, n_control))

# --- gene filter (scale-appropriate) -----------------------------------------
n_genes_in <- nrow(M)
if (scale %in% COUNT_SCALES) {
  # any non-finite in a count matrix is malformed -> drop; then a manual low-expression
  # CPM filter (filterByExpr stand-in, no edgeR): keep genes reaching CPM>=1 in at least
  # the smaller arm's worth of samples. Stabilises the voom mean-variance trend.
  ok_fin <- rowSums(!is.finite(M)) == 0L
  M <- M[ok_fin, , drop = FALSE]
  lib  <- colSums(M)
  cpmM <- sweep(M, 2L, lib / 1e6, "/")
  keep <- rowSums(cpmM >= 1) >= max(2L, min(n_case, n_control))
  M <- M[keep, , drop = FALSE]
} else {
  # log / already-log: drop genes with any NA/Inf/NaN (fpkm log2(x+1) is finite for
  # x>=0, so the filter mainly catches malformed rows / negatives-from-log_mu are fine).
  ok_fin <- rowSums(!is.finite(M)) == 0L
  M <- M[ok_fin, , drop = FALSE]
}
n_genes_tested <- nrow(M)
if (n_genes_tested == 0L)
  stop(sprintf("[de_ranklist] %s: no genes survive the %s filter", contrast, scale))

# --- model-ready matrix (E) : normalize/transform to a linear-model scale ------
# For voom paths we keep the DGEList so lmFit can use the precision weights (no
# collapse) OR we take E and average per subject (collapse, weights discarded).
voom_obj <- NULL
if (scale %in% COUNT_SCALES) {
  gfac <- factor(grp, levels = c(control, case))
  voom_obj <- voom(M, model.matrix(~ gfac))    # logCPM + weights (library-size norm; trend on ~group)
  E <- voom_obj$E
} else if (scale %in% LOG_XFORM) {
  E <- log2(M + 1)
} else {                                        # ALREADY_LOG
  E <- M
}

design_note <- NULL
if (!is.null(collapse_col)) {
  # ---- longitudinal collapse: one pseudo-sample per subject, then ~ group -----
  subj <- as.character(sheet[[collapse_col]][srow])
  # each subject must be entirely within one arm (between-subject factor).
  sg <- unique(data.table(subject = subj, group = grp))
  bad <- sg[, .N, by = subject][N > 1L]
  if (nrow(bad) > 0L)
    stop(sprintf("[de_ranklist] %s: subject(s) span >1 group (cannot collapse): %s",
                 contrast, paste(bad$subject, collapse = ", ")))
  subj_levels <- unique(subj)                    # stable, expr-order
  Es <- vapply(subj_levels, function(s) rowMeans(E[, subj == s, drop = FALSE]),
               numeric(nrow(E)))
  colnames(Es) <- subj_levels
  grp_s <- grp[match(subj_levels, subj)]
  g <- factor(grp_s, levels = c(control, case))
  design <- model.matrix(~ g)
  fit <- lmFit(Es, design)
  coef_name <- "gcase"
  design_note <- sprintf("~ group on %d subjects (collapsed from %d samples by mean over '%s')",
                         length(subj_levels), length(samples), collapse_col)
  n_unit_case <- sum(grp_s == case); n_unit_control <- sum(grp_s == control)
} else {
  # ---- sample-level model: ~ [covariates +] group, optional block correlation --
  g <- factor(grp, levels = c(control, case))
  fdata <- data.frame(g = g, stringsAsFactors = FALSE)
  rhs <- "g"
  for (cv in design_covs) {
    fdata[[cv]] <- factor(as.character(sheet[[cv]][srow]))
    rhs <- c(cv, rhs)                            # covariates first, group last
  }
  design <- model.matrix(as.formula(paste("~", paste(rhs, collapse = " + "))), data = fdata)
  coef_name <- "gcase"
  if (!coef_name %in% colnames(design))
    stop(sprintf("[de_ranklist] %s: case coef '%s' absent from design cols {%s}",
                 contrast, coef_name, paste(colnames(design), collapse = ", ")))
  fit_input <- if (!is.null(voom_obj)) voom_obj else E
  if (!is.null(block_col)) {
    blk <- as.character(sheet[[block_col]][srow])
    dc  <- duplicateCorrelation(fit_input, design, block = blk)
    fit <- lmFit(fit_input, design, block = blk, correlation = dc$consensus.correlation)
    design_note <- sprintf("~ %s + duplicateCorrelation(block='%s', consensus=%.4f)",
                           paste(rhs, collapse = " + "), block_col, dc$consensus.correlation)
  } else {
    fit <- lmFit(fit_input, design)
    design_note <- sprintf("~ %s", paste(rhs, collapse = " + "))
  }
  n_unit_case <- n_case; n_unit_control <- n_control
}

fit <- eBayes(fit)
tt <- topTable(fit, coef = coef_name, number = Inf, sort.by = "none")

# --- ranked list (FULL precision on `t` — the fgsea ranking statistic) --------
ranked <- data.table(
  gene_id   = rownames(tt),
  logFC     = tt$logFC,
  t         = tt$t,
  P.Value   = tt$P.Value,
  adj.P.Val = tt$adj.P.Val)
ranked <- ranked[order(-t, gene_id)]              # deterministic tie-break
data.table::fwrite(ranked, args[["out-ranked"]], sep = "\t", quote = FALSE, na = "NA")

# --- diagnostics sidecar (measured, not adjudicated) --------------------------
n_sig <- sum(tt$adj.P.Val < 0.05, na.rm = TRUE)
diag <- list(
  contrast          = contrast,
  dataset           = dataset,
  expression_scale  = scale,
  de_path           = if (scale %in% COUNT_SCALES) "voom_limma"
                      else if (scale %in% LOG_XFORM) "log2_lmfit" else "direct_lmfit",
  design            = design_note,
  coef              = coef_name,
  collapsed_to      = if (is.null(collapse_col)) NA else collapse_col,
  block             = if (is.null(block_col)) NA else block_col,
  design_covariates = if (length(design_covs)) design_covs else NA,
  case              = case,
  control           = control,
  n_samples         = length(samples),
  n_case_samples    = n_case,
  n_control_samples = n_control,
  n_case_units      = n_unit_case,           # subjects after collapse (== samples otherwise)
  n_control_units   = n_unit_control,
  n_genes_in        = n_genes_in,
  n_genes_tested    = n_genes_tested,
  design_rank       = as.integer(qr(design)$rank),
  residual_df       = as.numeric(unique(fit$df.residual))[1],
  n_sig_adj_p05     = n_sig,
  prop_sig_adj_p05  = rnd(n_sig / n_genes_tested),
  seed              = seed)
writeLines(toJSON(diag, auto_unbox = TRUE, pretty = TRUE, digits = SIGDIG, na = "null"),
           args[["out-diag"]])

message(sprintf(
  "[de_ranklist] %s (%s, %s): %s | %d vs %d units, %d genes tested, %d BH<0.05",
  contrast, dataset, scale, design_note, n_unit_case, n_unit_control, n_genes_tested, n_sig))
