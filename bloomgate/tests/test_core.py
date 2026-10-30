import unittest

from bloomgate.core import Bloom
from bloomgate.extra import Sketch


class CoreTests(unittest.TestCase):
    def test_no_false_negatives(self):
        bloom = Bloom(13, 5)
        for key in ["a", "café", "東京"]:
            bloom.add(key)
        self.assertTrue(all(bloom.contains(k) for k in ["a", "café", "東京"]))
        self.assertLessEqual(bloom.occupied(), 13)

    def test_repeated_insert_idempotent(self):
        b = Bloom(64, 3)
        b.add("x")
        before = b.occupied()
        b.add("x")
        self.assertEqual(b.occupied(), before)

    def test_negative_updates_rejected(self):
        with self.assertRaises(ValueError):
            Sketch(8).add("x", -1)
