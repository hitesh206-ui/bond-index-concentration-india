# Results template

## 1. Coverage classification results

This section will report how many indices fall into each coverage category:

- Full coverage
- Partial coverage
- Methodology-cap-only coverage
- Insufficient coverage

Suggested table:

| Coverage class | Number of indices | Share of sample | Interpretation |
|---|---:|---:|---|
| Full | To be filled | To be filled | Observed weighted concentration possible |
| Partial | To be filled | To be filled | Constituent-only analysis possible |
| Methodology-cap-only | To be filled | To be filled | Rule-implied scenario analysis possible |
| Insufficient | To be filled | To be filled | No concentration estimate reported |

## 2. Constituent-only concentration evidence

This section will use visible issuer information from `data/raw/constituents.csv`.

Suggested tables:

1. Visible issuer count by index segment
2. Issuer recurrence across duration buckets
3. Ownership-type mix
4. Sector mix
5. Group clustering summary

Possible interpretation:

> The visible issuer set suggests that several Indian bond index families are concentrated in recurring government-linked financial institutions, public-sector undertakings, public-sector banks, private banks, and infrastructure-finance entities.

## 3. Rule-implied concentration scenarios

This section will report scenario results from `data/interim/cap_based_scenarios.csv`.

Suggested table:

| Scenario | Index | Assumption | Rule-implied HHI | Effective issuers | Top-3 weight | Top-5 weight |
|---|---|---|---:|---:|---:|---:|
| To be filled | To be filled | To be filled | To be filled | To be filled | To be filled | To be filled |

Important wording:

> These scenario results are not observed portfolio concentrations. They represent assumption-based or rule-implied estimates under incomplete disclosure.

## 4. Observed weighted concentration results

This section will be completed only after official weights are available.

Suggested tables:

1. Issuer-level HHI by index
2. Group-level HHI by index
3. Sector-level HHI by index
4. Top-3/5/10 issuer concentration
5. Effective number of issuers, groups, and sectors

If weights remain unavailable, this section should state:

> Observed weighted concentration is not reported for partially disclosed indices because official constituent weights were unavailable. The paper therefore reports constituent-only and rule-implied evidence separately.

## 5. Policy and disclosure interpretation

This section will connect empirical findings to benchmark transparency and index governance.

Potential conclusions:

- Security count alone may overstate diversification in fixed-income benchmarks.
- Issuer-level caps may not eliminate group or sector concentration.
- G-sec indices can be diversified across securities but concentrated in one sovereign issuer.
- SDL indices can diversify across states but may still rely on a small number of state issuers.
- Partial portfolio disclosure limits investors' ability to measure benchmark concentration directly.

## 6. Robustness and limitations

This section will explain:

- observed results are reported only where weights are verified
- scenario results are separated from observed results
- issuer mapping involves judgement and is documented in `issuer_mapping.csv`
- incomplete PDF extraction remains a data limitation
- future work can update the dataset as index providers release more portfolio details
