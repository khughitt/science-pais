#!/usr/bin/env Rscript
# =============================================================================
# permutation_null.R — WP6: paired sample-label permutation null for ONE
# (concordance-pair × DB) cell. THE HEAVY RULE.
#
# The pre-reg's null is the FULL limma→fgsea→NES→ρ chain re-run under permuted
# SAMPLE labels (not a gene shuffle), so it inherits the real gene–gene and
# set–set correlation. For B paired permutations we relabel arm x WITHIN its
# locked pool and arm y WITHIN its locked pool INDEPENDENTLY (no cross-arm /
# four-group joint relabeling), re-fit limma → moderated-t → fgsea NES → Spearman
# ρ, and report one-sided p_perm = fraction of permuted ρ ≥ observed.
#
# NES routine (config permutation.null_nes): the permuted NES use **fgseaSimple**
# with a fixed gene-permutation count — the OBSERVED rho_obs here uses the SAME
# fgseaSimple routine, so p_perm is internally consistent (the headline reported
# ρ + scatter come from the WP5 multilevel NES via concordance.py; the two agree
# to ~1e-3). This computes the already-locked NES statistic; B is unchanged.
#
# Determinism (plan:0003 KD10): RNGkind("L'Ecuyer-CMRG") + BiocParallel
# bpparam(RNGseed = cell_seed) gives each permutation task an independent,
# fixed substream, so p_perm is reproducible regardless of worker count or run
# order; the per-cell seed is derived from the master seed + the cell's index.
# =============================================================================
suppressPackageStartupMessages({
  library(limma)
  library(fgsea)
  library(data.table)
  library(BiocParallel)
})

parse_args <- function() {
  a <- commandArgs(trailingOnly = TRUE)
  out <- list(); i <- 1
  while (i <= length(a)) { out[[sub("^--", "", a[i])]] <- a[i + 1]; i <- i + 2 }
  out
}
args <- parse_args()

pair      <- args[["pair"]]
db        <- args[["db"]]
B         <- as.integer(args[["B"]])
nperm     <- as.integer(args[["nperm"]])
min_size  <- as.integer(args[["min-size"]])
max_size  <- as.integer(args[["max-size"]])
cell_seed <- as.integer(args[["seed"]])
nthreads  <- as.integer(args[["threads"]])
rng_kind  <- args[["rng-kind"]]
for (k in c("B", "nperm", "min-size", "max-size", "seed", "threads"))
  if (is.na(as.integer(args[[k]]))) stop(sprintf("[permutation_null] --%s required (integer)", k))
if (!identical(rng_kind, "L'Ecuyer-CMRG"))
  stop(sprintf("[permutation_null] rng-kind '%s' not implemented — only L'Ecuyer-CMRG", rng_kind))

RNGkind(rng_kind)

# --- read one arm's pool: genes × pool-samples matrix + true case/control labels
read_pool <- function(expr, sheet_path, sample_col, group_col, case, control) {
  dt <- fread(cmd = sprintf("gzip -dc %s", shQuote(expr)),
              check.names = FALSE, na.strings = c("", "NA"))
  m <- as.matrix(dt[, -1L, with = FALSE]); rownames(m) <- as.character(dt[[1]])
  sheet <- fread(sheet_path, check.names = FALSE, na.strings = c("", "NA"))
  map <- unique(data.table(sample = as.character(sheet[[sample_col]]),
                           group  = as.character(sheet[[group_col]])))
  if (nrow(map[, .N, by = sample][N > 1L]) > 0L)
    stop("[permutation_null] a sample maps to >1 group")
  map <- map[group %in% c(case, control)]
  samples <- colnames(m)[colnames(m) %in% map$sample]
  if (!all(map$sample %in% colnames(m)))
    stop("[permutation_null] sheet sample(s) absent from expr matrix")
  grp_of <- setNames(map$group, map$sample)
  M <- m[, samples, drop = FALSE]
  M <- M[rowSums(!is.finite(M)) == 0L, , drop = FALSE]   # drop NA/Inf genes
  list(M = M, labels = unname(grp_of[samples]), case = case, control = control)
}

# --- limma moderated-t ranking for a given binary labelling of a pool ---------
fit_rank <- function(M, labels, case, control) {
  g <- factor(labels, levels = c(control, case))
  design <- model.matrix(~ g)
  fit <- eBayes(lmFit(M, design))
  tt <- topTable(fit, coef = 2L, number = Inf, sort.by = "none")
  stats <- tt$t; names(stats) <- rownames(tt)
  stats[is.finite(stats)]
}

# --- fgseaSimple NES vector over ALL pinned sets (NA where untestable) --------
nes_vec <- function(stats, pathways) {
  res <- suppressWarnings(suppressMessages(
    fgseaSimple(pathways = pathways, stats = stats, nperm = nperm,
                minSize = min_size, maxSize = max_size,
                scoreType = "std", BPPARAM = SerialParam())))
  v <- setNames(rep(NA_real_, length(pathways)), names(pathways))
  v[res$pathway] <- res$NES
  v
}

# --- Spearman ρ over the shared testable (non-NA both arms) universe ----------
rho_of <- function(nx, ny) {
  ok <- is.finite(nx) & is.finite(ny)
  if (sum(ok) < 3L) return(NA_real_)
  cor(nx[ok], ny[ok], method = "spearman")
}

# --- one permuted labelling of a pool (relabel within the locked pool) --------
permute_labels <- function(n, case_n, case, control) {
  lab <- rep(control, n)
  lab[sample.int(n, case_n)] <- case
  lab
}

xa <- read_pool(args[["x-expr"]], args[["x-sheet"]], args[["x-sample-col"]],
                args[["x-group-col"]], args[["x-case"]], args[["x-control"]])
ya <- read_pool(args[["y-expr"]], args[["y-sheet"]], args[["y-sample-col"]],
                args[["y-group-col"]], args[["y-case"]], args[["y-control"]])
pathways <- readRDS(args[["geneset"]])

nx <- ncol(xa$M); ny <- ncol(ya$M)
xcase_n <- sum(xa$labels == xa$case); ycase_n <- sum(ya$labels == ya$case)

# observed ρ — SAME fgseaSimple routine as the null (internal consistency)
set.seed(cell_seed)
rho_obs <- rho_of(nes_vec(fit_rank(xa$M, xa$labels, xa$case, xa$control), pathways),
                  nes_vec(fit_rank(ya$M, ya$labels, ya$case, ya$control), pathways))
if (!is.finite(rho_obs)) stop("[permutation_null] observed ρ undefined")

# B paired permutations: arm x and arm y relabelled INDEPENDENTLY within pools.
# bpparam(RNGseed) → each task b is a fixed L'Ecuyer substream (order/worker-
# count independent). nproc=1 fgseaSimple inside each task (no nested parallel).
bp <- MulticoreParam(workers = nthreads, RNGseed = cell_seed, progressbar = FALSE)
null_rho <- unlist(bplapply(seq_len(B), function(b) {
  lx <- permute_labels(nx, xcase_n, xa$case, xa$control)
  ly <- permute_labels(ny, ycase_n, ya$case, ya$control)
  rho_of(nes_vec(fit_rank(xa$M, lx, xa$case, xa$control), pathways),
         nes_vec(fit_rank(ya$M, ly, ya$case, ya$control), pathways))
}, BPPARAM = bp))

n_bad <- sum(!is.finite(null_rho))
if (n_bad > 0L)
  message(sprintf("[permutation_null] %d/%d permutations gave undefined ρ (excluded)", n_bad, B))
valid <- null_rho[is.finite(null_rho)]
B_eff <- length(valid)
# one-sided p_perm = fraction of permuted ρ ≥ observed (pre-reg:0002).
p_perm <- sum(valid >= rho_obs) / B_eff

perm <- data.table(pair = pair, db = db, rho_obs = rho_obs, p_perm = p_perm, B = B_eff)
fwrite(perm, args[["out-perm"]], sep = "\t", quote = FALSE, na = "NA")
fwrite(data.table(perm_index = seq_along(valid), rho_perm = valid),
       args[["out-nulldist"]], sep = "\t", quote = FALSE, na = "NA")

message(sprintf(
  "[permutation_null] %s x %s: rho_obs=%.6f, p_perm=%.5f (B_eff=%d, nperm=%d, seed=%d, workers=%d)",
  pair, db, rho_obs, p_perm, B_eff, nperm, cell_seed, nthreads))
