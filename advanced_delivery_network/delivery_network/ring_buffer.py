class RingBuffer:
    def __init__(self, capacity):
        if capacity < 1: raise ValueError("capacity must be positive")
        self._data = [None] * capacity; self._start = self._size = 0
    def append(self, value):
        if self._size < len(self._data):
            self._data[(self._start + self._size) % len(self._data)] = value; self._size += 1
        else:
            self._data[self._start] = value; self._start = (self._start + 1) % len(self._data)
    def values(self): return [self._data[(self._start + index) % len(self._data)] for index in range(self._size)]
