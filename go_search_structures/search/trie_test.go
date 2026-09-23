package search
import "testing"
func TestTrie(t *testing.T){tr:=NewTrie();tr.Insert("graph");tr.Insert("go");if got:=tr.Complete("g",2);len(got)!=2{t.Fatal("completion")}}
