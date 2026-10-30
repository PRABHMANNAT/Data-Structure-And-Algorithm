import unittest, random, itertools

from collections import Counter
from bloomgate.core import Bloom
from bloomgate.extra import Sketch


class OracleTests(unittest.TestCase):
    def test_one_sided_errors_against_exact_truth(self):
        rng = random.Random(113)
        for width in [4, 16, 64]:
            b = Bloom(width * 8, 4)
            s = Sketch(width)
            truth = Counter(str(rng.randrange(80)) for _ in range(300))
            for key, count in truth.items():
                b.add(key)
                s.add(key, count)
            for key in map(str, range(100)):
                if truth[key]:
                    self.assertTrue(b.contains(key))
                self.assertGreaterEqual(s.estimate(key), truth[key])
