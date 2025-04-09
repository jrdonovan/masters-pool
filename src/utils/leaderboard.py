import pandas as pd
import streamlit as st

import src.cache as cache
from src.module.tournamentLeaderboard import TournamentLeaderboard

CACHE_SUBFOLDER = "leaderboard"


def fetch_tournament_leaderboard() -> dict:
    """
    Fetches the tournament leaderboard data
    """
    latest_file = cache.get_latest_cache_file(CACHE_SUBFOLDER)

    if cache.is_cache_fresh(latest_file):
        print("Fetched leaderboard data from cache.")
        return cache.load_from_cache(latest_file)

    from api.liveGolfData import LiveGolfData

    api = LiveGolfData()
    leaderboard_data = api.get_leaderboard()
    cache.save_to_cache(leaderboard_data, CACHE_SUBFOLDER)
    print("Fetched leaderboard data from API and saved to cache.")
    return leaderboard_data


def load_tournament_leaderboard() -> pd.DataFrame:
    """
    Loads the tournament leaderboard data and returns it as a DataFrame.
    """
    leaderboard_data = fetch_tournament_leaderboard()

    tl = TournamentLeaderboard(
        _org_id=leaderboard_data["orgId"],
        _year=leaderboard_data["year"],
        _tourn_id=leaderboard_data["tournId"],
        _current_status=leaderboard_data["status"],
        _current_round_status=leaderboard_data["roundStatus"],
        _current_round_id=leaderboard_data["roundId"],
        _last_updated=leaderboard_data["lastUpdated"],
        _cut_lines=leaderboard_data["cutLines"],
    )
    tl.initialize_players(leaderboard_data["leaderboardRows"])
    st.session_state.tournament_leaderboard = tl

    df = tl.to_dataframe()
    return df
