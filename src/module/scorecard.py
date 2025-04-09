from dataclasses import dataclass, field
from typing import List, Dict

from src.module.fanduel import FanDuel
from src.module.playerRound import PlayerRound


@dataclass
class Scorecard:
    """
    Represents a scorecard for a player in a golf tournament.
    Attributes:
        _player_id (int): The ID of the player.
        _status (str): The status of the player (e.g., "active", "inactive").
        _position (str): The current position of the player in the tournament.
        _total (int): The total score of the player.
        _course_id (str): The ID of the golf course.
        _player_rounds (List[PlayerRound]): A list of PlayerRound objects representing the player's rounds.
        _fanduel_score (float): The FanDuel score for the scorecard.
    """

    _player_id: int
    _status: str
    _position: str
    _total: int
    _course_id: str
    _player_rounds: List[PlayerRound] = field(init=False)
    _fanduel_score: float = field(init=False, default=0.0)

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
    def course_id(self):
        return self._course_id

    @property
    def player_rounds(self):
        return self._player_rounds

    @player_rounds.setter
    def player_rounds(self, value: List[PlayerRound]):
        if not isinstance(value, list):
            raise ValueError("Player rounds must be a list.")
        self._player_rounds = value

    @property
    def fanduel_score(self):
        return self._fanduel_score

    @fanduel_score.setter
    def fanduel_score(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Fanduel score must be a number.")
        self._fanduel_score = value

    def initialize_player_rounds(self, round_data: Dict) -> None:
        rounds = []
        for round in round_data:
            round_obj = PlayerRound(
                _round_id=round["roundId"],
                _player_id=self._player_id,
                _complete=round["roundComplete"],
                _starting_hole=round["startingHole"],
                _current_hole=round["currentHole"],
                _current_round_score=round["currentRoundScore"],
                _strokes=round["totalShots"],
            )

            round_obj.initialize_holes(round["holes"])
            rounds.append(round_obj)
        self.player_rounds = rounds

        self._calculate_fanduel_score()

    def _calculate_fanduel_score(self) -> None:
        """
        Calculate the FanDuel score for the scorecard.
        """
        self.fanduel_score = 0.0
        for round in self.player_rounds:
            self.fanduel_score += round.fanduel_score

        fd = FanDuel()
        self.fanduel_score = fd.calculate_position_score(self.position)
