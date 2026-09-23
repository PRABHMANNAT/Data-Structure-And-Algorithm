package structures
import "testing"
func TestLRU(t *testing.T){c:=NewLRU[string,int](1);c.Put("a",1);c.Put("b",2);if _,ok:=c.Get("a");ok{t.Fatal("eviction")}}
