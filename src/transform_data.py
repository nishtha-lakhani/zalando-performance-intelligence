from pathlib import Path

from load_data import load_raw_data


# --------------------------------------------------
# 1. LOAD RAW DATA
# --------------------------------------------------

financial_kpis, operating_kpis, _ = load_raw_data()


# --------------------------------------------------
# 2. PREPARE FINANCIAL DATA
# --------------------------------------------------

# Keep only Group-level financial observations.
# B2C and B2B segment rows are retained in the raw dataset
# but are not used in the consolidated annual time series.
group_financials = financial_kpis[
    financial_kpis["segment"] == "Group"
].copy()

# Sort chronologically and reset the row index.
group_financials = (
    group_financials
    .sort_values("year")
    .reset_index(drop=True)
)


# --------------------------------------------------
# 3. PREPARE OPERATING DATA
# --------------------------------------------------

# Sort chronologically and reset the row index.
operating_kpis = (
    operating_kpis
    .sort_values("year")
    .reset_index(drop=True)
)


# --------------------------------------------------
# 4. CALCULATE FINANCIAL GROWTH
# --------------------------------------------------

group_financials["gmv_yoy_pct"] = (
    group_financials["gmv_eur_m"].pct_change() * 100
)

group_financials["revenue_yoy_pct"] = (
    group_financials["revenue_eur_m"].pct_change() * 100
)

group_financials["adjusted_ebit_yoy_pct"] = (
    group_financials["adjusted_ebit_eur_m"].pct_change() * 100
)


# --------------------------------------------------
# 5. CALCULATE OPERATING GROWTH
# --------------------------------------------------

operating_kpis["active_customers_yoy_pct"] = (
    operating_kpis["active_customers_m"].pct_change() * 100
)

operating_kpis["orders_yoy_pct"] = (
    operating_kpis["orders_m"].pct_change() * 100
)

operating_kpis["orders_per_customer_yoy_pct"] = (
    operating_kpis["orders_per_active_customer"].pct_change() * 100
)

operating_kpis["basket_size_yoy_pct"] = (
    operating_kpis["average_basket_size_eur"].pct_change() * 100
)


# --------------------------------------------------
# 6. MERGE FINANCIAL AND OPERATING DATA
# --------------------------------------------------

# Combine the Group financial dataset with the operating
# dataset using year as the common join key.
annual_performance = group_financials.merge(
    operating_kpis,
    on="year",
    how="inner",
    suffixes=("_financial", "_operating"),
)


# --------------------------------------------------
# 7. CALCULATE ANALYTICAL METRICS
# --------------------------------------------------

# Revenue recognized relative to GMV.
# This should NOT be interpreted as a marketplace take rate.
annual_performance["revenue_to_gmv_pct"] = (
    annual_performance["revenue_eur_m"]
    / annual_performance["gmv_eur_m"]
    * 100
)

# Free cash flow relative to revenue.
annual_performance["fcf_margin_pct"] = (
    annual_performance["free_cash_flow_eur_m"]
    / annual_performance["revenue_eur_m"]
    * 100
)

# Operating cash flow relative to revenue.
annual_performance["ocf_margin_pct"] = (
    annual_performance["operating_cash_flow_eur_m"]
    / annual_performance["revenue_eur_m"]
    * 100
)

# Capital expenditure relative to revenue.
# CapEx is reported as a negative cash outflow, so abs()
# converts it to a positive investment magnitude.
annual_performance["capex_to_revenue_pct"] = (
    annual_performance["capex_eur_m"].abs()
    / annual_performance["revenue_eur_m"]
    * 100
)

# Difference between management's Adjusted EBIT
# and accounting EBIT.
annual_performance["ebit_adjustment_gap_eur_m"] = (
    annual_performance["adjusted_ebit_eur_m"]
    - annual_performance["ebit_eur_m"]
)


# --------------------------------------------------
# 8. SELECT FINAL PROCESSED DATASET COLUMNS
# --------------------------------------------------

processed_annual = annual_performance[
    [
        # Period
        "year",

        # Scale
        "gmv_eur_m",
        "revenue_eur_m",

        # Profitability
        "adjusted_ebit_eur_m",
        "adjusted_ebit_margin_pct",
        "ebit_eur_m",
        "ebit_margin_pct",

        # Customer and commerce activity
        "active_customers_m",
        "orders_m",
        "orders_per_active_customer",
        "average_basket_size_eur",

        # Investment and cash
        "capex_eur_m",
        "net_working_capital_eur_m",
        "operating_cash_flow_eur_m",
        "free_cash_flow_eur_m",
        "cash_and_equivalents_eur_m",

        # Financial growth
        "gmv_yoy_pct",
        "revenue_yoy_pct",
        "adjusted_ebit_yoy_pct",

        # Operating growth
        "active_customers_yoy_pct",
        "orders_yoy_pct",
        "orders_per_customer_yoy_pct",
        "basket_size_yoy_pct",

        # Analyst-calculated metrics
        "revenue_to_gmv_pct",
        "fcf_margin_pct",
        "ocf_margin_pct",
        "capex_to_revenue_pct",
        "ebit_adjustment_gap_eur_m",
    ]
].copy()


# --------------------------------------------------
# 9. EXPORT PROCESSED DATASET
# --------------------------------------------------

# Identify the project root directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define the processed-data directory.
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

# Create the directory if it does not already exist.
PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

# Define the output file.
OUTPUT_PATH = PROCESSED_DIR / "annual_performance.csv"

# Export the processed dataset.
processed_annual.to_csv(
    OUTPUT_PATH,
    index=False,
)


# --------------------------------------------------
# 10. DISPLAY RESULTS
# --------------------------------------------------

print("Processed Annual Performance:")
print(processed_annual.round(2))

print("\nDataset shape:")
print(processed_annual.shape)

print("\nProcessed dataset saved to:")
print(OUTPUT_PATH)