# BICI009 Banking & PSU Bond Indices extraction notes

## Index family

BICI009 refers to the NIFTY Banking & PSU Bond Indices family.

Official portfolio source identified:

- https://www.niftyindices.com/Portfolio/NIFTY_Banking_and_PSU_Bond_Indices_Portfolio.pdf

Official factsheet source:

- https://www.niftyindices.com/Factsheet/Factsheet_NIFTY_BankingPSU_Bond_Indices.pdf

Official index page:

- https://www.niftyindices.com/indices/fixed-income/corporate-bond-indices/nifty-banking-psu-bond-indices

## Publicly verified characteristics

The index family measures Banking and PSU bonds across six Macaulay duration buckets and one aggregate debt index.

The index family is rebalanced and reconstituted quarterly.

The portfolio source states that issuer-level weights are capped at 10 percent.

## Sub-indices to capture

- NIFTY Banking & PSU Ultra Short Duration Bond Index
- NIFTY Banking & PSU Low Duration Bond Index
- NIFTY Banking & PSU Short Duration Bond Index
- NIFTY Banking & PSU Medium Duration Bond Index
- NIFTY Banking & PSU Medium to Long Duration Bond Index
- NIFTY Banking & PSU Long Duration Bond Index
- NIFTY Banking & PSU Debt Index

The index family also has A, B, and C variants. These should be treated as separate sample entries only if the paper expands beyond the initial 18-25 core-index sample.

## Data extraction status

As of this note, the public source path has been identified, but constituent rows and weights have not been entered.

## Required fields for `data/raw/constituents.csv`

For each row, capture:

- date
- index_id = BICI009
- security_name = exact sub-index name
- ISIN
- issuer_name
- weight, if shown
- maturity_date, if shown
- coupon, if shown
- rating, if shown
- source_file
- remarks

## Research integrity rule

Do not calculate observed HHI for BICI009 until actual portfolio weights are available. If only issuer names are available, enter constituent-only rows and mark weights as blank.
