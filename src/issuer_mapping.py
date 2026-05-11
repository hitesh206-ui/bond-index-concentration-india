"""Issuer standardization helpers."""

from __future__ import annotations

import pandas as pd


def standardize_text(value: object) -> str:
    """Standardize text fields for matching."""
    if pd.isna(value):
        return ""
    return str(value).strip().upper().replace("  ", " ")


def apply_issuer_mapping(
    constituents: pd.DataFrame,
    issuer_mapping: pd.DataFrame,
    issuer_col: str = "issuer_name",
) -> pd.DataFrame:
    """Merge constituent data with issuer mapping table."""
    constituents = constituents.copy()
    issuer_mapping = issuer_mapping.copy()

    constituents["issuer_key"] = constituents[issuer_col].apply(standardize_text)
    issuer_mapping["issuer_key"] = issuer_mapping["issuer_name"].apply(standardize_text)

    mapped = constituents.merge(
        issuer_mapping.drop_duplicates("issuer_key"),
        on="issuer_key",
        how="left",
        suffixes=("", "_mapping"),
    )
    return mapped.drop(columns=["issuer_key"])
