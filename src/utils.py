"""Shared utilities for DL course notebooks."""

import numpy as np
import matplotlib.pyplot as plt


def plot_prediction_comparison(y_true, y_pred, title="Prediction vs Ground Truth"):
    """Plot side-by-side comparison of ground truth and model prediction."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    im0 = axes[0].imshow(y_true, cmap="viridis")
    axes[0].set_title("Ground Truth")
    plt.colorbar(im0, ax=axes[0], fraction=0.046)

    im1 = axes[1].imshow(y_pred, cmap="viridis")
    axes[1].set_title("Prediction")
    plt.colorbar(im1, ax=axes[1], fraction=0.046)

    diff = y_pred - y_true
    im2 = axes[2].imshow(diff, cmap="RdBu_r")
    axes[2].set_title("Difference")
    plt.colorbar(im2, ax=axes[2], fraction=0.046)

    fig.suptitle(title)
    plt.tight_layout()
    return fig


def compute_metrics(y_true, y_pred):
    """Compute common regression metrics."""
    mse = np.mean((y_true - y_pred) ** 2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(y_true - y_pred))
    return {"mse": mse, "rmse": rmse, "mae": mae}
