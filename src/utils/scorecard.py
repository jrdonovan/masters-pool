import pandas as pd

import src.cache as cache
from src.utils.streamlit import set_session_state

CACHE_SUBFOLDER = "scorecard"


def fetch_scorecards(player_id: int) -> list:
    filepath = f"{CACHE_SUBFOLDER}/{player_id}"
    latest_file = cache.get_latest_cache_file(filepath)

    if cache.is_cache_fresh(latest_file):
        print("Fetched scorecard from cache.")
        return cache.load_from_cache(latest_file)

    from api.liveGolfData import LiveGolfData

    api = LiveGolfData()
    scorecard_data = api.get_scorecards(player_id)
    cache.save_to_cache(scorecard_data, filepath, f"scorecard_{player_id}")
    print(f"Fetched scorecard data from API for player ID {player_id} and saved to cache.")
    return scorecard_data


def load_scorecards() -> pd.DataFrame:
    raw_scorecards = fetch_scorecards()

    df = pool.to_dataframe()
    set_session_state("entries", df)
    return df
