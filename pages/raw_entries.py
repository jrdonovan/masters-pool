import pandas as pd
import streamlit as st

from src.module.entryFetcher import EntryFetcher

@st.cache_data
def load_entries() -> pd.DataFrame:
    ef = EntryFetcher(
        creds_file="REDACTED", # TODO: Remove this hardcoded path
        sheet_name="Masters Pool 2025 (Responses)",
    )
    entries = ef.get_entries()
    print(f"Loaded {len(entries)} entries.")
    df = pd.DataFrame([e.to_dict() for e in entries])
    df.index += 1
    return df

st.set_page_config(page_title="Raw Entries", page_icon=":golfer:", layout="wide")
st.title("Raw Entries")

df = load_entries()
st.dataframe(df)
