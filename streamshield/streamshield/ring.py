from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class RingBuffer(Generic[T]):
    """Fixed-capacity FIFO with O(1) append and pop-left."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._data: list[T | None] = [None] * capacity
        self._head = self._size = 0

    def append(self, item: T) -> None:
        if self._size == len(self._data):
            raise OverflowError("ring buffer is full")
        self._data[(self._head + self._size) % len(self._data)] = item
        self._size += 1

    def popleft(self) -> T:
        if not self._size:
            raise IndexError("ring buffer is empty")
        item = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % len(self._data)
        self._size -= 1
        return item  # type: ignore[return-value]

    def __iter__(self) -> Iterator[T]:
        for offset in range(self._size):
            item = self._data[(self._head + offset) % len(self._data)]
            yield item  # type: ignore[misc]

    def __len__(self) -> int:
        return self._size
