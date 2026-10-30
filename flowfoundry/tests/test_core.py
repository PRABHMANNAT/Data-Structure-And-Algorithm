import unittest

from flowfoundry.models import Arc
from flowfoundry.core import Network
from flowfoundry.extra import maximum


class CoreTests(unittest.TestCase):
    def test_parallel_and_antiparallel(self):
        n = Network(
            [Arc("s", "a", 4), Arc("s", "a", 3), Arc("a", "s", 2), Arc("a", "t", 9)]
        )
        self.assertEqual(maximum(n, "s", "t")[0], 7)

    def test_disconnected(self):
        n = Network([Arc("s", "a", 4), Arc("b", "t", 3)])
        self.assertEqual(maximum(n, "s", "t"), (0, []))

    def test_zero_capacity(self):
        n = Network([Arc("s", "t", 0)])
        self.assertEqual(maximum(n, "s", "t")[0], 0)
