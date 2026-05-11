# Concentration in Indian Bond Indices

## Working title

**Concentration in Indian Bond Indices: A Coverage-Aware Analysis of Issuer, Group, and Sectoral Risk**

## Research purpose

This repository supports an empirical research paper measuring issuer-level, group-level, and sector-level concentration in Indian fixed-income benchmarks. The project uses a coverage-aware framework to distinguish between indices with full constituent disclosure, partial disclosure, and methodology-cap-only information.

## Core research question

How concentrated are Indian bond indices once issuer, corporate group, and sectoral exposures are measured under a coverage-aware framework?

## Planned sample

The estimated sample is 18-25 Indian bond indices across categories such as:

- Government securities indices
- State development loan indices
- Corporate bond indices
- Banking and PSU bond indices
- Target maturity bond indices
- Money market or short-duration fixed-income indices, where data is available

## Main concentration metrics

- Issuer-level Herfindahl-Hirschman Index (HHI)
- Top-1, Top-3, Top-5, and Top-10 issuer weights
- Effective number of issuers
- Group-level HHI
- Sector-level HHI
- Coverage-adjusted concentration classification

## Coverage policy

Each index will be classified into one of three coverage categories:

1. **Full coverage**: constituent names and weights are available.
2. **Partial coverage**: some constituent or weight information is available, but not enough for complete direct measurement.
3. **Methodology-cap-only**: methodology rules are available, but constituent-level weights are not fully observable.

## Policy anchor

The paper will interpret concentration findings with reference to Indian index-provider regulation and bond-index methodology rules, including issuer-cap rules where applicable.

## Tools

- Excel for structured dataset building
- Python for cleaning, calculation, and reproducible analysis
- pandas and numpy for data processing
- matplotlib for charts
- GitHub for version control and project transparency

## Repository structure

```text
bond-index-concentration-india/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── docs/
├── notebooks/
├── outputs/
│   ├── figures/
│   └── tables/
├── paper/
└── src/
```

## Current status

Project initialized. The next step is to populate the index master, coverage log, methodology caps, and constituent templates.
