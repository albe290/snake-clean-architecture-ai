# state/snake.py
from collections import deque
from typing import Deque
from utils.types import Position, Direction


class Snake:
    def __init__(self, start: Position, direction: Direction):
        self.body: Deque[Position] = deque([start])
        self.direction = direction
        self._grow_pending = 0

    @property
    def head(self) -> Position:
        return self.body[0]

    def set_direction(self, new_direction: Direction) -> None:
        if new_direction != self.direction.opposite():
            self.direction = new_direction

    def move(self) -> None:
        dx, dy = self.direction.value
        x, y = self.head
        new_head = (x + dx, y + dy)

        self.body.appendleft(new_head)

        if self._grow_pending > 0:
            self._grow_pending -= 1
        else:
            self.body.pop()

    def grow(self, amount: int = 1) -> None:
        self._grow_pending += amount

    def occupies(self, position: Position) -> bool:
        return position in self.body
