# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Install the pinned TwoSampleMR tag into the r-mr conda env's R library.
#
# plan:0007 "Reproducible execution harness": TwoSampleMR is not on conda, so it
# is installed from a pinned GitHub tag via remotes (upgrade = "never"); ieugwasr
# (local LD clumping) and the remaining CRAN deps come with it. The RESOLVED
# versions are written into the sentinel for run_metadata.json.

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag, default = NULL) {
  i <- match(flag, args)
  if (is.na(i) || i == length(args)) return(default)
  args[[i + 1L]]
}

repo <- get_arg("--repo", "MRCIEU/TwoSampleMR")
ref <- get_arg("--ref")
sentinel <- get_arg("--sentinel")
if (is.null(ref) || is.null(sentinel)) stop("setup_twosamplemr.R: --ref and --sentinel are required")

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

versions <- list(
  twosamplemr_repo = repo,
  twosamplemr_ref = ref,
  twosamplemr_version = as.character(packageVersion("TwoSampleMR")),
  ieugwasr_version = as.character(packageVersion("ieugwasr")),
  mendelianrandomization_version = as.character(packageVersion("MendelianRandomization")),
  r_version = as.character(getRversion()),
  installed_at = format(Sys.time(), tz = "UTC", usetz = TRUE)
)

dir.create(dirname(sentinel), recursive = TRUE, showWarnings = FALSE)
writeLines(jsonlite::toJSON(versions, auto_unbox = TRUE, pretty = TRUE), sentinel)
cat("setup_twosamplemr: TwoSampleMR", versions$twosamplemr_version,
    "ieugwasr", versions$ieugwasr_version, "\n")
