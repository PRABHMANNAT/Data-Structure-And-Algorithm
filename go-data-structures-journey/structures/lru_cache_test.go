package structures
import "testing"
func TestLRUCache(t *testing.T){c:=NewLRUCache[string,int](1);c.Put("a",1);c.Put("b",2);if _,ok:=c.Get("a");ok{t.Fatal("cache did not evict")}}
