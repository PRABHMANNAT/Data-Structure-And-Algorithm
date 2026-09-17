class CircularQueue:
    def __init__(self, capacity):
        if capacity < 1: raise ValueError("capacity must be positive")
        self._data = [None] * capacity; self._head = self._size = 0
    def __len__(self): return self._size
    def enqueue(self, value):
        if self._size == len(self._data): raise OverflowError("queue is full")
        self._data[(self._head + self._size) % len(self._data)] = value; self._size += 1
    def dequeue(self):
        if not self._size: raise IndexError("dequeue from empty queue")
        value = self._data[self._head]; self._data[self._head] = None
        self._head = (self._head + 1) % len(self._data); self._size -= 1; return value
