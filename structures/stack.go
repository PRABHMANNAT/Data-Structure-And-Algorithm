package structures

// Stack is a last-in, first-out collection.
type Stack[T any] struct { items []T }
func (s *Stack[T]) Push(v T){s.items=append(s.items,v)}
func (s *Stack[T]) Pop()(T,bool){var z T;if len(s.items)==0{return z,false};i:=len(s.items)-1;v:=s.items[i];s.items=s.items[:i];return v,true}
func (s *Stack[T]) Peek()(T,bool){var z T;if len(s.items)==0{return z,false};return s.items[len(s.items)-1],true}
func (s *Stack[T]) Len()int{return len(s.items)}
