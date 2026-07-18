#!/usr/bin/env Rscript
# science:code
# status: workflow-owned
# task_ids: [t139]
# science:end
#
# Step-2 signature construction (frozen pre-reg parameter 2, single pipeline) +
# Gate-1a LODO reproducibility DIAGNOSTIC + provenance. NO PAIS projection, NO
# target labels touched.
#
#   filterByExpr(group) -> DGEList -> calcNormFactors(TMM) -> voom
#     -> lmFit(~group) -> eBayes -> topTable
#   signature = signed genes with P.Value < p_nominal_max AND |logFC| > abs_log2fc_min,
#               capped at top cap_top_n by |logFC|. Direction (sign of logFC) retained.
#
# Gate 1a (Amendment 1 operational defs): leave-one-donor-out over all 11 donors,
# full pipeline re-fit per fold; median pairwise Jaccard (union denominator);
# reproducible gene = selection frequency >= freq_min. Step 2 REPORTS the metric;
# it does NOT emit the packet GO/NO-GO (that is Step 5).

suppressPackageStartupMessages({
  library(edgeR); library(limma); library(data.table); library(jsonlite); library(tools)
})

`%||%` <- function(a, b) if (is.null(a)) b else a
arg <- function(flag) { i <- which(commandArgs(TRUE) == flag); if (length(i)) commandArgs(TRUE)[i + 1] else NULL }

counts_path <- arg("--counts")
donors_path <- arg("--donors")
config_path <- arg("--config")
sig_out     <- arg("--signature-out")
prov_out    <- arg("--provenance-out")
lodo_out    <- arg("--lodo-out")

cfg <- yaml::read_yaml(config_path)
P_MAX   <- cfg$signature$p_nominal_max
FC_MIN  <- cfg$signature$abs_log2fc_min
CAP     <- cfg$signature$cap_top_n
CASE    <- cfg$contrast$case_group          # frail
CONTROL <- cfg$contrast$control_group       # healthy-old
FREQ_MIN <- cfg$lodo$reproducible_freq_min
set.seed(cfg$determinism$seed)

## ---- load pseudobulk (gene x donor integer counts) + donor meta ------------
cnt <- as.data.frame(fread(cmd = paste("gzip -dc", shQuote(counts_path))))  # gz w/o R.utils
rownames(cnt) <- cnt[[1]]; cnt[[1]] <- NULL
cnt <- as.matrix(cnt)
meta <- as.data.frame(fread(donors_path))            # cols: donor, group, ...
stopifnot(all(meta$donor %in% colnames(cnt)))
cnt <- cnt[, meta$donor, drop = FALSE]
grp <- factor(meta$group, levels = c(CONTROL, CASE)) # ref = control -> coef is CASE vs CONTROL

## ---- frozen DE pipeline (returns full topTable) ----------------------------
run_de <- function(counts, group) {
  keep <- filterByExpr(counts, group = group)
  dge  <- DGEList(counts = counts[keep, , drop = FALSE])
  dge  <- calcNormFactors(dge, method = "TMM")
  des  <- model.matrix(~group)
  v    <- voom(dge, des)
  fit  <- eBayes(lmFit(v, des))
  tt   <- topTable(fit, coef = 2, number = Inf, sort.by = "none")
  tt$gene <- rownames(tt)
  list(tt = tt, n_kept = sum(keep))
}

## ---- signature genes from a topTable (frozen thresholds + cap) --------------
sig_genes <- function(tt) {
  hit <- tt[tt$P.Value < P_MAX & abs(tt$logFC) > FC_MIN, , drop = FALSE]
  hit <- hit[order(-abs(hit$logFC)), , drop = FALSE]
  if (nrow(hit) > CAP) hit <- hit[seq_len(CAP), , drop = FALSE]
  hit
}

## ---- full-data signature ----------------------------------------------------
full <- run_de(cnt, grp)
sig  <- sig_genes(full$tt)
sig$direction <- ifelse(sig$logFC > 0, "up_in_frail", "down_in_frail")

## optional symbol join (pseudobulk.genes sidecar next to counts) --------------
genes_side <- file.path(dirname(counts_path), "pseudobulk.genes.tsv")
sym <- if (file.exists(genes_side)) {
  g <- as.data.frame(fread(genes_side)); setNames(g$symbol, g$ensembl_id)
} else NULL
sig$symbol <- if (!is.null(sym)) sym[sig$gene] else NA_character_

out_sig <- data.frame(
  ensembl_id = sig$gene, symbol = sig$symbol, direction = sig$direction,
  logFC = round(sig$logFC, 5), P.Value = signif(sig$P.Value, 4),
  adj.P.Val = signif(sig$adj.P.Val, 4), AveExpr = round(sig$AveExpr, 4)
)
out_sig <- out_sig[order(-abs(out_sig$logFC)), ]
dir.create(dirname(sig_out), recursive = TRUE, showWarnings = FALSE)
fwrite(out_sig, sig_out, sep = "\t")

## ---- Gate 1a: leave-one-donor-out reproducibility (DIAGNOSTIC) --------------
donors <- meta$donor
fold_sets <- lapply(seq_along(donors), function(i) {
  idx <- setdiff(seq_along(donors), i)
  de_i <- run_de(cnt[, donors[idx], drop = FALSE], droplevels(grp[idx]))
  sig_genes(de_i$tt)$gene
})
jacc <- function(a, b) { u <- length(union(a, b)); if (u == 0) NA_real_ else length(intersect(a, b)) / u }
pairs <- combn(length(fold_sets), 2)
jvals <- apply(pairs, 2, function(p) jacc(fold_sets[[p[1]]], fold_sets[[p[2]]]))
all_genes <- unique(unlist(fold_sets))
freq <- sapply(all_genes, function(g) mean(sapply(fold_sets, function(s) g %in% s)))
n_repro <- sum(freq >= FREQ_MIN)
median_jacc <- median(jvals, na.rm = TRUE)

lodo <- list(
  n_folds = length(fold_sets),
  fold_signature_sizes = lengths(fold_sets),
  median_pairwise_jaccard = round(median_jacc, 4),
  reproducible_freq_min = FREQ_MIN,
  n_reproducible_genes = n_repro,
  thresholds = list(jaccard_pass_min = cfg$lodo$jaccard_pass_min,
                    jaccard_nogo_max = cfg$lodo$jaccard_nogo_max,
                    min_reproducible_genes = cfg$lodo$min_reproducible_genes),
  gate1a_diagnostic = ifelse(
    median_jacc >= cfg$lodo$jaccard_pass_min & n_repro >= cfg$lodo$min_reproducible_genes, "clears",
    ifelse(median_jacc < cfg$lodo$jaccard_nogo_max | n_repro < cfg$lodo$min_reproducible_genes,
           "trips-nogo", "borderline")),
  note = "Step-2 diagnostic only; the packet GO/NO-GO is emitted at Step 5."
)
writeLines(toJSON(lodo, auto_unbox = TRUE, pretty = TRUE), lodo_out)

## ---- provenance -------------------------------------------------------------
fmt_by_group <- tapply(meta$matrix_format %||% rep(NA, nrow(meta)), meta$group, function(x) paste(sort(unique(x)), collapse = "+"))
prov <- list(
  task = "t139", step = 2, generated_scope = "signature + Gate-1a diagnostic (no projection)",
  R_version = as.character(getRversion()),
  pkg_versions = list(limma = as.character(packageVersion("limma")),
                      edgeR = as.character(packageVersion("edgeR"))),
  inputs = list(counts = counts_path, counts_sha256 = as.character(md5sum(counts_path)),
                donors = donors_path),
  contrast = list(case = CASE, control = CONTROL,
                  n_case = sum(grp == CASE), n_control = sum(grp == CONTROL), unit = "donor"),
  pipeline = "filterByExpr(group)->DGEList->TMM->voom->lmFit(~group)->eBayes->topTable(coef=2)",
  thresholds = list(p_nominal_max = P_MAX, abs_log2fc_min = FC_MIN, cap_top_n = CAP),
  n_genes_after_filter = full$n_kept,
  signature_size = nrow(out_sig),
  signature_up = sum(out_sig$direction == "up_in_frail"),
  signature_down = sum(out_sig$direction == "down_in_frail"),
  batch_caveat = paste0(
    "SUBMISSION-batch is partly confounded with the contrast: all 5 frail + 3 healthy-old donors ",
    "are the F0xx submission (GSM4750xxx, matrix named .tsv.gz); the other 3 healthy-old are the ",
    "later OH submission (GSM5684xxx, .mtx.gz). Both files are MatrixMarket content (extension differs ",
    "only cosmetically), so parsing is uniform, but the frail-vs-old contrast is partly a between-",
    "submission contrast. Format/extension-by-group: ",
    paste(names(fmt_by_group), fmt_by_group, sep = "=", collapse = "; "),
    ". Recorded for the Step-3 batch/transfer gates."),
  seed = cfg$determinism$seed
)
writeLines(toJSON(prov, auto_unbox = TRUE, pretty = TRUE), prov_out)

cat(sprintf("[signature] %d genes (%d up / %d down in frail); LODO median Jaccard=%.3f, %d reproducible genes (%s)\n",
            nrow(out_sig), prov$signature_up, prov$signature_down, median_jacc, n_repro, lodo$gate1a_diagnostic))
