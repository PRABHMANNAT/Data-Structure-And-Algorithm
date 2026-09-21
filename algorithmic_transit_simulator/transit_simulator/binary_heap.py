from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class MinHeap(Generic[T]):
    """Stable binary min-heap for (priority, value) pairs."""

    def __init__(self) -> None:
        self._items: list[tuple[int, int, T]] = []
        self._sequence = 0

    def __len__(self) -> int:
        return len(self._items)

    def push(self, priority: int, value: T) -> None:
        self._items.append((priority, self._sequence, value))
        self._sequence += 1
        self._sift_up(len(self._items) - 1)

    def pop(self) -> tuple[int, T]:
        if not self._items:
            raise IndexError("pop from empty heap")
        root = self._items[0]
        tail = self._items.pop()
        if self._items:
            self._items[0] = tail
            self._sift_down(0)
        return root[0], root[2]

    def _sift_up(self, child: int) -> None:
        while child:
            parent = (child - 1) // 2
            if self._items[parent] <= self._items[child]:
                return
            self._items[parent], self._items[child] = self._items[child], self._items[parent]
            child = parent

    def _sift_down(self, parent: int) -> None:
        size = len(self._items)
        while (child := 2 * parent + 1) < size:
            if child + 1 < size and self._items[child + 1] < self._items[child]:
                child += 1
            if self._items[parent] <= self._items[child]:
                return
            self._items[parent], self._items[child] = self._items[child], self._items[parent]
            parent = child
