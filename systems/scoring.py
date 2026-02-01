# systems/scoring.py
from state.game_state import GameState


def update_score(state: GameState) -> None:
    if state.snake.head == state.food:
        state.snake.grow()
        state.score += 1
