package structures
import "testing"
func TestHashMap(t *testing.T){h:=NewHashMap[string,int]();h.Set("x",1);v,ok:=h.Get("x");if !ok||v!=1||!h.Delete("x"){t.Fatal("map failed")}}
