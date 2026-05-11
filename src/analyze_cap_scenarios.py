"""Analyze cap-based concentration scenarios.

This script intentionally analyzes only scenario-based rows from
`data/interim/cap_based_scenarios.csv`. These are not observed portfolio
weights and should not be reported as observed concentration results.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCENARIO_PATH = ROOT / "data" / "interim" / "cap_based_scenarios.csv"
OUTPUT_PATH = ROOT / "outputs" / "tables" / "cap_based_scenario_summary.csv"


def load_scenarios(path: Path = SCENARIO_PATH) -> pd.DataFrame:
    """Load cap-based scenario data."""
    if not path.exists():
        raise FileNotFoundError(f"Scenario file not found: {path}")
    return pd.read_csv(path)


def summarize_scenarios(df: pd.DataFrame) -> pd.DataFrame:
    """Create a clean scenario summary table."""
    columns = [
        "scenario_id",
        "index_id",
        "index_segment",
        "scenario_type",
        "issuer_count",
        "issuer_cap",
        "rule_implied_hhi",
        "rule_implied_effective_issuers",
        "top_1_weight",
        "top_3_weight",
        "top_5_weight",
        "top_10_weight",
        "remarks",
    ]
    available_columns = [col for col in columns if col in df.columns]
    return df[available_columns].copy()


def main() -> None:
    """Run scenario analysis and export summary."""
    scenarios = load_scenarios()
    summary = summarize_scenarios(scenarios)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved scenario summary to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
