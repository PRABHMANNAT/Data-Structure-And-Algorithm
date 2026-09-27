from streamshield.indexed_heap import IndexedMaxHeap

def test_replace_score() -> None:
    heap = IndexedMaxHeap(); heap.set("a", 1); heap.set("b", 2); heap.set("a", 3)
    assert heap.top(2) == [("a", 3), ("b", 2)]
