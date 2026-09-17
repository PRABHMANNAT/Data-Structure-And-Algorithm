import unittest
from advanced_delivery_network.delivery_network.ring_buffer import RingBuffer
class RingBufferTests(unittest.TestCase):
    def test_overwrites_oldest_events(self):
        buffer = RingBuffer(2); buffer.append("one"); buffer.append("two"); buffer.append("three")
        self.assertEqual(buffer.values(), ["two", "three"])
if __name__ == "__main__": unittest.main()
