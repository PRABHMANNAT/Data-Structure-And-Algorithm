package structures

// Ordered is the set of scalar types accepted by AVLTree.
type Ordered interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 | ~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr | ~float32 | ~float64 | ~string
}

// AVLTree is a self-balancing binary search tree.
type AVLTree[T Ordered] struct {
	root   *avlNode[T]
	length int
}
type avlNode[T Ordered] struct {
	value       T
	height      int
	left, right *avlNode[T]
}

// Insert adds value if absent in O(log n).
func (t *AVLTree[T]) Insert(value T) {
	var added bool
	t.root, added = insertAVL(t.root, value)
	if added {
		t.length++
	}
}
func insertAVL[T Ordered](n *avlNode[T], v T) (*avlNode[T], bool) {
	if n == nil {
		return &avlNode[T]{value: v, height: 1}, true
	}
	var a bool
	if v < n.value {
		n.left, a = insertAVL(n.left, v)
	} else if v > n.value {
		n.right, a = insertAVL(n.right, v)
	} else {
		return n, false
	}
	return balance(n), a
}

// Contains checks membership in O(log n).
func (t *AVLTree[T]) Contains(v T) bool {
	for n := t.root; n != nil; {
		if v < n.value {
			n = n.left
		} else if v > n.value {
			n = n.right
		} else {
			return true
		}
	}
	return false
}

// InOrder returns sorted tree values.
func (t *AVLTree[T]) InOrder() []T {
	out := make([]T, 0, t.length)
	var visit func(*avlNode[T])
	visit = func(n *avlNode[T]) {
		if n != nil {
			visit(n.left)
			out = append(out, n.value)
			visit(n.right)
		}
	}
	visit(t.root)
	return out
}

// Len returns item count.
func (t *AVLTree[T]) Len() int { return t.length }
func height[T Ordered](n *avlNode[T]) int {
	if n == nil {
		return 0
	}
	return n.height
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func update[T Ordered](n *avlNode[T]) { n.height = 1 + max(height(n.left), height(n.right)) }
func balance[T Ordered](n *avlNode[T]) *avlNode[T] {
	update(n)
	f := height(n.left) - height(n.right)
	if f > 1 {
		if height(n.left.left) < height(n.left.right) {
			n.left = rotateLeft(n.left)
		}
		return rotateRight(n)
	}
	if f < -1 {
		if height(n.right.right) < height(n.right.left) {
			n.right = rotateRight(n.right)
		}
		return rotateLeft(n)
	}
	return n
}
func rotateLeft[T Ordered](n *avlNode[T]) *avlNode[T] {
	r := n.right
	n.right = r.left
	r.left = n
	update(n)
	update(r)
	return r
}
func rotateRight[T Ordered](n *avlNode[T]) *avlNode[T] {
	l := n.left
	n.left = l.right
	l.right = n
	update(n)
	update(l)
	return l
}
