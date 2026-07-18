# science:code
# status: workflow-owned
# task_ids: [t139]
# science:end
"""Acquire pinned GEO/reference payloads for the t139 frailty feasibility packet.

Step-2 scope: download the configured targets (GSE157007 series matrix + RAW.tar,
and the MCPcounter deconvolution panel), stream a SHA-256, and write/append a
manifest. Record-or-verify discipline (fail-early, no unverified passthrough):

  * config sha256 == "PENDING-RETRIEVAL"  -> bootstrap: record the digest into the
                                             manifest (to be locked into config).
  * config sha256 is a real hash          -> VERIFY; mismatch => HALT (partial file
                                             removed; never leave a payload that
                                             masquerades as verified).

Streams to a `.partial` sibling and atomically renames only after hashing, so an
interrupted fetch never satisfies a Snakemake output. Uses stdlib urllib only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

import yaml

_UA = {"User-Agent": "t139-frailty-feasibility/D-008 (research; contact via repo)"}
_CHUNK = 1 << 20  # 1 MiB
_PENDING = {"PENDING-RETRIEVAL", "PENDING-GENERATION", ""}


def _spec(cfg: dict, key: str) -> dict:
    """Resolve a target spec from either geo.targets.<key> or refs.<key>."""
    if key in cfg.get("geo", {}).get("targets", {}):
        s = dict(cfg["geo"]["targets"][key])
    elif key in cfg.get("refs", {}):
        s = dict(cfg["refs"][key])
    else:
        raise SystemExit(f"acquire: unknown target '{key}'")
    if "url" not in s or "filename" not in s:
        raise SystemExit(f"acquire: target '{key}' is not a downloadable spec (no url/filename)")
    return s


def download(url: str, dest: Path) -> tuple[str, int]:
    """Stream-download url -> dest.partial -> dest; return (sha256_hex, n_bytes)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.name + ".partial")
    h = hashlib.sha256()
    n = 0
    req = urllib.request.Request(url, headers=_UA)
    print(f"[acquire] GET {url}", file=sys.stderr)
    with urllib.request.urlopen(req, timeout=600) as resp, open(tmp, "wb") as fh:
        while chunk := resp.read(_CHUNK):
            fh.write(chunk)
            h.update(chunk)
            n += len(chunk)
    tmp.replace(dest)
    return h.hexdigest(), n


def acquire_one(cfg: dict, key: str, raw_dir: Path) -> dict:
    spec = _spec(cfg, key)
    dest = raw_dir / spec["filename"]
    locked = str(spec.get("sha256", "")).strip()

    sha, nbytes = download(spec["url"], dest)

    if locked not in _PENDING and sha != locked:
        dest.unlink(missing_ok=True)
        sys.exit(
            f"[acquire] HALT: sha256 mismatch for {key} ({spec['filename']})\n"
            f"          expected {locked}\n"
            f"          got      {sha}\n"
            f"          (upstream re-deposit? re-verify provenance, then amend the "
            f"locked hash in config.yaml — never auto-accept.)"
        )
    status = "verified" if locked not in _PENDING else "recorded(bootstrap)"
    rec = {
        "key": key,
        "series": cfg.get("geo", {}).get("series"),
        "source_url": spec["url"],
        "local_path": str(dest),
        "filename": spec["filename"],
        "sha256": sha,
        "bytes": nbytes,
        "locked_sha256": locked,
        "status": status,
    }
    sys.stderr.write(
        f"[acquire] {key}: {status} sha256={sha[:16]}… bytes={nbytes}\n"
    )
    return rec


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--only", action="append", default=None,
                   help="acquire only these target keys (repeatable); default = all downloadable")
    p.add_argument("--manifest", required=True)
    a = p.parse_args()
    cfg = yaml.safe_load(Path(a.config).read_text())
    raw_dir = Path(cfg["paths"]["raw"])

    if a.only:
        keys = a.only
    else:
        keys = list(cfg.get("geo", {}).get("targets", {}).keys())
        keys += [k for k, v in cfg.get("refs", {}).items()
                 if isinstance(v, dict) and "url" in v]

    records = [acquire_one(cfg, k, raw_dir) for k in keys]

    Path(a.manifest).parent.mkdir(parents=True, exist_ok=True)
    manifest = {"records": {r["key"]: r for r in records}}
    Path(a.manifest).write_text(json.dumps(manifest, indent=2))
    print(f"[acquire] wrote manifest {a.manifest} ({len(records)} record(s))", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
