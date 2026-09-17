from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        if capacity < 1: raise ValueError("capacity must be positive")
        self.capacity = capacity; self._items = OrderedDict()
    def get(self, key, default=None):
        if key not in self._items: return default
        self._items.move_to_end(key); return self._items[key]
    def set(self, key, value):
        self._items[key] = value; self._items.move_to_end(key)
        if len(self._items) > self.capacity: self._items.popitem(last=False)
    def __len__(self): return len(self._items)
