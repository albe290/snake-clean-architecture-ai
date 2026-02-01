# systems/movement.py
from state.game_state import GameState


def update_movement(state: GameState) -> None:
    if not state.is_alive:
        return

    state.snake.move()
