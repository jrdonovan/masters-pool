from dataclasses import dataclass, field
from typing import List

from playerRound import PlayerRound

@dataclass
class Scorecard:
    _player_id: int
    _status: str
    _position: int
    _total: int
    _player_rounds: List[PlayerRound] = field(init=False, default=[])
    """
    Represents a scorecard for a player in a golf tournament.
    Attributes:
        _player_id (int): The ID of the player.
        _status (str): The status of the player (e.g., "active", "inactive").
        _position (int): The current position of the player in the tournament.
        _total (int): The total score of the player.
        _player_rounds (list): A list of PlayerRound objects representing the player's rounds.
    """

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Player ID must be an integer.")
        self._player_id = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Status must be a string.")
        self._status = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Position must be an integer.")
        self._position = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Total must be an integer.")
        self._total = value

    @property
    def player_rounds(self):
        return self._player_rounds

    @player_rounds.setter
    def player_rounds(self, value: List[PlayerRound]):
        if not isinstance(value, list):
            raise ValueError("Player rounds must be a list.")
        self._player_rounds = value