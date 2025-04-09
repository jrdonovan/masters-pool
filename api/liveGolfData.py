from api.apiBase import APIBase
import src.cache as cache
from src.utils.streamlit import get_secret


class LiveGolfData(APIBase):
    def __init__(self):
        base_url = "https://live-golf-data.p.rapidapi.com/"
        headers = {
            "X-RapidAPI-Key": get_secret("RAPID_API_KEY"),
            "X-RapidAPI-Host": "live-golf-data.p.rapidapi.com",
        }
        super().__init__(base_url, headers, timeout=30)

    def get_leaderboard(
        self,
        org_id: int = get_secret("ORG_ID"),
        tourn_id: str = get_secret("TOURN_ID"),
        year: str = get_secret("YEAR"),
        round_id: str = None,
    ) -> dict:
        """
        Fetches the leaderboard data
        """
        latest_file = cache.get_latest_cache_file("leaderboard")

        if cache.is_cache_fresh(latest_file):
            print("Fetched leaderboard data from cache.")
            return cache.load_from_cache(latest_file)
        params = {
            "orgId": org_id,
            "tournId": tourn_id,
            "year": year,
            "roundId": round_id,
        }
        print(
            f"Fetching and caching leaderboard for org_id: {org_id}, tourn_id: {tourn_id}, year: {year}, round_id: {round_id}"
        )
        data = super().send_request("leaderboard", params=params)
        cache.save_to_cache(data, "leaderboard")
        return data

    def get_players(
        self, last_name: str = None, first_name: str = None, player_id: str = None
    ) -> dict:
        """
        Fetches player data
        """
        params = {"lastName": last_name, "firstName": first_name, "playerId": player_id}
        print(
            f"Fetching players with last_name: {last_name}, first_name: {first_name}, player_id: {player_id}"
        )
        return super().send_request("players", params=params)

    def get_tournaments(
        self,
        org_id: int = get_secret("ORG_ID"),
        tourn_id: str = get_secret("TOURN_ID"),
        year: str = get_secret("YEAR"),
    ) -> dict:
        """
        Fetches tournament data
        """
        params = {"orgId": org_id, "tournId": tourn_id, "year": year}
        print(
            f"Fetching tournaments for org_id: {org_id}, tourn_id: {tourn_id}, year: {year}"
        )
        return super().send_request("tournaments", params=params)

    def get_scorecards(
        self,
        player_id: str,
        org_id: int = get_secret("ORG_ID"),
        tourn_id: str = get_secret("TOURN_ID"),
        year: str = get_secret("YEAR"),
        round_id: str = None,
    ) -> dict:
        """
        Fetches scorecard data
        """
        filepath = f"scorecard/{player_id}"
        latest_file = cache.get_latest_cache_file(filepath)

        if cache.is_cache_fresh(latest_file):
            print("Fetched scorecard from cache.")
            return cache.load_from_cache(latest_file)
        params = {
            "orgId": org_id,
            "tournId": tourn_id,
            "year": year,
            "playerId": player_id,
            "roundId": round_id,
        }
        print(
            f"Fetching and caching scorecard for player_id: {player_id}, org_id: {org_id}, tourn_id: {tourn_id}, year: {year}, round_id: {round_id}"
        )
        data = super().send_request("scorecard", params=params)
        cache.save_to_cache(data, filepath, f"scorecard_{player_id}")
        return data

    def get_scorecards_batch(
        self,
        player_ids: list
    ) -> dict:
        """
        Fetches scorecard data for a batch of player IDs
        """
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(self.get_scorecard, player_ids))
        return results
