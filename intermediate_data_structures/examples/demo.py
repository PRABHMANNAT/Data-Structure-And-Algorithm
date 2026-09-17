from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from intermediate_ds.binary_search_tree import BinarySearchTree
from intermediate_ds.graph import Graph

tree = BinarySearchTree()
for value in [7, 3, 9, 1, 5]:
    tree.insert(value)
print("BST inorder:", tree.inorder())

graph = Graph()
for edge in [("A", "B"), ("A", "C"), ("B", "D")]:
    graph.add_edge(*edge)
print("Graph BFS:", graph.bfs("A"))
