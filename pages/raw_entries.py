import streamlit as st
from streamlit_autorefresh import st_autorefresh

from src.utils.entries import load_entries


st.set_page_config(page_title="Raw Entries", page_icon=":golfer:", layout="wide")
st.title("Raw Entries")

# 🔁 Auto-refresh every 1 minute
st_autorefresh(interval=60 * 1000, key="refresh")

with st.spinner("Refreshing entries..."):
    df = load_entries()
st.dataframe(df)
