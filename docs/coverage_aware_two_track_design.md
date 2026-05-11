# Coverage-aware two-track research design

## Core idea

This project will not treat missing portfolio weights as a failure of the study. Instead, inconsistent index disclosure becomes part of the research problem.

The paper separates concentration evidence into two tracks:

1. Observed weighted concentration
2. Coverage-aware constituent and rule-implied concentration analysis

## Track 1: Observed weighted concentration

This track is used only when official constituent weights are available.

Allowed outputs:

- Observed issuer HHI
- Observed group HHI
- Observed sector HHI
- Observed Top-1, Top-3, Top-5, and Top-10 exposure weights
- Observed effective number of issuers, groups, and sectors

Entry rule:

- Portfolio weights must come from an official source.
- Weights must be entered as decimals in `data/raw/constituents.csv`.
- The source must be recorded in the `source_file` field.

## Track 2: Coverage-aware constituent and rule-implied analysis

This track is used when actual weights are missing but constituents, issuer caps, index rules, or visible issuer sets are available.

Allowed outputs:

- Visible issuer counts
- Unique issuer counts by index and index family
- Issuer recurrence across duration buckets
- Ownership-type clustering
- Group clustering
- Sector clustering
- Equal-weight visible-issuer scenarios
- Issuer-cap scenarios
- SDL equal-state scenarios
- Coverage-quality assessment

Entry rule:

- Scenario values must be stored separately from observed data.
- Scenario values must never be entered into the actual weight field in `constituents.csv`.
- Scenario results must be labelled as constituent-only, equal-weight, rule-implied, or assumption-based.

## Why this design is useful

Indian fixed-income index disclosure may vary across index families. Some indices provide detailed portfolio data, while others provide only constituent names, methodology rules, or factsheet characteristics.

A simple empirical paper would fail if weights are missing. This paper instead asks a broader question:

> How should issuer, group, and sectoral concentration be measured when benchmark coverage varies across index providers and index families?

This makes the paper a measurement-framework contribution rather than only a descriptive HHI study.

## Result taxonomy

### Observed weighted results

Use when official weights are available.

Label in tables:

```text
Observed weighted concentration
```

### Constituent-only evidence

Use when issuer names are available but weights are missing.

Label in tables:

```text
Constituent-only concentration evidence
```

### Rule-implied scenarios

Use when methodology caps or equal-weight rules are available.

Label in tables:

```text
Rule-implied concentration scenario
```

## Recommended paper structure

1. Introduction
2. Indian bond index landscape
3. Data and coverage classification
4. Coverage-aware methodology
5. Constituent-only concentration evidence
6. Rule-implied concentration scenarios
7. Observed weighted concentration, if available
8. Discussion and policy implications
9. Conclusion

## Key paper claim

Indian bond indices may appear diversified by security count, duration bucket, or rating bucket, but economic exposure can remain concentrated at issuer, group, sovereign, public-sector, banking, or state-government levels. A coverage-aware framework is necessary to distinguish observed weighted concentration from partial-disclosure and methodology-cap-based evidence.

## Research integrity rules

1. Do not guess weights.
2. Do not treat issuer caps as observed portfolio weights.
3. Do not mix observed and scenario-based values without labels.
4. Do not calculate observed HHI from blank or assumed weights.
5. Use missing weight disclosure as an empirical transparency finding.
