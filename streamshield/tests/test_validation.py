import pytest
from streamshield.model import Event
from streamshield.validation import validate_event

def test_rejects_empty_label() -> None:
    with pytest.raises(ValueError): validate_event(Event("x", 0, labels={"": "a"}))
