from collections import defaultdict, OrderedDict
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict

from src.module.fanduel import FanDuel
from src.module.hole import Hole
import src.utils.parse as parse


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
        _hole_results (defaultdict): A dictionary to store the results of each hole.
        _fanduel_score (Decimal): The FanDuel score for the round.
    """

    _round_id: int
    _player_id: int
    _complete: bool
    _starting_hole: int
    _current_hole: int
    _current_round_score: str
    _strokes: int
    _holes: OrderedDict = field(init=False, repr=False, default_factory=lambda: OrderedDict())
    _hole_results: defaultdict = field(init=False, default_factory=lambda: defaultdict(int))
    _fanduel_score: Decimal = field(init=False, default=Decimal("0"))

    def __post_init__(self):
        self.round_id = parse.parse_dict_to_number(self.round_id)
        self.starting_hole = parse.parse_dict_to_number(self.starting_hole)
        self.current_hole = parse.parse_dict_to_number(self.current_hole)

    @property
    def round_id(self):
        return self._round_id

    @round_id.setter
    def round_id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Round ID must be an integer.")
        self._round_id = value

    @property
    def player_id(self):
        return self._player_id

    @property
    def complete(self):
        return self._complete

    @property
    def starting_hole(self):
        return self._starting_hole

    @starting_hole.setter
    def starting_hole(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Starting hole must be an integer.")
        self._starting_hole = value

    @property
    def current_hole(self):
        return self._current_hole

    @current_hole.setter
    def current_hole(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Current hole must be an integer.")
        self._current_hole = value

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
    def holes(self, value: OrderedDict):
        if not isinstance(value, OrderedDict):
            raise ValueError("Holes must be an ordered dictionary.")
        self._holes = value

    @property
    def hole_results(self):
        return self._hole_results

    @hole_results.setter
    def hole_results(self, value: defaultdict):
        if not isinstance(value, defaultdict):
            raise ValueError("Hole results must be a defaultdict.")
        self._hole_results = value

    @property
    def fanduel_score(self):
        return self._fanduel_score

    @fanduel_score.setter
    def fanduel_score(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise ValueError("Fanduel score must be a number.")
        self._fanduel_score = value

    def initialize_holes(self, hole_data: Dict) -> None:
        for _, hole in hole_data.items():
            hole_obj = Hole(
                _id=hole["holeId"], _par=hole["par"], _score=hole["holeScore"]
            )
            self.holes[hole_obj.id] = hole_obj

        self._aggregate_hole_results()
        self._calculate_fanduel_score()

    def _aggregate_hole_results(self) -> None:
        """
        Aggregate the hole results for the round.
        """
        for _, hole in self.holes.items():
            self.hole_results[hole.result] += 1

    def _calculate_fanduel_score(self) -> None:
        """
        Calculate the FanDuel score for the round.
        """
        self.fanduel_score = Decimal("0")
        for _, hole in self.holes.items():
            self.fanduel_score += hole.fanduel_score

            if hole.id != self.starting_hole:
                previous_hole_result = self.holes.get(hole.previous_hole_id).result
                self.fanduel_score += FanDuel.calculate_streak_score(hole.result, previous_hole_result)
                self.fanduel_score += FanDuel.calculate_bounce_back_score(hole.result, previous_hole_result)

        if self.complete:
            bogey_count = self.hole_results.get("BOGEY", 0) + self.hole_results.get("DOUBLE_BOGEY_OR_WORSE", 0)
            self.fanduel_score += FanDuel.calculate_bogey_free_round_score(bogey_count)

        birdie_or_better_count = self.hole_results.get("BIRDIE", 0) + self.hole_results.get("EAGLE_OR_BETTER", 0)
        self.fanduel_score += FanDuel.calculate_birdie_or_better_score(birdie_or_better_count)
