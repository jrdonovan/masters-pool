from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class Entry:
    _timestamp: datetime
    _email: str
    _name: str
    _players: Dict
    _strokes: int
    """
    Represents an entry in the Masters Pool.
    Attributes:
        _timestamp (datetime): The timestamp of the entry.
        _email (str): The email address of the participant.
        _name (str): The name of the entry.
        _players (dict): A dictionary containing player selections.
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
    def players(self, value: Dict):
        if not isinstance(value, dict):
            raise ValueError("Players must be a dictionary.")
        self._players = value

    @property
    def strokes(self):
        return self._strokes

    @strokes.setter
    def strokes(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Strokes must be an integer.")
        self._strokes = value

    def to_dict(self) -> dict:
        d = {"timestamp": self._timestamp, "email": self._email, "name": self._name}
        parsed_players = {
            k: list(map(lambda x: x.strip(), v.split(",")))
            for k, v in self._players.items()
        }
        d = {**d, **parsed_players}
        d["strokes"] = self._strokes
        return d
