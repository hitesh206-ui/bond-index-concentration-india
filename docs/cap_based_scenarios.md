# Cap-based concentration scenarios

## Purpose

This file explains the role of `data/interim/cap_based_scenarios.csv`.

The cap-based scenario layer is used only when official constituent weights are unavailable. It does not replace observed portfolio concentration analysis.

## Scenario types

### Equal-weight constituent scenario

This scenario assumes all visible issuers in a segment receive equal weight.

Use case:

- Provides a simple concentration benchmark when constituents are visible but weights are not.
- Useful for showing that a segment with only four visible issuers is mechanically concentrated even before actual weights are known.

Limitations:

- Not an observed index weight.
- Should not be described as actual HHI.
- Must be labelled as an assumption-based scenario.

### Issuer-cap floor scenario

This scenario assumes that enough issuers are present for the index to allocate 10 percent to each of ten issuers.

Use case:

- Provides a rule-implied lower concentration benchmark under a 10 percent issuer cap.
- Shows the least concentrated structure possible if exactly ten issuers are each held at 10 percent.

Limitations:

- It is not an observed index portfolio.
- It ignores market-value and liquidity weighting.
- It does not capture group-level clustering if capped issuers belong to related public-sector or government-linked groups.

### Visible-issuer warning scenario

This scenario identifies cases where the visible issuer universe is smaller than the number required to fully use the issuer cap rule.

Use case:

- Flags missing rows or incomplete pasted/extracted source text.
- Prevents overclaiming from partial extracts.

## Reporting rule

Tables using these scenarios should be labelled as `rule-implied`, `constituent-only`, or `assumption-based`. They should not be mixed with observed portfolio-weight results.

## Research integrity note

Observed HHI can be calculated only after official weights are verified. Cap-based scenarios are useful for sensitivity analysis and methodological discussion, not for replacing source-weighted concentration measurement.
