# Missing and blocked data strategy

## Purpose

This document explains how the project handles missing constituent rows, missing weights, partial portfolio extracts, and methodology-cap-only information.

The goal is to preserve research integrity while still allowing useful preliminary analysis.

## Current blocked items

Observed concentration analysis is blocked because official portfolio weights are not yet available for the entered constituent rows.

Blocked observed metrics include:

- Observed issuer HHI
- Observed group HHI
- Observed sector HHI
- Observed Top-1, Top-3, Top-5, and Top-10 issuer weights
- Observed effective number of issuers
- Observed effective number of groups
- Observed effective number of sectors

## What can be done without weights

### 1. Constituent-count analysis

Allowed:

- Count visible issuers per index segment
- Count unique issuers across index families
- Count recurring issuers across duration buckets
- Identify issuer-type clustering, such as PSU, private bank, public sector bank, sovereign, or SDL issuer

Not allowed:

- Presenting constituent counts as portfolio-weighted diversification

### 2. Rule-implied cap analysis

Allowed:

- Use official issuer caps to create methodology-based concentration scenarios
- Use equal-weight assumptions only when explicitly labelled as scenarios
- Compare cap-based floors across index types

Not allowed:

- Presenting cap-based HHI as actual observed HHI

### 3. Coverage-aware disclosure analysis

Allowed:

- Classify indices into Full, Partial, Methodology-cap-only, or Insufficient coverage
- Compare data availability across index families
- Discuss how missing weights limit investor transparency

Not allowed:

- Treating missing data as randomly missing without justification

## How to handle missing weights

### Preferred treatment

Leave the weight field blank in `data/raw/constituents.csv` until the official weight is verified.

### Acceptable alternatives

If official weights are unavailable, create a separate scenario row in:

```text
data/interim/cap_based_scenarios.csv
```

The scenario must clearly state the assumption, such as:

- equal-weight visible issuer scenario
- issuer-cap floor scenario
- rule-implied state exposure scenario

### Prohibited treatment

Do not enter guessed weights in `data/raw/constituents.csv`.

Do not infer actual weights from issuer caps unless the source explicitly states that the index is equal-weighted or cap-weighted.

## Manual extraction protocol

When downloading or copying official source tables manually:

1. Record the source URL in `data/raw/source_inventory.csv`.
2. Copy the exact visible table into a temporary working file or note.
3. Enter each row in `data/raw/constituents.csv`.
4. Enter weights as decimals, not percentages.
5. Add `Manual extraction from official source` in the remarks field.
6. Record whether the source showed weights or only constituents.
7. Preserve the original source file locally for auditability.

## PDF extraction options

If a PDF table is available but difficult to extract:

1. Try copying text directly from the browser PDF viewer.
2. Try opening the PDF in Adobe Acrobat or a browser and exporting to Excel.
3. Try uploading the PDF to ChatGPT for table extraction.
4. Try using Tabula, Camelot, or Excel Power Query.
5. If all automated extraction fails, manually enter the rows and document this in remarks.

## Treatment in the paper

Use the following language for missing weights:

> Observed concentration metrics are reported only where official constituent weights are available. For partially disclosed indices, the paper reports constituent-only and methodology-cap-based scenarios separately from observed weighted results.

Use the following language for cap-based scenarios:

> Scenario results are not observed portfolio concentrations. They are used to interpret the concentration implications of index methodology rules under incomplete disclosure.

## Decision table

| Data situation | Action | Output allowed |
|---|---|---|
| Constituents and weights available | Enter full rows | Observed HHI and observed top weights |
| Constituents available but weights missing | Enter rows with blank weights | Constituent-count and equal-weight scenario only |
| Only issuer cap known | Enter cap rule | Rule-implied scenario only |
| Only index name known | Record in source tracker | No concentration result |
| Source inaccessible | Record blocker | No observed result |

## Current recommendation

Proceed with two parallel tracks:

1. Continue building constituent-only coverage for BICI007, BICI009, and SDL indices.
2. Keep observed concentration analysis blocked until official weights are obtained.

This allows the paper to develop the coverage-aware framework while avoiding unsupported empirical claims.
