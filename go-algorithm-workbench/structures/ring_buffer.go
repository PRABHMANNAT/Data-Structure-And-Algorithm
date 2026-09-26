package structures

// RingBuffer keeps the most recent fixed-capacity values.
type RingBuffer[T any] struct {
	data         []T
	start, count int
}

// NewRingBuffer allocates a positive capacity buffer.
func NewRingBuffer[T any](capacity int) *RingBuffer[T] {
	if capacity < 1 {
		panic("ring buffer capacity must be positive")
	}
	return &RingBuffer[T]{data: make([]T, capacity)}
}

// Add appends a value, overwriting the oldest value when full.
func (r *RingBuffer[T]) Add(v T) {
	if r.count < len(r.data) {
		r.data[(r.start+r.count)%len(r.data)] = v
		r.count++
		return
	}
	r.data[r.start] = v
	r.start = (r.start + 1) % len(r.data)
}

// Values returns entries from oldest to newest.
func (r *RingBuffer[T]) Values() []T {
	out := make([]T, r.count)
	for i := range out {
		out[i] = r.data[(r.start+i)%len(r.data)]
	}
	return out
}

// Len returns stored count.
func (r *RingBuffer[T]) Len() int { return r.count }
