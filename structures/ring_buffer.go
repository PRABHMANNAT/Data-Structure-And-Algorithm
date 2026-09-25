package structures

// RingBuffer stores a fixed number of recent values.
type RingBuffer[T any] struct{ data []T; head,size int }
func NewRingBuffer[T any](capacity int)*RingBuffer[T]{return &RingBuffer[T]{data:make([]T,capacity)}}
func(r *RingBuffer[T]) Add(v T){if len(r.data)==0{return};r.data[(r.head+r.size)%len(r.data)]=v;if r.size<len(r.data){r.size++}else{r.head=(r.head+1)%len(r.data)}}
func(r *RingBuffer[T]) Values()[]T{out:=make([]T,r.size);for i:=range out{out[i]=r.data[(r.head+i)%len(r.data)]};return out}
func(r *RingBuffer[T]) Len()int{return r.size}
