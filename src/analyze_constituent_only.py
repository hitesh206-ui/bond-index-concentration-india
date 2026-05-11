"""Constituent-only concentration evidence.

Analyzes visible issuer coverage when weights are missing.
These outputs are not observed weighted concentration results.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUTPUT = ROOT / "outputs" / "tables"


def standardize(value: object) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip().upper()


def load_mapped_data() -> pd.DataFrame:
    constituents = pd.read_csv(RAW / "constituents.csv")
    mapping = pd.read_csv(RAW / "issuer_mapping.csv")
    constituents["issuer_key"] = constituents["issuer_name"].apply(standardize)
    mapping["issuer_key"] = mapping["issuer_name"].apply(standardize)
    return constituents.merge(mapping.drop_duplicates("issuer_key"), on="issuer_key", how="left", suffixes=("", "_map"))


def main() -> None:
    df = load_mapped_data()
    OUTPUT.mkdir(parents=True, exist_ok=True)

    issuer_counts = (
        df.groupby(["index_id", "security_name"], dropna=False)
        .agg(
            visible_security_rows=("isin", "count"),
            visible_unique_issuers=("issuer_name", "nunique"),
            visible_unique_groups=("issuer_group", "nunique"),
            visible_unique_sectors=("sector", "nunique"),
        )
        .reset_index()
    )
    issuer_counts.to_csv(OUTPUT / "constituent_only_issuer_counts.csv", index=False)

    recurrence = (
        df.groupby(["index_id", "issuer_name"], dropna=False)
        .agg(
            visible_rows=("isin", "count"),
            visible_segments=("security_name", "nunique"),
            issuer_group=("issuer_group", "first"),
            ownership_type=("ownership_type", "first"),
            sector=("sector", "first"),
            sub_sector=("sub_sector", "first"),
        )
        .reset_index()
        .sort_values(["index_id", "visible_segments", "visible_rows"], ascending=[True, False, False])
    )
    recurrence.to_csv(OUTPUT / "constituent_only_issuer_recurrence.csv", index=False)

    ownership_mix = (
        df.groupby(["index_id", "ownership_type"], dropna=False)
        .agg(visible_rows=("isin", "count"), visible_unique_issuers=("issuer_name", "nunique"))
        .reset_index()
        .sort_values(["index_id", "visible_rows"], ascending=[True, False])
    )
    ownership_mix.to_csv(OUTPUT / "constituent_only_ownership_mix.csv", index=False)

    sector_mix = (
        df.groupby(["index_id", "sector"], dropna=False)
        .agg(visible_rows=("isin", "count"), visible_unique_issuers=("issuer_name", "nunique"))
        .reset_index()
        .sort_values(["index_id", "visible_rows"], ascending=[True, False])
    )
    sector_mix.to_csv(OUTPUT / "constituent_only_sector_mix.csv", index=False)

    print(f"Constituent-only outputs saved to {OUTPUT}")


if __name__ == "__main__":
    main()
