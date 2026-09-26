package structures

import "testing"

func TestStackAndQueue(t *testing.T) {
	s := Stack[int]{}
	s.Push(1)
	s.Push(2)
	if v, ok := s.Pop(); !ok || v != 2 {
		t.Fatal("stack must be LIFO")
	}
	q := Queue[string]{}
	q.Enqueue("a")
	q.Enqueue("b")
	if v, ok := q.Dequeue(); !ok || v != "a" {
		t.Fatal("queue must be FIFO")
	}
}
func TestList(t *testing.T) {
	l := List[int]{}
	l.Append(2)
	l.Prepend(1)
	if !l.RemoveFirst(func(v int) bool { return v == 2 }) || l.Len() != 1 {
		t.Fatal("list removal failed")
	}
}
func TestHeap(t *testing.T) {
	h := NewMinHeap(func(a, b int) bool { return a < b })
	for _, v := range []int{3, 1, 2} {
		h.Push(v)
	}
	for want := 1; want <= 3; want++ {
		got, _ := h.Pop()
		if got != want {
			t.Fatalf("got %d", got)
		}
	}
}
func TestDisjointSet(t *testing.T) {
	d := NewDisjointSet(4)
	d.Union(0, 1)
	d.Union(2, 3)
	if d.Connected(0, 2) || d.Groups() != 2 {
		t.Fatal("unexpected components")
	}
}
func TestTrie(t *testing.T) {
	trie := NewTrie()
	trie.Insert("tree")
	if !trie.Contains("tree") || trie.Contains("tre") || !trie.HasPrefix("tre") {
		t.Fatal("trie lookup failed")
	}
}
func TestAVL(t *testing.T) {
	tree := AVLTree[int]{}
	for _, v := range []int{3, 2, 1, 4, 5} {
		tree.Insert(v)
	}
	ordered := tree.InOrder()
	for i, v := range ordered {
		if v != i+1 {
			t.Fatal("tree not ordered")
		}
	}
}
func TestLRU(t *testing.T) {
	cache := NewLRUCache[string, int](2)
	cache.Put("a", 1)
	cache.Put("b", 2)
	cache.Get("a")
	evicted, ok := cache.Put("c", 3)
	if !ok || evicted != "b" {
		t.Fatal("wrong eviction")
	}
}
