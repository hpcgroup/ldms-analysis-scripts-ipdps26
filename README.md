# LDMS Analytics Notebooks for IPDPS'26 AD Appendix

This repository contains the Artifact A1 analysis code for reproducing the paper’s figures using Jupyter notebooks.

- Python version: 3.10.19
- Output: regenerates Figures 1–11 (one notebook per figure)
- Input data: requires the Perlmutter telemetry dataset (Artifact A2, restricted)

## Contents

- 1_overall_resource_usage.ipynb → Figure 1
- 2_gpu_fp_pipe_activity.ipynb → Figure 2
- 3_peak_hbm_usage.ipynb → Figure 3
- 4_arithmetic_intensity.ipynb → Figure 4
- 5_total_energy_consumption.ipynb → Figure 5
- 6_dist_spatial_imb.ipynb → Figure 6
- 7_spatial_imb_fp_compute_memory.ipynb → Figure 7
- 8_dist_temporal_imb.ipynb → Figure 8
- 9_temporal_imb_fb_compute_memory.ipynb → Figure 9
- 10_heatmap_fp64_dram_gputil.ipynb → Figure 10
- 11_correlation_heatmap.ipynb → Figure 11
Note: Some notebooks import a local helper module setup_plot (e.g., setup_plot.py). Ensure it is present in the repository and that you launch Jupyter from the repository root.

##  Prerequisites

- Python 3.10.19
- Access to Perlmutter DCGM data and its location on disk (local path on the authorized environment)
- A working pip (or conda) installation

## Creating a virtual environment

From the repository root:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install notebook ipykernel duckdb matplotlib numpy pandas pyarrow seaborn upsetplot cycler
```

## Launching Jupyter Notebook

Start Jupyter from inside so local imports (like `setup_plot.py`) resolve correctly.

## Data access note (Artifact A2)

The Perlmutter telemetry dataset (A2) is restricted because it was collected at a U.S. Department of Energy site.
