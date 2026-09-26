package structures

// Queue is a FIFO collection with amortized O(1) enqueue and dequeue.
type Queue[T any] struct {
	values []T
	head   int
}

// Enqueue appends a value.
func (q *Queue[T]) Enqueue(value T) { q.values = append(q.values, value) }

// Dequeue removes the oldest value. It reports false when empty.
func (q *Queue[T]) Dequeue() (T, bool) {
	var zero T
	if q.head == len(q.values) {
		return zero, false
	}
	value := q.values[q.head]
	q.values[q.head] = zero
	q.head++
	if q.head > 32 && q.head*2 >= len(q.values) {
		q.values = append([]T(nil), q.values[q.head:]...)
		q.head = 0
	}
	return value, true
}

// Len returns the number of queued values.
func (q *Queue[T]) Len() int { return len(q.values) - q.head }
