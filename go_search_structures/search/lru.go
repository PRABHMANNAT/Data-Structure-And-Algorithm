package search

type cacheEntry struct{ query string; results []Result }
type LRU struct{ cap int; entries map[string]cacheEntry; order []string }
func NewLRU(capacity int)*LRU{return &LRU{cap:capacity,entries:map[string]cacheEntry{}}}
func (c *LRU) touch(k string){for i,v:=range c.order{if v==k{c.order=append(c.order[:i],c.order[i+1:]...);break}};c.order=append(c.order,k)}
func (c *LRU) Get(k string)([]Result,bool){e,ok:=c.entries[k];if ok{c.touch(k);return append([]Result(nil),e.results...),true};return nil,false}
func (c *LRU) Put(k string,v []Result){if c.cap<=0{return};if _,ok:=c.entries[k];!ok&&len(c.entries)==c.cap{old:=c.order[0];delete(c.entries,old);c.order=c.order[1:]};c.entries[k]=cacheEntry{k,append([]Result(nil),v...)};c.touch(k)}
