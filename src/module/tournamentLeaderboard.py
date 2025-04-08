from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

from src.module.player import Player

@dataclass
class TournamentLeaderboard:
    """
    Represents a golf tournament leaderboard.
    Attributes:
        org_id (int): The organization ID.
        year (str): The year of the tournament.
        tourn_id (str): The tournament ID.
        status (str): The status of the tournament.
        round_status (str): The status of the round.
        round_id (str): The round ID.
        last_updated (datetime): The last updated timestamp.
        cut_lines (List[Dict]): The cut lines for the tournament.
        leaderboard_rows (List[Dict]): The leaderboard rows.
        players (List[Player]): The players in the tournament.
    """
    _org_id: int
    _year: str
    _tourn_id: str
    _status: str
    _round_status: str
    _round_id: str
    _last_updated: datetime
    _cut_lines: List[Dict]
    _leaderboard_rows: List[Dict]
    _players: List[Player] = field(init=False)

    def __post_init__(self):
        players = []
        for p in self.leaderboard_rows:
            player_args = {
                "_id": p["playerId"],
                "_first_name": p["firstName"],
                "_last_name": p["lastName"],
                "_is_amateur": p["isAmateur"]
            }
            player_obj = Player(
                **player_args,
                _playing_info={
                    "course_id": p["courseId"],
                    "status": p["status"],
                    "position": p["position"],
                    "total": p["total"],
                    "total_strokes_from_completed_rounds": p["totalStrokesFromCompletedRounds"]
                }
            )
            players.append(player_obj)
        self.players = players

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
    def status(self):
        return self._status

    @property
    def round_status(self):
        return self._round_status

    @property
    def round_id(self):
        return self._round_id

    @property
    def last_updated(self):
        return self._last_updated

    @property
    def cut_lines(self):
        return self._cut_lines

    @property
    def leaderboard_rows(self):
        return self._leaderboard_rows

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value: List[Player]):
        if not isinstance(value, list):
            raise ValueError("Players must be a list.")
        self._players = value
