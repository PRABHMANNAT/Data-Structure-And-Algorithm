package structures

type Stack[T any] struct { items []T }
func (s *Stack[T]) Len() int { return len(s.items) }
