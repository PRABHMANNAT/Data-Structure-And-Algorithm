package structures

// DoublyLinkedList supports constant-time removal from either end.
type DoublyLinkedList[T any] struct { head, tail *doublyNode[T]; len int }
type doublyNode[T any] struct { value T; prev, next *doublyNode[T] }
func (l *DoublyLinkedList[T]) PushFront(v T) { n:=&doublyNode[T]{value:v,next:l.head};if l.head!=nil{l.head.prev=n}else{l.tail=n};l.head=n;l.len++ }
func (l *DoublyLinkedList[T]) PushBack(v T) { n:=&doublyNode[T]{value:v,prev:l.tail};if l.tail!=nil{l.tail.next=n}else{l.head=n};l.tail=n;l.len++ }
func (l *DoublyLinkedList[T]) PopBack() (T,bool) { var z T;if l.tail==nil{return z,false};v:=l.tail.value;l.tail=l.tail.prev;if l.tail!=nil{l.tail.next=nil}else{l.head=nil};l.len--;return v,true }
func (l *DoublyLinkedList[T]) Len() int{return l.len}
