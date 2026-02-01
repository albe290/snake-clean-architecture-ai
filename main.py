# main.py
import time
import pygame

from config import GRID_WIDTH, GRID_HEIGHT, TICKS_PER_SECOND, FPS
from state.game_state import GameState
from engine.game_engine import GameEngine
from input.keyboard import KeyboardController
from input.ai_controller import AIController
from render.pygame_renderer import PygameRenderer


def build_game():
    state = GameState(GRID_WIDTH, GRID_HEIGHT)

    human_controller = KeyboardController()
    ai_controller = AIController(state)

    engine = GameEngine(
        state,
        ticks_per_second=TICKS_PER_SECOND,
        controller=ai_controller,  # start with AI
    )

    renderer = PygameRenderer(GRID_WIDTH, GRID_HEIGHT)

    return state, human_controller, ai_controller, engine, renderer


def main():
    pygame.init()

    state, human_controller, ai_controller, engine, renderer = build_game()
    active_controller = ai_controller

    render_clock = pygame.time.Clock()
    tick_duration = 1.0 / TICKS_PER_SECOND
    last_tick = time.perf_counter()

    running = True
    while running:
        # Collect events once per frame
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Quit
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Toggle AI ↔ Human
                if event.key == pygame.K_t:
                    if active_controller is ai_controller:
                        active_controller = human_controller
                        print("Switched to HUMAN controller")
                    else:
                        active_controller = ai_controller
                        print("Switched to AI controller")

                    engine.controller = active_controller

                # Restart when dead
                if not state.is_alive and event.key == pygame.K_r:
                    state, human_controller, ai_controller, engine, renderer = build_game()
                    active_controller = ai_controller
                    last_tick = time.perf_counter()

        # Feed events to the active controller (keyboard consumes, AI ignores)
        engine.controller.process_pygame_events(events)

        # Deterministic ticks (independent of FPS)
        now = time.perf_counter()
        while now - last_tick >= tick_duration and engine.running:
            engine.tick()
            last_tick += tick_duration

        # Draw every frame
        renderer.render(state)

        # Cap render FPS
        render_clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()



