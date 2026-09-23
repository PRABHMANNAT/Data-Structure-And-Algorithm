package structures

func (l *List[T]) RemoveFirst() (T,error) { var zero T; if l.head==nil{return zero,ErrEmpty}; v:=l.head.value; l.head=l.head.next; l.size--; if l.head==nil{l.tail=nil}; return v,nil }
