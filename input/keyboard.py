# input/keyboard.py
import pygame
from input.controller import InputController
from utils.types import Direction


class KeyboardController(InputController):
    def __init__(self):
        self._pending: Direction | None = None

    def process_pygame_events(self, events) -> None:
        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            if event.key in (pygame.K_UP, pygame.K_w):
                self._pending = Direction.UP
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self._pending = Direction.DOWN
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                self._pending = Direction.LEFT
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self._pending = Direction.RIGHT

    def get_direction(self) -> Direction | None:
        d = self._pending
        self._pending = None
        return d

