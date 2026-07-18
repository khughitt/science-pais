#!/usr/bin/env Rscript
# science:code
# status: workflow-owned
# task_ids: [t139]
# science:end
#
# Step-2b (Amendment 2): batch-adjusted learnability gate (Gate 1a-adj), PRE-TARGET.
# The ONLY change from the frozen primary (signature.R) is the design matrix:
#   ~ frailty            (primary)   ->   ~ submission + frailty   (adjusted)
# Everything else — filterByExpr(group), TMM, voom, thresholds, cap, LODO defs —
# is identical, so any divergence is attributable to the submission covariate.
#
# Motivation: all 5 frail + 3/6 healthy-old training donors are the F0xx submission
# (GSM4750xxx); the other 3 healthy-old are the later OH submission (GSM5684xxx).
# Frail-vs-old is therefore partly a between-submission contrast. Adjusting for
# submission identifies the frailty coefficient chiefly from the within-F0xx
# 5-frail-vs-3-old contrast (OH is old-only -> loads only on the submission term).
#
# Emits (NO PAIS projection, NO target labels):
#   - adjusted signature TSV
#   - Gate-1a-adj verdict JSON (adjusted LODO + signed-overlap-to-primary + rule)
#   - provenance JSON
# The verdict is a PRE-TARGET gate: NO-GO halts the packet before Step 3;
# borderline => INCONCLUSIVE; clears => Step 3 may proceed.

suppressPackageStartupMessages({
  library(edgeR); library(limma); library(data.table); library(jsonlite); library(tools)
})

`%||%` <- function(a, b) if (is.null(a)) b else a
arg <- function(flag) { i <- which(commandArgs(TRUE) == flag); if (length(i)) commandArgs(TRUE)[i + 1] else NULL }

counts_path  <- arg("--counts")
donors_path  <- arg("--donors")
config_path  <- arg("--config")
primary_path <- arg("--primary-signature")   # frozen results/.../signature.tsv
sig_out      <- arg("--signature-out")
prov_out     <- arg("--provenance-out")
verdict_out  <- arg("--verdict-out")

cfg <- yaml::read_yaml(config_path)
P_MAX    <- cfg$signature$p_nominal_max
FC_MIN   <- cfg$signature$abs_log2fc_min
CAP      <- cfg$signature$cap_top_n
CASE     <- cfg$contrast$case_group          # frail
CONTROL  <- cfg$contrast$control_group       # healthy-old
FREQ_MIN <- cfg$lodo$reproducible_freq_min
J_PASS   <- cfg$lodo$jaccard_pass_min
J_NOGO   <- cfg$lodo$jaccard_nogo_max
G_MIN    <- cfg$lodo$min_reproducible_genes
SUBM_LEVELS <- unlist(cfg$step2b$submission_levels)      # ref = F0xx
OV_PASS  <- cfg$step2b$signed_overlap_pass_min
OV_NOGO  <- cfg$step2b$signed_overlap_nogo_max
SHARE_MIN <- cfg$step2b$min_shared_signed_genes
set.seed(cfg$determinism$seed)

## ---- load pseudobulk + donor meta ------------------------------------------
cnt <- as.data.frame(fread(cmd = paste("gzip -dc", shQuote(counts_path))))
rownames(cnt) <- cnt[[1]]; cnt[[1]] <- NULL
cnt <- as.matrix(cnt)
meta <- as.data.frame(fread(donors_path))            # donor, group, gsm, matrix_format
stopifnot(all(meta$donor %in% colnames(cnt)))
cnt <- cnt[, meta$donor, drop = FALSE]

## ---- derive + ASSERT submission batch (Gate hinges on this structure) -------
# F0xx submission donors carry the "F0.." namespace; OH submission carry "OH..".
meta$submission <- ifelse(startsWith(meta$donor, "OH"), "OH", "F0xx")
stopifnot(all(meta$submission %in% SUBM_LEVELS))
xt <- table(meta$submission, meta$group)
exp_ct <- cfg$step2b$expected_crosstab
for (s in names(exp_ct)) for (g in names(exp_ct[[s]])) {
  got <- if (s %in% rownames(xt) && g %in% colnames(xt)) xt[s, g] else 0L
  if (got != exp_ct[[s]][[g]])
    stop(sprintf("[step2b] HALT: submission x group drift — %s/%s expected %d got %d (re-verify before proceeding).",
                 s, g, exp_ct[[s]][[g]], got))
}

grp  <- factor(meta$group, levels = c(CONTROL, CASE))          # ref healthy-old
subm <- factor(meta$submission, levels = SUBM_LEVELS)          # ref F0xx
COEF <- paste0("frailty", CASE)                                # "frailtyfrail"

## ---- frozen DE pipeline, adjusted design (only the design changes) ---------
run_de_adj <- function(counts, frailty, submission) {
  keep <- filterByExpr(counts, group = frailty)                # SAME filter as primary
  dge  <- DGEList(counts = counts[keep, , drop = FALSE])
  dge  <- calcNormFactors(dge, method = "TMM")
  submission <- droplevels(submission); frailty <- droplevels(frailty)
  if (nlevels(submission) < 2 || nlevels(frailty) < 2)
    stop("[step2b] HALT: a fold lost a submission or frailty level — adjusted coef not identifiable")
  des  <- model.matrix(~ submission + frailty)
  cn   <- paste0("frailty", levels(frailty)[2])                # matches COEF when frailty ref intact
  if (!cn %in% colnames(des)) stop(sprintf("[step2b] HALT: coef %s absent from design", cn))
  v    <- voom(dge, des)
  fit  <- eBayes(lmFit(v, des))
  tt   <- topTable(fit, coef = cn, number = Inf, sort.by = "none")
  tt$gene <- rownames(tt)
  list(tt = tt, n_kept = sum(keep))
}

sig_genes <- function(tt) {
  hit <- tt[tt$P.Value < P_MAX & abs(tt$logFC) > FC_MIN, , drop = FALSE]
  hit <- hit[order(-abs(hit$logFC)), , drop = FALSE]
  if (nrow(hit) > CAP) hit <- hit[seq_len(CAP), , drop = FALSE]
  hit
}

## ---- full-data adjusted signature ------------------------------------------
full <- run_de_adj(cnt, grp, subm)
sig  <- sig_genes(full$tt)
sig$direction <- ifelse(sig$logFC > 0, "up_in_frail", "down_in_frail")

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

## ---- adjusted LODO (identical defs to Gate 1a, adjusted model) --------------
donors <- meta$donor
fold_sets <- lapply(seq_along(donors), function(i) {
  idx <- setdiff(seq_along(donors), i)
  de_i <- run_de_adj(cnt[, donors[idx], drop = FALSE], grp[idx], subm[idx])
  sig_genes(de_i$tt)$gene
})
jacc <- function(a, b) { u <- length(union(a, b)); if (u == 0) NA_real_ else length(intersect(a, b)) / u }
pairs <- combn(length(fold_sets), 2)
jvals <- apply(pairs, 2, function(p) jacc(fold_sets[[p[1]]], fold_sets[[p[2]]]))
all_genes <- unique(unlist(fold_sets))
freq <- sapply(all_genes, function(g) mean(sapply(fold_sets, function(s) g %in% s)))
n_repro <- sum(freq >= FREQ_MIN)
median_jacc <- median(jvals, na.rm = TRUE)

## ---- signed overlap vs the FROZEN PRIMARY signature ------------------------
prim <- as.data.frame(fread(primary_path))           # ensembl_id, direction, ...
prim_dir <- setNames(prim$direction, prim$ensembl_id)
adj_dir  <- setNames(out_sig$direction, out_sig$ensembl_id)
A <- names(prim_dir); B <- names(adj_dir)
uni <- union(A, B); shared <- intersect(A, B)
signed_shared <- shared[prim_dir[shared] == adj_dir[shared]]
signed_jaccard <- if (length(uni)) length(signed_shared) / length(uni) else NA_real_
raw_jaccard    <- if (length(uni)) length(shared) / length(uni) else NA_real_
dir_concord    <- if (length(shared)) length(signed_shared) / length(shared) else NA_real_

## ---- Gate 1a-adj verdict (pre-target decision rule, Amendment 2) -----------
adj_lodo_clears <- (median_jacc >= J_PASS) && (n_repro >= G_MIN)
adj_lodo_nogo   <- (median_jacc <  J_NOGO) || (n_repro <  G_MIN)
overlap_clears  <- (!is.na(signed_jaccard) && signed_jaccard >= OV_PASS) && (length(signed_shared) >= SHARE_MIN)
overlap_nogo    <- (!is.na(signed_jaccard) && signed_jaccard <  OV_NOGO)

verdict <- if (adj_lodo_nogo || overlap_nogo) {
  "NO-GO"
} else if (adj_lodo_clears && overlap_clears) {
  "clears"
} else {
  "INCONCLUSIVE (borderline)"
}

verdict_obj <- list(
  gate = "1a-adj", step = "2b", scope = "pre-target batch-adjusted learnability (Amendment 2)",
  design = "~ submission + frailty", frailty_coef = COEF,
  submission_crosstab = as.list(as.data.frame.matrix(xt)),
  adjusted_signature = list(
    size = nrow(out_sig),
    up_in_frail = sum(out_sig$direction == "up_in_frail"),
    down_in_frail = sum(out_sig$direction == "down_in_frail"),
    n_genes_after_filter = full$n_kept),
  adjusted_lodo = list(
    n_folds = length(fold_sets),
    fold_signature_sizes = lengths(fold_sets),
    median_pairwise_jaccard = round(median_jacc, 4),
    n_reproducible_genes = n_repro,
    reproducible_freq_min = FREQ_MIN,
    clears = adj_lodo_clears, trips_nogo = adj_lodo_nogo),
  overlap_vs_primary = list(
    primary_size = length(A), adjusted_size = length(B),
    union = length(uni), shared_genes = length(shared),
    signed_shared_genes = length(signed_shared),
    signed_jaccard = round(signed_jaccard, 4),
    raw_jaccard = round(raw_jaccard, 4),
    direction_concordance = round(dir_concord, 4),
    clears = overlap_clears, trips_nogo = overlap_nogo),
  thresholds = list(
    jaccard_pass_min = J_PASS, jaccard_nogo_max = J_NOGO, min_reproducible_genes = G_MIN,
    signed_overlap_pass_min = OV_PASS, signed_overlap_nogo_max = OV_NOGO,
    min_shared_signed_genes = SHARE_MIN),
  verdict = verdict,
  decision_rule = paste(
    "NO-GO iff adjusted-LODO trips (median Jaccard < 0.30 or < 20 reproducible genes) OR signed",
    "overlap-to-primary < 0.30; clears iff adjusted-LODO clears (>=0.50 & >=20) AND signed overlap",
    ">=0.50 with >=20 shared signed genes; otherwise INCONCLUSIVE. NO-GO/borderline halt the packet",
    "before Step 3; the cytokine panel is non-adjudicating face validity until this clears."),
  note = "PRE-TARGET gate. No PAIS projection or target label is touched here."
)
writeLines(toJSON(verdict_obj, auto_unbox = TRUE, pretty = TRUE), verdict_out)

## ---- provenance -------------------------------------------------------------
prov <- list(
  task = "t139", step = "2b", amendment = 2,
  generated_scope = "batch-adjusted signature + Gate-1a-adj verdict (no projection)",
  R_version = as.character(getRversion()),
  pkg_versions = list(limma = as.character(packageVersion("limma")),
                      edgeR = as.character(packageVersion("edgeR"))),
  inputs = list(counts = counts_path, counts_sha256 = as.character(md5sum(counts_path)),
                donors = donors_path, primary_signature = primary_path,
                primary_sha256 = as.character(md5sum(primary_path))),
  pipeline = "filterByExpr(group)->DGEList->TMM->voom->lmFit(~submission+frailty)->eBayes->topTable(frailty coef)",
  contrast = list(case = CASE, control = CONTROL, adjusted_for = "submission",
                  identified_by = "within-F0xx 5-frail-vs-3-old (OH old-only loads on submission term)"),
  seed = cfg$determinism$seed
)
writeLines(toJSON(prov, auto_unbox = TRUE, pretty = TRUE), prov_out)

cat(sprintf(
  "[step2b] adjusted sig %d genes (%d up/%d down); adj-LODO Jaccard=%.3f, %d reproducible; signed overlap vs primary=%.3f (%d/%d shared signed); VERDICT: %s\n",
  nrow(out_sig), sum(out_sig$direction == "up_in_frail"), sum(out_sig$direction == "down_in_frail"),
  median_jacc, n_repro, signed_jaccard, length(signed_shared), length(shared), verdict))
