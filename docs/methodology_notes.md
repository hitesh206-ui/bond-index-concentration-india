# Methodology notes

## Concentration metrics

The project will calculate concentration at issuer, group, and sector levels.

### Herfindahl-Hirschman Index

HHI is calculated as the sum of squared portfolio weights:

```text
HHI = sum(weight_i^2)
```

Weights should be expressed as decimals before squaring. For example, a 10% issuer weight should be entered as 0.10.

### Effective number

The effective number of issuers, groups, or sectors is calculated as:

```text
Effective number = 1 / HHI
```

This converts concentration into an intuitive diversification measure.

### Top issuer weights

The project will calculate Top-1, Top-3, Top-5, and Top-10 issuer weights for each index.

## Unit of observation

The base unit is index-security-date. Securities are then aggregated to issuer, group, and sector levels.

## Data treatment

All reported concentration metrics must clearly state whether they are based on full coverage, partial coverage, or methodology-cap-only information.
