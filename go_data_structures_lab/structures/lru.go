package structures

type LRU[K comparable,V any] struct{ capacity int; order []K; values map[K]V }
func NewLRU[K comparable,V any](capacity int)*LRU[K,V]{return &LRU[K,V]{capacity:capacity,values:map[K]V{}}}
func (c *LRU[K,V]) touch(k K){for i,v:=range c.order{if v==k{c.order=append(c.order[:i],c.order[i+1:]...);break}};c.order=append(c.order,k)}
func (c *LRU[K,V]) Get(k K)(V,bool){v,ok:=c.values[k];if ok{c.touch(k)};return v,ok}
func (c *LRU[K,V]) Put(k K,v V){if c.capacity<=0{return};if _,ok:=c.values[k];!ok&&len(c.values)==c.capacity{old:=c.order[0];delete(c.values,old);c.order=c.order[1:]};c.values[k]=v;c.touch(k)}
