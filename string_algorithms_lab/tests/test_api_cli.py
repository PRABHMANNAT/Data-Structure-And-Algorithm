import contextlib
import io
import json
import unittest

from stringlab.api import compare, search
from stringlab.cli import main


class PublicInterfaceTests(unittest.TestCase):
    def test_result_and_dispatch(self):
        result = search("banana", "ana")
        self.assertEqual(result.positions, (1, 3))
        self.assertEqual(result.count, 2)
        self.assertEqual(len(compare("banana", "ana")), 5)
        with self.assertRaises(ValueError):
            search("abc", "a", "missing")

    def test_cli_json(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(main(["search", "banana", "ana", "--algorithm", "z"]), 0)
        self.assertEqual(json.loads(output.getvalue())["positions"], [1, 3])

    def test_cli_multi(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            main(["multi", "banana", "ana", "na"])
        self.assertEqual(json.loads(output.getvalue()), {"ana": [1, 3], "na": [2, 4]})


if __name__ == "__main__":
    unittest.main()
