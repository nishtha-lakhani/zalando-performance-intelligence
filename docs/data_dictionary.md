# Zalando Corporate Performance Intelligence
# Data Dictionary

This document defines the financial, operating, and analytical metrics used in the Zalando Corporate Performance Intelligence project.

The purpose of the data dictionary is to ensure that metrics are interpreted consistently across historical annual and quarterly reporting periods.

---

# 1. General Data Conventions

## Financial Units

Unless otherwise stated:

- Fields ending in `_eur_m` are stored in EUR millions.
- Fields ending in `_pct` are stored as percentage values.
- Example: `4.8` represents 4.8%, not 0.048.
- Customer and order fields ending in `_m` are stored in millions.
- Employee counts are stored as absolute numbers.
- EPS metrics are stored in EUR per share.

Raw reported values should not be silently rescaled.

---

## Reported vs Calculated Metrics

Metrics directly disclosed by Zalando are stored as reported values in the raw dataset.

Derived analytical metrics such as growth rates, margins, productivity ratios, and cash conversion ratios will generally be calculated programmatically in the processed-data layer.

This allows reported figures to remain separate from our own calculations and enables independent validation.

---

# 2. Reporting Period Fields

## Period

**Field:** `period`

**Definition:** Human-readable identifier for the reporting period.

**Examples:**

- `FY2025`
- `Q1 2026`
- `H1 2026`

---

## Period Type

**Field:** `period_type`

**Definition:** Classification of the reporting period.

**Expected values:**

- `FY` = Full fiscal year
- `Q` = Individual quarter
- `H1` = First half-year
- `9M` = First nine months, where applicable

---

## Year

**Field:** `year`

**Definition:** Fiscal year associated with the observation.

**Example:** `2025`

---

# 3. Growth and Revenue Metrics

## Gross Merchandise Volume (GMV)

**Field:** `gmv_eur_m`

**Full name:** Gross Merchandise Volume

**Unit:** EUR millions

**Definition:** Value of merchandise sold to customers after cancellations and returns and including VAT.

GMV excludes:

- B2B revenues such as ZEOS services
- Partner business commissions
- Retail media revenue
- Service charges such as express delivery fees

These excluded activities may contribute to revenue without contributing to GMV.

**Measurement timing:** GMV is recorded based on the time of the customer's order.

**Important:** Zalando dynamically reports GMV. GMV is retrospectively corrected for cancellations and returns, meaning prior-period GMV values may differ from figures originally published in earlier reports.

**Status:** Reported KPI.

---

## Revenue

**Field:** `revenue_eur_m`

**Unit:** EUR millions

**Definition:** Revenue recognized by the Zalando Group.

Revenue is recorded when control over the relevant goods or services is transferred.

Revenue is not equivalent to GMV.

Certain revenue streams, including B2B services, partner commissions, retail media, and selected service charges, may contribute to revenue while being excluded from GMV.

**Status:** Reported KPI.

---

## B2C Revenue

**Field:** `b2c_revenue_eur_m`

**Unit:** EUR millions

**Definition:** Revenue attributable to Zalando's Business-to-Consumer segment.

The B2C segment includes Zalando's consumer-facing commerce activities and supporting services.

For FY2025 reporting, the B2C segment also includes ABOUT YOU's Commerce business following the acquisition.

**Status:** Reported segment metric.

**Important:** Historical segment definitions must be checked before assuming B2C figures are directly comparable across all years.

---

## B2B Revenue

**Field:** `b2b_revenue_eur_m`

**Unit:** EUR millions

**Definition:** Revenue attributable to Zalando's Business-to-Business segment.

The B2B segment includes products and services offered to brands and retailers, including activities such as:

- ZEOS
- Zalando Fulfilment Solutions (ZFS)
- Multi-channel fulfilment
- SCAYLE
- Tradebyte
- Highsnobiety

**Important:** B2B revenue does not contribute to GMV.

**Status:** Reported segment metric.

---

## Revenue Reconciliation

**Field:** `reconciliation_revenue_eur_m`

**Unit:** EUR millions

**Definition:** Reconciliation adjustments required to bridge segment revenue to consolidated Group revenue.

Conceptually:

`Group Revenue = B2C Revenue + B2B Revenue + Reconciliation`

Reconciliation may include elimination of intersegment revenue.

**Status:** Reported metric.

---

# 4. Profitability Metrics

## EBIT

**Field:** `ebit_eur_m`

**Full name:** Earnings Before Interest and Taxes

**Unit:** EUR millions

**Definition:** Operating earnings before interest and income taxes as reported in Zalando's financial statements.

**Status:** Reported accounting metric.

---

## EBIT Margin

**Field:** `ebit_margin_pct`

**Unit:** Percent

**Formula:**

`EBIT Margin = EBIT / Revenue × 100`

**Interpretation:** Measures accounting operating profit generated per euro of revenue.

**Status:** Reported and independently recalculable.

---

## Adjusted EBIT

**Field:** `adjusted_ebit_eur_m`

**Unit:** EUR millions

**Definition:** Zalando defines Adjusted EBIT as EBIT before:

- equity-settled share-based payment expenses
- restructuring costs
- acquisition-related expenses
- significant non-operating one-time effects

Conceptually:

`Adjusted EBIT = EBIT + Relevant EBIT Adjustments`

**Status:** Zalando management-defined performance measure.

**Important:** Adjusted EBIT should not be treated as identical to accounting EBIT.

---

## Share-Based Payment Adjustment

**Field:** `share_based_payment_adjustment_eur_m`

**Unit:** EUR millions

**Definition:** Equity-settled share-based payment expenses excluded from EBIT when calculating Adjusted EBIT.

**Status:** Reported adjustment.

---

## Acquisition-Related Expense Adjustment

**Field:** `acquisition_related_adjustment_eur_m`

**Unit:** EUR millions

**Definition:** Acquisition-related expenses excluded from EBIT when calculating Adjusted EBIT.

These may include acquisition-related expenses and corresponding amortisation of acquired intangible assets.

**Status:** Reported adjustment.

---

## One-Time Effects Adjustment

**Field:** `one_time_effects_adjustment_eur_m`

**Unit:** EUR millions

**Definition:** Significant non-operating one-time effects excluded from EBIT when calculating Adjusted EBIT.

**Status:** Reported adjustment.

---

## Restructuring Cost Adjustment

**Field:** `restructuring_adjustment_eur_m`

**Unit:** EUR millions

**Definition:** Restructuring expenses excluded from EBIT when calculating Adjusted EBIT.

**Status:** Reported adjustment.

---

## Adjusted EBIT Margin

**Field:** `adjusted_ebit_margin_pct`

**Unit:** Percent

**Formula:**

`Adjusted EBIT Margin = Adjusted EBIT / Revenue × 100`

**Interpretation:** Measures adjusted operating profitability relative to revenue.

**Status:** Reported and independently recalculable.

---

## B2C Adjusted EBIT

**Field:** `b2c_adjusted_ebit_eur_m`

**Unit:** EUR millions

**Definition:** Adjusted EBIT attributable to the B2C segment.

**Status:** Reported segment metric.

---

## B2B Adjusted EBIT

**Field:** `b2b_adjusted_ebit_eur_m`

**Unit:** EUR millions

**Definition:** Adjusted EBIT attributable to the B2B segment.

**Status:** Reported segment metric.

---

## Adjusted EBIT Reconciliation

**Field:** `reconciliation_adjusted_ebit_eur_m`

**Unit:** EUR millions

**Definition:** Reconciliation adjustments required to bridge segment Adjusted EBIT to consolidated Group Adjusted EBIT.

Conceptually:

`Group Adjusted EBIT = B2C Adjusted EBIT + B2B Adjusted EBIT + Reconciliation`

---

## Net Income

**Field:** `net_income_eur_m`

**Unit:** EUR millions

**Definition:** Profit or loss remaining after operating results, financial result, and income taxes.

**Status:** Reported accounting metric.

---

# 5. Customer and Commerce Metrics

## Active Customers

**Field:** `active_customers_m`

**Unit:** Millions of customers

**Basis:** Last Twelve Months (LTM)

**Definition:** Number of customers who placed at least one order during the previous 12 months.

Customers are counted irrespective of returns.

Customers who completely cancelled their orders are excluded.

**Important:** This is a trailing-12-month measure rather than a point-in-time customer count.

**Status:** Reported operating KPI.

---

## Number of Orders

**Field:** `orders_m`

**Unit:** Millions of orders

**Definition:** Number of orders placed by customers during the reporting period, irrespective of cancellations or returns.

Orders placed may differ from orders delivered because orders near the end of the reporting period may still be in transit or subsequently cancelled.

**Status:** Reported operating KPI.

---

## Average GMV per Active Customer

**Field:** `gmv_per_active_customer_eur`

**Unit:** EUR per active customer

**Basis:** Last Twelve Months (LTM)

**Definition:** Average value of merchandise sold to active customers after cancellations and returns and including VAT during the last 12 months of the reporting period.

**Status:** Reported operating KPI.

---

## Average Orders per Active Customer

**Field:** `orders_per_active_customer`

**Unit:** Orders per active customer

**Basis:** Last Twelve Months (LTM)

**Definition:** Number of orders during the last 12 months divided by the number of active customers.

**Status:** Reported operating KPI.

---

## Average Basket Size

**Field:** `average_basket_size_eur`

**Unit:** EUR

**Basis:** Last Twelve Months (LTM)

**Definition:** Average GMV generated per order over the relevant trailing-12-month period.

**Status:** Reported operating KPI.

---

# 6. Investment Metrics

## Capital Expenditure (CapEx)

**Field:** `capex_eur_m`

**Full name:** Capital Expenditure

**Unit:** EUR millions

**Definition:** Zalando defines CapEx as the sum of payments for investments in:

- fixed assets
- intangible assets

excluding payments for the acquisition of companies.

Conceptually:

`CapEx = PP&E Investment Payments + Intangible Asset Investment Payments`

**Status:** Reported KPI.

**Sign convention:** Preserve Zalando's reported sign in the raw dataset. Cash investment outflows may therefore appear as negative values.

---

# 7. Working Capital

## Net Working Capital

**Field:** `net_working_capital_eur_m`

**Unit:** EUR millions

**Definition:** Zalando defines Net Working Capital as:

`Inventories + Trade and Other Receivables - Trade Payables and Similar Liabilities`

**Interpretation:** Measures the net amount of operating capital tied up in inventories and receivables after accounting for financing provided through trade payables and similar liabilities.

A negative Net Working Capital value is not automatically negative for business performance.

For a retailer/platform business, negative working capital may indicate that supplier and other operating liabilities finance part of the operating cycle.

**Status:** Reported metric.

---

# 8. Cash Flow Metrics

## Cash Flow from Operating Activities

**Field:** `operating_cash_flow_eur_m`

**Unit:** EUR millions

**Definition:** Net cash generated or consumed through Zalando's operating activities during the reporting period.

Operating cash flow is influenced by:

- operating earnings
- non-cash expenses
- taxes
- changes in inventories
- changes in receivables
- changes in trade payables
- changes in other operating assets and liabilities

**Status:** Reported accounting metric.

---

## Cash Flow from Investing Activities

**Field:** `investing_cash_flow_eur_m`

**Unit:** EUR millions

**Definition:** Net cash generated or consumed through investing activities.

This can include:

- investments in property, plant and equipment
- investments in intangible assets
- acquisitions
- equity investments
- movements in certain financial assets

**Status:** Reported accounting metric.

---

## Free Cash Flow

**Field:** `free_cash_flow_eur_m`

**Unit:** EUR millions

**Definition:** Zalando calculates Free Cash Flow based on operating cash flow after deducting specified investment cash outflows.

Formula:

`Free Cash Flow =`
`Cash Flow from Operating Activities`
`- Cash Paid for Investments in Property, Plant and Equipment`
`- Cash Paid for Investments in Intangible Assets`
`- Cash Paid for Acquisitions of Shares in Associated Companies / Subsidiaries Less Cash Acquired / Other Equity Investments`

**Important:** Zalando's reported Free Cash Flow therefore includes acquisition-related cash payments.

As a result, reported FCF may be materially affected by M&A activity and should not automatically be interpreted as underlying operating cash generation.

For analytical purposes, the project may later calculate additional cash-generation measures excluding major acquisition payments. Such measures must be clearly labelled as analyst-calculated and must not be presented as Zalando's reported FCF.

**Status:** Reported metric.

---

## Cash and Cash Equivalents

**Field:** `cash_and_equivalents_eur_m`

**Unit:** EUR millions

**Definition:** Cash and highly liquid cash-equivalent assets held at the reporting date.

**Important:** This is a period-end balance rather than a cash-flow measure.

**Status:** Reported accounting metric.

---

# 9. Capital Structure

## Equity Ratio

**Field:** `equity_ratio_pct`

**Unit:** Percent

**Definition:** Equity relative to total assets.

**Formula:**

`Equity Ratio = Equity / Total Assets × 100`

**Interpretation:** Measures the proportion of the asset base financed through equity.

**Status:** Reported and independently recalculable.

---

# 10. Workforce

## Average Number of Employees

**Field:** `average_employees`

**Unit:** Employees

**Definition:** Average number of employees during the relevant reporting period.

**Important:** This is an average-period measure rather than necessarily the number of employees at the reporting date.

Zalando's reported headcount excludes working students, interns, and apprentices where specified.

**Status:** Reported operating metric.

---

# 11. Per-Share Metrics

## Basic Earnings per Share

**Field:** `basic_eps_eur`

**Unit:** EUR per share

**Definition:** Earnings attributable to ordinary shareholders relative to the weighted-average number of ordinary shares outstanding on a basic basis.

**Status:** Reported accounting metric.

---

## Diluted Earnings per Share

**Field:** `diluted_eps_eur`

**Unit:** EUR per share

**Definition:** Earnings per share after accounting for the potential dilutive effect of relevant instruments.

**Status:** Reported accounting metric.

---

# 12. Analyst-Calculated Growth Metrics

The following fields should generally not be manually entered into the raw dataset.

They will be calculated programmatically.

## Revenue YoY Growth

**Field:** `revenue_yoy_pct`

**Formula:**

`(Current Revenue / Prior Comparable Revenue - 1) × 100`

---

## GMV YoY Growth

**Field:** `gmv_yoy_pct`

**Formula:**

`(Current GMV / Prior Comparable GMV - 1) × 100`

---

## Active Customer YoY Growth

**Field:** `active_customers_yoy_pct`

**Formula:**

`(Current Active Customers / Prior Comparable Active Customers - 1) × 100`

---

## Order YoY Growth

**Field:** `orders_yoy_pct`

**Formula:**

`(Current Orders / Prior Comparable Orders - 1) × 100`

---

## Orders per Customer YoY Growth

**Field:** `orders_per_customer_yoy_pct`

**Formula:**

`(Current Orders per Customer / Prior Comparable Orders per Customer - 1) × 100`

---

## Basket Size YoY Growth

**Field:** `basket_size_yoy_pct`

**Formula:**

`(Current Basket Size / Prior Comparable Basket Size - 1) × 100`

---

## Adjusted EBIT YoY Growth

**Field:** `adjusted_ebit_yoy_pct`

**Formula:**

`(Current Adjusted EBIT / Prior Comparable Adjusted EBIT - 1) × 100`

---

# 13. Analyst-Calculated Profitability Metrics

## Adjusted EBIT Margin Change

**Field:** `adjusted_ebit_margin_change_pp`

**Unit:** Percentage points

**Formula:**

`Current Adjusted EBIT Margin - Prior Comparable Adjusted EBIT Margin`

Example:

`5.0% - 4.0% = +1.0 percentage point`

Percentage-point change must not be confused with percentage growth.

---

## EBIT Adjustment Gap

**Field:** `ebit_adjustment_gap_eur_m`

**Unit:** EUR millions

**Formula:**

`Adjusted EBIT - EBIT`

**Purpose:** Measures the absolute amount of adjustments separating accounting EBIT from management's Adjusted EBIT measure.

---

## EBIT Adjustment Ratio

**Field:** `ebit_adjustment_ratio_pct`

**Unit:** Percent

**Formula:**

`(Adjusted EBIT - EBIT) / Revenue × 100`

**Purpose:** Measures the size of EBIT adjustments relative to revenue.

---

# 14. Analyst-Calculated Business Model Metrics

## Revenue to GMV Ratio

**Field:** `revenue_to_gmv_pct`

**Formula:**

`Revenue / GMV × 100`

**Purpose:** Measures the relationship between recognized Group revenue and merchandise volume.

**Important:** This must NOT be interpreted mechanically as a marketplace take rate.

Zalando revenue contains streams excluded from GMV, including B2B revenue and certain B2C service revenues.

Changes in this ratio may therefore reflect multiple business-model effects.

---

# 15. Analyst-Calculated Cash Metrics

## Free Cash Flow Margin

**Field:** `fcf_margin_pct`

**Formula:**

`Free Cash Flow / Revenue × 100`

---

## Operating Cash Flow Margin

**Field:** `ocf_margin_pct`

**Formula:**

`Operating Cash Flow / Revenue × 100`

---

## Operating Cash Conversion

**Field:** `ocf_to_adjusted_ebit`

**Formula:**

`Operating Cash Flow / Adjusted EBIT`

**Purpose:** Provides an indication of how strongly adjusted operating earnings translate into operating cash flow.

**Important:** Working-capital movements and other cash-flow effects can materially influence this ratio.

---

## CapEx Intensity

**Field:** `capex_to_revenue_pct`

**Formula:**

`Absolute CapEx / Revenue × 100`

**Purpose:** Measures capital investment intensity relative to revenue.

The absolute value of CapEx is used because Zalando may report investment cash outflows using a negative sign convention.

---

# 16. Analyst-Calculated Productivity Metrics

## Revenue per Employee

**Field:** `revenue_per_employee_eur`

**Formula:**

`Revenue in EUR / Average Number of Employees`

**Purpose:** Approximate workforce productivity indicator.

---

## Adjusted EBIT per Employee

**Field:** `adjusted_ebit_per_employee_eur`

**Formula:**

`Adjusted EBIT in EUR / Average Number of Employees`

**Purpose:** Approximate adjusted operating-profit productivity indicator.

---

# 17. Growth Driver Framework

A central analytical framework of this project is the relationship between customers, purchasing frequency, basket size, and GMV.

Conceptually:

`Active Customers × Orders per Active Customer × Average Basket Size ≈ GMV`

This framework will be used to investigate whether changes in Zalando's commerce activity are associated primarily with:

- customer-base growth
- changes in purchase frequency
- changes in average basket size

The relationship should be treated as an analytical decomposition rather than a causal model.

Rounding, metric definitions, LTM measurement, cancellations, returns, and other reporting differences may prevent exact reconciliation.

---

# 18. LTM

**Full name:** Last Twelve Months

**Abbreviation:** `LTM`

An LTM metric is calculated over the preceding twelve months rather than only the individual quarter in which it is reported.

This is particularly important for quarterly analysis of:

- active customers
- average GMV per active customer
- average orders per active customer
- average basket size

For example, an active-customer figure reported at Q2 2026 represents customer activity over the preceding twelve months according to Zalando's definition rather than customers acquired during Q2 alone.

---

# 19. Percentage Points

**Abbreviation:** `pp`

Percentage points measure the absolute difference between percentages.

Example:

If Adjusted EBIT margin increases from 4.0% to 5.0%:

`Percentage-point change = +1.0pp`

The relative percentage increase in the margin would instead be:

`(5.0 / 4.0 - 1) × 100 = 25%`

These measures are not interchangeable.

---

# 20. Historical Reporting Vintage

Zalando dynamically reports GMV.

Historical GMV observations may therefore change in subsequent reports because prior periods are retrospectively updated for cancellations and returns.

The project must preserve sufficient source metadata to identify:

- reporting period
- source document
- publication period
- source page
- whether the value is an originally reported or subsequently updated comparative figure
- relevant restatement or comparability notes

A consistent historical-vintage policy will be applied before constructing the final analytical time series.

---

# 21. ABOUT YOU Comparability

Zalando completed the acquisition of ABOUT YOU during FY2025.

ABOUT YOU's financial results were consolidated into the Zalando Group following closing on 11 July 2025.

Therefore, FY2025 reported Group figures are not fully like-for-like with FY2024.

This affects interpretation of metrics including:

- GMV
- revenue
- B2C revenue
- B2B revenue
- Adjusted EBIT
- EBIT
- margins
- customer KPIs
- employees
- CapEx
- working capital
- cash flows

Where available and analytically useful, reported growth should be considered alongside Zalando's pro-forma disclosures.

Reported figures and pro-forma figures must remain clearly distinguished.

---

# 22. Data Quality Principles

The following rules apply throughout the project:

1. Raw reported figures must not be silently modified.
2. Reported and analyst-calculated metrics must remain distinguishable.
3. Every reported observation must remain traceable to a source.
4. Units must be standardized and documented.
5. Annual, quarterly, H1, 9M, and LTM observations must not be treated as directly equivalent.
6. Restated or dynamically updated historical figures must be documented.
7. Acquisition effects and other structural breaks must be flagged.
8. Calculated metrics should be reproducible from the underlying raw data.
9. Apparent inconsistencies should be investigated rather than manually forced to reconcile.
10. Management explanations should be distinguished from conclusions demonstrated directly by the data.