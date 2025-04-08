import api.apiBase as APIBase

class LiveGolfData(APIBase):
    def __init__(self):
        base_url = "https://live-golf-data.p.rapidapi.com/"
        headers = {
            "X-RapidAPI-Key": "your_api_key_here", # TODO: Replace with actual API key
            "X-RapidAPI-Host": "live-golf-data.p.rapidapi.com"
        }
        super().__init__(base_url, headers, timeout=30)

    def get_leaderboard(self, org_id: int, tourn_id: str, year: str, round_id: str = None) -> dict:
        """
        Fetches the leaderboard data
        """
        params = {
            "orgId": org_id,
            "tournId": tourn_id,
            "year": year,
            "roundId": round_id
        }
        return super(APIBase, self).send_request("leaderboard", params=params)

    def get_players(self, last_name: str = None, first_name: str = None, player_id: str = None) -> dict:
        """
        Fetches player data
        """
        params = {
            "lastName": last_name,
            "firstName": first_name,
            "playerId": player_id
        }
        return super(APIBase, self).send_request("players", params=params)

    def get_tournaments(self, org_id: int = None, tourn_id: str = None, year: str = None) -> dict:
        """
        Fetches tournament data
        """
        params = {
            "orgId": org_id,
            "tournId": tourn_id,
            "year": year
        }
        return super(APIBase, self).send_request("tournaments", params=params)

    def get_scorecards(self, org_id: int, tourn_id: str, year: str, player_id: str, round_id: str = None) -> dict:
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
        return super(APIBase, self).send_request("scorecards", params=params)
