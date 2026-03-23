# Module 2: Deep Learning Best Practices & Applications

**Instructor:** Luca Monaco (CIMA Foundation)
**Date:** 27 May 2026, 14:00–16:00 CEST
**Format:** Remote (Microsoft Teams) + Google Colab

---

## 1. Introduction to Deep Learning (~20 min)

- From linear models to neural networks
- Key building blocks: neurons, layers, activation functions
- Backpropagation and gradient descent — intuition and mechanics
- Architecture overview:
  - **CNNs** — spatial feature extraction, convolution & pooling
  - **RNNs / LSTMs** — sequential data, memory mechanisms
  - **Transformers** — attention mechanism, parallelism, modern dominance
- When to use deep learning (and when not to)

## 2. The Modern ML Stack (~20 min)

- **Zarr** — chunked, compressed, cloud-ready N-dimensional arrays
  - Why Zarr over NetCDF for ML pipelines
  - Integration with xarray
- **PyTorch Lightning** — structured training loops, callbacks, multi-GPU
  - LightningModule and LightningDataModule patterns
- **Hydra** — hierarchical configuration management
  - Config composition, overrides, multirun sweeps
- **MLFlow** — experiment tracking, model registry
  - Logging metrics, parameters, and artifacts
- How these tools fit together in a real workflow

## 3. Hands-on 1: Precipitation Forecast Post-Processing (~30 min)

- **Goal:** Correct systematic biases in NWP precipitation forecasts using a CNN
- **Data:** ERA5 reanalysis total precipitation (pre-processed Zarr subset)
- **Walkthrough:**
  1. Load data with xarray + Zarr
  2. Build a simple CNN in PyTorch Lightning
  3. Configure hyperparameters with Hydra (OmegaConf inline)
  4. Train the model, track experiments with MLFlow
  5. Evaluate and visualize results
- **Notebook:** `notebooks/01_precipitation_postprocessing.ipynb`

## 4. Hands-on 2: Urban Thermal Comfort Modeling (~30 min)

- **Goal:** Predict thermal comfort index from meteorological + urban variables
- **Data:** ERA5-Land meteorological variables + land cover features (pre-processed Zarr)
- **Walkthrough:**
  1. Load multi-variable urban climate dataset from Zarr
  2. Feature engineering and dataset preparation
  3. Build an MLP / small CNN in PyTorch Lightning
  4. Configure and train with Hydra + MLFlow
  5. Evaluate classification/regression performance
- **Notebook:** `notebooks/02_urban_thermal_comfort.ipynb`

## 5. Wrap-up & Q&A (~20 min)

- Key takeaways
- Tips for scaling: larger datasets, distributed training, cloud deployment
- Resources and further reading
- Open Q&A
