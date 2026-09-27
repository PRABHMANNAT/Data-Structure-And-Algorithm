import pytest
from streamshield.engine import StreamEngine
from streamshield.errors import LateEvent
from streamshield.model import Event

def test_late_event_is_counted() -> None:
    engine = StreamEngine(lateness_ms=2); engine.ingest(Event("a", 10))
    with pytest.raises(LateEvent): engine.ingest(Event("a", 7))
    assert engine.stats().rejected_late == 1
