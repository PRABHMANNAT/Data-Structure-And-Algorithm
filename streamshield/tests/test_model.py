import pytest
from streamshield.model import Event

def test_event_requires_key() -> None:
    with pytest.raises(ValueError): Event("", 0)
