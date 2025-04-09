from dataclasses import dataclass, field
from typing import List

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
    """
    _round_id: int
    _player_id: int
    _complete: bool
    _starting_hole: int
    _current_hole: int
    _current_round_score: str
    _strokes: int
    _holes: List[Hole] = field(init=False)

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
