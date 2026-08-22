from pathlib import Path

import pandas as pd


# --------------------------------------------------
# 1. LOCATE PROCESSED DATA
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "annual_performance.csv"


# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

df = pd.read_csv(DATA_PATH)


# --------------------------------------------------
# 3. STRUCTURAL CHECKS
# --------------------------------------------------

# We expect one annual observation for every year
# from 2019 through 2025.
expected_years = list(range(2019, 2026))

assert df["year"].tolist() == expected_years, (
    "Years are missing, duplicated, or incorrectly ordered."
)

assert df["year"].is_unique, (
    "Duplicate annual observations found."
)


# --------------------------------------------------
# 4. CRITICAL MISSING-VALUE CHECKS
# --------------------------------------------------

critical_columns = [
    "year",
    "gmv_eur_m",
    "revenue_eur_m",
    "adjusted_ebit_eur_m",
    "adjusted_ebit_margin_pct",
    "active_customers_m",
    "orders_m",
    "orders_per_active_customer",
    "average_basket_size_eur",
]

assert not df[critical_columns].isna().any().any(), (
    "Missing values found in critical analytical fields."
)


# --------------------------------------------------
# 5. BASIC BUSINESS-RULE CHECKS
# --------------------------------------------------

assert (df["gmv_eur_m"] > 0).all(), (
    "GMV contains zero or negative values."
)

assert (df["revenue_eur_m"] > 0).all(), (
    "Revenue contains zero or negative values."
)

assert (df["active_customers_m"] > 0).all(), (
    "Active customers contain zero or negative values."
)

assert (df["orders_m"] > 0).all(), (
    "Orders contain zero or negative values."
)


# --------------------------------------------------
# 6. MARGIN RECONCILIATION
# --------------------------------------------------

df["calculated_adjusted_ebit_margin_pct"] = (
    df["adjusted_ebit_eur_m"]
    / df["revenue_eur_m"]
    * 100
)

df["margin_difference_pp"] = (
    df["calculated_adjusted_ebit_margin_pct"]
    - df["adjusted_ebit_margin_pct"]
)

assert (df["margin_difference_pp"].abs() < 0.1).all(), (
    "Calculated Adjusted EBIT margin does not reconcile "
    "with reported margin within tolerance."
)


# --------------------------------------------------
# 7. GMV DRIVER RECONCILIATION
# --------------------------------------------------

# Approximate GMV using:
# customers × orders/customer × basket size.
#
# active_customers_m is in millions, so the resulting
# figure is also EUR millions.

df["estimated_gmv_eur_m"] = (
    df["active_customers_m"]
    * df["orders_per_active_customer"]
    * df["average_basket_size_eur"]
)

df["gmv_reconciliation_difference_pct"] = (
    (
        df["estimated_gmv_eur_m"]
        / df["gmv_eur_m"]
        - 1
    )
    * 100
)


# --------------------------------------------------
# 8. DISPLAY VALIDATION RESULTS
# --------------------------------------------------

print("All structural and business-rule checks passed.")

print("\nAdjusted EBIT Margin Reconciliation:")
print(
    df[
        [
            "year",
            "adjusted_ebit_margin_pct",
            "calculated_adjusted_ebit_margin_pct",
            "margin_difference_pp",
        ]
    ].round(2)
)

print("\nGMV Driver Reconciliation:")
print(
    df[
        [
            "year",
            "gmv_eur_m",
            "estimated_gmv_eur_m",
            "gmv_reconciliation_difference_pct",
        ]
    ].round(2)
)