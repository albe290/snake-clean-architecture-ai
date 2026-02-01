# state/game_state.py
from utils.types import Position, Direction
from state.snake import Snake


class GameState:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.snake = Snake(
            start=(width // 2, height // 2),
            direction=Direction.RIGHT
        )

        self.food: Position = (5, 5)
        self.score = 0
        self.is_alive = True

    def in_bounds(self, position: Position) -> bool:
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def update(self) -> None:
        """
        Intentionally empty.
        GameState does NOT orchestrate logic.
        """
        pass

