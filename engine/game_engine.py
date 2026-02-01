# engine/game_engine.py

from state.game_state import GameState
from engine.clock import GameClock
from input.controller import InputController

from systems.movement import update_movement
from systems.collision import check_collisions
from systems.scoring import update_score
from systems.spawning import spawn_food


class GameEngine:
    def __init__(
        self,
        state: GameState,
        ticks_per_second: int = 10,
        controller: InputController | None = None,
    ):
        self.state = state
        self.clock = GameClock(ticks_per_second)
        self.controller = controller
        self.running = True

    def tick(self) -> None:
        if not self.state.is_alive:
            self.running = False
            return

        # Handle input (human or AI)
        if self.controller:
            new_direction = self.controller.get_direction()
            if new_direction:
                self.state.snake.set_direction(new_direction)

        # Run systems in deterministic order
        update_movement(self.state)
        check_collisions(self.state)
        update_score(self.state)
        spawn_food(self.state)

    def run(self) -> None:
        while self.running:
            self.tick()
            self.clock.wait_for_next_tick()
