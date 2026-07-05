# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Harmonise exposure<->outcome and run MR estimators (plan:0009 Task 3 naive arm).
#
# Deliberate copy-and-adapt of the plan:0007 `wave1-mr/scripts/harmonize_estimate.R`
# into the isolated `wave1-mr-hormone/` workflow (plan:0003 KD4 / plan:0007
# isolation convention — the frozen run-of-record is never edited). Same
# stream/selective-extract of the instrument SNPs from the multi-GB outcome by
# hm_rsid (grep, never a full in-memory load), harmonise_data(action = 2), and
# IVW/Egger/weighted-median estimator core as plan:0007. Load-bearing changes
# for the hormone pilot (plan:0009 Task 3):
#
#   1. New args + config-driven --stratum resolution (spec <- config$exposures).
#   2. Eligibility guard (loud skip): a quarantined stratum's Task-2 sidecar has
#      eligible_for_mr == false -> write a "skipped-quarantined" results JSON +
#      empty (header-only) harmonised TSV, no estimator run.
#   3. Exposure format_data mapping uses the Task-2 TSV's EA/OA columns (not
#      effect_allele/other_allele).
#   4. Graceful <3-harmonised handling: record "insufficient-harmonised-instruments"
#      and return, rather than stop() (weak is informative, not fatal).
#   5. Hormone estimand + KD1 (ancestry-flag/non-primary) + KD3 (bounded-sex)
#      labels, plus the machine-readable sample_overlap_uncorrected /
#      naive_comparator_only flags (naive arm; MRlap overlap correction is
#      Task 4).
#   6. Enforced weighted-median nboot: passed explicitly via `parameters =`
#      (mr() alone silently uses default_parameters()'s nboot=1000), and the
#      RESOLVED value is recorded in the results JSON.
#   7. Estimator-output hard-stop: a well-instrumented stratum returning fewer
#      than the configured methods, or any non-finite b/se/pval, is a
#      TECHNICAL fault (not "weak") and HALTs.
#   8. Harmonisation-dropout quality flag: high_harmonisation_dropout when
#      kept/input < estimate$harmonisation_dropout_warn_frac (flag, not gate).

suppressPackageStartupMessages({
  library(data.table)
  library(TwoSampleMR)
})

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag) { i <- match(flag, args); if (is.na(i)) stop(paste("missing", flag)); args[[i + 1L]] }
cfg <- yaml::read_yaml(get_arg("--config"))
stratum <- get_arg("--stratum")
instrument_path <- get_arg("--instrument")
sidecar_path <- get_arg("--sidecar")
outcome_path <- get_arg("--outcome")
harmonised_out <- get_arg("--harmonised-out")
results_out <- get_arg("--results-out")

# --- resolve this stratum's spec from config$exposures (edit 1) --------------
specs <- cfg$exposures
match_idx <- which(vapply(specs, function(s) identical(s$name, stratum), logical(1)))
if (length(match_idx) != 1)
  stop(sprintf("harmonize_estimate[%s]: stratum not found (or not unique) in config$exposures — HALT", stratum))
spec <- specs[[match_idx]]

dir.create(dirname(harmonised_out), recursive = TRUE, showWarnings = FALSE)
dir.create(dirname(results_out), recursive = TRUE, showWarnings = FALSE)

write_results <- function(...) {
  fields <- list(...)
  base <- list(
    stratum = stratum, accession = spec$accession,
    trait = spec$trait, sex = spec$sex,
    exposure = stratum, outcome = cfg$outcome$name
  )
  results <- modifyList(base, fields)
  writeLines(jsonlite::toJSON(results, auto_unbox = TRUE, pretty = TRUE, null = "null"), results_out)
}

# --- hormone estimand + KD1/KD3 labels (hoisted; used in all write_results calls) ----
estimand <- sprintf(paste0("germline-liability IV effect of a 1-SD increase in %s ",
  "(%s; Ruth 2020, European UKB continuous-trait GWAS) on long-COVID liability ",
  "(log-OR), 1000G-EUR-clumped genome-wide-significant instruments."),
  spec$trait, spec$sex)
labels <- list(
  ancestry_flag = paste0("Outcome GCST90454541 is a European-dominant (~85-90%) ",
    "multi-ancestry HGI broad/population meta; no EUR-only sibling. ANCESTRY-FLAGGED, ",
    "NON-PRIMARY (KD1) — exploratory/robustness only, never primary evidence for ",
    "hypothesis:0005 / question:0007 / question:0013."),
  bounded_sex = paste0("Male-only / female-only strata give a BOUNDED ",
    "exposure-architecture read against a mixed-sex outcome (KD3) — NOT a ",
    "genotype x sex effect-modification test. No sex-modification claim."),
  exposure_side = paste0("SHBG and total testosterone share Ruth instrument loci ",
    "(steroid-axis pleiotropy plausible; Egger+WM only partially bound it). ",
    "Female-testosterone is weakest-instrumented yet most decision-relevant."),
  sample_overlap_uncorrected = TRUE,   # Ruth = 100% UKB, HGI pools UKB → structural
  naive_comparator_only = TRUE)        # overlap NOT corrected here; MRlap is Task 4

# --- eligibility guard (edit 2: loud skip, no estimator run) -----------------
sidecar <- jsonlite::fromJSON(sidecar_path)
if (isFALSE(sidecar$eligible_for_mr)) {
  reasons <- sidecar$eligibility_reasons
  cat(sprintf("harmonize_estimate[%s]: SKIP — quarantined (eligible_for_mr=false), reasons=[%s]\n",
              stratum, paste(reasons, collapse = ",")))
  write_results(status = "skipped-quarantined", eligibility_reasons = I(reasons), methods = list(),
                estimand = estimand, labels = labels)
  fwrite(data.table(SNP = character(0), chr = integer(0), pos = numeric(0),
                     EA = character(0), OA = character(0), beta = numeric(0),
                     se = numeric(0), eaf = numeric(0), pval = numeric(0), F = numeric(0)),
         harmonised_out, sep = "\t")
  quit(save = "no", status = 0)
}

inst <- fread(instrument_path)
n_instruments_input <- nrow(inst)

# --- stream-extract the instrument SNPs from the outcome (no full load) -------
rsfile <- tempfile(); writeLines(unique(inst$SNP), rsfile)
invisible(gc(reset = TRUE))
t0 <- Sys.time()
cmd <- sprintf("bash -c 'zcat %s | head -1; zcat %s | grep -Fw -f %s'",
               shQuote(outcome_path), shQuote(outcome_path), shQuote(rsfile))
out_sub <- fread(cmd = cmd, showProgress = FALSE)
extract_secs <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
peak_mb <- sum(gc()[, 6])   # max used across the two heaps (MB), approximate
cat(sprintf("harmonize_estimate[%s]: extracted %d outcome rows for %d instruments in %.1fs (peak ~%.0f MB)\n",
            stratum, nrow(out_sub), nrow(inst), extract_secs, peak_mb))

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

# --- format for TwoSampleMR (edit 3: Task-2 TSV uses EA/OA) ------------------
exp_dat <- format_data(
  as.data.frame(inst), type = "exposure", snp_col = "SNP", beta_col = "beta",
  se_col = "se", effect_allele_col = "EA", other_allele_col = "OA",
  eaf_col = "eaf", pval_col = "pval")
exp_dat$exposure <- spec$name

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
cat(sprintf("harmonize_estimate[%s]: harmonised %d/%d instruments retained (action=%s); %d dropped\n",
            stratum, nrow(kept), n_before, cfg$harmonise$action, length(dropped)))

# --- harmonisation-dropout quality flag (edit 8, flag not gate) --------------
quality_flags <- character(0)
if (nrow(kept) / nrow(inst) < cfg$estimate$harmonisation_dropout_warn_frac)
  quality_flags <- c(quality_flags, "high_harmonisation_dropout")

# --- graceful <3-harmonised handling (edit 4: record, don't abort) -----------
if (nrow(kept) < 3) {
  cat(sprintf("WEAK: %s — only %d harmonised instruments (<3); recording, not estimating\n",
              stratum, nrow(kept)))
  write_results(status = "insufficient-harmonised-instruments",
                n_instruments_input = n_instruments_input, n_harmonised = nrow(kept),
                dropped = I(as.character(dropped)), quality_flags = I(quality_flags),
                methods = list(), estimand = estimand, labels = labels)
  fwrite(dat, harmonised_out, sep = "\t"); quit(save = "no", status = 0)
}

# --- estimators + enforced weighted-median bootstrap (edit 6, P1) ------------
set.seed(as.integer(cfg$estimate$weighted_median_seed))
wm_nboot <- as.integer(cfg$estimate$weighted_median_bootstrap_n)
params <- modifyList(default_parameters(), list(nboot = wm_nboot))
res   <- mr(dat, method_list = as.character(cfg$estimate$methods), parameters = params)
egger <- tryCatch(mr_pleiotropy_test(dat), error = function(e) NULL)   # Egger intercept

# --- estimator-output hard-stop (edit 7, P1 technical fault) -----------------
want <- as.character(cfg$estimate$methods)                     # every configured method present
got  <- res$method
if (!all(vapply(c("Inverse variance weighted","MR Egger","Weighted median"),
                function(m) any(grepl(m, got, fixed = TRUE)), logical(1))))
  stop(sprintf("harmonize_estimate[%s]: mr() returned %d/%d configured methods — HALT (technical)",
               stratum, length(got), length(want)))
if (!all(is.finite(c(res$b, res$se, res$pval))))
  stop(sprintf("harmonize_estimate[%s]: non-finite b/se/pval in estimator output — HALT (technical)",
               stratum))

ivw_b <- res$b[grepl("Inverse variance", res$method)]
signs <- sign(res$b)
concordant <- length(unique(signs)) == 1

egger_intercept <- if (is.null(egger)) {
  list(intercept = NULL, se = NULL, pval = NULL, reason = "mr_pleiotropy_test() failed or unavailable")
} else {
  list(intercept = egger$egger_intercept, se = egger$se, pval = egger$pval)
}

write_results(
  estimand = estimand, status = "estimated",
  n_instruments_input = n_instruments_input, n_harmonised = nrow(kept),
  mean_f_instruments = if ("F" %in% names(inst)) mean(inst$F) else NA,
  methods = lapply(seq_len(nrow(res)), function(i) {
    list(method = res$method[i], nsnp = res$nsnp[i], b = res$b[i],
         se = res$se[i], pval = res$pval[i], or = exp(res$b[i]))
  }),
  egger_intercept = egger_intercept,
  concordance = list(all_methods_same_sign = concordant, ivw_beta = if (length(ivw_b)) ivw_b else NA),
  dropped_snps = I(as.character(dropped)), quality_flags = I(quality_flags),
  harmonise_action = as.integer(cfg$harmonise$action),
  weighted_median_seed = cfg$estimate$weighted_median_seed,
  weighted_median_bootstrap_n_resolved = wm_nboot,
  resources = list(outcome_extract_seconds = extract_secs, peak_memory_mb = peak_mb),
  labels = labels
)

fwrite(dat, harmonised_out, sep = "\t")
cat("harmonize_estimate: wrote", results_out, "and", harmonised_out, "\n")
