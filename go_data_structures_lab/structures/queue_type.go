package structures

type Queue[T any] struct { items []T }
func (q *Queue[T]) Len() int { return len(q.items) }
