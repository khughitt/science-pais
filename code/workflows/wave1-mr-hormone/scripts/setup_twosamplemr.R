# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Install the pinned TwoSampleMR tag into the r-mr conda env's R library
# (plan:0009 Task 2, hormone-instrument workflow).
#
# Deliberate copy of the plan:0007 `wave1-mr/scripts/setup_twosamplemr.R`
# (isolation convention; the frozen run-of-record is not edited). TwoSampleMR
# is not on conda, so it is installed from a pinned GitHub tag via remotes
# (upgrade = "never"); ieugwasr (local LD clumping) and the remaining CRAN
# deps come with it.
#
# F1 (version gate): the R layer is the genuine drift risk in this pipeline
# (TwoSampleMR from a GitHub tag + ieugwasr from CRAN resolve at install
# time), so this copy HARD-FAILS unless the resolved versions match the
# config-pinned expectations — a fresh run cannot silently resolve a
# different R stack than the plan:0007 run of record. The sentinel still
# records the full resolved version set for run_metadata.json.

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag, default = NULL) {
  i <- match(flag, args)
  if (is.na(i) || i == length(args)) return(default)
  args[[i + 1L]]
}

config_path <- get_arg("--config")
repo <- get_arg("--repo", "MRCIEU/TwoSampleMR")
ref <- get_arg("--ref")
sentinel <- get_arg("--sentinel")
if (is.null(config_path) || is.null(ref) || is.null(sentinel))
  stop("setup_twosamplemr.R: --config, --ref and --sentinel are required")

cfg <- yaml::read_yaml(config_path)

# ieugwasr is a TwoSampleMR dependency (local plink clumping); install both so
# the resolved ieugwasr version is captured too.
if (!requireNamespace("ieugwasr", quietly = TRUE)) {
  remotes::install_cran("ieugwasr", upgrade = "never")
}
remotes::install_github(paste0(repo, "@", ref), upgrade = "never", dependencies = TRUE)

suppressPackageStartupMessages({
  library(TwoSampleMR)
  library(ieugwasr)
})

# --- F1: version-assert hard-fail --------------------------------------------
tsmr <- as.character(packageVersion("TwoSampleMR"))
if (tsmr != cfg$env$twosamplemr_version_expected)
  stop(sprintf("setup: TwoSampleMR %s != expected %s — HALT", tsmr, cfg$env$twosamplemr_version_expected))
ieu <- as.character(packageVersion("ieugwasr"))
if (!is.null(cfg$env$ieugwasr_version_expected) && ieu != cfg$env$ieugwasr_version_expected)
  stop(sprintf("setup: ieugwasr %s != expected %s — HALT", ieu, cfg$env$ieugwasr_version_expected))

versions <- list(
  twosamplemr_repo = repo,
  twosamplemr_ref = ref,
  twosamplemr_version = tsmr,
  twosamplemr_version_expected = cfg$env$twosamplemr_version_expected,
  ieugwasr_version = ieu,
  ieugwasr_version_expected = cfg$env$ieugwasr_version_expected,
  version_assert_pass = TRUE,
  mendelianrandomization_version = as.character(packageVersion("MendelianRandomization")),
  r_version = as.character(getRversion()),
  installed_at = format(Sys.time(), tz = "UTC", usetz = TRUE)
)

dir.create(dirname(sentinel), recursive = TRUE, showWarnings = FALSE)
writeLines(jsonlite::toJSON(versions, auto_unbox = TRUE, pretty = TRUE), sentinel)
cat("setup_twosamplemr: TwoSampleMR", versions$twosamplemr_version,
    "ieugwasr", versions$ieugwasr_version, "(version-assert PASS)\n")
