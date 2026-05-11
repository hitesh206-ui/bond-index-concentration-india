# Coverage-aware framework draft

## Motivation

Fixed-income benchmark concentration cannot always be measured using a single observed-weight approach because index disclosure varies across index families. Some benchmarks disclose constituent names and portfolio weights, while others disclose only constituents, methodology rules, issuer caps, factsheet summaries, or partial extracts.

This creates a measurement problem. If the study includes only fully disclosed indices, the sample may become too narrow and may exclude economically important benchmark families. If the study treats incomplete data as complete, the results may overstate empirical precision. This paper therefore adopts a coverage-aware framework that separates observed weighted evidence from constituent-only and rule-implied evidence.

## Framework

The framework classifies every index observation into one of three usable evidence categories.

### Observed weighted concentration

Observed weighted concentration is calculated only where official constituent weights are available. These observations support direct calculation of issuer HHI, group HHI, sector HHI, top exposure weights, and effective number measures.

### Constituent-only concentration evidence

Constituent-only evidence is used where issuer names are available but weights are missing. These observations do not support observed HHI, but they can still reveal economically meaningful patterns such as repeated issuers across duration buckets, clustering in government-linked financial institutions, public-sector undertakings, banks, state issuers, or sovereign-linked borrowers.

### Rule-implied concentration scenarios

Rule-implied scenarios are used where methodology rules are observable. Examples include issuer-cap rules, rating-sensitive caps, or equal-state structures in state development loan indices. These scenarios are not observed portfolio results. They are used to interpret the concentration implications of index construction rules under incomplete disclosure.

## Research contribution

The framework contributes to fixed-income benchmark analysis in three ways.

First, it avoids treating missing benchmark weights as randomly missing. Instead, disclosure availability is recorded as an explicit feature of the dataset.

Second, it recognizes that bond index concentration is multidimensional. A benchmark may be diversified across securities but concentrated by issuer, issuer group, ownership type, sector, state, or sovereign exposure.

Third, it separates measurement precision from economic interpretation. Observed weighted results provide the strongest empirical evidence. Constituent-only and rule-implied results provide lower-precision but still useful evidence about potential concentration channels.

## Reporting convention

All tables and figures should identify the evidence type used:

- Observed weighted concentration
- Constituent-only concentration evidence
- Rule-implied concentration scenario

The paper should not mix observed and scenario-based values without explicit labels.

## Interpretation

The framework allows the paper to make careful statements such as:

> Where official weights are available, concentration is measured directly. Where weights are unavailable, the paper reports constituent-only and rule-implied evidence separately, highlighting both concentration channels and disclosure limitations.

This strengthens the paper because incomplete disclosure becomes part of the research question rather than a weakness hidden in the methodology.
