"""Plotting helpers for concentration analysis."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot_bar(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str,
    output_path: str | None = None,
) -> None:
    """Create a simple bar chart and optionally save it."""
    plot_df = df.sort_values(y_col, ascending=False)
    ax = plot_df.plot(kind="bar", x=x_col, y=y_col, legend=False)
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches="tight")

    plt.close()
