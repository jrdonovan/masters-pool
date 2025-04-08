import pandas as pd
import streamlit as st

from src.module.tournamentLeaderboard import TournamentLeaderboard

@st.cache_data
def load_tournament_leaderboard() -> pd.DataFrame:
    """
    Fetches the tournament leaderboard data
    """
    from api.liveGolfData import LiveGolfData

    api = LiveGolfData()
    leaderboard_data = api.get_leaderboard()
    print("Fetched leaderboard data")
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

df = load_tournament_leaderboard()
st.dataframe(df)
