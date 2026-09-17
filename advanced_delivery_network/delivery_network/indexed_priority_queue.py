class IndexedPriorityQueue:
    """Min-priority queue with O(log n) key decreases."""
    def __init__(self): self._heap = []; self._positions = {}
    def __len__(self): return len(self._heap)
    def _swap(self, first, second):
        self._heap[first], self._heap[second] = self._heap[second], self._heap[first]
        self._positions[self._heap[first][1]] = first; self._positions[self._heap[second][1]] = second
    def _up(self, index):
        while index:
            parent = (index - 1) // 2
            if self._heap[parent][0] <= self._heap[index][0]: break
            self._swap(parent, index); index = parent
    def _down(self, index):
        while 2 * index + 1 < len(self._heap):
            child = 2 * index + 1
            if child + 1 < len(self._heap) and self._heap[child + 1][0] < self._heap[child][0]: child += 1
            if self._heap[index][0] <= self._heap[child][0]: break
            self._swap(index, child); index = child
    def push_or_decrease(self, key, priority):
        if key in self._positions:
            index = self._positions[key]
            if priority >= self._heap[index][0]: return False
            self._heap[index] = (priority, key); self._up(index); return True
        self._positions[key] = len(self._heap); self._heap.append((priority, key)); self._up(len(self._heap) - 1); return True
    def pop(self):
        if not self._heap: raise IndexError("pop from empty priority queue")
        item = self._heap[0]; last = self._heap.pop(); del self._positions[item[1]]
        if self._heap:
            self._heap[0] = last; self._positions[last[1]] = 0; self._down(0)
        return item
