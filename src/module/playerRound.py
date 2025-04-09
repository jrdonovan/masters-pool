from dataclasses import dataclass, field
from typing import List, Dict

from src.module.hole import Hole


@dataclass
class PlayerRound:
    """
    Represents a player's round in a golf tournament.
    Attributes:
        _round_id (int): The ID of the round.
        _player_id (int): The ID of the player.
        _complete (bool): Indicates if the round is complete.
        _starting_hole (int): The hole where the player started.
        _current_hole (int): The current hole the player is on.
        _current_round_score (str): The current score of the player in the round.
        _strokes (int): The number of strokes taken by the player in the round.
        _holes (List[Hole]): A list of Hole objects representing the holes played in the round.
        _fanduel_score (float): The FanDuel score for the round.
    """

    _round_id: int
    _player_id: int
    _complete: bool
    _starting_hole: int
    _current_hole: int
    _current_round_score: str
    _strokes: int
    _holes: List[Hole] = field(init=False)
    _fanduel_score: float = field(init=False, default=0.0)

    @property
    def round_id(self):
        return self._round_id

    @property
    def player_id(self):
        return self._player_id

    @property
    def complete(self):
        return self._complete

    @property
    def starting_hole(self):
        return self._starting_hole

    @property
    def current_hole(self):
        return self._current_hole

    @property
    def current_round_score(self):
        return self._current_round_score

    @property
    def strokes(self):
        return self._strokes

    @property
    def holes(self):
        return self._holes

    @holes.setter
    def holes(self, value: List[Hole]):
        if not isinstance(value, list):
            raise ValueError("Holes must be a list.")
        self._holes = value

    @property
    def fanduel_score(self):
        return self._fanduel_score

    @fanduel_score.setter
    def fanduel_score(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Fanduel score must be a number.")
        self._fanduel_score = value

    def initialize_holes(self, hole_data: Dict) -> None:
        holes = []
        for _, hole in hole_data.items():
            hole_obj = Hole(
                _id=hole["holeId"], _par=hole["par"], _score=hole["holeScore"]
            )
            holes.append(hole_obj)

        self.holes = holes

        self._calculate_fanduel_score()

    def _calculate_fanduel_score(self) -> None:
        """
        Calculate the FanDuel score for the round.
        """
        self.fanduel_score = 0
        for hole in self.holes:
            self.fanduel_score += hole.fanduel_score
