from dataclasses import dataclass, field

from src.module.scorecard import Scorecard
from src.utils.scorecard import fetch_scorecards


@dataclass
class Player:
    """
    Represents a golf player.
    Attributes:
        _id (int): The ID of the player.
        _first_name (str): The first name of the player.
        _last_name (str): The last name of the player.
        _is_amateur (bool): Indicator of a player's amateur status.
        _full_name (str): The full name of the player.
        _scorecard (Scorecard): The player's scorecard in the tournament.
        _fanduel_score (float): The FanDuel score for the player.
    """

    _id: int
    _first_name: str
    _last_name: str
    _is_amateur: bool
    _full_name: str = field(init=False, default="")
    _scorecard: Scorecard = field(init=False, repr=False)
    _fanduel_score: float = field(init=False, default=0.0)

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def is_amateur(self):
        return self._is_amateur

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Full name must be a string.")
        self._full_name = value

    @property
    def scorecard(self):
        return self._scorecard

    @scorecard.setter
    def scorecard(self, value: Scorecard):
        if not isinstance(value, Scorecard):
            raise ValueError("Scorecard must be a Scorecard object.")
        self._scorecard = value

    @property
    def fanduel_score(self):
        return self._fanduel_score

    @fanduel_score.setter
    def fanduel_score(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Fanduel score must be a number.")
        self._fanduel_score = value

    def initialize_scorecard(
        self, status: str, position: int, total: int, course_id: str
    ) -> None:
        """
        Initialize the player's scorecard by fetching data from the API.
        This method fetches the scorecard data for the player and populates the scorecard attribute.
        """
        player_scorecard = fetch_scorecards(self.id)

        scorecard = Scorecard(
            _player_id=self._id,
            _status=status,
            _position=position,
            _total=total,
            _course_id=course_id
        )
        scorecard.initialize_player_rounds(player_scorecard)
        self.scorecard = scorecard

        self.fanduel_score = self.scorecard.fanduel_score
