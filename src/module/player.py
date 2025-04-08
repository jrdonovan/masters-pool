from dataclasses import dataclass, field
from typing import Dict

from src.module.playerRound import PlayerRound
from src.module.scorecard import Scorecard

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
        _playing_info (dict): Information about the player's current status in the tournament.
        _scorecard (Scorecard): The player's scorecard in the tournament.
    """
    _id: int
    _first_name: str
    _last_name: str
    _is_amateur: bool
    _full_name: str = field(init=False, default="")
    _playing_info: Dict = field(default_factory=dict)
    _scorecard: Scorecard = field(init=False)

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"
        self._initialize_scorecard()

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
    def playing_info(self):
        return self._playing_info

    @playing_info.setter
    def playing_info(self, value: Dict):
        if not isinstance(value, dict):
            raise ValueError("Playing info must be a dictionary.")
        self._playing_info = value

    @property
    def scorecard(self):
        return self._scorecard

    @scorecard.setter
    def scorecard(self, value: Scorecard):
        if not isinstance(value, Scorecard):
            raise ValueError("Scorecard must be a Scorecard object.")
        self._scorecard = value

    def _initialize_scorecard(self):
        from api.liveGolfData import LiveGolfData

        api = LiveGolfData()
        raw_scorecard = api.get_scorecards(player_id=self._id)

        rounds = []
        for round in raw_scorecard:
            round_obj = PlayerRound(
                _round_id=round["roundId"],
                _player_id=self._id,
                _complete=round["roundComplete"],
                _starting_hole=round["startingHole"],
                _current_hole=round["currentHole"],
                _current_round_score=round["currentRoundScore"],
                _strokes=round["totalShots"],
            )
            rounds.append(round_obj)

        self.scorecard = Scorecard(
            _player_id=self._id,
            _status=self.playing_info["status"],
            _position=self.playing_info["position"],
            _total=self.playing_info["total"],
            _course_id=self.playing_info["course_id"],
            _player_rounds=rounds
        )
