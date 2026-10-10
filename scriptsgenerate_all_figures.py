"""
Run every chart in the project and save all PNGs into figures/.

Usage (from the project root):
    python scripts/generate_all_figures.py
"""
import os
import sys

# Make `src` importable when running this script from the project root
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from src.loader import load_data, describe_column
from src import plotting


def main():
    figures_dir = os.path.join(ROOT, "figures")
    os.makedirs(figures_dir, exist_ok=True)

    print("Loading data...")
    df = load_data()
    print(f"Loaded {len(df)} rows, {df.shape[1]} columns.")

    # Descriptive stats for the report
    print("\n=== Area of the house (excluding basement) ===")
    for k, v in describe_column(df, "Area of the house(excluding basement)").items():
        print(f"  {k}: {v}")

    print("\n=== Price ===")
    for k, v in describe_column(df, "Price").items():
        print(f"  {k}: {v}")

    # Generate each figure
    jobs = [
        ("01_hist_price.png", plotting.plot_price_histogram),
        ("02_scatter_living_lot.png", plotting.plot_scatter_living_lot),
        ("03_floors.png", plotting.plot_floors),
        ("04_grade_condition.png", plotting.plot_grade_condition),
        ("05_basement.png", plotting.plot_basement),
        ("06_scatter_basement.png", plotting.plot_scatter_basement),
        ("07_airport_schools.png", plotting.plot_airport_schools),
        ("08_lat_long.png", plotting.plot_lat_long),
        ("09_correlation_matrix.png", plotting.plot_correlation_matrix),
    ]

    for fname, func in jobs:
        out = os.path.join(figures_dir, fname)
        print(f"Generating {fname} ...")
        func(df, save_path=out)

    print(f"\nAll figures saved to: {figures_dir}")


if __name__ == "__main__":
    main()
