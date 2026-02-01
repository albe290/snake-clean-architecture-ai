# utils/types.py
from enum import Enum
from typing import Tuple

Position = Tuple[int, int]


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def opposite(self) -> "Direction":
        dx, dy = self.value
        return Direction((-dx, -dy))
