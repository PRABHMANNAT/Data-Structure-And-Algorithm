import unittest

from cachecraft.core import LRU
from cachecraft.extra import LFU


class CoreTests(unittest.TestCase):
    def test_lru_eviction_and_links(self):
        c = LRU(2)
        for key in "aba":
            c.access(key)
        self.assertEqual(c.access("c"), (False, "b"))
        self.assertEqual(c.snapshot(), ["a", "c"])
        self.assertIs(c.head.next.prev, c.head)
        self.assertIs(c.tail.prev.next, c.tail)

    def test_lfu_lru_tie_break(self):
        c = LFU(2)
        for key in "aba":
            c.access(key)
        self.assertEqual(c.access("c"), (False, "b"))
        self.assertEqual(c.access("a"), (True, None))

    def test_capacity_one(self):
        for cls in (LRU, LFU):
            c = cls(1)
            c.access("x")
            self.assertEqual(c.access("y"), (False, "x"))
