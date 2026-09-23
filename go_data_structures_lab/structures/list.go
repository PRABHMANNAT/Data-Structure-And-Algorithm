package structures

// List is a singly linked, generic sequence.
type List[T any] struct { head, tail *listNode[T]; size int }
func (l *List[T]) Len() int { return l.size }
func (l *List[T]) IsEmpty() bool { return l.size == 0 }
