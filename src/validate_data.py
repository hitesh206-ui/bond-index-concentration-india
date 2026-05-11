"""Validate raw data files before concentration analysis.

This script checks whether the project CSV files contain the minimum required
columns and flags rows where concentration analysis is blocked by missing weights
or missing issuer mappings.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUTPUT = ROOT / "outputs" / "tables" / "data_validation_report.csv"

REQUIRED_COLUMNS = {
    "index_master.csv": [
        "index_id",
        "index_name",
        "provider",
        "index_category",
        "coverage_type",
    ],
    "constituents.csv": [
        "date",
        "index_id",
        "security_name",
        "isin",
        "issuer_name",
        "weight",
        "source_file",
    ],
    "issuer_mapping.csv": [
        "issuer_name",
        "standardized_issuer_name",
        "issuer_group",
        "ownership_type",
        "sector",
        "sub_sector",
        "mapping_confidence",
    ],
    "coverage_log.csv": [
        "index_id",
        "coverage_type",
        "constituents_available",
        "weights_available",
        "methodology_available",
        "coverage_score",
    ],
    "methodology_caps.csv": [
        "index_id",
        "issuer_cap",
        "methodology_source",
        "remarks",
    ],
}


def load_csv(filename: str) -> pd.DataFrame:
    """Load a raw project CSV file."""
    path = RAW / filename
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return pd.read_csv(path)


def validate_columns(filename: str, df: pd.DataFrame) -> list[dict[str, str]]:
    """Check required columns for a file."""
    rows: list[dict[str, str]] = []
    for column in REQUIRED_COLUMNS[filename]:
        rows.append(
            {
                "file": filename,
                "check": f"required_column:{column}",
                "status": "pass" if column in df.columns else "fail",
                "details": "" if column in df.columns else f"Missing column {column}",
            }
        )
    return rows


def validate_constituents(df: pd.DataFrame) -> list[dict[str, str]]:
    """Check concentration-readiness of constituent rows."""
    rows: list[dict[str, str]] = []
    if "weight" in df.columns:
        missing_weight_count = int(df["weight"].isna().sum() + (df["weight"].astype(str).str.strip() == "").sum())
        rows.append(
            {
                "file": "constituents.csv",
                "check": "missing_weights",
                "status": "warning" if missing_weight_count else "pass",
                "details": f"Rows missing weights: {missing_weight_count}",
            }
        )
    if "issuer_name" in df.columns:
        missing_issuer_count = int(df["issuer_name"].isna().sum() + (df["issuer_name"].astype(str).str.strip() == "").sum())
        rows.append(
            {
                "file": "constituents.csv",
                "check": "missing_issuer_names",
                "status": "warning" if missing_issuer_count else "pass",
                "details": f"Rows missing issuer names: {missing_issuer_count}",
            }
        )
    return rows


def main() -> None:
    """Run validation and export a report."""
    report_rows: list[dict[str, str]] = []

    for filename in REQUIRED_COLUMNS:
        df = load_csv(filename)
        report_rows.extend(validate_columns(filename, df))
        if filename == "constituents.csv":
            report_rows.extend(validate_constituents(df))

    report = pd.DataFrame(report_rows)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(OUTPUT, index=False)
    print(f"Saved data validation report to {OUTPUT}")


if __name__ == "__main__":
    main()
