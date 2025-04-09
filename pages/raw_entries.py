import gspread
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

import src.cache as cache
from module.pool import Pool

CACHE_SUBFOLDER = "entries"


def fetch_entries() -> list:
    """
    Fetches entries from the Google Sheets API.
    """
    latest_file = cache.get_latest_cache_file(CACHE_SUBFOLDER)

    if cache.is_cache_fresh(latest_file):
        print("Fetched entries from cache.")
        return cache.load_from_cache(latest_file)

    gc = gspread.service_account(
        filename="REDACTED"
    )  # TODO: Remove this hardcoded path
    data = gc.open("Masters Pool 2025 (Responses)").sheet1.get_all_records()
    cache.save_to_cache(data, CACHE_SUBFOLDER)
    print("Fetched entries from API and saved to cache.")
    return data


def load_entries() -> pd.DataFrame:
    raw_entries = fetch_entries()
    pool = Pool(_name="Masters Pool 2025")

    pool.initialize_entries(raw_entries)

    df = pool.to_dataframe()
    st.session_state.entries = df
    return df


st.set_page_config(page_title="Raw Entries", page_icon=":golfer:", layout="wide")
st.title("Raw Entries")

# 🔁 Auto-refresh every 1 minute
st_autorefresh(interval=60* 1000, key="refresh")

df = load_entries()
st.dataframe(df)
