# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Run MRlap overlap-corrected MR for one hormone stratum (plan:0009 Task 4).
#
# One call per stratum: germline hormone liability (canonical Ruth exposure) ->
# long-COVID (canonical HGI outcome), using MRlap's own genome-wide instrument
# selection + internal cross-trait LDSC (GenomicSEM engine) against the staged
# EUR eur_w_ld_chr / w_hm3.snplist references (Task 1). MRlap returns BOTH its
# own uncorrected ("observed") estimate on its distance-pruned instrument set
# AND the overlap-corrected estimate; both are on MRlap's standardized
# (SD-outcome-liability per 1-SD-exposure) scale -- NOT log-OR, so no
# `or = exp(b)` is ever computed here. Design-of-record: doc/plans/
# 2026-07-05-plan0009-task4-mrlap.md ("run_mrlap.R" section + Step 6).
#
# Load-bearing details:
#   1. CWD isolation: MRlap writes temp files named from exposure_name/
#      outcome_name into the PROCESS CWD -- the shared outcome_name would
#      collide across strata under any -c>1 Snakemake run. setwd() into a
#      stratum-specific tempdir before the call, restore after (on.exit). All
#      paths the isolated process must still see (exposure/outcome canonical
#      files, the ld/hm3 reference dirs from config, the results/dump outputs)
#      are resolved to ABSOLUTE paths *before* the setwd, else MRlap would try
#      to resolve the config's project-root-relative `ld`/`hm3` strings inside
#      the tempdir and fail to find them.
#   2. Defensive extraction: every load-bearing field is located by name, never
#      guessed -- an absent field HALTs naming it, rather than silently
#      emitting a null. LDSC standard-error fields are treated as optional
#      (recorded null if absent; not a HALT) per the plan's "+se if present"
#      qualifier.
#   3. LDSC-plausibility floor: a NON-gating quality_flags array flags a
#      degenerate/ill-converged LDSC fit (h2<=0, |rg|>1, implausible
#      int_crosstrait) beside the numbers -- it does not stop the run.
#   4. ldsc_ancestry_mismatch: true + a fixed one-line note on every record --
#      the EUR LDSC reference vs the ~10-15%-non-European outcome makes the
#      correction-driving int_crosstrait ancestry-approximate (compounds KD1).
#   5. Determinism: MRlap's corrected-effect SE is analytic (delta method, no
#      bootstrap/resampling in this pinned build) -- no RNG seed is set here.
#   6. IV floor (informative, not fatal): m_IVs < instrument.min_instruments_mr
#      -> status "insufficient-mrlap-ivs", values recorded but non-quotable.
#   7. Hard-stop (technical fault): unlocatable load-bearing field, or
#      non-finite observed/corrected effect/se/p, or m_IVs absent/0 -> stop().
#      A wide/weak but FINITE corrected estimate is a valid scientific outcome
#      (esp. female testosterone), not a fault -> status "corrected".

suppressPackageStartupMessages({
  library(data.table)
  library(jsonlite)
  library(MRlap)
})

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag) { i <- match(flag, args); if (is.na(i)) stop(paste("missing", flag)); args[[i + 1L]] }
cfg <- yaml::read_yaml(get_arg("--config"))
stratum <- get_arg("--stratum")
exposure_path <- get_arg("--exposure")
outcome_path <- get_arg("--outcome")
results_out <- get_arg("--results-out")
dump_out <- get_arg("--dump-out")

# --- resolve this stratum's spec from config$exposures (build_instrument.R pattern) ----
specs <- cfg$exposures
match_idx <- which(vapply(specs, function(s) identical(s$name, stratum), logical(1)))
if (length(match_idx) != 1)
  stop(sprintf("run_mrlap[%s]: stratum not found (or not unique) in config$exposures — HALT", stratum))
spec <- specs[[match_idx]]

# --- read both canonical sumstats (before any CWD change) ---------------------
exp_dt <- as.data.frame(data.table::fread(exposure_path))
out_dt <- as.data.frame(data.table::fread(outcome_path))

# --- resolve every path/config value the isolated process must see to an
#     ABSOLUTE path *before* setwd() -----------------------------------------
# normalizePath(<file>, mustWork=FALSE) does NOT absolutize a not-yet-existing
# file on this platform (it returns the input relative path), which after setwd()
# would write into the tempdir. So absolutize via the PARENT dir (created here,
# so it exists) + basename — robust for output files that do not exist yet.
dir.create(dirname(results_out), recursive = TRUE, showWarnings = FALSE)
dir.create(dirname(dump_out), recursive = TRUE, showWarnings = FALSE)
abs_out <- function(p) file.path(normalizePath(dirname(p), mustWork = TRUE), basename(p))
results_out_abs <- abs_out(results_out)
dump_out_abs <- abs_out(dump_out)
ld_abs <- normalizePath(cfg$mrlap$ld, mustWork = TRUE)
hm3_abs <- normalizePath(cfg$mrlap$hm3, mustWork = TRUE)

# --- CWD isolation: MRlap writes temp files named from exposure_name/
#     outcome_name into the process CWD; the shared outcome_name would
#     collide across strata under any -c>1 run, so correctness must not
#     depend on -c1 ----------------------------------------------------------
work <- file.path(tempdir(), paste0("mrlap_", stratum))
dir.create(work, recursive = TRUE, showWarnings = FALSE)
old <- setwd(work)
on.exit(setwd(old), add = TRUE)

# --- the MRlap call (pinned params) -----------------------------------------
# MRlap's corrected-effect SE/covariance are estimated by a Monte-Carlo sampling
# strategy (get_correction runs thousands of simulations), NOT analytically — so
# the run IS stochastic. Seed it for reproducibility; the seed is recorded in the
# per-stratum JSON. (Earlier "analytic SE" assumption was wrong.)
mrlap_seed <- as.integer(cfg$mrlap$seed)
if (is.na(mrlap_seed)) stop("run_mrlap: cfg$mrlap$seed missing/non-integer — HALT")
set.seed(mrlap_seed)
res <- MRlap::MRlap(
  exposure = exp_dt, outcome = out_dt,
  exposure_name = spec$name, outcome_name = cfg$outcome$name,
  ld = ld_abs, hm3 = hm3_abs,
  MR_threshold    = as.numeric(cfg$mrlap$MR_threshold),
  MR_pruning_dist = as.numeric(cfg$mrlap$MR_pruning_dist),
  MR_pruning_LD   = as.numeric(cfg$mrlap$MR_pruning_LD),
  MR_reverse      = as.numeric(cfg$mrlap$MR_reverse),
  save_logfiles = FALSE, verbose = TRUE
)
saveRDS(res, dump_out_abs)   # full return preserved (provenance; nothing silently dropped)

# --- defensive field location: never guess, HALT naming what's missing ------
require_field <- function(container, name, where) {
  if (is.null(container) || !(name %in% names(container)) || is.null(container[[name]]))
    stop(sprintf("run_mrlap[%s]: load-bearing field '%s' not found (or NULL) in %s — HALT (technical)",
                  stratum, name, where))
  container[[name]]
}
optional_field <- function(container, name) {
  if (is.null(container) || !(name %in% names(container))) return(NA)
  val <- container[[name]]
  if (is.null(val)) NA else val
}

mrc <- res[["MRcorrection"]]
if (is.null(mrc))
  stop(sprintf("run_mrlap[%s]: res$MRcorrection not found in MRlap return — HALT (technical)", stratum))
ldsc <- res[["LDSC"]]
if (is.null(ldsc))
  stop(sprintf("run_mrlap[%s]: res$LDSC not found in MRlap return — HALT (technical)", stratum))

observed_effect    <- require_field(mrc, "observed_effect", "res$MRcorrection")
observed_effect_se <- require_field(mrc, "observed_effect_se", "res$MRcorrection")
observed_effect_p  <- require_field(mrc, "observed_effect_p", "res$MRcorrection")
corrected_effect    <- require_field(mrc, "corrected_effect", "res$MRcorrection")
corrected_effect_se <- require_field(mrc, "corrected_effect_se", "res$MRcorrection")
corrected_effect_p  <- require_field(mrc, "corrected_effect_p", "res$MRcorrection")
test_difference <- require_field(mrc, "test_difference", "res$MRcorrection")
p_difference    <- require_field(mrc, "p_difference", "res$MRcorrection")
m_IVs <- require_field(mrc, "m_IVs", "res$MRcorrection")

h2_exp   <- require_field(ldsc, "h2_exp", "res$LDSC")
h2_out   <- require_field(ldsc, "h2_out", "res$LDSC")
int_exp  <- require_field(ldsc, "int_exp", "res$LDSC")
int_out  <- require_field(ldsc, "int_out", "res$LDSC")
gcov     <- require_field(ldsc, "gcov", "res$LDSC")
int_crosstrait <- require_field(ldsc, "int_crosstrait", "res$LDSC")
rg       <- require_field(ldsc, "rg", "res$LDSC")
# SE fields are optional (plan: "+se if present") -- recorded null, not a HALT.
h2_exp_se         <- optional_field(ldsc, "h2_exp_se")
h2_out_se         <- optional_field(ldsc, "h2_out_se")
int_crosstrait_se <- optional_field(ldsc, "int_crosstrait_se")

# --- pruned-SNP exposure/outcome association dataframe (non-fatal if absent) -
# Field name is not pinned by the plan beyond "the pruned-SNP ... dataframe
# this pinned build returns" -- try the plausible locations defensively; if
# none match this pinned build's actual return shape, record null (a note, not
# a HALT) and flag it for the real Step-10 run.
extract_pruned_snps <- function(res_obj) {
  candidates <- list(
    res_obj[["MRcorrection"]][["IVs"]], res_obj[["MRcorrection"]][["SNPs"]],
    res_obj[["MRcorrection"]][["pruned_SNPs"]], res_obj[["IVs"]],
    res_obj[["SNPs"]], res_obj[["pruned_SNPs"]]
  )
  for (cand in candidates) {
    if (is.data.frame(cand)) {
      rsid_col <- intersect(c("SNP", "rsid", "rsID", "hm_rsid"), names(cand))
      if (length(rsid_col)) return(unique(as.character(cand[[rsid_col[1]]])))
    } else if (is.character(cand) && length(cand)) {
      return(unique(cand))
    }
  }
  NULL
}
pruned_snps <- extract_pruned_snps(res)
if (is.null(pruned_snps))
  cat(sprintf("run_mrlap[%s]: pruned-SNP dataframe not locatable in this MRlap return shape — recording pruned_snps: null (non-fatal)\n",
              stratum))

# --- LDSC-plausibility floor (NON-gating quality_flags; NA/NULL-safe) --------
quality_flags <- character(0)
le0 <- function(x) !is.na(x) && x <= 0
gt1_abs <- function(x) !is.na(x) && abs(x) > 1
if (le0(h2_exp) || le0(h2_out)) quality_flags <- c(quality_flags, "ldsc_h2_nonpositive")
if (gt1_abs(rg)) quality_flags <- c(quality_flags, "ldsc_rg_out_of_bounds")
if (gt1_abs(int_crosstrait)) quality_flags <- c(quality_flags, "ldsc_crosstrait_intercept_implausible")

# --- hard-stop (technical fault): unlocatable already HALTed above; here catch
#     non-finite observed/corrected effect+se+p, or m_IVs absent/0 -----------
if (!all(is.finite(c(observed_effect, observed_effect_se, observed_effect_p,
                      corrected_effect, corrected_effect_se, corrected_effect_p))))
  stop(sprintf("run_mrlap[%s]: non-finite observed/corrected effect or se/p from MRlap — HALT (technical)",
               stratum))
if (is.null(m_IVs) || length(m_IVs) == 0 || !is.finite(m_IVs) || m_IVs == 0)
  stop(sprintf("run_mrlap[%s]: m_IVs absent/0 — MRlap produced no estimate — HALT (technical)", stratum))

# --- IV floor (informative, mirrors the naive 3-instrument floor) -----------
min_iv <- as.integer(cfg$instrument$min_instruments_mr)
status <- if (m_IVs < min_iv) "insufficient-mrlap-ivs" else "corrected"
if (status == "insufficient-mrlap-ivs")
  cat(sprintf("run_mrlap[%s]: WEAK — only %d MRlap instruments (<%d); recording, not quotable\n",
              stratum, m_IVs, min_iv))

# --- KD1/KD3 + overlap-correction labels (mirrors harmonize_estimate.R, updated
#     for "overlap-correction does NOT lift the ceiling") -------------------
labels <- list(
  ancestry_flag = paste0("Outcome GCST90454541 is a European-dominant (~85-90%) ",
    "multi-ancestry HGI broad/population meta; no EUR-only sibling. ANCESTRY-FLAGGED, ",
    "NON-PRIMARY (KD1) — exploratory/robustness only, never primary evidence for ",
    "hypothesis:0005 / question:0007 / question:0013. Overlap-correction does NOT lift this."),
  bounded_sex = paste0("Male-only / female-only strata give a BOUNDED ",
    "exposure-architecture read against a mixed-sex outcome (KD3) — NOT a ",
    "genotype x sex effect-modification test. No sex-modification claim."),
  exposure_side = paste0("SHBG and total testosterone share Ruth instrument loci ",
    "(steroid-axis pleiotropy plausible). Female-testosterone is weakest-instrumented ",
    "yet most decision-relevant — a wide/weak corrected estimate is informative, not a failure."),
  sample_overlap_corrected = TRUE,
  naive_comparator_only = FALSE,
  overlap_correction_does_not_lift_ceiling = TRUE
)

# --- assemble + write the per-stratum results JSON --------------------------
result <- list(
  stratum = stratum, accession = spec$accession,
  trait = spec$trait, sex = spec$sex,
  exposure = stratum, outcome = cfg$outcome$name,
  exposure_n = spec$n, outcome_total_n = cfg$outcome$total_n,
  status = status,
  scale = "MRlap standardized (SD-outcome-liability per 1-SD exposure) — NOT log-OR; no OR",
  mrlap_observed = list(b = observed_effect, se = observed_effect_se, pval = observed_effect_p),
  mrlap_corrected = list(b = corrected_effect, se = corrected_effect_se, pval = corrected_effect_p),
  difference = list(test = test_difference, pval = p_difference),
  m_ivs = m_IVs,
  pruned_snps = if (is.null(pruned_snps)) NA else I(pruned_snps),
  ldsc = list(
    h2_exp = h2_exp, h2_exp_se = h2_exp_se, h2_out = h2_out, h2_out_se = h2_out_se,
    int_exp = int_exp, int_out = int_out, gcov = gcov,
    int_crosstrait = int_crosstrait, int_crosstrait_se = int_crosstrait_se, rg = rg,
    quality_flags = I(quality_flags)
  ),
  ldsc_ancestry_mismatch = TRUE,
  `_ldsc_ancestry_note` = paste0(
    "MRlap cross-trait LDSC uses the EUR eur_w_ld_chr ref; the outcome is ~10-15% ",
    "non-European -> outcome h2/int_crosstrait (the correction driver) are ",
    "ancestry-approximate. Compounds KD1."),
  overlap_signal = list(
    cross_trait_ldsc_intercept = int_crosstrait,
    `_note` = paste0(
      "int_crosstrait encodes the UKB sample overlap MRlap corrects for; MRlap ",
      "does not emit a literal overlap fraction — the intercept + N are the ",
      "correction inputs.")
  ),
  mrlap_params = list(
    MR_threshold = as.numeric(cfg$mrlap$MR_threshold),
    MR_pruning_dist = as.numeric(cfg$mrlap$MR_pruning_dist),
    MR_pruning_LD = as.numeric(cfg$mrlap$MR_pruning_LD),
    MR_reverse = as.numeric(cfg$mrlap$MR_reverse),
    seed = mrlap_seed
  ),
  labels = labels
)
writeLines(jsonlite::toJSON(result, auto_unbox = TRUE, pretty = TRUE, na = "null"), results_out_abs)

cat(sprintf("run_mrlap[%s]: status=%s m_IVs=%d observed_b=%.4g corrected_b=%.4g int_crosstrait=%.4g quality_flags=[%s]\n",
            stratum, status, as.integer(m_IVs), observed_effect, corrected_effect, int_crosstrait,
            paste(quality_flags, collapse = ",")))
