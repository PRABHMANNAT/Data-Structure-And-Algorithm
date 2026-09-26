package structures

// List is a singly linked list with O(1) append and prepend.
type List[T any] struct {
	head, tail *listNode[T]
	length     int
}
type listNode[T any] struct {
	value T
	next  *listNode[T]
}

// Append adds a value at the tail.
func (l *List[T]) Append(value T) {
	n := &listNode[T]{value: value}
	if l.tail == nil {
		l.head = n
	} else {
		l.tail.next = n
	}
	l.tail = n
	l.length++
}

// Prepend adds a value at the head.
func (l *List[T]) Prepend(value T) {
	n := &listNode[T]{value: value, next: l.head}
	l.head = n
	if l.tail == nil {
		l.tail = n
	}
	l.length++
}

// RemoveFirst removes the first matching value according to equal in O(n).
func (l *List[T]) RemoveFirst(equal func(T) bool) bool {
	var previous *listNode[T]
	for current := l.head; current != nil; current = current.next {
		if equal(current.value) {
			if previous == nil {
				l.head = current.next
			} else {
				previous.next = current.next
			}
			if l.tail == current {
				l.tail = previous
			}
			l.length--
			return true
		}
		previous = current
	}
	return false
}

// Values materializes list contents from head to tail.
func (l *List[T]) Values() []T {
	out := make([]T, 0, l.length)
	for n := l.head; n != nil; n = n.next {
		out = append(out, n.value)
	}
	return out
}

// Len returns number of list nodes.
func (l *List[T]) Len() int { return l.length }
