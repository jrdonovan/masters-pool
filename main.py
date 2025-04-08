import os
import sys

import streamlit as st


def refresh_entries():
    """
    Refreshes the entries from the Google Sheet.
    """
    # This function should contain the logic to refresh entries.
    # For example, it could call a method from EntryFetcher to get new entries.
    pass


def refresh_leaderboard():
    """
    Refreshes the leaderboard.
    """
    # This function should contain the logic to refresh the leaderboard.
    # For example, it could call a method from EntryFetcher to get new leaderboard data.
    pass


def main():
    home_page = st.Page("pages/home.py", title="Home")
    entries_page = st.Page("pages/raw_entries.py", title="Raw Entries")
    pool_leaderboard_page = st.Page("pages/pool_leaderboard.py", title="Pool Leaderboard", default=True)
    tournament_leaderboard_page = st.Page("pages/tournament_leaderboard.py", title="Tournament Leaderboard")
    scorecards_page = st.Page("pages/scorecards.py", title="Scorecards")

    pg = st.navigation(
        [home_page, entries_page, pool_leaderboard_page, tournament_leaderboard_page, scorecards_page],
    )
    pg.run()


if __name__ == "__main__":
    # Add the parent directory to the system path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    main()
