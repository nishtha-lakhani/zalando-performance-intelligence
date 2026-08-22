from pathlib import Path

from load_data import load_raw_data


# --------------------------------------------------
# 1. LOAD RAW DATA
# --------------------------------------------------

_, _, interim_kpis = load_raw_data()


# --------------------------------------------------
# 2. PREPARE INTERIM DATA
# --------------------------------------------------

interim_performance = interim_kpis.copy()


# Create a numeric quarter/order field so periods can
# be sorted consistently.
period_order = {
    "Q1 2025": 1,
    "Q2 2025": 2,
    "H1 2025": 3,
    "Q1 2026": 4,
    "Q2 2026": 5,
    "H1 2026": 6,
}

interim_performance["period_order"] = (
    interim_performance["period"].map(period_order)
)

interim_performance = (
    interim_performance
    .sort_values("period_order")
    .reset_index(drop=True)
)


# --------------------------------------------------
# 3. CALCULATE REPORTED YOY GROWTH
# --------------------------------------------------

# Match each 2026 observation to its comparable
# 2025 period rather than comparing adjacent rows.

comparison_data = interim_performance[
    [
        "period",
        "gmv_eur_m",
        "revenue_eur_m",
        "adjusted_ebit_eur_m",
    ]
].copy()

comparison_data = comparison_data.rename(
    columns={
        "period": "comparison_period",
        "gmv_eur_m": "comparison_gmv_eur_m",
        "revenue_eur_m": "comparison_revenue_eur_m",
        "adjusted_ebit_eur_m": "comparison_adjusted_ebit_eur_m",
    }
)

interim_performance = interim_performance.merge(
    comparison_data,
    on="comparison_period",
    how="left",
)


interim_performance["gmv_yoy_pct"] = (
    (
        interim_performance["gmv_eur_m"]
        / interim_performance["comparison_gmv_eur_m"]
        - 1
    )
    * 100
)

interim_performance["revenue_yoy_pct"] = (
    (
        interim_performance["revenue_eur_m"]
        / interim_performance["comparison_revenue_eur_m"]
        - 1
    )
    * 100
)

interim_performance["adjusted_ebit_yoy_pct"] = (
    (
        interim_performance["adjusted_ebit_eur_m"]
        / interim_performance["comparison_adjusted_ebit_eur_m"]
        - 1
    )
    * 100
)


# --------------------------------------------------
# 4. CALCULATE ANALYTICAL METRICS
# --------------------------------------------------

interim_performance["revenue_to_gmv_pct"] = (
    interim_performance["revenue_eur_m"]
    / interim_performance["gmv_eur_m"]
    * 100
)

interim_performance["fcf_margin_pct"] = (
    interim_performance["free_cash_flow_eur_m"]
    / interim_performance["revenue_eur_m"]
    * 100
)

interim_performance["ocf_margin_pct"] = (
    interim_performance["operating_cash_flow_eur_m"]
    / interim_performance["revenue_eur_m"]
    * 100
)

interim_performance["capex_to_revenue_pct"] = (
    interim_performance["capex_eur_m"].abs()
    / interim_performance["revenue_eur_m"]
    * 100
)

interim_performance["ebit_adjustment_gap_eur_m"] = (
    interim_performance["adjusted_ebit_eur_m"]
    - interim_performance["ebit_eur_m"]
)


# --------------------------------------------------
# 5. SELECT PROCESSED COLUMNS
# --------------------------------------------------

processed_interim = interim_performance[
    [
        "period",
        "period_type",
        "year",
        "comparison_period",

        # Scale
        "gmv_eur_m",
        "revenue_eur_m",

        # Profitability
        "adjusted_ebit_eur_m",
        "adjusted_ebit_margin_pct",
        "ebit_eur_m",
        "ebit_margin_pct",

        # Customer activity
        "active_customers_m",
        "orders_m",
        "gmv_per_active_customer_eur",
        "orders_per_active_customer",
        "average_basket_size_eur",

        # Investment and cash
        "capex_eur_m",
        "operating_cash_flow_eur_m",
        "free_cash_flow_eur_m",

        # Reported growth
        "gmv_yoy_pct",
        "revenue_yoy_pct",
        "adjusted_ebit_yoy_pct",

        # Analyst-calculated metrics
        "revenue_to_gmv_pct",
        "fcf_margin_pct",
        "ocf_margin_pct",
        "capex_to_revenue_pct",
        "ebit_adjustment_gap_eur_m",

        # Source information
        "source_document",
        "source_page",
        "notes",
    ]
].copy()


# --------------------------------------------------
# 6. EXPORT PROCESSED DATA
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

OUTPUT_PATH = PROCESSED_DIR / "interim_performance.csv"

processed_interim.to_csv(
    OUTPUT_PATH,
    index=False,
)


# --------------------------------------------------
# 7. DISPLAY RESULTS
# --------------------------------------------------

print("Interim Performance:")
print(
    processed_interim[
        [
            "period",
            "gmv_eur_m",
            "revenue_eur_m",
            "adjusted_ebit_eur_m",
            "gmv_yoy_pct",
            "revenue_yoy_pct",
            "adjusted_ebit_yoy_pct",
        ]
    ].round(1)
)

print("\nDataset shape:")
print(processed_interim.shape)

print("\nProcessed dataset saved to:")
print(OUTPUT_PATH)