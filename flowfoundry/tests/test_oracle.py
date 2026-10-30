import unittest, random, itertools

from flowfoundry.models import Arc
from flowfoundry.core import Network
from flowfoundry.extra import maximum


class OracleTests(unittest.TestCase):
    def test_exhaustive_min_cut_certificate(self):
        rng = random.Random(31)
        vertices = list("sabcdt")
        for _ in range(70):
            arcs = [Arc("s", "t", 0)] + [
                Arc(a, b, rng.randrange(8))
                for a in vertices
                for b in vertices
                if a != b and rng.random() < 0.24
            ]
            n = Network(arcs)
            flow, _ = maximum(n, "s", "t")
            best = float("inf")
            for mask in range(16):
                left = {"s"} | {v for i, v in enumerate("abcd") if mask >> i & 1}
                best = min(
                    best,
                    sum(
                        a.capacity
                        for a in arcs
                        if a.source in left and a.target not in left
                    ),
                )
            self.assertEqual(flow, best)
            balance = {v: 0 for v in vertices}
            for a, index in n.original:
                sent = a.capacity - n.adj[a.source][index].remaining
                self.assertTrue(0 <= sent <= a.capacity)
                balance[a.source] -= sent
                balance[a.target] += sent
            self.assertEqual(balance["s"], -flow)
            self.assertEqual(balance["t"], flow)
            self.assertTrue(all(balance[v] == 0 for v in "abcd"))
