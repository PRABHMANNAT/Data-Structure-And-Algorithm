package structures

func (l *List[T]) Values() []T { out:=make([]T,0,l.size); for n:=l.head;n!=nil;n=n.next { out=append(out,n.value) }; return out }
