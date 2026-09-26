// Package structures provides reusable generic data structures.
package structures

// Stack is a last-in, first-out collection backed by a slice.
type Stack[T any] struct{ values []T }

// Push adds value in O(1) amortized time.
func (s *Stack[T]) Push(value T) { s.values = append(s.values, value) }

// Pop removes and returns the newest value in O(1). It reports false when empty.
func (s *Stack[T]) Pop() (T, bool) {
	var zero T
	if len(s.values) == 0 {
		return zero, false
	}
	last := len(s.values) - 1
	value := s.values[last]
	s.values[last] = zero
	s.values = s.values[:last]
	return value, true
}

// Peek returns the newest value without removing it in O(1).
func (s *Stack[T]) Peek() (T, bool) {
	var zero T
	if len(s.values) == 0 {
		return zero, false
	}
	return s.values[len(s.values)-1], true
}

// Len returns the number of values in O(1).
func (s *Stack[T]) Len() int { return len(s.values) }
