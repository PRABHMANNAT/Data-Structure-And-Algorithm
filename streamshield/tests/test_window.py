from streamshield.model import Event
from streamshield.window import SlidingWindow

def test_expiry_updates_total() -> None:
    window = SlidingWindow(10); window.add(Event("a", 1, 2)); window.add(Event("b", 12, 3))
    assert window.expire(12) == 1 and window.total == 3
