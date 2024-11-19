# GIS Utilities

A Python utility for converting GIS data from CSV format (with WKT geometry) to Shapefile format.

## Features

- Converts CSV files containing WKT (Well-Known Text) geometry to ESRI Shapefiles
- Supports custom geometry column names
- Configurable coordinate reference system (CRS)
- Simple error handling and success messages

## Prerequisites

Make sure you have the following Python packages installed:

```bash
pip install pandas geopandas shapely
```

## Installation

1. Clone or download this repository
2. Place `gis_utils.py` in your project directory

## Usage

### Function Signature

```python
csv_wkt_to_shapefile(in_csv, out_shp, geom_col, crs='EPSG:4326')
```

### Parameters

- `in_csv` (str): Path to input CSV file
- `out_shp` (str): Path for output shapefile
- `geom_col` (str): Name of the column containing WKT geometry
- `crs` (str, optional): Coordinate reference system. Defaults to 'EPSG:4326' (WGS84)

### Example Usage

#### In Python Interactive Shell

```python
# Start Python shell in your project directory
from gis_utils import csv_wkt_to_shapefile

# Convert CSV to Shapefile
csv_wkt_to_shapefile(
    in_csv='Data/my_data.csv',
    out_shp='Data/output.shp',
    geom_col='the_geom'
)
```

#### Example Input CSV Format

Your CSV file should include a column containing WKT geometry. For example:

```csv
the_geom,LINES,DESCRIPTION,TYPE
"MULTILINESTRING ((-87.628 41.876, -87.627 41.876))",Line1,Description1,Type1
"MULTILINESTRING ((-87.626 41.875, -87.625 41.875))",Line2,Description2,Type2
```

## Error Handling

The function will print success or error messages:
- Success: "Successfully converted [input] to [output]"
- Error: "Error converting file: [error message]"

## Directory Structure

Recommended project structure:
```
your_project/
├── gis_utils.py
├── Data/
│   ├── input.csv
│   └── output.shp
└── README.md
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.