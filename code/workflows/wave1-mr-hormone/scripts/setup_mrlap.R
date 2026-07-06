# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Install MRlap + GenomicSEM (both GitHub-only, no CRAN release) at PINNED
# commits into the r-mrlap conda env, plus their transitive engine
# TwoSampleMR/ieugwasr, and HARD-FAIL unless the resolved commit SHAs AND
# package versions match config (plan:0009 Task 4, MRlap overlap-corrected MR).
#
# Deliberate mirror of `setup_twosamplemr.R` (isolation convention within this
# workflow). MRlap `Imports` TwoSampleMR + ieugwasr and calls
# `TwoSampleMR::mr_ivw()` / `mr_egger_regression()` inside `run_MR` — so the
# corrected arm can drift with those unpinned even when MRlap's SHA is fixed.
# Pinning + asserting all four closes that: the correction-machinery
# reproducibility gate for the whole corrected arm.

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag, default = NULL) {
  i <- match(flag, args)
  if (is.na(i) || i == length(args)) return(default)
  args[[i + 1L]]
}

config_path <- get_arg("--config")
sentinel <- get_arg("--sentinel")
if (is.null(config_path) || is.null(sentinel))
  stop("setup_mrlap.R: --config and --sentinel are required")

cfg <- yaml::read_yaml(config_path)

# GitHub tarball downloads (esp. the larger MRlap repo) can exceed R's default
# 60s download.file timeout on a slow link and fail as "download ... failed" —
# raise it generously so a slow-but-working download is not aborted mid-stream.
options(timeout = max(600, getOption("timeout")))

# --- install in dependency order (idempotent; install_github -> codeload fallback) --
# ALL THREE GitHub packages can hit this environment's intermittent api.github.com
# connect timeout (~10s) whenever the conda env is rebuilt from scratch (e.g. a new
# SNAKEMAKE_CONDA_PREFIX or a cleaned .snakemake/conda). For each package we:
#   (1) SKIP when already satisfied at the pinned ref (an intact env re-runs instantly),
#   (2) try install_github once (best case: records GithubSHA1),
#   (3) else fall back to a DIRECT codeload.github.com tarball at the SAME pinned ref
#       (bypassing api.github.com) + install_local, retried.
# install_local does NOT populate GithubSHA1, so for that path the pin is enforced by
# the SHA-keyed download URL and the tarball sha256 is recorded as content provenance.
# A single per-package `satisfied()` predicate is the gate — a half-installed or
# wrong-pin library is never passed through. The final asserts remain the hard gate.
retries <- 4L
retry_sleep_s <- 20

installed_sha <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) return(NA_character_)
  sha <- utils::packageDescription(pkg)$GithubSHA1
  if (is.null(sha)) NA_character_ else substr(sha, 1, 40)
}
installed_version <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) return(NA_character_)
  as.character(utils::packageVersion(pkg))
}
file_sha256 <- function(path) tryCatch(unname(tools::sha256sum(path)), error = function(e) NA_character_)

# provenance recorded per GitHub package: $method + (for install_local) $tarball_sha256
install_info <- list()

# satisfied(pkg, ref, expected_version):
#   TRUE iff pkg is importable AND consistent with its pin —
#     * if it carries a GithubSHA1, that must equal `ref` (catches a wrong install_github);
#     * if no GithubSHA1 (install_local), presence is accepted (we only ever install_local
#       from the pinned-SHA codeload URL);
#     * if expected_version is given, the installed version must also match.
satisfied <- function(pkg, ref = NULL, expected_version = NULL) {
  if (!requireNamespace(pkg, quietly = TRUE)) return(FALSE)
  if (!is.null(expected_version) && !identical(installed_version(pkg), expected_version)) return(FALSE)
  sha <- installed_sha(pkg)
  if (!is.na(sha) && !is.null(ref) && sha != substr(ref, 1, 40)) return(FALSE)
  TRUE
}

# ensure_github: idempotent skip -> install_github once -> codeload install_local (retried) -> HALT.
ensure_github <- function(pkg, repo, ref, expected_version = NULL) {
  ok <- function() satisfied(pkg, ref, expected_version)
  if (isTRUE(ok())) {
    method <- if (is.na(installed_sha(pkg))) "install_local_codeload" else "install_github"
    install_info[[pkg]] <<- list(method = method, tarball_sha256 = NA_character_)
    message(sprintf("setup_mrlap: %s already satisfied (%s) — skipping", pkg, method))
    return(invisible())
  }
  # one install_github attempt (best case: records GithubSHA1)
  tryCatch(
    remotes::install_github(paste0(repo, "@", ref), upgrade = "never", dependencies = TRUE),
    error = function(e) message(sprintf("setup_mrlap: %s install_github errored: %s", pkg, conditionMessage(e))))
  if (isTRUE(ok())) {
    install_info[[pkg]] <<- list(method = "install_github", tarball_sha256 = NA_character_)
    message(sprintf("setup_mrlap: %s via install_github @ pinned ref", pkg))
    return(invisible())
  }
  # codeload fallback (bypasses api.github.com), retried
  message(sprintf("setup_mrlap: %s install_github did not satisfy pin; falling back to codeload tarball + install_local", pkg))
  url  <- sprintf("https://codeload.github.com/%s/tar.gz/%s", repo, ref)
  dest <- file.path(dirname(sentinel), paste0(gsub("/", "_", repo), "-", substr(ref, 1, 40), ".tar.gz"))
  dir.create(dirname(dest), recursive = TRUE, showWarnings = FALSE)
  for (attempt in seq_len(retries)) {
    sha256 <- tryCatch({
      utils::download.file(url, dest, mode = "wb", quiet = FALSE)   # options(timeout=600) applies
      s <- file_sha256(dest)
      remotes::install_local(dest, upgrade = "never", force = TRUE, dependencies = TRUE)
      s
    }, error = function(e) {
      message(sprintf("setup_mrlap: %s codeload attempt %d/%d errored: %s", pkg, attempt, retries, conditionMessage(e)))
      NA_character_
    })
    if (isTRUE(ok())) {
      install_info[[pkg]] <<- list(method = "install_local_codeload", tarball_sha256 = sha256)
      message(sprintf("setup_mrlap: %s via codeload install_local (attempt %d/%d, sha256 %s)", pkg, attempt, retries, sha256))
      return(invisible())
    }
    message(sprintf("setup_mrlap: %s not satisfied after codeload attempt %d/%d", pkg, attempt, retries))
    if (attempt < retries) Sys.sleep(retry_sleep_s)
  }
  stop(sprintf("setup_mrlap: %s not installed at pinned ref after install_github + %d codeload attempts — HALT", pkg, retries))
}

# 1. ieugwasr (CRAN) — transitive dep of TwoSampleMR; install if absent (retried).
for (attempt in seq_len(retries)) {
  if (requireNamespace("ieugwasr", quietly = TRUE)) break
  tryCatch(remotes::install_cran("ieugwasr", upgrade = "never"),
           error = function(e) message(sprintf("setup_mrlap: ieugwasr (CRAN) attempt %d/%d errored: %s",
                                                attempt, retries, conditionMessage(e))))
  if (!requireNamespace("ieugwasr", quietly = TRUE) && attempt < retries) Sys.sleep(retry_sleep_s)
}
if (!requireNamespace("ieugwasr", quietly = TRUE))
  stop("setup_mrlap: ieugwasr (CRAN) not installed after retries — HALT")

# 2-4. the three GitHub packages, in dependency order.
ensure_github("TwoSampleMR", cfg$mrlap_env$twosamplemr_repo, cfg$mrlap_env$twosamplemr_ref,
              expected_version = cfg$mrlap_env$twosamplemr_version_expected)
ensure_github("GenomicSEM",  cfg$mrlap_env$genomicsem_repo,  cfg$mrlap_env$genomicsem_ref)
ensure_github("MRlap",       cfg$mrlap_env$mrlap_repo,       cfg$mrlap_env$mrlap_ref)

suppressPackageStartupMessages({
  library(TwoSampleMR)
  library(ieugwasr)
  library(GenomicSEM)
  library(MRlap)
})

# --- final pin asserts (hard-fail) -------------------------------------------
# Uniform re-check via satisfied() for the SHA-pinned engines (asserts GithubSHA1
# when install_github was used; for the codeload install_local path the pin is
# enforced by the SHA-keyed URL and presence is required), plus explicit version
# asserts for the version-pinned engines.
if (!satisfied("GenomicSEM", cfg$mrlap_env$genomicsem_ref))
  stop(sprintf("setup_mrlap: GenomicSEM not satisfied at pinned ref %s — HALT", cfg$mrlap_env$genomicsem_ref))
if (!satisfied("MRlap", cfg$mrlap_env$mrlap_ref))
  stop(sprintf("setup_mrlap: MRlap not satisfied at pinned ref %s — HALT", cfg$mrlap_env$mrlap_ref))
for (pv in list(c("TwoSampleMR", cfg$mrlap_env$twosamplemr_version_expected),
                c("ieugwasr",   cfg$mrlap_env$ieugwasr_version_expected))) {
  got <- as.character(utils::packageVersion(pv[[1]]))
  if (got != pv[[2]])
    stop(sprintf("setup_mrlap: %s %s != pinned %s — HALT", pv[[1]], got, pv[[2]]))
}
message(sprintf("setup_mrlap: install methods -> TwoSampleMR:%s GenomicSEM:%s MRlap:%s",
                install_info[["TwoSampleMR"]]$method, install_info[["GenomicSEM"]]$method,
                install_info[["MRlap"]]$method))

# --- sentinel -----------------------------------------------------------------
mrlap_sha <- utils::packageDescription("MRlap")$GithubSHA1        # NULL for install_local
if (is.null(mrlap_sha)) mrlap_sha <- NA_character_
genomicsem_sha <- utils::packageDescription("GenomicSEM")$GithubSHA1
if (is.null(genomicsem_sha)) genomicsem_sha <- NA_character_
twosamplemr_version <- as.character(utils::packageVersion("TwoSampleMR"))
ieugwasr_version <- as.character(utils::packageVersion("ieugwasr"))

installed_pkgs <- c("MRlap", "GenomicSEM", "TwoSampleMR", "ieugwasr")
sessionInfo_pkgs <- setNames(
  lapply(installed_pkgs, function(p) as.character(utils::packageVersion(p))),
  installed_pkgs
)
github_install_methods <- setNames(
  lapply(c("TwoSampleMR", "GenomicSEM", "MRlap"), function(p) install_info[[p]]$method),
  c("TwoSampleMR", "GenomicSEM", "MRlap")
)

sentinel_data <- list(
  mrlap_sha = mrlap_sha,
  mrlap_install_method = install_info[["MRlap"]]$method,
  mrlap_tarball_sha256 = install_info[["MRlap"]]$tarball_sha256,
  genomicsem_sha = genomicsem_sha,
  genomicsem_install_method = install_info[["GenomicSEM"]]$method,
  github_install_methods = github_install_methods,
  mrlap_ref_expected = cfg$mrlap_env$mrlap_ref,
  genomicsem_ref_expected = cfg$mrlap_env$genomicsem_ref,
  twosamplemr_version = twosamplemr_version,
  twosamplemr_version_expected = cfg$mrlap_env$twosamplemr_version_expected,
  ieugwasr_version = ieugwasr_version,
  ieugwasr_version_expected = cfg$mrlap_env$ieugwasr_version_expected,
  sha_and_version_assert_pass = TRUE,
  r_version = as.character(getRversion()),
  sessionInfo_pkgs = sessionInfo_pkgs,
  installed_at_note = format(Sys.time(), tz = "UTC", usetz = TRUE)
)

dir.create(dirname(sentinel), recursive = TRUE, showWarnings = FALSE)
writeLines(jsonlite::toJSON(sentinel_data, auto_unbox = TRUE, pretty = TRUE), sentinel)
cat("setup_mrlap: MRlap", mrlap_sha, "GenomicSEM", genomicsem_sha,
    "TwoSampleMR", twosamplemr_version, "ieugwasr", ieugwasr_version,
    "(SHA+version-assert PASS)\n")
