package structures

// Deque is a double-ended queue implemented with a circular buffer.
type Deque[T any] struct {
	data         []T
	head, length int
}

// PushFront inserts at the front in amortized O(1).
func (d *Deque[T]) PushFront(v T) {
	d.ensure()
	d.head = (d.head - 1 + len(d.data)) % len(d.data)
	d.data[d.head] = v
	d.length++
}

// PushBack inserts at the back in amortized O(1).
func (d *Deque[T]) PushBack(v T) { d.ensure(); d.data[(d.head+d.length)%len(d.data)] = v; d.length++ }

// PopFront removes the front value in O(1).
func (d *Deque[T]) PopFront() (T, bool) {
	var z T
	if d.length == 0 {
		return z, false
	}
	v := d.data[d.head]
	d.data[d.head] = z
	d.head = (d.head + 1) % len(d.data)
	d.length--
	return v, true
}

// PopBack removes the back value in O(1).
func (d *Deque[T]) PopBack() (T, bool) {
	var z T
	if d.length == 0 {
		return z, false
	}
	i := (d.head + d.length - 1) % len(d.data)
	v := d.data[i]
	d.data[i] = z
	d.length--
	return v, true
}

// Len returns item count.
func (d *Deque[T]) Len() int { return d.length }
func (d *Deque[T]) ensure() {
	if d.length < len(d.data) {
		return
	}
	n := max(4, d.length*2)
	next := make([]T, n)
	for i := 0; i < d.length; i++ {
		next[i] = d.data[(d.head+i)%len(d.data)]
	}
	d.data = next
	d.head = 0
}
