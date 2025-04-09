import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

import src.cache as cache
from src.module.tournamentLeaderboard import TournamentLeaderboard


def fetch_tournament_leaderboard() -> dict:
    """
    Fetches the tournament leaderboard data
    """
    latest_file = cache.get_latest_cache_file()

    if cache.is_cache_fresh(latest_file):
        print("Fetched leaderboard data from cache.")
        return cache.load_from_cache(latest_file)

    from api.liveGolfData import LiveGolfData

    api = LiveGolfData()
    leaderboard_data = api.get_leaderboard()
    cache.save_to_cache(leaderboard_data)
    print("Fetched leaderboard data from API and saved to cache.")
    return leaderboard_data

def load_tournament_leaderboard() -> pd.DataFrame:
    leaderboard_data = fetch_tournament_leaderboard()

    tl = TournamentLeaderboard(
        _org_id=leaderboard_data["orgId"],
        _year=leaderboard_data["year"],
        _tourn_id=leaderboard_data["tournId"],
        _current_status=leaderboard_data["status"],
        _current_round_status=leaderboard_data["roundStatus"],
        _current_round_id=leaderboard_data["roundId"],
        _last_updated=leaderboard_data["lastUpdated"],
        _cut_lines=leaderboard_data["cutLines"]
    )
    tl.initialize_players(leaderboard_data["leaderboardRows"])
    st.session_state.tournament_leaderboard = tl

    df = tl.to_dataframe()
    return df


st.set_page_config(page_title="Tournament Leaderboard", page_icon=":golfer:", layout="wide")
st.title("Tournament Leaderboard")

# 🔁 Auto-refresh every 1 minute
# st_autorefresh(interval=60 * 1000, key="refresh")

df = load_tournament_leaderboard()
st.dataframe(df)
