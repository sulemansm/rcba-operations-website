import streamlit as st
import pandas as pd
from database import load_reports

if st.session_state.role != "admin":
    st.error("Admins only")
    st.stop()

st.title("Admin Dashboard")

rows = load_reports()

if not rows:
    st.info("No reports submitted yet.")
    st.stop()

columns = [
    "ID",
    "Title",
    "Venue",
    "Start Time",
    "End Time",
    "Avenue",
    "Created By"
]

df = pd.DataFrame(rows, columns=columns)

st.metric("Total Reports", len(df))

st.dataframe(df, use_container_width=True)