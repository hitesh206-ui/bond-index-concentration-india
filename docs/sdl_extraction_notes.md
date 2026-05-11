# SDL extraction notes

## Purpose

This note tracks extraction for State Development Loan indices in the project.

## Priority SDL indices

### BICI004 - Nifty 3 Year SDL

Index page:

- https://www.niftyindices.com/indices/fixed-income/sdl-indices/nifty-3-year-sdl

Current working rule:

- Three states or Union Territories are selected.
- Selected state or UT exposures are treated as approximately equal-weighted unless official weights indicate otherwise.
- Approximate state issuer exposure: 1/3 each.

### BICI005 - Nifty 5 Year SDL

Index page:

- https://www.niftyindices.com/indices/fixed-income/sdl-indices/nifty-5-year-sdl

Current working rule:

- Three states or Union Territories are selected.
- Selected state or UT exposures are treated as approximately equal-weighted unless official weights indicate otherwise.
- Approximate state issuer exposure: 1/3 each.

### BICI006 - NIFTY 10 Year SDL Index

Index page:

- https://www.niftyindices.com/indices/fixed-income/sdl-indices/nifty-10-year-sdl-index

Current working rule:

- Top 14 states are selected based on previous-year primary issuance volume.
- Exact weighting rule remains to be verified from official portfolio or methodology source.

### BICI010 - Nifty SDL Dec 2028 Index

Index page:

- https://www.niftyindices.com/indices/fixed-income/target-maturity-index/nifty-sdl-dec-2028-index

Current working rule:

- 13 states or Union Territories are selected.
- Public description indicates equal exposure across selected state or UT issuers.
- Approximate state issuer exposure: 1/13 each.

## Required constituent fields

For every SDL constituent row, capture:

- date
- index_id
- security_name
- ISIN
- issuer_name as state or Union Territory name
- weight, if available
- maturity_date, if available
- coupon, if available
- rating, if available
- source_file
- remarks

## Sector and group mapping

SDL issuers should be mapped as:

- ownership_type: State government / Union Territory
- sector: State development loans
- sub_sector: SDL issuer
- issuer_group: State or Union Territory name

## Research role

SDL indices are useful for showing that fixed-income benchmarks can be concentrated not only by corporate issuer or sector, but also by state issuer exposure.

## Limitation

Observed SDL concentration should not be finalized unless official constituent weights are verified. Equal-weight assumptions should be labelled as rule-implied or methodology-based scenarios.
