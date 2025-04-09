import pandas as pd
import streamlit as st

from api.liveGolfData import LiveGolfData
from src.module.tournamentLeaderboard import TournamentLeaderboard

CACHE_SUBFOLDER = "leaderboard"


def fetch_tournament_leaderboard() -> dict:
    """
    Fetches the tournament leaderboard data
    """
    api = LiveGolfData()
    leaderboard_data = api.get_leaderboard()
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
