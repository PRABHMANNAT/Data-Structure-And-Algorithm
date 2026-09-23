package structures

func (s *Stack[T]) Push(v T) { s.items=append(s.items,v) }
func (s *Stack[T]) Pop() (T,error) { var z T; if len(s.items)==0{return z,ErrEmpty}; i:=len(s.items)-1; v:=s.items[i]; s.items=s.items[:i]; return v,nil }
func (s *Stack[T]) Peek() (T,error) { var z T; if len(s.items)==0{return z,ErrEmpty}; return s.items[len(s.items)-1],nil }
