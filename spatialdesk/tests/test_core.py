import unittest

from spatialdesk.models import Point
from spatialdesk.core import Node, nearest
from spatialdesk.extra import within


class CoreTests(unittest.TestCase):
    def test_equal_distance_ties(self):
        root = Node([Point("b", -1, 0), Point("a", 1, 0)])
        self.assertEqual([p.name for _, p in nearest(root, 0, 0, 1)[0]], ["a"])

    def test_closed_radius_boundary(self):
        root = Node([Point("edge", 3, 4), Point("outside", 6, 0)])
        self.assertEqual([p.name for p in within(root, 0, 0, 5)[0]], ["edge"])

    def test_duplicate_coordinates(self):
        root = Node([Point("a", 0, 0), Point("b", 0, 0)])
        self.assertEqual(len(nearest(root, 0, 0, 2)[0]), 2)
