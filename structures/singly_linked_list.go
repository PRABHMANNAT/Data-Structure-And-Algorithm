package structures

// SinglyLinkedList stores values in insertion order.
type SinglyLinkedList[T any] struct { head, tail *singlyNode[T]; len int }
type singlyNode[T any] struct { value T; next *singlyNode[T] }
func (l *SinglyLinkedList[T]) Append(v T) { n:=&singlyNode[T]{value:v}; if l.tail==nil { l.head=n } else { l.tail.next=n }; l.tail=n; l.len++ }
func (l *SinglyLinkedList[T]) Prepend(v T) { n:=&singlyNode[T]{value:v,next:l.head}; l.head=n; if l.tail==nil { l.tail=n }; l.len++ }
func (l *SinglyLinkedList[T]) RemoveFirst() (T,bool) { var z T; if l.head==nil{return z,false}; v:=l.head.value;l.head=l.head.next;l.len--;if l.head==nil{l.tail=nil};return v,true }
func (l *SinglyLinkedList[T]) Len() int { return l.len }
func (l *SinglyLinkedList[T]) Values() []T { out:=make([]T,0,l.len);for n:=l.head;n!=nil;n=n.next {out=append(out,n.value)};return out }
