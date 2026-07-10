# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env Rscript
# =============================================================================
# rma_celfiles.R — WP4b front-end: raw Affymetrix .CEL -> probe x sample log2.
#
# The ArrayExpress GWI deposit (E-MEXP-2069) ships ONLY raw .CEL files (no
# processed matrix), so — unlike the GEO series-matrix microarray deposits
# (GSE16059/GSE67311) whose RMA-normalized log2 is embedded and read by
# parse_series_matrix.py — this step MUST normalize from raw. It RMA-normalizes
# the staged CEL blobs (affy::ReadAffy + rma: bg-correct + quantile-normalize +
# median-polish summarize) and emits the SAME probe x sample contract
# parse_series_matrix.py produces, so the downstream chain is reused VERBATIM:
#   harmonize_microarray.R (hgu133plus2.db / GPL570) -> collapse_probes.R (median).
#
# Inputs are the content-addressed acquisition blobs (`<payload>.data`), NOT
# `.CEL`-named files; affy reads a CEL by content, so filenames are passed
# explicitly and sampleNames are set from the aligned --sample list (the blob
# path carries no usable name). --sample / --disease are the per-array sample id
# and case/control-source label, aligned 1:1 with --cel; the samples sheet the
# `prebuilt` handler's `sheet` group_source reads is written from them (this
# script fabricates no group — level_map lives in config, same as GSE67311).
#
# RMA is computed in PURE R (limma + stats), NOT via affy::rma / oligo::rma:
# this host's Bioconductor threaded C (affy rma.background.correct +
# preprocessCore normalize.quantiles) fails with `pthread_create() is 22`
# (EINVAL) — the new glibc/kernel rejects the small hardcoded thread stack those
# libraries request, and it is a COMPILE-TIME defect (no env-var/thread-limit
# fix). affy is used ONLY to read CELs (unthreaded) + resolve the probe->probeset
# map; the three RMA stages are then done thread-free and identically to canonical
# RMA: (1) convolution background = limma normexp (the exact normal+exponential
# model RMA uses), (2) quantile normalization = limma::normalizeQuantiles (same
# Bolstad algorithm as preprocessCore), (3) probeset summary = stats::medpolish
# (median polish) on log2 PM, expression = overall + per-array column effect.
#
# Deterministic: normexp MLE, quantile, and medpolish are fixed given the same CEL
# bytes; log2 values are rounded (signif 6) and written through `gzip -n` (no
# name/mtime) so re-runs are byte-identical (KD10). Single platform only (one CDF).
# =============================================================================
suppressPackageStartupMessages({
  library(affy)
  library(limma)
  library(jsonlite)
})

parse_args <- function() {
  a <- commandArgs(trailingOnly = TRUE)
  out <- list(); i <- 1
  while (i <= length(a)) { out[[sub("^--", "", a[i])]] <- a[i + 1]; i <- i + 2 }
  out
}
args <- parse_args()
split_csv <- function(x) if (is.null(x) || x == "") character(0) else strsplit(x, ",", fixed = TRUE)[[1]]

cels     <- split_csv(args[["cel"]])       # staged blob paths (aligned)
samples  <- split_csv(args[["sample"]])    # per-array sample id (aligned)
disease  <- split_csv(args[["disease"]])   # per-array source label (aligned)
platform <- args[["platform"]]             # e.g. GPL570 (cosmetic; carried into the sheet/report)
if (is.null(platform)) stop("[rma_celfiles] --platform is required")
if (length(cels) == 0L)
  stop("[rma_celfiles] no CEL blobs supplied (--cel)")
if (length(samples) != length(cels) || length(disease) != length(cels))
  stop(sprintf("[rma_celfiles] --cel/--sample/--disease length mismatch (%d/%d/%d)",
               length(cels), length(samples), length(disease)))
missing <- cels[!file.exists(cels)]
if (length(missing) > 0L)
  stop(sprintf("[rma_celfiles] missing CEL blob(s): %s", paste(missing, collapse = ", ")))

# --- read CELs (affy: unthreaded) -> PM intensities + probe->probeset map -------
ab <- ReadAffy(filenames = cels)
sampleNames(ab) <- samples
cdf_name <- annotation(ab)                 # e.g. "hgu133plus2" (chip type from the CEL header)
pm_int <- pm(ab)                           # PM feature x array (raw intensities)
pns <- probeNames(ab)                      # probeset id per PM feature row
pm_int <- pm_int[, samples, drop = FALSE]  # enforce requested array order

# --- (1) RMA convolution background (limma normexp) on the intensity scale ------
pm_bg <- backgroundCorrect.matrix(pm_int, method = "normexp", verbose = FALSE)
# --- (2) quantile normalization (limma; same algorithm as preprocessCore) -------
pm_qn <- normalizeQuantiles(pm_bg)
# --- (3) log2 + median-polish probeset summary (stats::medpolish, thread-free) --
lpm <- log2(pm_qn)
idx <- split(seq_len(nrow(lpm)), pns)
probesets <- sort(names(idx))              # deterministic row order
mat <- matrix(NA_real_, nrow = length(probesets), ncol = length(samples),
              dimnames = list(probesets, samples))
for (ps in probesets) {
  rows <- idx[[ps]]
  mp <- medpolish(lpm[rows, , drop = FALSE], trace.iter = FALSE, eps = 0.01, maxiter = 20)
  mat[ps, ] <- mp$overall + mp$col         # RMA probeset estimate per array
}

n_probes <- nrow(mat)
n_samples <- ncol(mat)
if (n_probes == 0L || n_samples == 0L)
  stop(sprintf("[rma_celfiles] empty RMA matrix (%d probesets x %d samples)", n_probes, n_samples))

# --- probe x sample matrix (ID_REF rows, sample cols), deterministic gzip ------
mat_r <- signif(mat, 6)
df <- data.frame(ID_REF = rownames(mat_r), check.names = FALSE, stringsAsFactors = FALSE)
df <- cbind(df, as.data.frame(mat_r, check.names = FALSE))
dir.create(dirname(args[["out-expr"]]), recursive = TRUE, showWarnings = FALSE)
con <- pipe(sprintf("gzip -n > %s", shQuote(args[["out-expr"]])), "w")
write.table(df, con, sep = "\t", quote = FALSE, row.names = FALSE)
close(con)

# --- samples sheet: sample + disease + platform (group_source `sheet` reads it) -
dir.create(dirname(args[["out-samples"]]), recursive = TRUE, showWarnings = FALSE)
samples_df <- data.frame(sample = samples, disease = disease, platform = platform,
                         check.names = FALSE, stringsAsFactors = FALSE)
write.table(samples_df, args[["out-samples"]], sep = "\t", quote = FALSE, row.names = FALSE)

report <- list(
  platform = platform,
  cdf = cdf_name,
  affy_version = as.character(packageVersion("affy")),
  limma_version = as.character(packageVersion("limma")),
  normalization = "pure-R RMA: limma normexp bg + limma quantile + stats::medpolish summary (affy threaded C unavailable in env)",
  n_probes = n_probes,
  n_samples = n_samples,
  disease_counts = as.list(table(disease))
)
if (!is.null(args[["out-report"]]))
  write_json(report, args[["out-report"]], auto_unbox = TRUE, pretty = TRUE)

message(sprintf("[rma_celfiles] PASS %s (%s): %d probes x %d samples (%s)",
                platform, cdf_name, n_probes, n_samples,
                paste(sprintf("%s=%d", names(table(disease)), as.integer(table(disease))), collapse = " ")))
