package structures

func (l *List[T]) Append(value T) { n:=&listNode[T]{value:value}; if l.tail==nil { l.head=n; l.tail=n } else { l.tail.next=n; l.tail=n }; l.size++ }
func (l *List[T]) Prepend(value T) { n:=&listNode[T]{value:value,next:l.head}; l.head=n; if l.tail==nil { l.tail=n }; l.size++ }
