# input/ai_controller.py

from input.controller import InputController
from utils.types import Direction
from state.game_state import GameState


class AIController(InputController):
    """
    Simple heuristic-based AI controller.

    Policy:
    - Never reverse direction
    - Avoid walls and self-collision
    - Prefer moves that reduce Manhattan distance to food
    """

    def __init__(self, state: GameState):
        self.state = state

    def get_direction(self) -> Direction | None:
        head_x, head_y = self.state.snake.head
        food_x, food_y = self.state.food

        safe_moves: list[Direction] = []

        for direction in Direction:
            # Prevent reversing
            if direction == self.state.snake.direction.opposite():
                continue

            dx, dy = direction.value
            next_pos = (head_x + dx, head_y + dy)

            # Avoid walls
            if not self.state.in_bounds(next_pos):
                continue

            # Avoid self collision
            if next_pos in self.state.snake.body:
                continue

            safe_moves.append(direction)

        if not safe_moves:
            return None  # no safe move available

        # Choose move that minimizes distance to food
        def manhattan_distance(dir_: Direction) -> int:
            dx, dy = dir_.value
            nx, ny = head_x + dx, head_y + dy
            return abs(nx - food_x) + abs(ny - food_y)

        return min(safe_moves, key=manhattan_distance)
