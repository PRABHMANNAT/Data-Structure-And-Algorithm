from streamshield.model import Event
from streamshield.serializers import event_from_json, event_to_json

def test_event_json_roundtrip() -> None:
    assert event_from_json(event_to_json(Event("x", 1))) == Event("x", 1)
