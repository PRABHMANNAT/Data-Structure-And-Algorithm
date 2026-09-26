package structures

// MinHeap stores values ordered by the supplied less function.
type MinHeap[T any] struct {
	values []T
	less   func(T, T) bool
}

// NewMinHeap creates an empty heap. less must define a strict ordering.
func NewMinHeap[T any](less func(T, T) bool) *MinHeap[T] { return &MinHeap[T]{less: less} }

// Push inserts a value in O(log n).
func (h *MinHeap[T]) Push(value T) {
	h.values = append(h.values, value)
	for i := len(h.values) - 1; i > 0; {
		p := (i - 1) / 2
		if !h.less(h.values[i], h.values[p]) {
			break
		}
		h.values[i], h.values[p] = h.values[p], h.values[i]
		i = p
	}
}

// Pop removes the smallest value in O(log n).
func (h *MinHeap[T]) Pop() (T, bool) {
	var zero T
	if len(h.values) == 0 {
		return zero, false
	}
	out := h.values[0]
	last := len(h.values) - 1
	h.values[0] = h.values[last]
	h.values[last] = zero
	h.values = h.values[:last]
	for i := 0; ; {
		left := i*2 + 1
		if left >= len(h.values) {
			break
		}
		best := left
		right := left + 1
		if right < len(h.values) && h.less(h.values[right], h.values[left]) {
			best = right
		}
		if !h.less(h.values[best], h.values[i]) {
			break
		}
		h.values[i], h.values[best] = h.values[best], h.values[i]
		i = best
	}
	return out, true
}

// Len returns the item count.
func (h *MinHeap[T]) Len() int { return len(h.values) }
