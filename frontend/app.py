import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category_ui import analytics_by_category_tab
from analytics_by_month import analytics_months_tab
from analytics_by_day import analytics_day_tab

API_URL = "http://localhost:8000"

st.title('Expense Management System')

tab1, tab2, tab3,tab4 = st.tabs(["Add/Update", "Analytics by Category","Analytics by Month","Analytics by Day"])

with tab1:
    add_update_tab()

with tab2:
    analytics_by_category_tab()

with tab3:
    analytics_months_tab()

with tab4:
    analytics_day_tab()
















