package structures

func (l *List[T]) Reverse() { var prev *listNode[T]; cur:=l.head; l.tail=l.head; for cur!=nil { next:=cur.next; cur.next=prev; prev=cur; cur=next }; l.head=prev }
