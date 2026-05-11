# Methodology draft

## Research design

This study measures concentration in Indian fixed-income benchmarks using a coverage-aware framework. The framework separates directly observed concentration from partial-disclosure and methodology-cap-based concentration scenarios.

## Unit of analysis

The base unit of analysis is an index-security observation. Each security is mapped to an issuer, issuer group, ownership type, sector, and sub-sector.

The main analytical levels are:

1. Issuer-level concentration
2. Group-level concentration
3. Sector-level concentration

## Coverage-aware classification

Each index is classified into one of the following coverage categories:

### Full coverage

Constituent names and portfolio weights are available. These indices are eligible for observed concentration analysis.

### Partial coverage

Constituent information is available but weights are missing or incomplete. These indices are eligible for constituent-only analysis and scenario analysis, but not observed HHI.

### Methodology-cap-only coverage

Constituent weights are unavailable, but methodology rules such as issuer caps are known. These indices are eligible for rule-implied scenario analysis only.

## Concentration metrics

### Herfindahl-Hirschman Index

The Herfindahl-Hirschman Index is calculated as:

```text
HHI = sum(w_i^2)
```

where `w_i` is the decimal portfolio weight of issuer, group, or sector `i`.

### Effective number

The effective number of issuers, groups, or sectors is calculated as:

```text
Effective number = 1 / HHI
```

This converts concentration into an intuitive diversification-equivalent measure.

### Top exposure weights

The study calculates:

- Top-1 exposure weight
- Top-3 exposure weight
- Top-5 exposure weight
- Top-10 exposure weight

These measures are calculated at issuer level and, where relevant, group and sector levels.

## Issuer-group mapping

Issuer-level analysis may understate economic concentration when multiple issuers belong to the same government-linked group, financial conglomerate, or public-sector ecosystem. Therefore, the study maps issuers to broader groups and recomputes concentration at the group level.

Examples include:

- PFC-REC Group
- Indian Railways / Government of India
- LIC Group
- Government-linked development finance institutions
- State or Union Territory issuers for SDL indices

## Sector mapping

Each issuer is assigned to a sector and sub-sector, such as:

- Sovereign
- State development loans
- Financial institution
- Housing finance
- Infrastructure finance
- Power generation
- Oil and gas
- Banking
- Public-sector undertaking

## Scenario analysis

Scenario analysis is used only when observed weights are unavailable.

### Equal-weight visible-issuer scenario

This assumes all visible issuers within an index segment receive equal weight.

### Issuer-cap scenario

This uses stated methodology caps, such as a 10 percent issuer cap, to create a rule-implied benchmark.

These scenarios are not observed portfolio results. They are used to evaluate the concentration implications of methodology rules and incomplete disclosure.

## Research integrity rule

Observed HHI, observed top issuer weights, and observed effective issuer counts are calculated only when official constituent weights are available and entered as numeric decimal weights.

Scenario-based measures must be clearly labelled as assumption-based or rule-implied.
