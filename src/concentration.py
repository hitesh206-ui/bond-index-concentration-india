"""Concentration metrics for Indian bond index analysis."""

from __future__ import annotations

import pandas as pd


def calculate_hhi(weights: pd.Series) -> float:
    """Calculate Herfindahl-Hirschman Index from decimal weights."""
    clean_weights = pd.to_numeric(weights, errors="coerce").dropna()
    return float((clean_weights ** 2).sum())


def calculate_effective_number(hhi: float) -> float:
    """Convert HHI into effective number of issuers, groups, or sectors."""
    if hhi == 0 or pd.isna(hhi):
        return float("nan")
    return float(1 / hhi)


def calculate_top_n_weight(weights: pd.Series, n: int) -> float:
    """Calculate combined weight of the top n exposures."""
    clean_weights = pd.to_numeric(weights, errors="coerce").dropna()
    return float(clean_weights.sort_values(ascending=False).head(n).sum())


def aggregate_weights(df: pd.DataFrame, group_cols: list[str], weight_col: str = "weight") -> pd.DataFrame:
    """Aggregate security-level weights to issuer, group, or sector level."""
    required_cols = set(group_cols + [weight_col])
    missing = required_cols.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    return (
        df.groupby(group_cols, dropna=False, as_index=False)[weight_col]
        .sum()
        .sort_values(weight_col, ascending=False)
    )


def calculate_index_concentration(
    df: pd.DataFrame,
    index_col: str = "index_id",
    exposure_col: str = "issuer_name",
    weight_col: str = "weight",
) -> pd.DataFrame:
    """Calculate concentration metrics for each index and exposure level."""
    required_cols = {index_col, exposure_col, weight_col}
    missing = required_cols.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    rows = []
    for index_id, index_df in df.groupby(index_col):
        exposure_weights = aggregate_weights(index_df, [exposure_col], weight_col)
        weights = exposure_weights[weight_col]
        hhi = calculate_hhi(weights)
        rows.append(
            {
                index_col: index_id,
                f"{exposure_col}_hhi": hhi,
                f"{exposure_col}_effective_number": calculate_effective_number(hhi),
                f"{exposure_col}_top_1_weight": calculate_top_n_weight(weights, 1),
                f"{exposure_col}_top_3_weight": calculate_top_n_weight(weights, 3),
                f"{exposure_col}_top_5_weight": calculate_top_n_weight(weights, 5),
                f"{exposure_col}_top_10_weight": calculate_top_n_weight(weights, 10),
            }
        )

    return pd.DataFrame(rows)
