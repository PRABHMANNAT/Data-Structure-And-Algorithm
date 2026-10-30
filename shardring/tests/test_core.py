import unittest

from shardring.models import Server
from shardring.core import Ring
from shardring.extra import rendezvous


class CoreTests(unittest.TestCase):
    def test_stable_order(self):
        servers = [Server("a", 1), Server("b", 2)]
        self.assertEqual(
            Ring(servers).owner("key"), Ring(list(reversed(servers))).owner("key")
        )
        self.assertEqual(
            rendezvous(servers, "key"), rendezvous(list(reversed(servers)), "key")
        )

    def test_distinct_replicas(self):
        ring = Ring([Server("a", 3), Server("b", 1)])
        self.assertEqual(len(set(ring.preference("key", 2))), 2)

    def test_single_server(self):
        self.assertEqual(Ring([Server("solo", 1)]).owner("anything"), "solo")
