package structures
import "testing"
func TestAdvanced(t *testing.T){m:=NewHashMap[string,int]();m.Set("x",1);if v,_:=m.Get("x");v!=1{t.Fatal("map")};h:=NewMinHeap(func(a,b int)bool{return a<b});h.Push(2);h.Push(1);if v,_:=h.Pop();v!=1{t.Fatal("heap")};tr:=NewTrie();tr.Insert("go");if !tr.Contains("go"){t.Fatal("trie")}}
