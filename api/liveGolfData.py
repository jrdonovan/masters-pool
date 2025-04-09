from streamlit import secrets

from api.apiBase import APIBase

class LiveGolfData(APIBase):
    def __init__(self):
        base_url = "https://live-golf-data.p.rapidapi.com/"
        headers = {
            "X-RapidAPI-Key": secrets["RAPID_API_KEY"],
            "X-RapidAPI-Host": "live-golf-data.p.rapidapi.com"
        }
        super().__init__(base_url, headers, timeout=30)

    def get_leaderboard(self, org_id: int = secrets["ORG_ID"], tourn_id: str = secrets["TOURN_ID"], year: str = secrets["YEAR"], round_id: str = None) -> dict:
        """
        Fetches the leaderboard data
        """
        params = {
            "orgId": org_id,
            "tournId": tourn_id,
            "year": year,
            "roundId": round_id
        }
        print(f"Fetching leaderboard for org_id: {org_id}, tourn_id: {tourn_id}, year: {year}, round_id: {round_id}")
        return super().send_request("leaderboard", params=params)

    def get_players(self, last_name: str = None, first_name: str = None, player_id: str = None) -> dict:
        """
        Fetches player data
        """
        params = {
            "lastName": last_name,
            "firstName": first_name,
            "playerId": player_id
        }
        print(f"Fetching players with last_name: {last_name}, first_name: {first_name}, player_id: {player_id}")
        return super().send_request("players", params=params)

    def get_tournaments(self, org_id: int = secrets["ORG_ID"], tourn_id: str = secrets["TOURN_ID"], year: str = secrets["YEAR"]) -> dict:
        """
        Fetches tournament data
        """
        params = {
            "orgId": org_id,
            "tournId": tourn_id,
            "year": year
        }
        print(f"Fetching tournaments for org_id: {org_id}, tourn_id: {tourn_id}, year: {year}")
        return super().send_request("tournaments", params=params)

    def get_scorecards(self, player_id: str, org_id: int = secrets["ORG_ID"], tourn_id: str = secrets["TOURN_ID"], year: str = secrets["YEAR"], round_id: str = None) -> dict:
        """
        Fetches scorecard data
        """
        params = {
            "orgId": org_id,
            "tournId": tourn_id,
            "year": year,
            "playerId": player_id,
            "roundId": round_id
        }
        print(f"Fetching scorecard for player_id: {player_id}, org_id: {org_id}, tourn_id: {tourn_id}, year: {year}, round_id: {round_id}")
        return super().send_request("scorecard", params=params)
