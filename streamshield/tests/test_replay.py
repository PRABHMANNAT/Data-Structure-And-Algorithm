from streamshield.engine import StreamEngine
from streamshield.model import Event
from streamshield.replay import replay

def test_replay_orders_events() -> None:
    assert replay(StreamEngine(), [Event("a", 2), Event("b", 1)]).stats().accepted == 2
