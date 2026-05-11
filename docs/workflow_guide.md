# Workflow guide

## Step 1: Update source inventory

Before entering new data, add the source to:

```text
data/raw/source_inventory.csv
```

Record the source type, URL, extraction status, and priority.

## Step 2: Add index metadata

If the index is not already in the sample, add it to:

```text
data/raw/index_master.csv
```

Required fields include index ID, index name, provider, category, coverage type, and methodology source.

## Step 3: Record coverage status

Add or update the index in:

```text
data/raw/coverage_log.csv
```

Use one of the following coverage types:

- Full
- Partial
- Methodology-cap-only
- Insufficient

## Step 4: Add methodology caps

If the index methodology has issuer, sector, group, rating, or other caps, record them in:

```text
data/raw/methodology_caps.csv
```

Use decimal form. For example, a 10 percent issuer cap should be entered as `0.10`.

## Step 5: Enter constituents

Enter each constituent row in:

```text
data/raw/constituents.csv
```

Minimum required fields:

- date
- index_id
- security_name
- isin
- issuer_name
- weight, if available
- rating, if available
- source_file
- remarks

If weights are missing, leave the weight field blank and clearly state that weights are unavailable in the remarks field.

## Step 6: Map issuers

For every new issuer, add a row to:

```text
data/raw/issuer_mapping.csv
```

Map the issuer to:

- standardized issuer name
- issuer group
- ownership type
- sector
- sub-sector
- mapping confidence
- mapping source

## Step 7: Validate the dataset

Run:

```bash
python src/validate_data.py
```

This creates:

```text
outputs/tables/data_validation_report.csv
```

## Step 8: Run scenario analysis

For cap-based and assumption-based rows, run:

```bash
python src/analyze_cap_scenarios.py
```

This creates:

```text
outputs/tables/cap_based_scenario_summary.csv
```

## Step 9: Run observed concentration analysis

Only run this after verified numeric weights are entered:

```bash
python src/analyze_observed_concentration.py
```

This creates:

```text
outputs/tables/observed_concentration_results.csv
```

## Step 10: Generate figures

Run:

```bash
python src/generate_figures.py
```

Figures are saved in:

```text
outputs/figures/
```

## Research integrity warning

Never mix observed concentration results with scenario-based results unless the table clearly labels which values are observed and which values are assumption-based.
