import unittest

from quantilewatch.core import add, remove, select, size, quantile
from quantilewatch.extra import rolling


class CoreTests(unittest.TestCase):
    def test_even_quantile(self):
        root = None
        for v in [1, 3, 5, 7]:
            root = add(root, v)
        self.assertEqual(quantile(root, 0.5), 4)
        self.assertEqual(quantile(root, 0.25), 2.5)

    def test_duplicate_deletion(self):
        root = add(add(None, 5), 5)
        root = remove(root, 5)
        self.assertEqual(size(root), 1)
        self.assertEqual(select(root, 0), 5)

    def test_previous_window_no_leakage(self):
        rows = rolling([5, 5, 5, 5, 100], 4)
        self.assertTrue(rows[-1].outlier)
        self.assertFalse(any(r.outlier for r in rows[:4]))
