from collections.abc import Iterable
from .engine import StreamEngine
from .model import Event

def replay(engine: StreamEngine, events: Iterable[Event]) -> StreamEngine:
    for event in sorted(events, key=lambda item: item.timestamp): engine.ingest(event)
    return engine
