# Deep Learning Best Practices & Applications

**Module 2** of the CIMA Foundation PhD Course on Deep Learning
**Instructor:** Luca Monaco
**Date:** 27 May 2026, 14:00-16:00 CEST
**Format:** Remote (Microsoft Teams) + Google Colab

## Quick Start

Open the notebooks directly in Google Colab:

| Notebook | Colab |
|----------|-------|
| Precipitation Post-Processing | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USER/202605_Monaco_DLcourse/blob/main/notebooks/01_precipitation_postprocessing.ipynb) |
| Urban Thermal Comfort | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USER/202605_Monaco_DLcourse/blob/main/notebooks/02_urban_thermal_comfort.ipynb) |

No local setup required -- all dependencies are installed within the notebooks.

## Project Structure

```
notebooks/
  01_precipitation_postprocessing.ipynb  -- CNN for NWP bias correction
  02_urban_thermal_comfort.ipynb         -- MLP for UTCI prediction
data/
  README.md                              -- Data provenance & download instructions
  download.py                            -- CDS API download helper
slides/
  outline.md                             -- Presentation outline (2h session)
src/
  utils.py                               -- Shared plotting & metrics utilities
pyproject.toml                           -- Project metadata & dependencies
CLAUDE.md                                -- Developer guide
README.md                                -- This file
```

## Session Outline

1. **Introduction to Deep Learning** (~20 min) -- neurons, backprop, CNN/RNN/Transformer overview
2. **The Modern ML Stack** (~20 min) -- Zarr, PyTorch Lightning, Hydra, MLFlow
3. **Hands-on 1: Precipitation Post-Processing** (~30 min) -- CNN bias correction with full stack
4. **Hands-on 2: Urban Thermal Comfort** (~30 min) -- MLP regression with full stack
5. **Wrap-up & Q&A** (~20 min)

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
- [ERA5 on CDS](https://cds.climate.copernicus.eu/)
