# Data and sample draft

## Sample construction

The study focuses on Indian fixed-income benchmark indices. The target sample consists of approximately 18 to 25 indices across sovereign, state development loan, corporate bond, banking and PSU, target maturity, and money-market index categories, subject to public data availability.

The initial pilot sample includes 10 index entries:

1. Nifty Composite G-sec Index
2. Nifty 4-8 yr G-Sec
3. Nifty 8-13 yr G-Sec
4. Nifty 3 Year SDL
5. Nifty 5 Year SDL
6. NIFTY 10 Year SDL Index
7. NIFTY AAA Corporate Bond Indices
8. NIFTY AA+ Corporate Bond Indices
9. NIFTY Banking & PSU Bond Indices
10. Nifty SDL Dec 2028 Index

## Index categories

The pilot sample is designed to capture variation across three major concentration channels.

### Sovereign concentration

Government securities indices provide a benchmark case where security-level diversification may exist but issuer-level diversification is limited because the issuer is the Government of India.

### State issuer concentration

State development loan indices allow concentration to be measured across state and Union Territory issuers.

### Corporate and public-sector concentration

Corporate bond and Banking & PSU indices allow measurement of issuer-level, group-level, and sector-level concentration across financial institutions, public-sector undertakings, infrastructure finance companies, and private corporate issuers.

## Data sources

The project uses publicly accessible sources, including:

- Nifty Indices index pages
- Nifty Indices factsheets
- Nifty Indices portfolio files
- Index methodology documents
- Issuer annual reports and official issuer websites
- Public shareholding and ownership disclosures where needed for issuer mapping

No Bloomberg, Refinitiv, WRDS, or other paid institutional databases are required.

## Data files

The main dataset is organized across the following files:

- `data/raw/index_master.csv`
- `data/raw/constituents.csv`
- `data/raw/issuer_mapping.csv`
- `data/raw/methodology_caps.csv`
- `data/raw/coverage_log.csv`
- `data/raw/source_inventory.csv`
- `data/interim/cap_based_scenarios.csv`
- `data/interim/sample_expansion_tracker.csv`

## Coverage classification

Each index is classified as Full, Partial, Methodology-cap-only, or Insufficient.

Full coverage requires constituent names and portfolio weights. Partial coverage captures cases where constituents are visible but weights are missing or incomplete. Methodology-cap-only coverage captures cases where portfolio data is unavailable but index rules such as issuer caps are public.

## Current data limitation

At the current stage, BICI007 has visible constituent rows from the NIFTY AAA Corporate Bond Indices source text, but observed portfolio weights are not yet available. As a result, the project can run constituent-only and cap-based scenario analysis, but not observed HHI for BICI007.

## Planned sample expansion

The next priority is to add constituent data for:

1. NIFTY Banking & PSU Bond Indices
2. Nifty SDL Dec 2028 Index
3. Nifty 3 Year SDL
4. Nifty 5 Year SDL
5. Additional corporate bond rating buckets

## Weight treatment

Weights must be entered as decimals. For example, a 10 percent index weight must be entered as `0.10`.

Observed concentration results will be calculated only for rows with verified numeric weights.
