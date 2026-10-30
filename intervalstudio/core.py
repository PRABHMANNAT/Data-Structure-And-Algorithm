"""AVL interval index augmented with subtree maximum end times."""


class Node:
    def __init__(self, job):
        self.job = job
        self.left = self.right = None
        self.height = 1
        self.maximum = job.end


def height(n):
    return n.height if n else 0


def update(n):
    n.height = 1 + max(height(n.left), height(n.right))
    n.maximum = max(
        n.job.end, n.left.maximum if n.left else -1, n.right.maximum if n.right else -1
    )
    return n


def rotate(n, left):
    pivot = n.right if left else n.left
    if left:
        n.right = pivot.left
        pivot.left = n
    else:
        n.left = pivot.right
        pivot.right = n
    update(n)
    return update(pivot)


def insert(root, job):
    if root is None:
        return Node(job)
    if (job.start, job.name) < (root.job.start, root.job.name):
        root.left = insert(root.left, job)
    else:
        root.right = insert(root.right, job)
    update(root)
    balance = height(root.left) - height(root.right)
    if balance > 1:
        if height(root.left.left) < height(root.left.right):
            root.left = rotate(root.left, True)
        return rotate(root, False)
    if balance < -1:
        if height(root.right.right) < height(root.right.left):
            root.right = rotate(root.right, False)
        return rotate(root, True)
    return root


def overlaps(root, start, end):
    found = []

    def visit(node):
        if node is None or node.maximum <= start:
            return
        visit(node.left)
        if node.job.overlaps(start, end):
            found.append(node.job.name)
        if node.job.start < end:
            visit(node.right)

    visit(root)
    return sorted(found)
