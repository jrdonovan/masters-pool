from dataclasses import dataclass

@dataclass
class PlayerRound:
    """
    Represents a player's round in a golf tournament.
    Attributes:
        _player_id (int): The ID of the player.
        _thru (str): The current hole the player is on.
        _tee_time (str): The tee time of the player.
    """
    _player_id: int
    _thru: str
    _tee_time: str

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Player ID must be an integer.")
        self._player_id = value

    @property
    def thru(self):
        return self._thru

    @thru.setter
    def thru(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Thru must be a string.")
        self._thru = value

    @property
    def tee_time(self):
        return self._tee_time

    @tee_time.setter
    def tee_time(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Tee time must be a string.")
        self._tee_time = value