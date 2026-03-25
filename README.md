# Deep Learning Best Practices & Applications

**Module 2** of the CIMA Foundation PhD Course on Deep Learning
**Instructor:** Luca Monaco
**Date:** 27 May 2026, 14:00-15:00 CEST
**Format:** Remote (Microsoft Teams) + Google Colab

## Quick Start

Open the notebooks directly in Google Colab:

| Notebook | Colab |
|----------|-------|
| Precipitation Post-Processing | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meteocima/Monaco_DLCourse/blob/main/notebooks/01_precipitation_postprocessing.ipynb) |
| Urban Thermal Comfort | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meteocima/Monaco_DLCourse/blob/main/notebooks/02_urban_thermal_comfort.ipynb) |

No local setup required — the notebooks auto-clone the repo and install dependencies via [uv](https://docs.astral.sh/uv/) when running on Colab.

## Project Structure

```
notebooks/
  01_precipitation_postprocessing.ipynb  -- CNN for NWP bias correction
  02_urban_thermal_comfort.ipynb         -- MLP for UTCI prediction
data/
  README.md                              -- Data provenance & download instructions
  download.py                            -- CDS API download helper
slides/
  outline.md                             -- Presentation outline (1h session)
src/
  utils.py                               -- Shared plotting & metrics utilities
pyproject.toml                           -- Project metadata & dependencies
requirements.txt                         -- Pinned deps for Colab installs
README.md                                -- This file
```

## Session Outline

1. **Introduction to Deep Learning** (~10 min) -- neurons, backprop, CNN/RNN/Transformer overview
2. **The Modern ML Stack** (~10 min) -- Zarr, PyTorch Lightning, Hydra, MLFlow
3. **Hands-on 1: Precipitation Post-Processing** (~15 min) -- CNN bias correction with full stack
4. **Hands-on 2: Urban Thermal Comfort** (~15 min) -- MLP regression with full stack
5. **Wrap-up & Q&A** (~10 min)

## Prerequisites

- Google account (for Colab)
- Basic Python knowledge
- Familiarity with NumPy and basic ML concepts

## Local Development

```bash
# Requires uv (https://docs.astral.sh/uv/)
uv sync
uv run jupyter lab
```

## References

- [PyTorch Lightning Docs](https://lightning.ai/docs/pytorch/stable/)
- [Zarr Docs](https://zarr.readthedocs.io/)
- [Hydra Docs](https://hydra.cc/docs/intro/)
- [MLFlow Docs](https://mlflow.org/docs/latest/)
- [WeatherBench 2](https://weatherbench2.readthedocs.io/) — ERA5 Zarr on Google Cloud (Notebook 1)
- [ARCO-ERA5](https://github.com/google-research/arco-era5) — Full ERA5 Zarr on Google Cloud (Notebook 2)
