from collections.abc import Iterator
from contextlib import contextmanager
from .engine import StreamEngine
from .model import Event

@contextmanager
def buffered_ingest(engine: StreamEngine) -> Iterator[list[Event]]:
    """Collect a batch and apply it only when the context succeeds."""
    batch: list[Event] = []
    yield batch
    for event in batch: engine.ingest(event)
