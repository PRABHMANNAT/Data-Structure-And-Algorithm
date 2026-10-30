import unittest, random, itertools

from shardring.models import Server
from shardring.core import Ring
from shardring.extra import rendezvous


class OracleTests(unittest.TestCase):
    def test_membership_movement_invariants(self):
        original = [Server("a", 1), Server("b", 2), Server("c", 1)]
        added = original + [Server("d", 1)]
        a, b = Ring(original, 23), Ring(added, 23)
        for i in range(1000):
            key = str(i)
            old, new = a.owner(key), b.owner(key)
            if old != new:
                self.assertEqual(new, "d")
            old, new = rendezvous(original, key), rendezvous(added, key)
            if old != new:
                self.assertEqual(new, "d")
            self.assertEqual(set(b.preference(key, 4)), set("abcd"))
