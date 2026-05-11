# Data collection log

## Current extraction status

### BICI007 - NIFTY AAA Corporate Bond Indices

Status: constituent names and ISINs partially entered; weights pending.

Source recorded:

- https://www.niftyindices.com/Portfolio/Portfolio_NIFTY_AAA_Corporate_Bond_Indices.pdf
- https://www.niftyindices.com/Factsheet/Factsheet_NIFTY_AAA_Corporate_Bond_Indices.pdf

Public search snippets confirm that the NIFTY AAA Corporate Bond Indices are rebalanced and reconstituted quarterly and that issuer-level weights are capped at 10 percent. However, the available tool extraction did not expose reliable constituent weights from the PDF.

Action required:

1. Manually download the official portfolio PDF from the Nifty Indices page.
2. Open the PDF locally or convert it to Excel/CSV.
3. Extract the weight column for each constituent.
4. Enter weights as decimals in `data/raw/constituents.csv`.
5. Keep the original PDF in a local archive or upload a permissible copy if redistribution is allowed.

## Research integrity rule

Do not calculate issuer HHI, group HHI, top issuer weights, or effective number of issuers until portfolio weights are verified from source documents.

## Recommended extraction order

1. BICI007 - NIFTY AAA Corporate Bond Indices
2. BICI009 - NIFTY Banking & PSU Bond Indices
3. BICI010 - Nifty SDL Dec 2028 Index
4. BICI004 - Nifty 3 Year SDL
5. BICI005 - Nifty 5 Year SDL
