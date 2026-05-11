"""Generate concentration figures from observed results or cap-based scenarios.

Observed figures are created only if `outputs/tables/observed_concentration_results.csv`
exists. Scenario figures are created if `data/interim/cap_based_scenarios.csv` exists.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TABLES = ROOT / "outputs" / "tables"
OUTPUT_FIGURES = ROOT / "outputs" / "figures"
SCENARIO_PATH = ROOT / "data" / "interim" / "cap_based_scenarios.csv"
OBSERVED_PATH = OUTPUT_TABLES / "observed_concentration_results.csv"


def save_bar_chart(df: pd.DataFrame, x_col: str, y_col: str, title: str, output_path: Path) -> None:
    """Save a basic bar chart."""
    plot_df = df.dropna(subset=[y_col]).sort_values(y_col, ascending=False)
    if plot_df.empty:
        return

    ax = plot_df.plot(kind="bar", x=x_col, y=y_col, legend=False)
    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel(y_col)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def generate_scenario_figures() -> None:
    """Generate figures from cap-based scenario rows."""
    if not SCENARIO_PATH.exists():
        return

    scenarios = pd.read_csv(SCENARIO_PATH)
    if "rule_implied_hhi" in scenarios.columns:
        save_bar_chart(
            scenarios,
            x_col="scenario_id",
            y_col="rule_implied_hhi",
            title="Rule-implied HHI by cap-based scenario",
            output_path=OUTPUT_FIGURES / "cap_scenario_rule_implied_hhi.png",
        )
    if "rule_implied_effective_issuers" in scenarios.columns:
        save_bar_chart(
            scenarios,
            x_col="scenario_id",
            y_col="rule_implied_effective_issuers",
            title="Rule-implied effective issuers by cap-based scenario",
            output_path=OUTPUT_FIGURES / "cap_scenario_effective_issuers.png",
        )


def generate_observed_figures() -> None:
    """Generate figures from observed concentration results."""
    if not OBSERVED_PATH.exists():
        return

    observed = pd.read_csv(OBSERVED_PATH)
    figure_specs = [
        ("issuer_name_hhi", "observed_issuer_hhi.png", "Observed issuer HHI by index"),
        ("issuer_group_hhi", "observed_group_hhi.png", "Observed group HHI by index"),
        ("sector_hhi", "observed_sector_hhi.png", "Observed sector HHI by index"),
        ("issuer_name_effective_number", "observed_effective_issuers.png", "Observed effective number of issuers by index"),
    ]

    for y_col, filename, title in figure_specs:
        if y_col in observed.columns:
            save_bar_chart(
                observed,
                x_col="index_id",
                y_col=y_col,
                title=title,
                output_path=OUTPUT_FIGURES / filename,
            )


def main() -> None:
    """Generate available figures."""
    generate_scenario_figures()
    generate_observed_figures()
    print(f"Figures saved to {OUTPUT_FIGURES}")


if __name__ == "__main__":
    main()
