class _Node:
    def __init__(self, key, value): self.key, self.value, self.left, self.right, self.height = key, value, None, None, 1

class AVLTree:
    """Balanced map supporting ordered range scans."""
    def __init__(self): self.root = None
    def _height(self, node): return node.height if node else 0
    def _rotate_left(self, node):
        top = node.right; node.right = top.left; top.left = node
        node.height = 1 + max(self._height(node.left), self._height(node.right)); top.height = 1 + max(self._height(top.left), self._height(top.right)); return top
    def _rotate_right(self, node):
        top = node.left; node.left = top.right; top.right = node
        node.height = 1 + max(self._height(node.left), self._height(node.right)); top.height = 1 + max(self._height(top.left), self._height(top.right)); return top
    def insert(self, key, value): self.root = self._insert(self.root, key, value)
    def _insert(self, node, key, value):
        if not node: return _Node(key, value)
        if key < node.key: node.left = self._insert(node.left, key, value)
        elif key > node.key: node.right = self._insert(node.right, key, value)
        else: node.value = value; return node
        node.height = 1 + max(self._height(node.left), self._height(node.right)); balance = self._height(node.left) - self._height(node.right)
        if balance > 1 and key < node.left.key: return self._rotate_right(node)
        if balance < -1 and key > node.right.key: return self._rotate_left(node)
        if balance > 1: node.left = self._rotate_left(node.left); return self._rotate_right(node)
        if balance < -1: node.right = self._rotate_right(node.right); return self._rotate_left(node)
        return node
    def range(self, low, high):
        out=[]
        def walk(node):
            if not node: return
            if node.key > low: walk(node.left)
            if low <= node.key <= high: out.append((node.key,node.value))
            if node.key < high: walk(node.right)
        walk(self.root); return out
