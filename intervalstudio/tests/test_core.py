import unittest

from intervalstudio.models import Booking
from intervalstudio.core import insert, overlaps, height
from intervalstudio.extra import optimal


class CoreTests(unittest.TestCase):
    def test_half_open(self):
        root = insert(insert(None, Booking("a", 0, 2, 3)), Booking("b", 2, 4, 4))
        self.assertEqual(overlaps(root, 2, 4), ["b"])

    def test_greedy_counterexample(self):
        jobs = [
            Booking("long", 0, 10, 10),
            Booking("a", 0, 5, 8),
            Booking("b", 5, 10, 8),
        ]
        self.assertEqual(optimal(jobs)[0], 16)

    def test_rotations_preserve_augmentation(self):
        root = None
        for i in range(30):
            root = insert(root, Booking(str(i), i, i + 3, i))

        def check(n):
            if not n:
                return -1
            a, b = check(n.left), check(n.right)
            self.assertLessEqual(abs(height(n.left) - height(n.right)), 1)
            self.assertEqual(n.maximum, max(n.job.end, a, b))
            return n.maximum

        check(root)
        self.assertLess(root.height, 8)
