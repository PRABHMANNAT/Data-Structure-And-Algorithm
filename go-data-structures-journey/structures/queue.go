package structures

// Queue is a first-in, first-out collection.
type Queue[T any] struct{ items []T; head int }
func(q *Queue[T]) Enqueue(v T){q.items=append(q.items,v)}
func(q *Queue[T]) Dequeue()(T,bool){var z T;if q.head==len(q.items){return z,false};v:=q.items[q.head];q.head++;if q.head*2>=len(q.items){q.items=append([]T(nil),q.items[q.head:]...);q.head=0};return v,true}
func(q *Queue[T]) Len()int{return len(q.items)-q.head}
