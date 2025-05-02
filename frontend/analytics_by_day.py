import streamlit as st
import requests
from collections import defaultdict
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://localhost:8000"  # Replace with your actual API base URL


def summarize_by_category_day(expenses):
    category_totals = defaultdict(float)
    for entry in expenses:
        category = entry.get("category", "Uncategorized")
        amount = entry.get("amount", 0)
        category_totals[category] += amount
    return dict(category_totals)


def analytics_day_tab():
    selected_date = st.date_input(
        "Enter the date",
        datetime(2024, 8, 1),
        label_visibility="collapsed",
        key="day_tab_date"
    )

    response = requests.get(f"{API_URL}/expenses/{selected_date}")

    if response.status_code == 200:
        existing_expenses = response.json()
        if not existing_expenses:
            st.info("No expenses found for this date.")
            return

        st.subheader(f"📅 Expense Summary for {selected_date.strftime('%Y-%m-%d')}")

        # Displaying the expenses in a table format
        expenses_df = pd.DataFrame(existing_expenses)
        st.dataframe(expenses_df)  # Display the expenses as a table

        # Summarizing the expenses by category
        summary = summarize_by_category_day(existing_expenses)
        # for category, total in summary.items():
        #     st.write(f"**{category}**: ${total:.2f}")

        # Pie chart
        fig, ax = plt.subplots()

        # Calculate explode values: explode the largest slice
        explode = [0.1 if size == max(summary.values()) else 0 for size in summary.values()]

        # Plot the pie chart without shadow
        ax.pie(summary.values(), labels=summary.keys(), autopct='%1.1f%%', startangle=90, explode=explode)

        # Now create the same pie chart with shadow for the largest slice
        ax.pie(summary.values(), labels=summary.keys(), autopct='%1.1f%%', startangle=90, explode=explode, shadow=True)

        # Equal aspect ratio ensures that pie chart is drawn as a circle.
        ax.axis('equal')

        st.pyplot(fig)

    else:
        st.error("Failed to retrieve expenses.")





