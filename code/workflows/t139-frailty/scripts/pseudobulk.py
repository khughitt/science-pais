# science:code
# status: workflow-owned
# task_ids: [t139]
# science:end
"""Donor-level pseudobulk from GSE157007 scRNA GEX libraries (Step 2).

For each kept GEX donor (5 frail + 6 healthy-old), extract its 10x triplet from
the pinned RAW.tar, sum raw counts across ALL cells per gene -> one pseudobulk
count vector per donor. Donors are aligned on the INTERSECTION of Ensembl gene
ids present in every donor's features (records the drop). GEX libraries only [A1].

Handles the format heterogeneity verified in the metadata: the F0xx submission
ships `_matrix.tsv.gz`, the later OH submission ships `_matrix.mtx.gz`. Format and
orientation are auto-detected and cross-checked against each library's features/
barcodes counts; a mismatch HALTs (fail-early, no silent mis-orientation).

Stdlib only (tarfile/gzip); streams entries so memory stays bounded.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import io
import sys
import tarfile
from pathlib import Path


def _open_member(tar: tarfile.TarFile, name: str) -> io.TextIOWrapper:
    f = tar.extractfile(name)
    if f is None:
        raise SystemExit(f"[pseudobulk] HALT: member {name} not found in tar")
    return io.TextIOWrapper(gzip.GzipFile(fileobj=f), encoding="utf-8")


def _member(tar_names: dict[str, str], basename: str) -> str:
    """Resolve a GSM-prefixed basename to its full path inside the tar."""
    if basename in tar_names:
        return tar_names[basename]
    raise SystemExit(f"[pseudobulk] HALT: {basename} not found among tar members")


def read_features(tar, name):
    """10x features.tsv -> (ensembl_ids, symbols, gex_row_mask). Row order == matrix gene rows."""
    ids, syms, is_gex = [], [], []
    with _open_member(tar, name) as fh:
        for line in fh:
            p = line.rstrip("\n").split("\t")
            ids.append(p[0])
            syms.append(p[1] if len(p) > 1 else p[0])
            # 3rd col = feature_type when present; a GEX library should be all
            # "Gene Expression", but guard against a mixed CITE feature set.
            is_gex.append((len(p) < 3) or (p[2].strip() == "Gene Expression"))
    return ids, syms, is_gex


def count_lines(tar, name):
    n = 0
    with _open_member(tar, name) as fh:
        for _ in fh:
            n += 1
    return n


def sum_matrix(tar, name, n_features, n_cells):
    """Return per-gene summed counts (length n_features), auto-detecting mtx vs dense."""
    with _open_member(tar, name) as fh:
        first = fh.readline()
        if first.startswith("%%MatrixMarket"):
            return _sum_mtx(fh, n_features, n_cells)
        return _sum_dense(first, fh, n_features, n_cells)


def _sum_mtx(fh, n_features, n_cells):
    # skip remaining % comment lines, then the dims line "R C NNZ"
    line = fh.readline()
    while line.startswith("%"):
        line = fh.readline()
    r, c, _nnz = (int(x) for x in line.split())
    if r == n_features:
        gene_axis = 0           # genes are rows (10x convention)
    elif c == n_features:
        gene_axis = 1
    else:
        raise SystemExit(
            f"[pseudobulk] HALT: mtx dims ({r}x{c}) match neither n_features={n_features} "
            f"nor n_cells={n_cells}")
    totals = [0] * n_features
    for line in fh:
        if not line.strip():
            continue
        a, b, v = line.split()
        gi = (int(a) if gene_axis == 0 else int(b)) - 1
        totals[gi] += int(float(v))
    return totals


def _sum_dense(first, fh, n_features, n_cells):
    """Dense genes×cells TSV, streamed. A DATA row's last cell is an integer
    count; a barcode HEADER row's cells are non-numeric -> skipped. The row-label
    offset (`off`) is inferred from the first data row's width (n_cells vs
    n_cells+1), not from the header (which would mis-set it)."""
    import itertools

    def _is_num(x):
        try:
            float(x); return True
        except ValueError:
            return False

    totals = []
    off = None
    for line in itertools.chain([first], fh):
        if not line.strip():
            continue
        tok = line.rstrip("\n").split("\t")
        if not _is_num(tok[-1]):
            continue                      # header / annotation row
        ncol = len(tok)
        this_off = 1 if ncol == n_cells + 1 else (0 if ncol == n_cells else None)
        if this_off is None:
            raise SystemExit(
                f"[pseudobulk] HALT: dense row width {ncol} matches neither "
                f"n_cells ({n_cells}) nor n_cells+1 ({n_cells + 1})")
        if off is None:
            off = this_off
        totals.append(sum(int(float(x)) for x in tok[off:]))
    if len(totals) != n_features:
        raise SystemExit(
            f"[pseudobulk] HALT: dense TSV produced {len(totals)} gene rows, "
            f"expected n_features={n_features}")
    return totals


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--donor-map", required=True)
    ap.add_argument("--raw-tar", required=True)
    ap.add_argument("--counts-out", required=True)
    ap.add_argument("--donors-out", required=True)
    ap.add_argument("--genes-out", required=True)
    a = ap.parse_args()

    kept = [r for r in csv.DictReader(open(a.donor_map), delimiter="\t") if r["keep"] == "1"]
    if not kept:
        raise SystemExit("[pseudobulk] HALT: no kept GEX donors in donor map")

    print(f"[pseudobulk] opening tar {a.raw_tar} …", file=sys.stderr)
    with tarfile.open(a.raw_tar, "r") as tar:
        tar_names = {Path(m.name).name: m.name for m in tar.getmembers()}

        per_donor: dict[str, dict[str, int]] = {}   # donor -> {ensembl: count}
        sym_of: dict[str, str] = {}
        for r in kept:
            donor = r["subject_id"]
            feats = _member(tar_names, r["features_file"])
            barc = _member(tar_names, r["barcodes_file"])
            mat = _member(tar_names, r["matrix_file"])
            ids, syms, is_gex = read_features(tar, feats)
            n_cells = count_lines(tar, barc)
            totals = sum_matrix(tar, mat, len(ids), n_cells)
            d = {}
            for gid, sym, gex, tot in zip(ids, syms, is_gex, totals):
                if not gex:
                    continue
                d[gid] = d.get(gid, 0) + tot          # collapse duplicate ids
                sym_of.setdefault(gid, sym)
            per_donor[donor] = d
            print(f"[pseudobulk] {donor} ({r['group']}, {r['matrix_format']}): "
                  f"{len(ids)} features, {n_cells} cells, {sum(totals)} total counts",
                  file=sys.stderr)

    donors = [r["subject_id"] for r in kept]
    common = set.intersection(*(set(per_donor[d]) for d in donors))
    common = sorted(common)
    print(f"[pseudobulk] {len(common)} genes common to all {len(donors)} donors", file=sys.stderr)
    if len(common) < 5000:
        raise SystemExit(f"[pseudobulk] HALT: only {len(common)} common genes — suspect a parse/ref mismatch")

    # counts matrix: ensembl_id + one column per donor
    Path(a.counts_out).parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(a.counts_out, "wt", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["ensembl_id", *donors])
        for gid in common:
            w.writerow([gid, *(per_donor[d][gid] for d in donors)])

    with open(a.genes_out, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["ensembl_id", "symbol"])
        for gid in common:
            w.writerow([gid, sym_of.get(gid, gid)])

    kept_by_donor = {r["subject_id"]: r for r in kept}
    with open(a.donors_out, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["donor", "group", "gsm", "matrix_format"])
        for d in donors:
            r = kept_by_donor[d]
            w.writerow([d, r["group"], r["gsm"], r["matrix_format"]])

    print(f"[pseudobulk] wrote {a.counts_out} ({len(common)} genes x {len(donors)} donors)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
