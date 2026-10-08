import random
import unittest

from stringlab.aho_corasick import AhoCorasick
from stringlab.streaming_aho import AhoStream
from stringlab.streaming_kmp import KMPStream


class StreamingTests(unittest.TestCase):
    def test_kmp_crosses_chunk_boundaries(self):
        stream = KMPStream("aba")
        self.assertEqual(stream.feed("ab"), [])
        self.assertEqual(stream.feed("aba"), [0, 2])
        self.assertEqual(stream.feed(""), [])

    def test_aho_crosses_chunk_boundaries(self):
        stream = AhoStream(["ana", "na"])
        first = stream.feed("ban")
        second = stream.feed("ana")
        self.assertEqual(first, {"ana": [], "na": []})
        self.assertEqual(second, {"ana": [1, 3], "na": [2, 4]})

    def test_random_chunking(self):
        randomizer = random.Random(7)
        patterns = ["aba", "ba", "b"]
        for _ in range(100):
            text = "".join(randomizer.choices("ab", k=randomizer.randrange(30)))
            chunks = [text[i:i + 3] for i in range(0, len(text), 3)]
            stream = AhoStream(patterns)
            got = {pattern: [] for pattern in patterns}
            for chunk in chunks:
                for pattern, positions in stream.feed(chunk).items():
                    got[pattern].extend(positions)
            self.assertEqual(got, AhoCorasick(patterns).find_all(text))


if __name__ == "__main__":
    unittest.main()
