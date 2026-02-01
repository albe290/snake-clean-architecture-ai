# systems/collision.py
from state.game_state import GameState


def check_collisions(state: GameState) -> None:
    head = state.snake.head

    # Wall collision
    if not state.in_bounds(head):
        state.is_alive = False
        return

    # Self collision
    if head in list(state.snake.body)[1:]:
        state.is_alive = False
