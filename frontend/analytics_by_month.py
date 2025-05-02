import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def analytics_months_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")
    monthly_summary = response.json()

    # All 12 months reference
    month_names = [datetime(1900, m, 1).strftime('%B') for m in range(1, 13)]
    all_months = pd.DataFrame({
        "Month Number": list(range(1, 13)),
        "Month Name": month_names
    })

    # API data
    df = pd.DataFrame(monthly_summary)
    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    }, inplace=True)

    # Merge and fill missing values
    df_full = pd.merge(all_months, df, on=["Month Number", "Month Name"], how="left")
    df_full["Total"] = df_full["Total"].fillna(0)

    # Set correct categorical order for chart
    df_full["Month Name"] = pd.Categorical(df_full["Month Name"], categories=month_names, ordered=True)
    df_full.sort_values("Month Name", inplace=True)

    # Display
    st.title("Expense Breakdown By Months")
    st.bar_chart(data=df_full.set_index("Month Name")["Total"], use_container_width=True)

    df_full["Total"] = df_full["Total"].map("{:.2f}".format)
    df_display = df_full.set_index("Month Number")
    st.table(df_display)
