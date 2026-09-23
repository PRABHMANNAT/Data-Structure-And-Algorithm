package structures

type Deque[T any] struct { items []T }
func (d *Deque[T]) PushFront(v T){d.items=append([]T{v},d.items...)}
func (d *Deque[T]) PushBack(v T){d.items=append(d.items,v)}
func (d *Deque[T]) PopFront()(T,error){var z T;if len(d.items)==0{return z,ErrEmpty};v:=d.items[0];d.items=d.items[1:];return v,nil}
func (d *Deque[T]) PopBack()(T,error){var z T;if len(d.items)==0{return z,ErrEmpty};i:=len(d.items)-1;v:=d.items[i];d.items=d.items[:i];return v,nil}
