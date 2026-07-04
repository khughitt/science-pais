# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Stage the MRlap cross-trait LDSC reference (plan:0009 Task 1).

dataset:eur-ldsc-ld-score-reference. MRlap runs cross-trait LDSC internally and
needs two path arguments: `ld` = the eur_w_ld_chr folder, `hm3` = w_hm3.snplist.

- eur_w_ld_chr: DOI-archival, checksummed Zenodo mirror (record 8182036), md5
  verified (HARD-STOP on mismatch), extracted; the required chr 1..22 ldscore +
  M_5_50 files are validated exactly and archival extras recorded as ignored.
  Deliberately NOT MRlap's non-archival UT-Austin Box link (plan:0009 review Dim 3).
- w_hm3.snplist: DOI-archival, checksummed Zenodo mirror (record 7773502), md5
  verified (HARD-STOP on mismatch). The original Broad Alkes-group GCS bucket
  404'd at staging, so the Zenodo mirror is the pinned source.

The LDSC reference is GRCh37 and rsID-keyed. The staged Ruth exposures and HGI
outcome are GRCh38 harmonised sumstats, so reconciliation is by rsID/hm_rsid
(build-independent), with a hard stop later if rsIDs are missing.
"""
from __future__ import annotations

import argparse
import bz2
import gzip
import hashlib
import json
import sys
import tarfile
import urllib.request
from pathlib import Path

import yaml

_UA = {"User-Agent": "wave1-mr-hormone/plan-0009 (research; contact via repo)"}


def _hash_download(url: str, dest: Path) -> tuple[str, str]:
    """Stream-download; return (md5_hex, sha256_hex)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    md5, sha = hashlib.md5(), hashlib.sha256()
    req = urllib.request.Request(url, headers=_UA)
    with urllib.request.urlopen(req, timeout=600) as resp, open(dest, "wb") as fh:
        while chunk := resp.read(1 << 20):
            fh.write(chunk)
            md5.update(chunk)
            sha.update(chunk)
    return md5.hexdigest(), sha.hexdigest()


def stage_eur_w_ld_chr(spec: dict, ldsc_dir: Path) -> dict:
    archive = ldsc_dir / spec["archive_name"]
    got_md5, sha = _hash_download(spec["url"], archive)
    if spec.get("md5") and got_md5 != spec["md5"]:
        raise SystemExit(
            f"stage_ldsc_ref: eur_w_ld_chr md5 mismatch: expected {spec['md5']}, got {got_md5} — HALT"
        )
    # Extract into ldsc_dir/eur_w_ld_chr/ (archive root is the eur_w_ld_chr folder).
    with tarfile.open(archive, "r:*") as tar:
        _safe_extract(tar, ldsc_dir)
    ld_folder = ldsc_dir / "eur_w_ld_chr"
    if not ld_folder.is_dir():
        # some mirrors nest differently; find the folder that holds *.l2.ldscore.gz
        cands = {q.parent for q in ldsc_dir.rglob("*.l2.ldscore.gz")}
        if len(cands) != 1:
            raise SystemExit(f"stage_ldsc_ref: cannot locate eur_w_ld_chr folder, found {cands} — HALT")
        ld_folder = cands.pop()
    # Required set = chromosomes 1..22, each with its matching .l2.M_5_50 sidecar.
    # Archival extras (e.g. `6_old.l2.ldscore.gz`) are recorded as ignored, NOT
    # counted as chromosomes — MRlap/LDSC address the folder by chr prefix.
    all_ldscore = sorted(ld_folder.glob("*.l2.ldscore.gz"))
    required_names = {f"{c}.l2.ldscore.gz" for c in range(1, 23)}
    missing = []
    for chrom in range(1, 23):
        score = ld_folder / f"{chrom}.l2.ldscore.gz"
        m5 = ld_folder / f"{chrom}.l2.M_5_50"
        if not score.is_file():
            missing.append(f"{score.name} (missing ldscore)")
        elif not m5.is_file():
            missing.append(f"{m5.name} (missing M_5_50 sidecar)")
    if missing:
        raise SystemExit(
            f"stage_ldsc_ref: eur_w_ld_chr missing required chr 1..22 files: {missing} — HALT"
        )
    extras = sorted(f.name for f in all_ldscore if f.name not in required_names)
    return {
        "archive": str(archive),
        "archive_md5": got_md5,
        "archive_sha256": sha,
        "expected_md5": spec.get("md5", ""),
        "doi": spec.get("doi", ""),
        "license": spec.get("license", ""),
        "ld_folder": str(ld_folder),
        "required_chromosomes": "1..22",
        "n_required_ldscore_files": 22,
        "extra_ldscore_files_ignored": extras,
    }


def stage_hm3(spec: dict, ldsc_dir: Path) -> dict:
    archive = ldsc_dir / spec["archive_name"]
    got_md5, sha = _hash_download(spec["url"], archive)
    if spec.get("md5") and got_md5 != spec["md5"]:
        raise SystemExit(
            f"stage_ldsc_ref: w_hm3.snplist md5 mismatch: expected {spec['md5']}, got {got_md5} — HALT"
        )
    snplist = ldsc_dir / "w_hm3.snplist"
    raw = archive.read_bytes()   # ~few MB compressed — fine in memory
    if archive.suffix == ".gz":
        data = gzip.decompress(raw)
    elif archive.suffix == ".bz2":
        data = bz2.decompress(raw)
    else:
        raise SystemExit(f"stage_ldsc_ref: unsupported hm3 archive suffix {archive.suffix} — HALT")
    snplist.write_bytes(data)
    n = data.count(b"\n")
    return {
        "archive": str(archive),
        "archive_md5": got_md5,
        "archive_sha256": sha,
        "snplist": str(snplist),
        "n_rows": n,
        "license": spec.get("license", ""),
    }


def _safe_extract(tar: tarfile.TarFile, path: Path) -> None:
    """Extract with a traversal guard (no absolute paths / .. escapes)."""
    base = path.resolve()
    for member in tar.getmembers():
        target = (base / member.name).resolve()
        if not str(target).startswith(str(base)):
            raise SystemExit(f"stage_ldsc_ref: unsafe path in archive: {member.name} — HALT")
    tar.extractall(path)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--ldsc-dir", required=True)   # e.g. data/raw/ldsc
    p.add_argument("--manifest", required=True)
    a = p.parse_args()
    cfg = yaml.safe_load(Path(a.config).read_text())
    ref = cfg["ldsc_ref"]
    ldsc_dir = Path(a.ldsc_dir)

    eur = stage_eur_w_ld_chr(ref["eur_w_ld_chr"], ldsc_dir)
    sys.stderr.write(
        f"stage_ldsc_ref: eur_w_ld_chr md5 OK ({eur['archive_md5'][:12]}…), "
        f"{eur['n_required_ldscore_files']} required chr files (1..22), "
        f"{len(eur['extra_ldscore_files_ignored'])} extra ignored\n"
    )
    hm3 = stage_hm3(ref["hm3"], ldsc_dir)
    sys.stderr.write(f"stage_ldsc_ref: w_hm3.snplist rows={hm3['n_rows']} sha256={hm3['archive_sha256'][:12]}…\n")

    manifest = {
        "name": ref["name"],
        "build": ref["build"],
        "rsid_keyed": True,
        "build_reconciliation": (
            "Staged Ruth exposures and HGI outcome are GRCh38 harmonised sumstats; "
            "the LDSC (eur_w_ld_chr) and 1000G references are GRCh37. The LDSC "
            "reference is rsID-keyed, so join is by rsID/hm_rsid → build-independent; "
            "hard-stop later if rsIDs are missing. PASS."
        ),
        "eur_w_ld_chr": eur,
        "hm3": hm3,
    }
    Path(a.manifest).parent.mkdir(parents=True, exist_ok=True)
    Path(a.manifest).write_text(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
