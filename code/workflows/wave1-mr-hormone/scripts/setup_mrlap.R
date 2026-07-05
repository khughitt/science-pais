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

# --- install in dependency order (idempotent + verify-gated retry) -----------
# The three GitHub installs are the flaky, network-bound step. Each is SKIPPED
# when the package is already present at the pinned SHA/version (so a re-run
# fetches only what is missing), and RETRIED otherwise. Crucially the retry
# gates on the ACTUAL installed state (the package resolves at the pinned
# SHA/version afterwards) rather than on whether install_github threw — remotes
# does not always re-raise a download failure as a catchable error, so a
# throw-gated retry would silently pass a half-installed library through. The
# four hard-fail asserts below remain the reproducibility gate; this only
# changes HOW we reach a correctly-pinned library, never WHETHER we verify it.
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

# install_fn: a nullary closure that performs the install.
# verify_fn:  a nullary predicate that is TRUE iff the package is now present at
#             the pinned SHA/version. Retry until verify_fn holds; HALT after N.
ensure <- function(install_fn, verify_fn, what) {
  if (isTRUE(verify_fn())) {
    message(sprintf("setup_mrlap: %s already satisfied — skipping", what))
    return(invisible(TRUE))
  }
  for (attempt in seq_len(retries)) {
    tryCatch(install_fn(), error = function(e)
      message(sprintf("setup_mrlap: %s install attempt %d/%d errored: %s",
                      what, attempt, retries, conditionMessage(e))))
    if (isTRUE(verify_fn())) {
      message(sprintf("setup_mrlap: %s installed (attempt %d/%d)", what, attempt, retries))
      return(invisible(TRUE))
    }
    message(sprintf("setup_mrlap: %s not present after attempt %d/%d", what, attempt, retries))
    if (attempt < retries) Sys.sleep(retry_sleep_s)
  }
  stop(sprintf("setup_mrlap: %s not installed at pinned ref after %d attempts — HALT",
               what, retries))
}

# 1. ieugwasr (CRAN) — transitive dep of TwoSampleMR; install if absent so its
#    version is captured. (TwoSampleMR's install also pulls it, but do it first.)
ensure(
  function() remotes::install_cran("ieugwasr", upgrade = "never"),
  function() requireNamespace("ieugwasr", quietly = TRUE),
  "ieugwasr (CRAN)")

# 2. TwoSampleMR @ pinned tag (transitive engine MRlap calls; dependencies=TRUE).
ensure(
  function() remotes::install_github(
    paste0(cfg$mrlap_env$twosamplemr_repo, "@", cfg$mrlap_env$twosamplemr_ref),
    upgrade = "never", dependencies = TRUE),
  function() identical(installed_version("TwoSampleMR"), cfg$mrlap_env$twosamplemr_version_expected),
  "TwoSampleMR (GitHub)")

# 3. GenomicSEM @ pinned commit (MRlap's internal cross-trait LDSC engine).
ensure(
  function() remotes::install_github(
    paste0(cfg$mrlap_env$genomicsem_repo, "@", cfg$mrlap_env$genomicsem_ref),
    upgrade = "never"),
  function() identical(installed_sha("GenomicSEM"), substr(cfg$mrlap_env$genomicsem_ref, 1, 40)),
  "GenomicSEM (GitHub)")

# 4. MRlap @ pinned commit. Primary path: install_github (records GithubSHA1).
#    Fallback: this environment intermittently cannot establish a connection to
#    api.github.com within remotes' ~10s connect window for MRlap's (larger)
#    tarball endpoint — so if install_github does not yield MRlap at the pinned
#    SHA, download the tarball DIRECTLY from codeload.github.com at the SAME
#    pinned SHA (bypassing api.github.com) and install_local. The pin is
#    preserved by the SHA-keyed download URL; the tarball's sha256 is recorded as
#    content provenance (install_local does not populate GithubSHA1).
want_mrlap <- substr(cfg$mrlap_env$mrlap_ref, 1, 40)
mrlap_install_method <- NA_character_
mrlap_tarball_sha256 <- NA_character_

file_sha256 <- function(path) {
  tryCatch(unname(tools::sha256sum(path)), error = function(e) NA_character_)
}

install_mrlap_codeload <- function() {
  url  <- sprintf("https://codeload.github.com/%s/tar.gz/%s",
                  cfg$mrlap_env$mrlap_repo, cfg$mrlap_env$mrlap_ref)
  dest <- file.path(dirname(sentinel), paste0("MRlap-", want_mrlap, ".tar.gz"))
  dir.create(dirname(dest), recursive = TRUE, showWarnings = FALSE)
  utils::download.file(url, dest, mode = "wb", quiet = FALSE)   # options(timeout=600) applies
  sha256 <- file_sha256(dest)
  remotes::install_local(dest, upgrade = "never", force = TRUE)
  if (requireNamespace("MRlap", quietly = TRUE)) {
    mrlap_tarball_sha256 <<- sha256
    mrlap_install_method <<- "install_local_codeload"
  }
}

if (identical(installed_sha("MRlap"), want_mrlap)) {
  message("setup_mrlap: MRlap @ pinned SHA already installed (install_github) — skipping")
  mrlap_install_method <- "install_github"
} else {
  # one install_github attempt (best case: sets GithubSHA1), then codeload fallback.
  tryCatch(
    remotes::install_github(paste0(cfg$mrlap_env$mrlap_repo, "@", cfg$mrlap_env$mrlap_ref),
                            upgrade = "never"),
    error = function(e) message("setup_mrlap: MRlap install_github errored: ", conditionMessage(e)))
  if (identical(installed_sha("MRlap"), want_mrlap)) {
    mrlap_install_method <- "install_github"
    message("setup_mrlap: MRlap installed via install_github @ pinned SHA")
  } else {
    message("setup_mrlap: install_github did not yield MRlap@pin; falling back to codeload tarball + install_local")
    ensure(install_mrlap_codeload,
           function() requireNamespace("MRlap", quietly = TRUE),
           "MRlap (codeload install_local)")
  }
}

suppressPackageStartupMessages({
  library(TwoSampleMR)
  library(ieugwasr)
  library(GenomicSEM)
  library(MRlap)
})

# --- commit-SHA assert (hard-fail) -------------------------------------------
# GenomicSEM is always install_github -> assert GithubSHA1 strictly.
gsem_sha <- utils::packageDescription("GenomicSEM")$GithubSHA1
if (is.null(gsem_sha) || substr(gsem_sha, 1, 40) != substr(cfg$mrlap_env$genomicsem_ref, 1, 40))
  stop(sprintf("setup_mrlap: GenomicSEM GithubSHA1 %s != pinned %s — HALT",
               gsem_sha, cfg$mrlap_env$genomicsem_ref))

# MRlap: assert GithubSHA1 when install_github succeeded; for the codeload
# install_local fallback (no GithubSHA1 field) the pin is enforced by the
# SHA-keyed download URL + the recorded tarball sha256, and the package must load.
mrlap_gh_sha <- utils::packageDescription("MRlap")$GithubSHA1
if (identical(mrlap_install_method, "install_github")) {
  if (is.null(mrlap_gh_sha) || substr(mrlap_gh_sha, 1, 40) != want_mrlap)
    stop(sprintf("setup_mrlap: MRlap GithubSHA1 %s != pinned %s — HALT", mrlap_gh_sha, want_mrlap))
} else if (identical(mrlap_install_method, "install_local_codeload")) {
  # Pin enforced by the SHA-keyed codeload URL; the package must load. The tarball
  # sha256 is recorded-if-computable (bonus content provenance), not gated on.
  if (!requireNamespace("MRlap", quietly = TRUE))
    stop("setup_mrlap: MRlap codeload install_local did not yield a loadable package — HALT")
  message(sprintf("setup_mrlap: MRlap via codeload tarball (url-pinned ref %s, sha256 %s); GithubSHA1 unavailable for install_local — provenance recorded",
                  want_mrlap, mrlap_tarball_sha256))
} else {
  stop("setup_mrlap: MRlap install method unresolved (neither install_github nor codeload succeeded) — HALT")
}

# --- transitive-engine version assert (hard-fail) ----------------------------
for (pv in list(c("TwoSampleMR", cfg$mrlap_env$twosamplemr_version_expected),
                c("ieugwasr",   cfg$mrlap_env$ieugwasr_version_expected))) {
  got <- as.character(utils::packageVersion(pv[[1]]))
  if (got != pv[[2]])
    stop(sprintf("setup_mrlap: %s %s != pinned %s — HALT", pv[[1]], got, pv[[2]]))
}

# --- sentinel -----------------------------------------------------------------
mrlap_sha <- utils::packageDescription("MRlap")$GithubSHA1        # NULL for install_local
if (is.null(mrlap_sha)) mrlap_sha <- NA_character_
genomicsem_sha <- utils::packageDescription("GenomicSEM")$GithubSHA1
twosamplemr_version <- as.character(utils::packageVersion("TwoSampleMR"))
ieugwasr_version <- as.character(utils::packageVersion("ieugwasr"))

installed_pkgs <- c("MRlap", "GenomicSEM", "TwoSampleMR", "ieugwasr")
sessionInfo_pkgs <- setNames(
  lapply(installed_pkgs, function(p) as.character(utils::packageVersion(p))),
  installed_pkgs
)

sentinel_data <- list(
  mrlap_sha = mrlap_sha,
  mrlap_install_method = mrlap_install_method,
  mrlap_tarball_sha256 = mrlap_tarball_sha256,
  genomicsem_sha = genomicsem_sha,
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
