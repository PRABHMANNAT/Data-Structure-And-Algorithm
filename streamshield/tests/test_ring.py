import pytest
from streamshield.ring import RingBuffer

def test_fifo_and_capacity() -> None:
    ring = RingBuffer[int](2); ring.append(1); ring.append(2)
    assert ring.popleft() == 1
    ring.append(3)
    assert list(ring) == [2, 3]
