import streamlit as st
from streamlit_autorefresh import st_autorefresh

from src.utils.leaderboard import load_tournament_leaderboard


st.set_page_config(
    page_title="Tournament Leaderboard", page_icon=":golfer:", layout="wide"
)
st.title("Tournament Leaderboard")

# 🔁 Auto-refresh every 1 minute
st_autorefresh(interval=60 * 1000, key="refresh")

with st.spinner("Refreshing leaderboard..."):
    df = load_tournament_leaderboard()
st.dataframe(df)
