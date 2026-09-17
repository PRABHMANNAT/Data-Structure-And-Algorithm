import unittest
from advanced_delivery_network.delivery_network.cli import build_parser
class CliTests(unittest.TestCase):
    def test_parser_accepts_route_arguments(self):
        args = build_parser().parse_args(["network.json", "A", "B"])
        self.assertEqual((args.origin, args.destination), ("A", "B"))
if __name__ == "__main__": unittest.main()
