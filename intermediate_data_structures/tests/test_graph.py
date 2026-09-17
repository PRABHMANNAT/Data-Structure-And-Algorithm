import unittest
from intermediate_data_structures.intermediate_ds.graph import Graph
class GraphTests(unittest.TestCase):
    def test_breadth_first_search(self):
        graph = Graph(); graph.add_edge("a", "c"); graph.add_edge("a", "b"); graph.add_edge("b", "d")
        self.assertEqual(graph.bfs("a"), ["a", "b", "c", "d"])
if __name__ == "__main__": unittest.main()
