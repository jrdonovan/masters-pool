from dataclasses import dataclass, field

def _get_previous_hole_id(hole_id: int) -> int:
    """
    Helper function to get the previous hole ID.
    Args:
        hole_id (int): The current hole ID.
    Returns:
        int: The previous hole ID.
    """
    return 18 if hole_id == 1 else hole_id - 1

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
    _previous_hole_id: int = field(default_factory=_get_previous_hole_id)

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
