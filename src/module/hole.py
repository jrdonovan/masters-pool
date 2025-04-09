from dataclasses import dataclass, field

from src.module.fanduel import FanDuel
import src.utils.parse as parse


@dataclass
class Hole:
    """
    Represents a hole in the golf course.
    Attributes:
        _id (int): The ID of the hole.
        _par (int): The par value of the hole.
        _score (int): The number of strokes taken by the player on the hole.
        _previous_hole_id (int): The ID of the previous hole.
        _result (str): The result of the hole (e.g., "EAGLE", "BIRDIE", "PAR", "BOGEY").
        _fanduel_score (float): The FanDuel score for the hole.
    """

    _id: int
    _par: int
    _score: int
    _previous_hole_id: int = field(init=False, repr=False)
    _result: str = field(init=False, default="")
    _fanduel_score: float = field(init=False, default=0.0)

    def __post_init__(self):
        self.id = parse.parse_dict_to_number(self.id)
        self.par = parse.parse_dict_to_number(self.par)
        self.score = parse.parse_dict_to_number(self.score)
        self._calculate_previous_hole_id()
        self._calculate_hole_result()
        self._calculate_fanduel_score()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer.")
        self._id = value

    @property
    def par(self):
        return self._par

    @par.setter
    def par(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Par must be an integer.")
        self._par = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Score must be an integer.")
        self._score = value

    @property
    def previous_hole_id(self):
        return self._previous_hole_id

    @previous_hole_id.setter
    def previous_hole_id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Previous hole ID must be an integer.")
        self._previous_hole_id = value

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Result must be a string.")
        self._result = value

    @property
    def fanduel_score(self):
        return self._fanduel_score

    @fanduel_score.setter
    def fanduel_score(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("FanDuel score must be a number.")
        self._fanduel_score = value

    def _calculate_previous_hole_id(self) -> None:
        """
        Helper method to calculate the previous hole ID.
        """
        self.previous_hole_id = 18 if self.id == 1 else self.id - 1

    def _calculate_hole_result(self) -> None:
        diff = self.par - self.score
        if diff < 0:
            self.result = "DOUBLE_BOGEY_OR_WORSE" if abs(diff) > 1 else "BOGEY"
        elif diff == 0:
            self.result = "PAR"
        else:
            self.result = "EAGLE_OR_BETTER" if diff > 1 else "BIRDIE"

    def _calculate_fanduel_score(self) -> None:
        """
        Calculate the FanDuel score for the hole.
        """
        fd = FanDuel()
        self.fanduel_score = fd.calculate_hole_result_score(self.result)
