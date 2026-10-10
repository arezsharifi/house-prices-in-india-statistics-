"""
Small statistical helpers — manual Gaussian KDE (no seaborn needed).
"""
import numpy as np


def gaussian_kde(data, x_grid, bandwidth=None):
    """
    Compute a Gaussian kernel density estimate.

    Uses Silverman's rule of thumb for bandwidth if not provided.
    This replaces seaborn's kde=True.
    """
    data = np.asarray(data)
    data = data[~np.isnan(data)]
    n = len(data)
    if n == 0:
        return np.zeros_like(x_grid)

    if bandwidth is None:
        std = np.std(data, ddof=1)
        iqr = np.subtract(*np.percentile(data, [75, 25]))
        bandwidth = 0.9 * min(std, iqr / 1.34) * n ** (-1 / 5)
        if bandwidth <= 0:
            bandwidth = 1.0

    diff = (x_grid[:, None] - data[None, :]) / bandwidth
    kernel = np.exp(-0.5 * diff ** 2) / np.sqrt(2 * np.pi)
    return kernel.sum(axis=1) / (n * bandwidth)
