# Data dictionary

## index_master.csv

| Column | Description |
|---|---|
| index_id | Unique project identifier for each index |
| index_name | Official index name |
| provider | Index provider |
| index_category | G-sec, SDL, corporate bond, banking and PSU, target maturity, money market, or other |
| duration_bucket | Duration or maturity category where applicable |
| rating_bucket | Rating category where applicable |
| rebalance_frequency | Rebalance frequency stated in the methodology |
| methodology_source | Source document or URL for index rules |
| coverage_type | Full, Partial, Methodology-cap-only, or Insufficient |
| remarks | Notes on classification or data issues |

## constituents.csv

| Column | Description |
|---|---|
| date | Observation date |
| index_id | Index identifier matching index_master.csv |
| security_name | Security or bond name |
| isin | Security ISIN where available |
| issuer_name | Raw issuer name |
| weight | Index weight as a decimal, not percent |
| maturity_date | Bond maturity date |
| coupon | Coupon rate where available |
| rating | Credit rating where available |
| source_file | Source file or source URL |
| remarks | Notes on assumptions or data quality |

## issuer_mapping.csv

| Column | Description |
|---|---|
| issuer_name | Raw issuer name from constituent file |
| standardized_issuer_name | Cleaned issuer name |
| issuer_group | Corporate group, public-sector cluster, sovereign, or other economic group |
| ownership_type | Sovereign, state government, PSU, private, municipal, or other |
| sector | Main sector classification |
| sub_sector | More detailed sector classification |
| mapping_confidence | High, Medium, or Low |
| mapping_source | Source used for classification |
| remarks | Notes on judgement calls |
