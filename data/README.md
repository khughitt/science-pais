# `data/` — raw & processed payloads (host-local, off-Dropbox)

This repository lives under Dropbox (`~/d/health/processes/post-acute-infection`),
so large raw/processed data payloads must **not** sit physically inside the repo —
they would sync to Dropbox and fill it. Instead:

- **`data/raw`** and **`data/processed`** are **symlinks** to
  `/data/proj/post-acute-infection/{raw,processed}` on the large local disk
  (`/data`, multi-TB), created on this host (`titan`).
- Every workflow still references repo-relative paths (`data/raw/...`,
  `data/processed/...`); only the physical bytes live off-Dropbox. No workflow
  config changes are needed.
- Both symlinks and everything under them are gitignored (see `.gitignore`).
  `results/` (small, tracked-selectively) and workflow descriptors stay in the repo.

## Recreating on a fresh clone / another host

The symlinks are host-local and are **not** committed. On a new machine, recreate
them before running any workflow that stages data:

```bash
mkdir -p /data/proj/post-acute-infection/{raw,processed}
ln -s /data/proj/post-acute-infection/raw       data/raw
ln -s /data/proj/post-acute-infection/processed data/processed
```

Then re-stage inputs via the workflows (e.g.
`uv run snakemake -s code/workflows/wave1-mr-hormone/Snakefile --use-conda -c1 stage_all`),
which re-download from their pinned, checksummed sources.
