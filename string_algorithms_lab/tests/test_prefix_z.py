import unittest

from stringlab.prefix import prefix_function
from stringlab.z_algorithm import z_values
from stringlab.z_search import find_all


class PrefixZTests(unittest.TestCase):
    def test_prefix_function(self):
        self.assertEqual(prefix_function("ababcabab"), [0, 0, 1, 2, 0, 1, 2, 3, 4])
        self.assertEqual(prefix_function(""), [])

    def test_z_values(self):
        self.assertEqual(z_values("aaaaa"), [0, 4, 3, 2, 1])
        self.assertEqual(z_values(""), [])

    def test_sentinel_cannot_collide(self):
        self.assertEqual(find_all("$\0$\0", "$\0"), [0, 2])


if __name__ == "__main__":
    unittest.main()
