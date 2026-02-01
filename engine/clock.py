# engine/clock.py
import time


class GameClock:
    def __init__(self, ticks_per_second: int):
        self.tick_duration = 1.0 / ticks_per_second
        self.last_tick = time.perf_counter()

    def wait_for_next_tick(self) -> None:
        now = time.perf_counter()
        elapsed = now - self.last_tick
        remaining = self.tick_duration - elapsed

        if remaining > 0:
            time.sleep(remaining)

        self.last_tick = time.perf_counter()
