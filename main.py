import os
import sys

import streamlit as st


def main():
    home_page = st.Page("pages/home.py", title="Home", default=True)
    entries_page = st.Page("pages/entries.py", title="Entries")
    pool_leaderboard_page = st.Page(
        "pages/pool_leaderboard.py", title="Pool Leaderboard"
    )
    tournament_leaderboard_page = st.Page(
        "pages/tournament_leaderboard.py", title="Tournament Leaderboard"
    )
    scorecards_page = st.Page("pages/scorecards.py", title="Scorecards")

    pg = st.navigation(
        [
            home_page,
            entries_page,
            pool_leaderboard_page,
            tournament_leaderboard_page,
            scorecards_page,
        ],
    )
    pg.run()


if __name__ == "__main__":
    # Add the parent directory to the system path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    main()
