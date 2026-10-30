import unittest, random, itertools

from cachecraft.core import LRU
from cachecraft.extra import LFU


class OracleTests(unittest.TestCase):
    def test_randomized_reference_policies(self):
        rng = random.Random(17)
        for capacity in range(1, 7):
            a, b = LRU(capacity), LFU(capacity)
            recent = []
            counts = {}
            last = {}
            for time in range(500):
                key = str(rng.randrange(12))
                hit = key in recent
                evicted = None
                if hit:
                    recent.remove(key)
                elif len(recent) == capacity:
                    evicted = recent.pop(0)
                recent.append(key)
                self.assertEqual(a.access(key), (hit, evicted))
                self.assertEqual(a.snapshot(), recent)
                hit = key in counts
                evicted = None
                if not hit and len(counts) == capacity:
                    evicted = min(counts, key=lambda k: (counts[k], last[k]))
                    del counts[evicted]
                    del last[evicted]
                counts[key] = counts.get(key, 0) + 1
                last[key] = time
                self.assertEqual(b.access(key), (hit, evicted))
                self.assertEqual(dict(b.snapshot()), counts)
