import pandas as pd

from api.liveGolfData import LiveGolfData
from src.utils.streamlit import set_session_state

CACHE_SUBFOLDER = "scorecard"


def fetch_scorecards(player_id: int) -> list:
    api = LiveGolfData()
    scorecard_data = api.get_scorecards(player_id)
    return scorecard_data


def load_scorecards() -> pd.DataFrame:
    raw_scorecards = fetch_scorecards()

    df = pool.to_dataframe()
    set_session_state("entries", df)
    return df
