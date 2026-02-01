# systems/spawning.py
import random
from state.game_state import GameState


def spawn_food(state: GameState) -> None:
    if state.snake.head != state.food:
        return

    while True:
        pos = (
            random.randint(0, state.width - 1),
            random.randint(0, state.height - 1),
        )
        if not state.snake.occupies(pos):
            state.food = pos
            return
