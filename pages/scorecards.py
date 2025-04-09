import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Scorecards", page_icon=":golfer:", layout="wide")
st.title("Scorecards")
st.write("Scorecards for each golfer in the tournament.")

# 🔁 Auto-refresh every 1 minute
st_autorefresh(interval=60 * 1000, key="refresh")
