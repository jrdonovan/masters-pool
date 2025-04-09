from collections import OrderedDict
from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class Entry:
    _timestamp: datetime
    _email: str
    _name: str
    _players: OrderedDict
    _strokes: int
    """
    Represents an entry in the Masters Pool.
    Attributes:
        _timestamp (datetime): The timestamp of the entry.
        _email (str): The email address of the participant.
        _name (str): The name of the entry.
        _players (OrderedDict): A dictionary containing player selections.
        _strokes (int): Total combined strokes of the winner.
    """

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: datetime):
        if not isinstance(value, datetime):
            raise ValueError("Timestamp must be a datetime object.")
        self._timestamp = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Email must be a string.")
        self._email = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value: OrderedDict):
        if not isinstance(value, OrderedDict):
            raise ValueError("Players must be an ordered dictionary.")
        self._players = value

    @property
    def strokes(self):
        return self._strokes

    @strokes.setter
    def strokes(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Strokes must be an integer.")
        self._strokes = value

    def calculate_fanduel_score(self) -> None:
        """
        Calculates the FanDuel score based on the strokes.
        """
        # Placeholder for actual calculation logic
        self._fanduel_score = self._strokes * 0.1

    def to_dict(self, descriptive: bool = False) -> dict:
        d = {"name": self._name}
        if descriptive:
            d["timestamp"] = self.timestamp
            d["email"] = self.email

        d = {**d, **self.players}
        d["strokes"] = self._strokes
        return d
