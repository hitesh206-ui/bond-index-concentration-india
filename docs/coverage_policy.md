# Coverage policy

This project uses a coverage-aware framework because Indian bond index information may not be disclosed consistently across index families.

## Coverage classes

### Full coverage

Use this class when constituent names and weights are available for the index observation date.

### Partial coverage

Use this class when some constituent or weight information is available, but not enough to reconstruct the complete index portfolio.

Partial coverage metrics should be labelled as disclosed-portfolio estimates or lower-bound estimates.

### Methodology-cap-only

Use this class when constituent-level weights are not available, but index methodology rules are available.

Metrics based on methodology-cap-only information must not be presented as observed portfolio concentration. They should be labelled as rule-implied or cap-implied estimates.

## Coverage score

Suggested scoring:

- 3 = full constituent and weight data available
- 2 = partial constituent or weight data available
- 1 = methodology rules available only
- 0 = insufficient information

## Reporting rule

Every table or figure should identify the coverage class used for each index.
