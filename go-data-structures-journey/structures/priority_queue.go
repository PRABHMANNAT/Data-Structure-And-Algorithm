package structures

// PriorityQueue is a minimum binary heap.
type PriorityQueue[T any] struct{ items []T; less func(T,T)bool }
func NewPriorityQueue[T any](less func(T,T)bool)*PriorityQueue[T]{return &PriorityQueue[T]{less:less}}
func(p *PriorityQueue[T]) Push(v T){p.items=append(p.items,v);for i:=len(p.items)-1;i>0;{parent:=(i-1)/2;if !p.less(p.items[i],p.items[parent]){break};p.items[i],p.items[parent]=p.items[parent],p.items[i];i=parent}}
func(p *PriorityQueue[T]) Pop()(T,bool){var z T;if len(p.items)==0{return z,false};v:=p.items[0];last:=len(p.items)-1;p.items[0]=p.items[last];p.items=p.items[:last];for i:=0;;{left:=2*i+1;if left>=len(p.items){break};child:=left;if r:=left+1;r<len(p.items)&&p.less(p.items[r],p.items[left]){child=r};if !p.less(p.items[child],p.items[i]){break};p.items[i],p.items[child]=p.items[child],p.items[i];i=child};return v,true}
func(p *PriorityQueue[T]) Len()int{return len(p.items)}
