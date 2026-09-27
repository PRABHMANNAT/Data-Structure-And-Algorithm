from __future__ import annotations
import random
from collections.abc import Iterator
from .model import Event

def events(seed: int = 0, count: int = 100) -> Iterator[Event]:
    rng = random.Random(seed)
    for timestamp in range(count):
        yield Event(f"key-{rng.randrange(10)}", timestamp, rng.random())
