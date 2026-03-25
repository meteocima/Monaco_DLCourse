# Deep Learning Best Practices & Applications

> Learn to apply deep learning to real geoscience problems using a modern, production-ready ML stack — all from your browser, no setup required.

**Module 2** of the CIMA Foundation PhD Course on Deep Learning<br>
**Instructor:** Luca Monaco<br>
**Date:** 27 May 2026, 14:00-16:00 CEST<br>
**Format:** Remote (Teams) + Google Colab

---

## Get Started in One Click

Pick a notebook and open it directly in Google Colab — everything installs automatically:

| Notebook | What you'll build | Colab |
|----------|-------------------|-------|
| **Precipitation Post-Processing** | A CNN that corrects bias in NWP rainfall forecasts using ERA5 data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meteocima/Monaco_DLCourse/blob/main/notebooks/01_precipitation_postprocessing.ipynb) |
| **Urban Thermal Comfort** | An MLP that predicts "feels-like" temperature (UTCI) from meteorological variables | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meteocima/Monaco_DLCourse/blob/main/notebooks/02_urban_thermal_comfort.ipynb) |

<details>
<summary>Versione italiana dei notebook</summary>

| Notebook | Colab |
|----------|-------|
| Post-Processing delle Precipitazioni | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meteocima/Monaco_DLCourse/blob/main/notebooks/01_precipitation_postprocessing_it.ipynb) |
| Comfort Termico Urbano | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/meteocima/Monaco_DLCourse/blob/main/notebooks/02_urban_thermal_comfort_it.ipynb) |

</details>

---

## What You'll Learn

By the end of this session you will be able to:

- **Build and train** neural networks (CNN, MLP) in PyTorch Lightning with minimal boilerplate
- **Access cloud data** directly from Zarr stores (ERA5 reanalysis) — no downloads, no NetCDF wrangling
- **Manage experiments** with structured configs (Hydra/OmegaConf) and automatic tracking (MLFlow)
- **Evaluate models** with proper metrics, visualisations, and feature-importance analysis
- **Reproduce results** using a modern Python toolchain (uv) with locked dependencies

## The Stack

| Tool | Role |
|------|------|
| [**Zarr**](https://zarr.readthedocs.io/) + [**xarray**](https://xarray.dev/) | Cloud-native, chunked N-dimensional data — read only what you need |
| [**PyTorch Lightning**](https://lightning.ai/docs/pytorch/stable/) | Structured training loops, callbacks, multi-GPU — without the boilerplate |
| [**Hydra**](https://hydra.cc/docs/intro/) / **OmegaConf** | YAML-based configuration with overrides and hyperparameter sweeps |
| [**MLFlow**](https://mlflow.org/docs/latest/) | Experiment tracking — log metrics, parameters, and artifacts automatically |
| [**uv**](https://docs.astral.sh/uv/) | Fast, modern Python package manager (replaces pip + virtualenv) |

## Session Outline (2 hours)

| Time | Topic |
|------|-------|
| ~20 min | **Introduction to Deep Learning** — neurons, backprop, CNN / RNN / Transformer overview |
| ~20 min | **The Modern ML Stack** — how Zarr, Lightning, Hydra, and MLFlow fit together |
| ~20 min | **Slides wrap-up & Q&A** |
| ~30 min | **Hands-on 1: Precipitation Post-Processing** — train a CNN to correct NWP bias |
| ~30 min | **Hands-on 2: Urban Thermal Comfort** — train an MLP to predict UTCI |

## Prerequisites

- A **Google account** (to run the notebooks on Colab)
- **Basic Python** — if you can write a `for` loop and use NumPy arrays, you're ready
- Some familiarity with ML concepts (train/test split, loss functions) is helpful but not required — the notebooks explain everything step by step

## Running Locally

```bash
# Requires uv (https://docs.astral.sh/uv/)
uv sync              # install all dependencies
uv run jupyter lab   # launch the notebooks
```

## References & Further Reading

- [PyTorch Lightning Docs](https://lightning.ai/docs/pytorch/stable/)
- [Zarr Docs](https://zarr.readthedocs.io/)
- [Hydra Docs](https://hydra.cc/docs/intro/)
- [MLFlow Docs](https://mlflow.org/docs/latest/)
- [WeatherBench 2](https://weatherbench2.readthedocs.io/) — ERA5 Zarr on Google Cloud (Notebook 1)
- [ARCO-ERA5](https://github.com/google-research/arco-era5) — Full ERA5 Zarr on Google Cloud (Notebook 2)
