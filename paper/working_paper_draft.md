# Concentration in Indian Bond Indices: A Coverage-Aware Analysis of Issuer, Group, and Sectoral Risk

## Abstract

This paper studies concentration in Indian fixed-income benchmarks using a coverage-aware framework. Bond index concentration is measured across issuer, group, and sector dimensions. The framework distinguishes observed weighted concentration from constituent-only evidence and rule-implied concentration scenarios. This distinction is necessary because public disclosure differs across Indian bond index families: some sources provide constituent weights, while others provide only constituent names, methodology rules, issuer caps, or partial index factsheet information. The paper argues that security count alone can overstate diversification in fixed-income benchmarks. Indian bond indices may be diversified across securities or duration buckets while remaining concentrated in sovereign, state-government, public-sector, banking, development-finance, or infrastructure-finance exposures. The study contributes a replicable framework for measuring concentration under incomplete disclosure and provides preliminary evidence on concentration channels in Indian bond benchmarks.

## 1. Introduction

Fixed-income benchmarks play an increasingly important role in portfolio construction, passive investing, product design, and performance evaluation. In equity markets, benchmark concentration is often discussed through the dominance of large constituents or sectors. In bond markets, however, concentration is more complex. A bond index may contain many securities while still being exposed to a small number of issuers, issuer groups, sovereign entities, public-sector borrowers, banks, or state governments.

This distinction is particularly important in Indian fixed-income benchmarks. Indian bond indices span government securities, state development loans, corporate bonds, banking and public-sector undertaking bonds, target maturity indices, and money-market instruments. These index families differ not only in duration, credit rating, and issuer type, but also in the extent to which constituent and weight information is publicly available.

This paper studies concentration in Indian bond indices using a coverage-aware framework. The framework distinguishes between three types of evidence: observed weighted concentration, constituent-only concentration evidence, and rule-implied concentration scenarios. Observed weighted concentration is calculated only when official constituent weights are available. Constituent-only evidence is used when issuer names are available but weights are missing. Rule-implied scenarios are used when methodology rules, issuer caps, or equal-weight structures are available but observed weights are unavailable.

The paper focuses on issuer, group, and sectoral concentration. Issuer-level analysis captures direct exposure to individual borrowers. Group-level analysis captures economic concentration when different issuers are linked through corporate groups, public-sector ecosystems, government ownership, or development finance structures. Sectoral analysis captures broader exposure to sovereign, state government, banking, financial institution, infrastructure finance, utilities, and public-sector categories.

The study is motivated by a central measurement problem: fixed-income benchmark diversification cannot be assessed by security count alone. A government securities index may hold several securities while having one sovereign issuer. A state development loan index may hold multiple state issuers but still be exposed to a small subset of state governments. A corporate bond index may be diversified across securities but dominated by government-linked financial institutions, public-sector undertakings, infrastructure finance entities, or banks.

The paper makes three contributions. First, it introduces a coverage-aware framework for measuring benchmark concentration under uneven public disclosure. Second, it applies issuer, group, and sectoral concentration measures to Indian fixed-income benchmarks. Third, it distinguishes observed weighted results from constituent-only and rule-implied evidence, avoiding unsupported empirical claims when official weights are unavailable.

## 2. Indian bond index landscape and sample

The study focuses on Indian fixed-income benchmark indices. The target sample consists of approximately 18 to 25 indices across sovereign, state development loan, corporate bond, banking and PSU, target maturity, and money-market index categories, subject to public data availability.

The initial pilot sample includes government securities indices, state development loan indices, corporate bond index families, banking and PSU bond indices, and target maturity SDL indices. The pilot sample is designed to capture variation across sovereign concentration, state issuer concentration, corporate issuer concentration, banking exposure, public-sector exposure, and development-finance exposure.

The main data files are organized into index metadata, constituent records, issuer mapping, methodology caps, coverage logs, source inventory, cap-based scenarios, and sample expansion trackers.

## 3. Coverage-aware framework

Fixed-income benchmark concentration cannot always be measured using a single observed-weight approach because index disclosure varies across index families. Some benchmarks disclose constituent names and portfolio weights, while others disclose only constituents, methodology rules, issuer caps, factsheet summaries, or partial extracts.

The framework classifies every index observation into three usable evidence categories.

### 3.1 Observed weighted concentration

Observed weighted concentration is calculated only where official constituent weights are available. These observations support direct calculation of issuer HHI, group HHI, sector HHI, top exposure weights, and effective number measures.

### 3.2 Constituent-only concentration evidence

Constituent-only evidence is used where issuer names are available but weights are missing. These observations do not support observed HHI, but they can still reveal economically meaningful patterns such as repeated issuers across duration buckets, clustering in government-linked financial institutions, public-sector undertakings, banks, state issuers, or sovereign-linked borrowers.

### 3.3 Rule-implied concentration scenarios

Rule-implied scenarios are used where methodology rules are observable. Examples include issuer-cap rules, rating-sensitive caps, or equal-state structures in state development loan indices. These scenarios are not observed portfolio results. They are used to interpret the concentration implications of index construction rules under incomplete disclosure.

## 4. Methodology

The base unit of analysis is an index-security observation. Each security is mapped to an issuer, issuer group, ownership type, sector, and sub-sector.

The main concentration metric is the Herfindahl-Hirschman Index:

```text
HHI = sum(w_i^2)
```

where `w_i` is the decimal portfolio weight of issuer, group, or sector `i`.

The effective number of issuers, groups, or sectors is calculated as:

```text
Effective number = 1 / HHI
```

The study also calculates Top-1, Top-3, Top-5, and Top-10 exposure weights where weights are available. For partial-disclosure indices, the paper reports visible issuer counts, issuer recurrence, ownership-type clustering, sector clustering, and rule-implied scenarios.

## 5. Preliminary constituent-only evidence

The preliminary constituent-only dataset suggests that several Indian bond index families are concentrated in recurring government-linked financial institutions, public-sector undertakings, public-sector banks, private banks, infrastructure-finance entities, and development-finance institutions.

For BICI007, the visible AAA corporate bond constituent universe includes issuers such as NABARD, National Housing Bank, Power Finance Corporation, REC, SIDBI, EXIM Bank, and Indian Railway Finance Corporation. For BICI009, the visible Banking and PSU index universe includes private banks, public-sector banks, public-sector undertakings, and infrastructure-linked public-sector issuers.

These findings do not represent observed portfolio-weight concentration. They show that visible issuer identity and recurrence are informative even before official portfolio weights are obtained.

## 6. Rule-implied concentration scenarios

The scenario file separates rule-implied and equal-weight assumptions from observed data. Existing scenarios include equal-weight visible-issuer scenarios for AAA corporate bond buckets, issuer-cap floor scenarios for AAA corporate bonds, equal-state scenarios for SDL indices, and visible-issuer scenarios for the Banking and PSU index family.

These scenario results are not observed portfolio concentrations. They represent assumption-based or rule-implied estimates under incomplete disclosure.

## 7. Observed weighted concentration results

This section will be completed only after official portfolio weights are available. Observed issuer HHI, group HHI, sector HHI, top exposure weights, and effective number measures will be reported only for indices with verified numeric weights.

If official weights remain unavailable for certain indices, those indices will remain in the constituent-only or rule-implied categories.

## 8. Discussion and policy implications

The preliminary evidence supports the claim that fixed-income benchmark diversification cannot be evaluated by security count alone. Several Indian bond benchmarks may be diversified across securities or duration buckets but economically concentrated in government-linked issuer groups, public-sector financial institutions, banks, infrastructure-finance companies, sovereign debt, or state-government issuers.

Issuer caps may reduce single-issuer dominance but may not eliminate group-level or sectoral concentration. A benchmark can comply with issuer caps while still having material exposure to public-sector ecosystems, banking-sector risk, or government-linked borrowers.

The coverage-aware framework also highlights a disclosure issue. If official weights are not readily available, investors cannot independently calculate weighted issuer HHI, group HHI, sector HHI, or effective number of issuers. In that case, partial-disclosure evidence and rule-implied scenarios can improve transparency, but they cannot replace observed weighted analysis.

## 9. Limitations

This study relies on publicly available sources. The most important limitation is the availability of official portfolio weights. Observed concentration metrics are reported only where official weights are available. For partially disclosed indices, the paper reports constituent-only evidence and rule-implied scenarios separately.

Issuer-group and sector mapping involve judgement. Mapping decisions are documented in the issuer mapping file, including source notes and mapping confidence.

Scenario results are not observed portfolio results. They are used to interpret the concentration implications of index methodology rules under incomplete disclosure.

## 10. Conclusion

This paper proposes a coverage-aware framework for measuring issuer, group, and sectoral concentration in Indian fixed-income benchmarks. The framework separates observed weighted concentration from constituent-only evidence and rule-implied concentration scenarios. This distinction allows the study to proceed without overstating empirical precision when portfolio weights are missing.

The preliminary evidence suggests that Indian bond benchmark concentration is multidimensional. Security-level diversification may coexist with issuer, group, sector, sovereign, public-sector, banking, development-finance, or state-government concentration. Future updates to the dataset can add observed weighted results as more official portfolio data becomes available.
