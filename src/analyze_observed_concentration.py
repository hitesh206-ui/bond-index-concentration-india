"""Calculate observed concentration metrics from verified constituent weights.

This script should be run only after `data/raw/constituents.csv` contains
verified portfolio weights as decimals.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from concentration import calculate_index_concentration
from issuer_mapping import apply_issuer_mapping


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUTPUT = ROOT / "outputs" / "tables" / "observed_concentration_results.csv"


def load_inputs() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load constituent and issuer mapping data."""
    constituents = pd.read_csv(RAW / "constituents.csv")
    issuer_mapping = pd.read_csv(RAW / "issuer_mapping.csv")
    return constituents, issuer_mapping


def filter_weighted_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Keep rows with numeric weights only."""
    df = df.copy()
    df["weight"] = pd.to_numeric(df["weight"], errors="coerce")
    return df.dropna(subset=["weight", "issuer_name"])


def build_results(weighted: pd.DataFrame) -> pd.DataFrame:
    """Calculate issuer, group, and sector concentration metrics."""
    issuer_results = calculate_index_concentration(weighted, exposure_col="issuer_name")

    group_results = calculate_index_concentration(weighted, exposure_col="issuer_group")
    sector_results = calculate_index_concentration(weighted, exposure_col="sector")

    results = issuer_results.merge(group_results, on="index_id", how="outer")
    results = results.merge(sector_results, on="index_id", how="outer")
    return results


def main() -> None:
    """Run observed concentration analysis."""
    constituents, issuer_mapping = load_inputs()
    mapped = apply_issuer_mapping(constituents, issuer_mapping)
    weighted = filter_weighted_rows(mapped)

    if weighted.empty:
        raise ValueError(
            "No verified numeric weights found in data/raw/constituents.csv. "
            "Observed concentration analysis is blocked until weights are entered."
        )

    results = build_results(weighted)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(OUTPUT, index=False)
    print(f"Saved observed concentration results to {OUTPUT}")


if __name__ == "__main__":
    main()
