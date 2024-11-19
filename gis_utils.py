import pandas as pd
import geopandas as gpd
from shapely import wkt
from pathlib import Path


def csv_wkt_to_shapefile(in_csv: str, out_shp: str, geom_col: str, crs: str = 'EPSG:4326') -> bool:
    """
    Convert a CSV file containing WKT geometry to a shapefile.

    Example use:
        csv_wkt_to_shapefile(in_csv='Data/data.csv',
                            out_shp='Data/data.shp',
                            geom_col='the_geom')

    Parameters:
        in_csv (str): Path to input CSV file
        out_shp (str): Path for output shapefile
        geom_col (str): Name of the column containing WKT geometry
        crs (str): Coordinate reference system (default: WGS84)

    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Validate input file exists
        if not Path(in_csv).exists():
            raise FileNotFoundError(f"Input file not found: {in_csv}")

        # Read CSV file
        df = pd.read_csv(in_csv)

        # Validate geometry column exists
        if geom_col not in df.columns:
            raise ValueError(f"Geometry column '{geom_col}' not found in CSV")

        # Convert WKT strings to geometry objects
        df['geometry'] = df[geom_col].apply(wkt.loads)

        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame(df, geometry='geometry', crs=crs)

        # Drop the original WKT geometry column
        if geom_col != 'geometry':
            gdf = gdf.drop(columns=[geom_col])

        # Create output directory if it doesn't exist
        Path(out_shp).parent.mkdir(parents=True, exist_ok=True)

        # Save to shapefile
        gdf.to_file(out_shp)

        print(f"Successfully converted {in_csv} to {out_shp}")
        return True

    except Exception as e:
        print(f"Error converting file: {str(e)}")
        return False