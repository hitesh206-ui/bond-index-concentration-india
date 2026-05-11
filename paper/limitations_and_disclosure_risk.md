# Limitations and disclosure-risk section draft

## Data limitations

This study relies on publicly available index pages, factsheets, portfolio files, methodology documents, and issuer-level public disclosures. The use of public data improves replicability, but it also creates limitations because constituent and weight disclosure is not uniform across index families.

The most important limitation is the availability of portfolio weights. Observed issuer, group, and sectoral concentration measures require official constituent weights. Where such weights are unavailable, the paper does not estimate observed HHI. Instead, it reports constituent-only evidence and rule-implied scenarios separately.

## Partial-disclosure problem

Partial disclosure is not treated as a minor data inconvenience. It is part of the research problem. Benchmark users may be able to identify the securities or issuers in an index but may not always be able to calculate exact portfolio concentration without constituent weights.

This limitation matters because index concentration is a portfolio-weighted concept. Issuer count alone may understate or overstate true concentration depending on how weights are distributed.

## Scenario limitations

Rule-implied and equal-weight scenarios are not observed portfolio results. They are used to interpret the concentration implications of index methodology rules when observed weights are unavailable.

For example, a 10 percent issuer cap provides information about maximum issuer exposure but does not reveal actual weights. Similarly, an equal-weight visible-issuer scenario can show mechanical concentration under a simple assumption, but it cannot replace official portfolio-weight data.

## Issuer mapping limitations

Issuer-group and sector mapping involve judgement. The study documents mapping decisions in `data/raw/issuer_mapping.csv`, including mapping confidence and source notes. Some entities may have complex ownership structures, government links, listed subsidiaries, or changing control relationships. These cases are marked for verification where necessary.

## Generalizability

The initial sample focuses on Indian bond indices with publicly accessible information. Results should be interpreted in the context of the available sample and coverage classification. As additional index files become available, the dataset can be expanded and observed concentration results can be updated.

## Disclosure-risk interpretation

Missing or partial portfolio-weight disclosure creates a benchmark transparency issue. Investors may know that an index has issuer caps or visible constituents, but without weights they cannot independently calculate issuer HHI, group HHI, sector HHI, top issuer exposures, or effective number of issuers.

This paper therefore treats disclosure coverage as an analytical variable. A benchmark with incomplete public weight disclosure is not automatically excluded from the study, but its results are classified according to the level of evidence available.

## Reviewer-facing limitation statement

A concise limitation statement for the paper is:

> Observed weighted concentration metrics are reported only where official constituent weights are available. For partially disclosed indices, the paper reports constituent-only evidence and rule-implied concentration scenarios separately. These scenario results are not treated as observed portfolio concentration, but as evidence on the concentration implications of index methodology and partial disclosure.
