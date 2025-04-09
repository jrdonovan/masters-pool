import gspread
import pandas as pd

import src.cache as cache
from src.module.pool import Pool
from src.utils.streamlit import get_secret, set_session_state

CACHE_SUBFOLDER = "entries"


def fetch_entries() -> list:
    """
    Fetches entries from the Google Sheets API.
    """
    latest_file = cache.get_latest_cache_file(CACHE_SUBFOLDER)

    if cache.is_cache_fresh(latest_file):
        print("Fetched entries from cache.")
        return cache.load_from_cache(latest_file)

    gc = gspread.service_account_from_dict(info=get_secret("google"))
    data = gc.open(get_secret("SHEET_NAME")).sheet1.get_all_records()
    cache.save_to_cache(data, CACHE_SUBFOLDER)
    print("Fetched entries from API and saved to cache.")
    return data


def load_entries() -> pd.DataFrame:
    raw_entries = fetch_entries()
    pool = Pool(_name="Masters Pool 2025")

    pool.initialize_entries(raw_entries)

    df = pool.to_dataframe()
    set_session_state("entries", df)
    return df
