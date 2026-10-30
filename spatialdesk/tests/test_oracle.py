import unittest, random, itertools

from spatialdesk.models import Point
from spatialdesk.core import Node, nearest
from spatialdesk.extra import within


class OracleTests(unittest.TestCase):
    def test_random_search_against_full_scan(self):
        rng = random.Random(14)
        for _ in range(80):
            points = [
                Point(str(i), rng.randrange(-10, 11), rng.randrange(-10, 11))
                for i in range(35)
            ]
            root = Node(points)
            x, y = rng.randrange(-10, 11), rng.randrange(-10, 11)
            k = rng.randint(1, len(points))
            radius = rng.randrange(12)
            expected = sorted(points, key=lambda p: (p.distance2(x, y), p.name))[:k]
            self.assertEqual(
                [p.name for _, p in nearest(root, x, y, k)[0]],
                [p.name for p in expected],
            )
            self.assertEqual(
                [p.name for p in within(root, x, y, radius)[0]],
                sorted(p.name for p in points if p.distance2(x, y) <= radius**2),
            )
