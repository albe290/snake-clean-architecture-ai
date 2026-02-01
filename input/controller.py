# input/controller.py

from abc import ABC, abstractmethod
from utils.types import Direction


class InputController(ABC):
    def process_pygame_events(self, events) -> None:
        """
        Optional hook for event-driven controllers (keyboard).
        AI controllers safely ignore events.
        """
        return

    @abstractmethod
    def get_direction(self) -> Direction | None:
        pass
