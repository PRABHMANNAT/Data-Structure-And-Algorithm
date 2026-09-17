class BinarySearchTree:
    class _Node:
        def __init__(self, key): self.key = key; self.left = self.right = None
    def __init__(self): self.root = None
    def insert(self, key):
        if self.root is None: self.root = self._Node(key); return
        node = self.root
        while True:
            branch = "left" if key < node.key else "right"
            child = getattr(node, branch)
            if child is None: setattr(node, branch, self._Node(key)); return
            node = child
    def contains(self, key):
        node = self.root
        while node:
            if key == node.key: return True
            node = node.left if key < node.key else node.right
        return False
    def inorder(self):
        def walk(node):
            if node: yield from walk(node.left); yield node.key; yield from walk(node.right)
        return list(walk(self.root))
