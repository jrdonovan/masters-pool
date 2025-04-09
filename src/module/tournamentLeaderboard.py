from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime
import pandas as pd
from typing import List, Dict

from src.module.player import Player
import src.utils as utils


@dataclass
class TournamentLeaderboard:
    """
    Represents a golf tournament leaderboard.
    Attributes:
        _org_id (int): The organization ID.
        _year (str): The year of the tournament.
        _tourn_id (str): The tournament ID.
        _current_status (str): The status of the tournament.
        _current_round_status (str): The status of the round.
        _current_round_id (int): The round ID.
        _last_updated (datetime): The last updated timestamp.
        _cut_lines (List[Dict]): The cut lines for the tournament.
        _players (OrderedDict): The players in the tournament.
    """

    _org_id: int
    _year: str
    _tourn_id: str
    _current_status: str
    _current_round_status: str
    _current_round_id: int
    _last_updated: datetime
    _cut_lines: List[Dict]
    _players: OrderedDict = field(init=False, default_factory=OrderedDict)

    def __post_init__(self):
        self.current_round_id = utils.parse_dict_to_number(self.current_round_id)

        for cl in self.cut_lines:
            cut_count = cl["cutCount"]
            cl["cutCount"] = utils.parse_dict_to_number(cut_count)

        self.last_updated = utils.parse_dict_to_date(self.last_updated)

    @property
    def org_id(self):
        return self._org_id

    @property
    def year(self):
        return self._year

    @property
    def tourn_id(self):
        return self._tourn_id

    @property
    def current_status(self):
        return self._current_status

    @property
    def current_round_status(self):
        return self._current_round_status

    @property
    def current_round_id(self):
        return self._current_round_id

    @current_round_id.setter
    def current_round_id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Current Round ID must be an integer.")
        self._current_round_id = value

    @property
    def last_updated(self):
        return self._last_updated

    @last_updated.setter
    def last_updated(self, value: datetime):
        if not isinstance(value, datetime):
            raise ValueError("Last updated must be a datetime object.")
        self._last_updated = value

    @property
    def cut_lines(self):
        return self._cut_lines

    @cut_lines.setter
    def cut_lines(self, value: List[Dict]):
        if not isinstance(value, list):
            raise ValueError("Cut lines must be a list.")
        self._cut_lines = value

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value: OrderedDict):
        if not isinstance(value, OrderedDict):
            raise ValueError("Players must be an OrderedDict.")
        self._players = value

    def initialize_players(self, leaderboard_data: List) -> None:
        d = OrderedDict()
        for p in leaderboard_data:
            for r in p["rounds"]:
                r["roundId"] = utils.parse_dict_to_number(r["roundId"])
                r["strokes"] = utils.parse_dict_to_number(r["strokes"])

            player = Player(
                _id=p["playerId"],
                _first_name=p["firstName"],
                _last_name=p["lastName"],
                _is_amateur=p["isAmateur"],
            )

            d[player.id] = {
                "position": p["position"],
                "status": p["status"].upper(),
                "total": p["total"],
                "player": player,
                "rounds": p["rounds"],
            }
        self.players = d

    def initialize_player_scorecards(self):
        for p in self.players:
            p.initialize_scorecard(
                status=p.playing_info["status"],
                position=p.playing_info["position"],
                total=p.playing_info["total"],
                course_id=p.playing_info["course_id"],
            )

    def to_dataframe(self) -> pd.DataFrame:
        """
        Converts the TournamentLeaderboard object to a pandas DataFrame.
        This method is useful for displaying the leaderboard in a tabular format.
        """
        data = []
        for _, player_info in self.players.items():
            rounds = {r["roundId"]: r["scoreToPar"] for r in player_info["rounds"]}
            data.append(
                {
                    "Position": player_info["position"],
                    "Player": player_info["player"].full_name,
                    "Total Score": player_info["total"],
                    "Round 1": rounds.get(1, "-"),
                    "Round 2": rounds.get(2, "-"),
                    "Round 3": rounds.get(3, "-"),
                    "Round 4": rounds.get(4, "-"),
                    "Status": player_info["status"],
                }
            )
        df = pd.DataFrame(data)
        df.index += 1
        return df
