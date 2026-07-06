#!/usr/bin/env bash
# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#
# Fixture test for canonicalize_sumstats.py (plan:0009 Task 4, Step 5).
#
# Exercises all three hard-stops + the success path on tiny synthetic gz
# fixtures — no conda env, no MRlap, no real GWAS downloads. Runs in seconds:
#
#   (a) missing column   — a Ruth-family fixture missing `hm_beta` from its
#       header must HARD-STOP with a message naming the missing column.
#   (b) unresolved N     — an outcome-family fixture against a stub config
#       whose `outcome:` block carries no `total_n` must HARD-STOP with an
#       "unresolved N" message.
#   (c) success           — a valid 3-row Ruth fixture with all mapped columns
#       present + a stub config carrying the stratum's `n:` must succeed:
#       exit 0, 8-column canonical header, exactly 3 data rows, the injected N
#       on every row.
#
# Usage: bash code/workflows/wave1-mr-hormone/tests/test_canonicalize.sh
# (run from anywhere; no conda env required — stdlib gzip/csv + pyyaml only)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
SCRIPT="$REPO_ROOT/code/workflows/wave1-mr-hormone/scripts/canonicalize_sumstats.py"

if ! python3 -c "import yaml" >/dev/null 2>&1; then
  echo "SKIP: pyyaml not importable in this shell (python3 -c 'import yaml' failed) — cannot run test_canonicalize.sh here" >&2
  exit 0
fi

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

fail() { echo "FAIL: $*" >&2; exit 1; }

# =============================================================================
# (a) missing column — Ruth-family fixture missing hm_beta
# =============================================================================
mkdir -p "$WORK/a"
cat > "$WORK/a/config.yaml" <<'EOF'
exposures:
  - name: "fake-shbg-combined"
    n: 370125
outcome:
  total_n: 1100445
EOF

{
  # NOTE: no hm_beta column here (deliberately missing)
  printf "hm_rsid\thm_chrom\thm_pos\thm_effect_allele\thm_other_allele\tstandard_error\n"
  printf "rs1\t1\t1000\tA\tG\t0.01\n"
} | gzip > "$WORK/a/exposure.h.tsv.gz"

set +e
out_a="$(python3 "$SCRIPT" --config "$WORK/a/config.yaml" --source-family ruth-exposure \
  --stratum fake-shbg-combined --in "$WORK/a/exposure.h.tsv.gz" \
  --out "$WORK/a/canonical.tsv.gz" 2>&1)"
rc_a=$?
set -e

[[ "$rc_a" -ne 0 ]] || fail "(a) expected non-zero exit for missing hm_beta, got 0. Output: $out_a"
[[ "$out_a" == *"hm_beta"* ]] || fail "(a) expected message to mention missing column 'hm_beta', got: $out_a"
[[ "$out_a" == *"missing column"* ]] || fail "(a) expected message to say 'missing column', got: $out_a"
[[ ! -f "$WORK/a/canonical.tsv.gz" ]] || fail "(a) expected no output file to be written on hard-stop"
echo "PASS (a) missing column: exit=$rc_a, message names hm_beta + 'missing column'"

# =============================================================================
# (b) unresolved N — outcome-family fixture, stub config with no outcome.total_n
# =============================================================================
mkdir -p "$WORK/b"
cat > "$WORK/b/config.yaml" <<'EOF'
exposures: []
outcome:
  name: "fake-outcome"
EOF

{
  printf "rsid\tchromosome\tbase_pair_location\teffect_allele\tother_allele\tbeta\tstandard_error\n"
  printf "rs1\t1\t1000\tA\tG\t0.01\t0.002\n"
} | gzip > "$WORK/b/outcome.h.tsv.gz"

set +e
out_b="$(python3 "$SCRIPT" --config "$WORK/b/config.yaml" --source-family hgi-outcome \
  --stratum outcome --in "$WORK/b/outcome.h.tsv.gz" \
  --out "$WORK/b/canonical.tsv.gz" 2>&1)"
rc_b=$?
set -e

[[ "$rc_b" -ne 0 ]] || fail "(b) expected non-zero exit for absent total_n, got 0. Output: $out_b"
[[ "$out_b" == *"unresolved N"* ]] || fail "(b) expected message to say 'unresolved N', got: $out_b"
[[ ! -f "$WORK/b/canonical.tsv.gz" ]] || fail "(b) expected no output file to be written on hard-stop"
echo "PASS (b) unresolved N: exit=$rc_b, message says 'unresolved N'"

# =============================================================================
# (c) success — valid 3-row Ruth fixture, config carries the stratum's n:
# =============================================================================
mkdir -p "$WORK/c"
cat > "$WORK/c/config.yaml" <<'EOF'
exposures:
  - name: "fake-shbg-combined"
    n: 370125
outcome:
  total_n: 1100445
EOF

{
  printf "hm_rsid\thm_chrom\thm_pos\thm_effect_allele\thm_other_allele\thm_beta\tstandard_error\textra_col\n"
  printf "rs1\t1\t1000\tA\tG\t0.010\t0.002\tjunk1\n"
  printf "rs2\t2\t2000\tC\tT\t-0.020\t0.003\tjunk2\n"
  printf "rs3\t3\t3000\tG\tA\t0.005\t0.001\tjunk3\n"
} | gzip > "$WORK/c/exposure.h.tsv.gz"

set +e
out_c="$(python3 "$SCRIPT" --config "$WORK/c/config.yaml" --source-family ruth-exposure \
  --stratum fake-shbg-combined --in "$WORK/c/exposure.h.tsv.gz" \
  --out "$WORK/c/canonical.tsv.gz" 2>&1)"
rc_c=$?
set -e

[[ "$rc_c" -eq 0 ]] || fail "(c) expected exit 0, got $rc_c. Output: $out_c"
[[ -f "$WORK/c/canonical.tsv.gz" ]] || fail "(c) expected canonical output gz to exist"
[[ -f "$WORK/c/canonical.tsv.gz.canonical.json" ]] || fail "(c) expected .canonical.json sidecar to exist"

header_c="$(zcat "$WORK/c/canonical.tsv.gz" | head -n1)"
expected_header="$(printf 'rsid\tchr\tpos\ta1\ta2\tbeta\tse\tN')"
[[ "$header_c" == "$expected_header" ]] \
  || fail "(c) expected header '$expected_header', got '$header_c'"

n_data_rows_c="$(zcat "$WORK/c/canonical.tsv.gz" | tail -n +2 | wc -l)"
[[ "$n_data_rows_c" -eq 3 ]] || fail "(c) expected 3 data rows, got $n_data_rows_c"

n_col_with_injected_n="$(zcat "$WORK/c/canonical.tsv.gz" | tail -n +2 | awk -F'\t' '{print $8}' | sort -u)"
[[ "$n_col_with_injected_n" == "370125" ]] \
  || fail "(c) expected injected N=370125 on every data row, got distinct values: $n_col_with_injected_n"

echo "PASS (c) success: exit=0, 8-col header correct, 3 data rows, N=370125 on every row"

# =============================================================================
# (d) NA-rsid / NA-effect drop — rows whose rsid is "NA"/"." or whose beta/se is
#     an NA token must be dropped (the join-key cartesian-bomb guard). Sidecar
#     records n_dropped_na_rsid.
# =============================================================================
mkdir -p "$WORK/d"
cat > "$WORK/d/config.yaml" <<'EOF'
exposures:
  - name: "fake-shbg-combined"
    n: 370125
outcome:
  total_n: 1100445
EOF

{
  printf "hm_rsid\thm_chrom\thm_pos\thm_effect_allele\thm_other_allele\thm_beta\tstandard_error\n"
  printf "rs1\t1\t1000\tA\tG\t0.010\t0.002\n"     # keep
  printf "NA\t2\t2000\tC\tT\t-0.020\t0.003\n"     # drop: NA rsid
  printf ".\t3\t3000\tG\tA\t0.005\t0.001\n"       # drop: '.' rsid
  printf "rs4\t4\t4000\tT\tC\tNA\t0.004\n"        # drop: NA beta (not an na_rsid)
  printf "rs5\t5\t5000\tA\tT\t0.030\t0.006\n"     # keep
} | gzip > "$WORK/d/exposure.h.tsv.gz"

set +e
out_d="$(python3 "$SCRIPT" --config "$WORK/d/config.yaml" --source-family ruth-exposure \
  --stratum fake-shbg-combined --in "$WORK/d/exposure.h.tsv.gz" \
  --out "$WORK/d/canonical.tsv.gz" 2>&1)"
rc_d=$?
set -e

[[ "$rc_d" -eq 0 ]] || fail "(d) expected exit 0, got $rc_d. Output: $out_d"
n_data_rows_d="$(zcat "$WORK/d/canonical.tsv.gz" | tail -n +2 | wc -l)"
[[ "$n_data_rows_d" -eq 2 ]] || fail "(d) expected 2 surviving rows (rs1,rs5), got $n_data_rows_d"
surviving_ids_d="$(zcat "$WORK/d/canonical.tsv.gz" | tail -n +2 | cut -f1 | sort | tr '\n' ',')"
[[ "$surviving_ids_d" == "rs1,rs5," ]] || fail "(d) expected surviving rsids 'rs1,rs5,', got '$surviving_ids_d'"
# no NA token leaked into the join-key column
zcat "$WORK/d/canonical.tsv.gz" | tail -n +2 | cut -f1 | grep -qiE '^(na|nan|\.|none|null|)$' \
  && fail "(d) an NA-token rsid leaked into the output" || true
dropped_na_d="$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['n_dropped_na_rsid'])" "$WORK/d/canonical.tsv.gz.canonical.json")"
[[ "$dropped_na_d" -eq 2 ]] || fail "(d) expected sidecar n_dropped_na_rsid=2, got $dropped_na_d"
echo "PASS (d) NA-rsid drop: 2 survive (rs1,rs5), n_dropped_na_rsid=2, no NA token in output"

echo "test_canonicalize.sh: ALL PASS"
