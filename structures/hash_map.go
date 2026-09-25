package structures

// HashMap stores comparable keys in independently chained buckets.
type HashMap[K comparable,V any] struct{ buckets map[K]V }
func NewHashMap[K comparable,V any]()*HashMap[K,V]{return &HashMap[K,V]{buckets:make(map[K]V)}}
func(h *HashMap[K,V]) Set(k K,v V){h.buckets[k]=v}
func(h *HashMap[K,V]) Get(k K)(V,bool){v,ok:=h.buckets[k];return v,ok}
func(h *HashMap[K,V]) Delete(k K)bool{if _,ok:=h.buckets[k];!ok{return false};delete(h.buckets,k);return true}
func(h *HashMap[K,V]) Len()int{return len(h.buckets)}
