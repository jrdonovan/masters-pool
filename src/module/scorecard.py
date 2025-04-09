from dataclasses import dataclass
from typing import List

from src.module.playerRound import PlayerRound

@dataclass
class Scorecard:
    """
    Represents a scorecard for a player in a golf tournament.
    Attributes:
        _player_id (int): The ID of the player.
        _status (str): The status of the player (e.g., "active", "inactive").
        _position (int): The current position of the player in the tournament.
        _total (int): The total score of the player.
        _player_rounds (List[PlayerRound]): A list of PlayerRound objects representing the player's rounds.
    """
    _player_id: int
    _status: str
    _position: int
    _total: int
    _course_id: int
    _player_rounds: List[PlayerRound]

    @property
    def player_id(self):
        return self._player_id

    @property
    def status(self):
        return self._status

    @property
    def position(self):
        return self._position

    @property
    def total(self):
        return self._total

    @property
    def player_rounds(self):
        return self._player_rounds
