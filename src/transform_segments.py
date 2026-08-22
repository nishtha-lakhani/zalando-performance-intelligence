from pathlib import Path

from load_data import load_raw_data


# --------------------------------------------------
# 1. LOAD RAW DATA
# --------------------------------------------------

financial_kpis, _, _ = load_raw_data()

# --------------------------------------------------
# 2. KEEP SEGMENT OBSERVATIONS
# --------------------------------------------------

segment_performance = financial_kpis[
    financial_kpis["segment"].isin(["B2C", "B2B"])
].copy()


# --------------------------------------------------
# 3. SORT DATA
# --------------------------------------------------

segment_performance = (
    segment_performance
    .sort_values(["year", "segment"])
    .reset_index(drop=True)
)


# --------------------------------------------------
# 4. SELECT RELEVANT COLUMNS
# --------------------------------------------------

segment_performance = segment_performance[
    [
        "year",
        "segment",
        "revenue_eur_m",
        "adjusted_ebit_eur_m",
        "adjusted_ebit_margin_pct",
        "ebit_eur_m",
    ]
].copy()


# --------------------------------------------------
# 5. CALCULATE SEGMENT GROWTH
# --------------------------------------------------

segment_performance["revenue_yoy_pct"] = (
    segment_performance
    .groupby("segment")["revenue_eur_m"]
    .pct_change()
    * 100
)

segment_performance["adjusted_ebit_yoy_pct"] = (
    segment_performance
    .groupby("segment")["adjusted_ebit_eur_m"]
    .pct_change()
    * 100
)


# --------------------------------------------------
# 6. CALCULATE SEGMENT REVENUE MIX
# --------------------------------------------------

group_revenue = (
    financial_kpis[
        financial_kpis["segment"] == "Group"
    ][["year", "revenue_eur_m"]]
    .rename(
        columns={
            "revenue_eur_m": "group_revenue_eur_m"
        }
    )
)

segment_performance = segment_performance.merge(
    group_revenue,
    on="year",
    how="left",
)

segment_performance["share_of_group_revenue_pct"] = (
    segment_performance["revenue_eur_m"]
    / segment_performance["group_revenue_eur_m"]
    * 100
)


# --------------------------------------------------
# 7. EXPORT
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

OUTPUT_PATH = PROCESSED_DIR / "segment_performance.csv"

segment_performance.to_csv(
    OUTPUT_PATH,
    index=False,
)


# --------------------------------------------------
# 8. DISPLAY RESULTS
# --------------------------------------------------

print("Segment Performance:")
print(segment_performance.round(2))

print("\nDataset shape:")
print(segment_performance.shape)

print("\nProcessed dataset saved to:")
print(OUTPUT_PATH)