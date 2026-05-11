# Project roadmap

## Current project status

The repository has been initialized with research documentation, data templates, starter Python modules, a pilot index sample, pilot constituent rows for BICI007, issuer mapping, and cap-based concentration scenarios.

## Completed

- Repository initialized
- README expanded with research scope
- Data templates created
- Pilot index sample added
- Coverage log added
- Methodology cap table added
- Pilot AAA constituent universe added from user-extracted source text
- Issuer mapping added for pilot issuers
- Cap-based scenario dataset added
- Scenario interpretation documentation added
- GitHub issues created for sample construction and weight extraction

## Still left

### 1. Source-weight extraction

Observed concentration cannot be calculated until official index weights are obtained.

Priority files:

1. NIFTY AAA Corporate Bond Indices
2. NIFTY Banking & PSU Bond Indices
3. Nifty SDL Dec 2028 Index
4. Nifty 3 Year SDL
5. Nifty 5 Year SDL

Required work:

- Download or copy official portfolio files
- Extract constituent weights
- Enter weights as decimals in `data/raw/constituents.csv`
- Record the source file or URL for every row
- Mark manual extraction assumptions in remarks

### 2. Expand sample

The pilot sample currently has 10 index entries. The target sample is 18-25 indices.

Potential additions:

- Additional G-sec maturity buckets
- Additional SDL maturity buckets
- AA and AA- corporate bond index families
- Banking and PSU variants
- Target maturity government or PSU bond indices
- Money market fixed-income indices, if coverage is sufficient

### 3. Complete issuer mapping

For every new constituent issuer:

- Standardize issuer name
- Map issuer group
- Classify ownership type
- Classify sector and sub-sector
- Assign mapping confidence
- Record source

### 4. Run observed concentration analysis

After weights are available:

- Issuer HHI
- Group HHI
- Sector HHI
- Top-1, Top-3, Top-5, and Top-10 issuer weights
- Effective number of issuers, groups, and sectors

### 5. Compare observed results with cap-based scenarios

Use cap-based scenarios only as rule-implied or assumption-based benchmarks.

Do not mix observed and scenario-based results in the same result table without clear labels.

### 6. Generate figures

Planned figures:

- Issuer HHI by index
- Effective number of issuers by index
- Top-5 issuer concentration by index
- Group HHI vs issuer HHI
- Sector concentration heatmap
- Coverage-quality dashboard

### 7. Draft paper sections

Recommended writing order:

1. Data and sample
2. Methodology
3. Coverage-aware framework
4. Preliminary scenario results
5. Literature review
6. Introduction
7. Policy implications
8. Conclusion

## Immediate next tasks

1. Extract actual weights from official portfolio files.
2. Add BICI009 Banking & PSU constituents.
3. Add BICI010 SDL Dec 2028 constituents.
4. Run first observed concentration table once weights are available.
