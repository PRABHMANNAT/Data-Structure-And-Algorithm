from intermediate_data_structures.intermediate_ds.binary_search_tree import BinarySearchTree
from intermediate_data_structures.intermediate_ds.graph import Graph

tree = BinarySearchTree()
for value in [7, 3, 9, 1, 5]:
    tree.insert(value)
print("BST inorder:", tree.inorder())

graph = Graph()
for edge in [("A", "B"), ("A", "C"), ("B", "D")]:
    graph.add_edge(*edge)
print("Graph BFS:", graph.bfs("A"))
