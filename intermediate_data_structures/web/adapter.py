from intermediate_ds.binary_search_tree import BinarySearchTree
from workbench.validation import numbers, integer

def run(data):
    values = numbers(data)
    target = integer(data, 'find')
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
    def shape(node):
        return None if node is None else dict(value=node.key,left=shape(node.left),right=shape(node.right))
    def height(node):
        return 0 if node is None else 1 + max(height(node.left),height(node.right))
    return dict(values=values,ordered=tree.inorder(),found=tree.contains(target),target=target,
                height=height(tree.root),tree=shape(tree.root))
