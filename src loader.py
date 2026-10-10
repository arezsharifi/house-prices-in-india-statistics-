"""
Load and clean the Indian House Price dataset.
"""
import pandas as pd
import os


def load_data(path: str = None) -> pd.DataFrame:
    """
    Load the Excel file and return a cleaned DataFrame.

    Parameters
    ----------
    path : str, optional
        Path to the Excel file. If None, uses the default location
        `data/indian_house_price.xlsx` relative to the project root.

    Returns
    -------
    pd.DataFrame
    """
    if path is None:
        # Compute project root (parent of src/)
        here = os.path.dirname(os.path.abspath(__file__))
        root = os.path.dirname(here)
        path = os.path.join(root, "data", "indian_house_price.xlsx")

    df = pd.read_excel(path)
    df.columns = df.columns.str.strip()

    # Basic sanity
    if "Price" not in df.columns:
        raise ValueError("Column 'Price' not found in dataset.")

    df = df.dropna(subset=["Price"]).copy()

    # Convenience flag used in several charts
    df["Has_Basement"] = (df["Area of the basement"] > 0).astype(int)

    return df


def describe_column(df: pd.DataFrame, col: str) -> dict:
    """Return N, missing, mean, median, mode for one column."""
    s = df[col]
    return {
        "N Valid": int(s.count()),
        "N Missing": int(s.isna().sum()),
        "Mean": round(float(s.mean()), 2),
        "Median": round(float(s.median()), 2),
        "Mode": float(s.mode().iloc[0]) if not s.mode().empty else None,
    }
