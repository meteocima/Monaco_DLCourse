# Data

This directory contains small preprocessed data samples used in the course notebooks.

## Datasets

### 1. ERA5 Total Precipitation (Notebook 1)

- **Source:** [Copernicus Climate Data Store (CDS)](https://cds.climate.copernicus.eu/)
- **Variable:** Total precipitation (`tp`)
- **Domain:** Europe (35°N–60°N, 10°W–30°E)
- **Resolution:** 0.25° × 0.25°
- **Period:** 2018–2020 (subset)
- **License:** [Copernicus License](https://cds.climate.copernicus.eu/api/v2/terms/static/licence-to-use-copernicus-products.pdf)

### 2. Urban Climate Variables (Notebook 2)

- **Source:** [ERA5-Land](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land) + [Copernicus Land Cover](https://land.copernicus.eu/)
- **Variables:** 2m temperature, 2m dewpoint, 10m wind speed, surface solar radiation, land cover class
- **Domain:** Selected European urban areas
- **License:** Copernicus License

## Downloading Data

The notebooks include cells that generate synthetic sample data for demonstration purposes, so no download is required to run them.

To work with real data, you can use the CDS API:

```bash
pip install cdsapi
```

Then configure your API key following [CDS API instructions](https://cds.climate.copernicus.eu/api-how-to).

A download helper is provided:

```bash
python data/download.py --dataset precipitation --years 2018 2020
python data/download.py --dataset urban --cities "Rome,Milan,Berlin"
```
