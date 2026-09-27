from collections import OrderedDict
from typing import Generic, TypeVar
K = TypeVar("K"); V = TypeVar("V")

class LRU(Generic[K, V]):
    def __init__(self, capacity: int = 128) -> None: self.capacity, self._items = capacity, OrderedDict()
    def get(self, key: K) -> V | None:
        if key not in self._items: return None
        self._items.move_to_end(key); return self._items[key]
    def put(self, key: K, value: V) -> None:
        self._items[key] = value; self._items.move_to_end(key)
        if len(self._items) > self.capacity: self._items.popitem(last=False)
