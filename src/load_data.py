from pathlib import Path

import pandas as pd


# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "zalando_raw_data.xlsx"


# --------------------------------------------------
# LOAD RAW DATA
# --------------------------------------------------

def load_raw_data():
    """Load all raw Zalando KPI datasets from Excel."""

    financial_kpis = pd.read_excel(
        RAW_DATA_PATH,
        sheet_name="financial_kpis",
    )

    operating_kpis = pd.read_excel(
        RAW_DATA_PATH,
        sheet_name="operating_kpis",
    )

    interim_kpis = pd.read_excel(
        RAW_DATA_PATH,
        sheet_name="interim_kpis",
    )

    return financial_kpis, operating_kpis, interim_kpis


# --------------------------------------------------
# DIRECT EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    financial_kpis, operating_kpis, interim_kpis = load_raw_data()

    print("Financial KPIs:")
    print(financial_kpis)

    print("\nOperating KPIs:")
    print(operating_kpis)

    print("\nInterim KPIs:")
    print(interim_kpis)