from .binary_heap import MinHeap
class PriorityQueue:
    def __init__(self): self._heap = MinHeap(); self._order = 0
    def push(self, item, priority):
        self._heap.push((priority, self._order, item)); self._order += 1
    def pop(self): return self._heap.pop()[2]
    def __len__(self): return len(self._heap)
