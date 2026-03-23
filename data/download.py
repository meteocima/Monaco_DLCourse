"""Download ERA5 data from the Copernicus Climate Data Store.

Requires a configured CDS API key. See: https://cds.climate.copernicus.eu/api-how-to
"""

import argparse


def download_precipitation(years: tuple[int, int], output_dir: str = "data"):
    """Download ERA5 total precipitation for Europe."""
    import cdsapi

    c = cdsapi.Client()
    c.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "variable": "total_precipitation",
            "year": [str(y) for y in range(years[0], years[1] + 1)],
            "month": [f"{m:02d}" for m in range(1, 13)],
            "day": [f"{d:02d}" for d in range(1, 32)],
            "time": ["00:00", "06:00", "12:00", "18:00"],
            "area": [60, -10, 35, 30],  # N, W, S, E
            "format": "netcdf",
        },
        f"{output_dir}/era5_precipitation.nc",
    )
    print(f"Downloaded precipitation data to {output_dir}/era5_precipitation.nc")


def download_urban(cities: list[str], output_dir: str = "data"):
    """Download ERA5-Land data for urban areas."""
    import cdsapi

    # City bounding boxes (approximate)
    city_boxes = {
        "Rome": [42.1, 12.2, 41.6, 12.8],
        "Milan": [45.6, 9.0, 45.3, 9.4],
        "Berlin": [52.7, 13.1, 52.3, 13.6],
    }

    c = cdsapi.Client()
    for city in cities:
        if city not in city_boxes:
            print(f"Unknown city: {city}, skipping")
            continue
        area = city_boxes[city]
        c.retrieve(
            "reanalysis-era5-land",
            {
                "product_type": "reanalysis",
                "variable": [
                    "2m_temperature",
                    "2m_dewpoint_temperature",
                    "10m_u_component_of_wind",
                    "10m_v_component_of_wind",
                    "surface_solar_radiation_downwards",
                ],
                "year": ["2020"],
                "month": ["06", "07", "08"],
                "day": [f"{d:02d}" for d in range(1, 32)],
                "time": [f"{h:02d}:00" for h in range(24)],
                "area": area,
                "format": "netcdf",
            },
            f"{output_dir}/era5land_{city.lower()}.nc",
        )
        print(f"Downloaded {city} data to {output_dir}/era5land_{city.lower()}.nc")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download ERA5 data for DL course")
    parser.add_argument(
        "--dataset",
        choices=["precipitation", "urban"],
        required=True,
    )
    parser.add_argument("--years", nargs=2, type=int, default=[2018, 2020])
    parser.add_argument("--cities", type=str, default="Rome,Milan,Berlin")
    parser.add_argument("--output-dir", type=str, default="data")
    args = parser.parse_args()

    if args.dataset == "precipitation":
        download_precipitation(tuple(args.years), args.output_dir)
    elif args.dataset == "urban":
        download_urban(args.cities.split(","), args.output_dir)
