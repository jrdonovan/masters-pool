from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Organization:
    """
    Represents a golf organization.
    Attributes:
        _name (str): The name of the organization.
        _external_id (str): The external ID of the organization.
        _id (int): The ID of the organization.
    """
    _name: str
    _external_id: str
    _id: Optional[int] = field(default=None)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer.")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value: str):
        if not isinstance(value, str):
            raise ValueError("External ID must be a string.")
        self._external_id = value
