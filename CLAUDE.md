# CLAUDE.md

## Project Overview

Teaching materials for **Module 2: Deep Learning Best Practices & Applications**, part of the CIMA Foundation PhD course. Instructor: Luca Monaco, 27 May 2026.

Two hands-on Colab notebooks demonstrate applying a modern ML stack (Zarr, PyTorch Lightning, Hydra, MLFlow) to geoscience problems:
1. Precipitation forecast post-processing (CNN)
2. Urban thermal comfort prediction (MLP)

## Setup

```bash
uv sync              # install all dependencies
uv run jupyter lab   # launch notebooks locally
```

## Important: always use `uv`

**Never use bare `python3`, `python`, or `pip`.**  All Python commands must go through `uv`:

| Instead of | Use |
|---|---|
| `python3 script.py` | `uv run python script.py` |
| `python3 -c "..."` | `uv run python -c "..."` |
| `pip install foo` | `uv add foo` |
| `ruff check .` | `uv run ruff check .` |
| `pytest` | `uv run pytest` |

## Key Dependencies

| Package | Role |
|---------|------|
| `torch` + `pytorch-lightning` | Model definition & training loop |
| `zarr` + `xarray` | Chunked N-dimensional array storage & access |
| `hydra-core` / `omegaconf` | Configuration management |
| `mlflow` | Experiment tracking |
| `matplotlib` | Visualization |
| `cdsapi` | ERA5 data download (optional) |

## Running Notebooks

Notebooks are designed for Google Colab (free GPU). Each includes a `!pip install` cell. For local runs, `uv sync` provides all dependencies.

## Project Structure

- `notebooks/` — Jupyter notebooks for hands-on exercises
- `data/` — Data README and download script (synthetic data generated in-notebook)
- `slides/` — Presentation outline
- `src/` — Shared Python utilities
