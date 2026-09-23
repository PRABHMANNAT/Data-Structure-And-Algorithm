package structures

func (q *Queue[T]) Enqueue(v T) { q.items=append(q.items,v) }
func (q *Queue[T]) Dequeue() (T,error) { var z T; if len(q.items)==0{return z,ErrEmpty}; v:=q.items[0]; q.items=q.items[1:]; return v,nil }
func (q *Queue[T]) Front() (T,error) { var z T; if len(q.items)==0{return z,ErrEmpty}; return q.items[0],nil }
