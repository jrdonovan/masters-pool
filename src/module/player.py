from dataclasses import dataclass

@dataclass
class Player:
    """
    Represents a golf player.
    Attributes:
        _id (int): The ID of the player.
        _full_name (str): The full name of the player.
        _first_name (str): The first name of the player.
        _last_name (str): The last name of the player.
        _country (str): The country of the player.
    """
    _id: int
    _full_name: str
    _first_name: str
    _last_name: str
    _country: str

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer.")
        self._id = value

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Full name must be a string.")
        self._full_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("First name must be a string.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string.")
        self._last_name = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Country must be a string.")
        self._country = value
