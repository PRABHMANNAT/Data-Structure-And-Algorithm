package structures

// MinHeap stores ordered values with logarithmic insertion and removal.
type MinHeap[T comparable] struct { items []T; less func(T,T)bool }
func NewMinHeap[T comparable](less func(T,T)bool)*MinHeap[T]{return &MinHeap[T]{less:less}}
func (h *MinHeap[T]) Len()int{return len(h.items)}
func (h *MinHeap[T]) Push(v T){h.items=append(h.items,v);for i:=len(h.items)-1;i>0;{p:=(i-1)/2;if !h.less(h.items[i],h.items[p]){break};h.items[i],h.items[p]=h.items[p],h.items[i];i=p}}
func (h *MinHeap[T]) Pop()(T,error){var z T;if len(h.items)==0{return z,ErrEmpty};v:=h.items[0];last:=len(h.items)-1;h.items[0]=h.items[last];h.items=h.items[:last];for i:=0;;{l:=2*i+1;r:=l+1;s:=i;if l<len(h.items)&&h.less(h.items[l],h.items[s]){s=l};if r<len(h.items)&&h.less(h.items[r],h.items[s]){s=r};if s==i{break};h.items[i],h.items[s]=h.items[s],h.items[i];i=s};return v,nil}
