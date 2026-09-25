package structures
import "testing"
func TestTrie(t *testing.T){tr:=NewTrie();tr.Insert("go");if !tr.Contains("go")||tr.Contains("g")||!tr.HasPrefix("g"){t.Fatal("trie failed")}}
