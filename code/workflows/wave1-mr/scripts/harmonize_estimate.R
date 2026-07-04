# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Harmonise exposure<->outcome and run MR estimators (Wave-1 pilot, plan:0007 3-4).
#
# STREAM/selective-extract the instrument SNPs from the multi-GB outcome by
# hm_rsid (grep, never a full in-memory load); record peak memory + wall-clock.
# harmonise_data(action = 2) (infer palindromic by EAF, drop ambiguous; log all
# drops). Effects are log-OR (both binary). IVW (primary), MR-Egger,
# weighted-median; the WM bootstrap SE uses a fixed seed. Emit harmonised table +
# mr_results.json with the ancestry/mechanics-only label.

suppressPackageStartupMessages({
  library(data.table)
  library(TwoSampleMR)
})

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag) { i <- match(flag, args); if (is.na(i)) stop(paste("missing", flag)); args[[i + 1L]] }
cfg <- yaml::read_yaml(get_arg("--config"))
instrument_path <- get_arg("--instrument")
outcome_path <- get_arg("--outcome")
harmonised_out <- get_arg("--harmonised-out")
results_out <- get_arg("--results-out")

inst <- fread(instrument_path)

# --- stream-extract the instrument SNPs from the outcome (no full load) -------
rsfile <- tempfile(); writeLines(unique(inst$SNP), rsfile)
invisible(gc(reset = TRUE))
t0 <- Sys.time()
cmd <- sprintf("bash -c 'zcat %s | head -1; zcat %s | grep -Fw -f %s'",
               shQuote(outcome_path), shQuote(outcome_path), shQuote(rsfile))
out_sub <- fread(cmd = cmd, showProgress = FALSE)
extract_secs <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
peak_mb <- sum(gc()[, 6])   # max used across the two heaps (MB), approximate
cat(sprintf("harmonize_estimate: extracted %d outcome rows for %d instruments in %.1fs (peak ~%.0f MB)\n",
            nrow(out_sub), nrow(inst), extract_secs, peak_mb))

pick <- function(dt, cands, what) { h <- cands[cands %in% names(dt)]
  if (!length(h)) stop(sprintf("no column for %s (tried %s)", what, paste(cands, collapse=", "))); h[[1]] }
oc <- list(
  rsid = pick(out_sub, c("hm_rsid","rsid","variant_id"), "rsid"),
  ea   = pick(out_sub, c("hm_effect_allele","effect_allele"), "effect_allele"),
  oa   = pick(out_sub, c("hm_other_allele","other_allele"), "other_allele"),
  beta = pick(out_sub, c("hm_beta","beta"), "beta"),
  se   = pick(out_sub, c("standard_error","se"), "se"),
  eaf  = pick(out_sub, c("hm_effect_allele_frequency","effect_allele_frequency"), "eaf"),
  pval = pick(out_sub, c("p_value","pval","p"), "pval")
)

# --- format for TwoSampleMR --------------------------------------------------
exp_dat <- format_data(
  as.data.frame(inst), type = "exposure", snp_col = "SNP", beta_col = "beta",
  se_col = "se", effect_allele_col = "effect_allele", other_allele_col = "other_allele",
  eaf_col = "eaf", pval_col = "pval"
)
exp_dat$exposure <- cfg$exposure$name

out_dat <- format_data(
  as.data.frame(out_sub), type = "outcome", snp_col = oc$rsid, beta_col = oc$beta,
  se_col = oc$se, effect_allele_col = oc$ea, other_allele_col = oc$oa,
  eaf_col = oc$eaf, pval_col = oc$pval
)
out_dat$outcome <- cfg$outcome$name

n_before <- nrow(exp_dat)
dat <- harmonise_data(exp_dat, out_dat, action = as.integer(cfg$harmonise$action))
kept <- dat[dat$mr_keep, , drop = FALSE]
dropped <- dat[!dat$mr_keep, "SNP"]
cat(sprintf("harmonize_estimate: harmonised %d/%d instruments retained (action=%s); %d dropped\n",
            nrow(kept), n_before, cfg$harmonise$action, length(dropped)))
if (nrow(kept) < 3) stop("harmonize_estimate: < 3 harmonised instruments — estimators unreliable, HALT")

# --- estimators: IVW (primary), Egger, weighted-median (seeded) --------------
set.seed(as.integer(cfg$estimate$weighted_median_seed))
res <- mr(dat, method_list = as.character(cfg$estimate$methods))
egger <- tryCatch(mr_pleiotropy_test(dat), error = function(e) NULL)

by_method <- setNames(lapply(seq_len(nrow(res)), function(i) as.list(res[i, ])), res$method)
ivw_b <- res$b[grepl("Inverse variance", res$method)]
signs <- sign(res$b)
concordant <- length(unique(signs)) == 1

results <- list(
  estimand = "germline-liability IV effect of SLE liability (log-OR) on long-COVID liability (log-OR)",
  label = paste0("MECHANICS-ONLY — outcome is a European-dominant multi-ancestry meta ",
                 "(no EUR-only sibling); NOT a valid ancestry-matched primary estimate ",
                 "and NOT evidence for/against hypothesis:0007 or question:0022 ",
                 "(plan:0007 ancestry hard-stop + acceptance gate)."),
  exposure = cfg$exposure$name, outcome = cfg$outcome$name,
  n_instruments_harmonised = nrow(kept),
  mean_f_instruments = if ("F" %in% names(inst)) mean(inst$F) else NA,
  methods = lapply(seq_len(nrow(res)), function(i) {
    list(method = res$method[i], nsnp = res$nsnp[i], b = res$b[i],
         se = res$se[i], pval = res$pval[i], or = exp(res$b[i]))
  }),
  egger_intercept = if (is.null(egger)) NULL else list(
    intercept = egger$egger_intercept, se = egger$se, pval = egger$pval),
  concordance = list(all_methods_same_sign = concordant, ivw_beta = if (length(ivw_b)) ivw_b else NA),
  dropped_snps = as.character(dropped),
  resources = list(outcome_extract_seconds = extract_secs, peak_memory_mb = peak_mb),
  weighted_median_seed = cfg$estimate$weighted_median_seed
)

dir.create(dirname(harmonised_out), recursive = TRUE, showWarnings = FALSE)
fwrite(dat, harmonised_out, sep = "\t")
dir.create(dirname(results_out), recursive = TRUE, showWarnings = FALSE)
writeLines(jsonlite::toJSON(results, auto_unbox = TRUE, pretty = TRUE, null = "null"), results_out)
cat("harmonize_estimate: wrote", results_out, "and", harmonised_out, "\n")
