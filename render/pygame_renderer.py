# render/pygame_renderer.py
import pygame
from state.game_state import GameState
from config import CELL_SIZE, HUD_HEIGHT, WINDOW_TITLE


class PygameRenderer:
    def __init__(self, grid_width: int, grid_height: int):
        pygame.display.set_caption(WINDOW_TITLE)

        self.grid_width = grid_width
        self.grid_height = grid_height

        self.width_px = grid_width * CELL_SIZE
        self.height_px = grid_height * CELL_SIZE + HUD_HEIGHT

        self.screen = pygame.display.set_mode((self.width_px, self.height_px))
        self.font = pygame.font.SysFont("arial", 22)

    def _cell_rect(self, x: int, y: int) -> pygame.Rect:
        # y is offset by HUD
        return pygame.Rect(x * CELL_SIZE, HUD_HEIGHT + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def render(self, state: GameState) -> None:
        # Background
        self.screen.fill((15, 15, 18))

        # HUD bar
        pygame.draw.rect(self.screen, (25, 25, 30), pygame.Rect(0, 0, self.width_px, HUD_HEIGHT))

        # Score text
        score_text = f"Score: {state.score}"
        if not state.is_alive:
            score_text += "   |   GAME OVER (Press R to restart, Esc to quit)"
        text_surface = self.font.render(score_text, True, (230, 230, 230))
        self.screen.blit(text_surface, (12, 12))

        # Optional grid (subtle)
        for x in range(self.grid_width):
            pygame.draw.line(
                self.screen, (22, 22, 26),
                (x * CELL_SIZE, HUD_HEIGHT),
                (x * CELL_SIZE, HUD_HEIGHT + self.grid_height * CELL_SIZE),
                1
            )
        for y in range(self.grid_height):
            pygame.draw.line(
                self.screen, (22, 22, 26),
                (0, HUD_HEIGHT + y * CELL_SIZE),
                (self.grid_width * CELL_SIZE, HUD_HEIGHT + y * CELL_SIZE),
                1
            )

        # Food
        fx, fy = state.food
        pygame.draw.rect(self.screen, (255, 80, 80), self._cell_rect(fx, fy), border_radius=6)

        # Snake
        for i, (sx, sy) in enumerate(state.snake.body):
            rect = self._cell_rect(sx, sy)
            if i == 0:
                pygame.draw.rect(self.screen, (80, 255, 120), rect, border_radius=8)  # head
            else:
                pygame.draw.rect(self.screen, (60, 200, 95), rect, border_radius=6)   # body

        pygame.display.flip()
