"""
Every figure in the project, one function each.
All charts use matplotlib only (no seaborn).
"""
import numpy as np
import matplotlib.pyplot as plt
from src.stats_helpers import gaussian_kde


def _save(fig, save_path):
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")


# ------------------------------------------------------------
# Page 8 — Histogram of Price
# ------------------------------------------------------------
def plot_price_histogram(df, save_path=None):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(df["Price"], bins=30, color="steelblue",
            edgecolor="white", density=True, label="Histogram")

    x_grid = np.linspace(df["Price"].min(), df["Price"].max(), 500)
    kde = gaussian_kde(df["Price"].values, x_grid)
    ax.plot(x_grid, kde, color="black", linewidth=2, label="KDE")

    ax.set_title("Simple Histogram of Price",
                 fontsize=14, fontweight="bold")
    ax.set_xlabel("Price")
    ax.set_ylabel("Density")
    ax.legend(loc="upper right")

    mean_val = df["Price"].mean()
    std_val = df["Price"].std()
    n_val = df["Price"].count()
    ax.text(0.98, 0.95,
            f"Mean = {mean_val:,.2f}\nStd. Dev. = {std_val:,.3f}\nN = {n_val}",
            transform=ax.transAxes, ha="right", va="top", fontsize=9,
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    plt.tight_layout()
    _save(fig, save_path)
    return fig


# ------------------------------------------------------------
# Page 9 — Price vs living area, Price vs lot area
# ------------------------------------------------------------
def plot_scatter_living_lot(df, save_path=None):
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    axes[0].scatter(df["living area"], df["Price"],
                    alpha=0.5, edgecolors="k", linewidths=0.3,
                    color="steelblue")
    axes[0].set_title("Scatter Plot of Price by living area",
                      fontsize=13, fontweight="bold")
    axes[0].set_xlabel("living area")
    axes[0].set_ylabel("Price")
    axes[0].ticklabel_format(style="plain", axis="y")

    axes[1].scatter(df["lot area"], df["Price"],
                    alpha=0.5, edgecolors="k", linewidths=0.3,
                    color="steelblue")
    axes[1].set_title("Scatter Plot of Price by lot area",
                      fontsize=13, fontweight="bold")
    axes[1].set_xlabel("lot area")
    axes[1].set_ylabel("Price")
    axes[1].ticklabel_format(style="plain", axis="y")

    plt.tight_layout()
    _save(fig, save_path)
    return fig


# ------------------------------------------------------------
# Page 10 — Number of floors
# ------------------------------------------------------------
def plot_floors(df, save_path=None):
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    floor_counts = df["number of floors"].value_counts().sort_index()
    axes[0].bar(floor_counts.index, floor_counts.values,
                width=0.4, color="steelblue", edgecolor="white")
    axes[0].set_title("Simple Bar of number of floors",
                      fontsize=13, fontweight="bold")
    axes[0].set_xlabel("number of floors")
    axes[0].set_ylabel("Frequency")

    mean_f = df["number of floors"].mean()
    std_f = df["number of floors"].std()
    n_f = df["number of floors"].count()
    axes[0].text(0.98, 0.95,
                 f"Mean = {mean_f:.2f}\nStd. Dev. = {std_f:.3f}\nN = {n_f}",
                 transform=axes[0].transAxes, ha="right", va="top",
                 fontsize=9,
                 bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    axes[1].scatter(df["number of floors"], df["Price"],
                    alpha=0.5, edgecolors="k", linewidths=0.3,
                    color="steelblue")
    axes[1].set_title("Scatter Plot of Price by number of floors",
                      fontsize=13, fontweight="bold")
    axes[1].set_xlabel("number of floors")
    axes[1].set_ylabel("Price")
    axes[1].ticklabel_format(style="plain", axis="y")

    plt.tight_layout()
    _save(fig, save_path)
    return fig


# ------------------------------------------------------------
# Page 11 — Grade & condition
# ------------------------------------------------------------
def plot_grade_condition(df, save_path=None):
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    grade_mean = df.groupby("grade of the house")["Price"].mean().sort_index()
    axes[0].bar(grade_mean.index.astype(str), grade_mean.values,
                color="dodgerblue", edgecolor="white")
    axes[0].set_title("Simple Bar Mean of Price by grade of the house",
                      fontsize=13, fontweight="bold")
    axes[0].set_xlabel("grade of the house")
    axes[0].set_ylabel("Mean Price")
    axes[0].ticklabel_format(style="plain", axis="y")

    cond_mean = df.groupby("condition of the house")["Price"].mean().sort_index()
    axes[1].bar(cond_mean.index.astype(str), cond_mean.values,
                color="dodgerblue", edgecolor="white")
    axes[1].set_title("Simple Bar Mean of Price by condition of the house",
                      fontsize=13, fontweight="bold")
    axes[1].set_xlabel("condition of the house")
    axes[1].set_ylabel("Mean Price")
    axes[1].ticklabel_format(style="plain", axis="y")

    plt.tight_layout()
    _save(fig, save_path)
    return fig


# ------------------------------------------------------------
# Page 12 — Basement
# ------------------------------------------------------------
def plot_basement(df, save_path=None):
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    axes[0].hist(df["Area of the basement"], bins=20,
                 color="dodgerblue", edgecolor="white")
    axes[0].set_title("Simple Histogram of Area of the basement",
                      fontsize=13, fontweight="bold")
    axes[0].set_xlabel("Area of the basement")
    axes[0].set_ylabel("Frequency")

    mean_b = df["Area of the basement"].mean()
    std_b = df["Area of the basement"].std()
    n_b = df["Area of the basement"].count()
    axes[0].text(0.98, 0.95,
                 f"Mean = {mean_b:.2f}\nStd. Dev. = {std_b:.3f}\nN = {n_b}",
                 transform=axes[0].transAxes, ha="right", va="top",
                 fontsize=9,
                 bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    hb_mean = df.groupby("Has_Basement")["Price"].mean()
    axes[1].bar(hb_mean.index.astype(str), hb_mean.values,
                color="dodgerblue", edgecolor="white")
    axes[1].set_title("Has_Basement", fontsize=13, fontweight="bold")
    axes[1].set_xlabel("Has_Basement")
    axes[1].set_ylabel("Mean Price")
    axes[1].ticklabel_format(style="plain", axis="y")

    plt.tight_layout()
    _save(fig, save_path)
    return fig


# ------------------------------------------------------------
# Page 13 — Scatter Price vs living area, colored by basement
# ------------------------------------------------------------
def plot_scatter_basement(df, save_path=None):
    fig, ax = plt.subplots(figsize=(10, 6))

    mask0 = df["Has_Basement"] == 0
    mask1 = df["Has_Basement"] == 1

    ax.scatter(df.loc[mask0, "living area"], df.loc[mask0, "Price"],
               alpha=0.6, edgecolors="k", linewidths=0.3,
               color="#440154", label="Area of the basement = 0")
    ax.scatter(df.loc[mask1, "living area"], df.loc[mask1, "Price"],
               alpha=0.6, edgecolors="k", linewidths=0.3,
               color="#21918c", label="Area of the basement = 1")

    ax.set_title("Scatter Plot of Price by living area (colored by basement)",
                 fontsize=13, fontweight="bold")
    ax.set_xlabel("living area")
    ax.set_ylabel("Price")
    ax.ticklabel_format(style="plain", axis="y")
    ax.legend(title="Area of the\nbasement", loc="upper left")

    plt.tight_layout()
    _save(fig, save_path)
    return fig


# ------------------------------------------------------------
# Page 14 — Distance from airport & schools nearby
# ------------------------------------------------------------
def plot_airport_schools(df, save_path=None):
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    d_air = df["Distance from the airport"].dropna().values
    axes[0].hist(d_air, bins=30, color="steelblue",
                 edgecolor="white", density=True)
    x_grid = np.linspace(d_air.min(), d_air.max(), 500)
    kde = gaussian_kde(d_air, x_grid)
    axes[0].plot(x_grid, kde, color="black", linewidth=2)
    axes[0].set_title("Distance from the airport",
                      fontsize=13, fontweight="bold")
    axes[0].set_xlabel("Distance from the airport")
    axes[0].set_ylabel("Density")

    school_mean = (df.groupby("Number of schools nearby")["Price"]
                     .mean().sort_index())
    axes[1].bar(school_mean.index.astype(str), school_mean.values,
                color="dodgerblue", edgecolor="white")
    axes[1].set_title("Simple Bar Mean of Price by Number of schools nearby",
                      fontsize=13, fontweight="bold")
    axes[1].set_xlabel("Number of schools nearby")
    axes[1].set_ylabel("Mean Price")
    axes[1].ticklabel_format(style="plain", axis="y")

    plt.tight_layout()
    _save(fig, save_path)
    return fig


# ------------------------------------------------------------
# Page 15 — Latitude & Longitude
# ------------------------------------------------------------
def plot_lat_long(df, save_path=None):
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    axes[0].scatter(df["Lattitude"], df["Price"],
                    alpha=0.5, edgecolors="k", linewidths=0.3,
                    color="steelblue")
    axes[0].set_title("Scatter Plot of Price by Latitude",
                      fontsize=13, fontweight="bold")
    axes[0].set_xlabel("Latitude")
    axes[0].set_ylabel("Price")
    axes[0].ticklabel_format(style="plain", axis="y")

    axes[1].scatter(df["Longitude"], df["Price"],
                    alpha=0.5, edgecolors="k", linewidths=0.3,
                    color="steelblue")
    axes[1].set_title("Scatter Plot of Price by Longitude",
                      fontsize=13, fontweight="bold")
    axes[1].set_xlabel("Longitude")
    axes[1].set_ylabel("Price")
    axes[1].ticklabel_format(style="plain", axis="y")

    plt.tight_layout()
    _save(fig, save_path)
    return fig


# ------------------------------------------------------------
# Bonus — Correlation matrix
# ------------------------------------------------------------
def plot_correlation_matrix(df, save_path=None):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()

    fig, ax = plt.subplots(figsize=(14, 10))
    im = ax.imshow(corr.values, cmap="coolwarm",
                   vmin=-1, vmax=1, aspect="auto")

    ax.set_xticks(np.arange(len(corr.columns)))
    ax.set_yticks(np.arange(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90, fontsize=8)
    ax.set_yticklabels(corr.columns, fontsize=8)

    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            val = corr.values[i, j]
            ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                    color="white" if abs(val) > 0.5 else "black",
                    fontsize=6)

    ax.set_title("Correlation Matrix of Numeric Variables",
                 fontsize=14, fontweight="bold")
    fig.colorbar(im, ax=ax, shrink=0.8)

    plt.tight_layout()
    _save(fig, save_path)
    return fig
