package structures

type HashMap[K comparable,V any] struct { entries map[K]V }
func NewHashMap[K comparable,V any]() *HashMap[K,V] { return &HashMap[K,V]{entries:make(map[K]V)} }
func (m *HashMap[K,V]) Set(k K,v V){m.entries[k]=v}
func (m *HashMap[K,V]) Get(k K)(V,bool){v,ok:=m.entries[k];return v,ok}
func (m *HashMap[K,V]) Delete(k K){delete(m.entries,k)}
func (m *HashMap[K,V]) Len()int{return len(m.entries)}
