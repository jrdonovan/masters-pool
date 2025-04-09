from dataclasses import dataclass, field

@dataclass
class Hole:
    """
    Represents a hole in the golf course.
    Attributes:
        _hole_id (int): The ID of the hole.
        _par (int): The par value of the hole.
        _previous_hole_id (int): The ID of the previous hole.
    """
    _hole_id: int
    _par: int
    _previous_hole_id: int = field(init=False)

    def __post__init__(self):
        self._calculate_previous_hole_id()

    @property
    def hole_id(self):
        return self._hole_id

    @hole_id.setter
    def hole_id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Hole ID must be an integer.")
        self._hole_id = value

    @property
    def par(self):
        return self._par

    @par.setter
    def par(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Par must be an integer.")
        self._par = value

    @property
    def previous_hole_id(self):
        return self._previous_hole_id

    def _calculate_previous_hole_id(self) -> None:
        """
        Helper method to calculate the previous hole ID.
        """
        self.previous_hole_id = (18 if self.hole_id == 1 else self.hole_id - 1) if self.hole_id > 1 else None
