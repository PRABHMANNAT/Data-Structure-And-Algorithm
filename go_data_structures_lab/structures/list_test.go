package structures
import "testing"
func TestList(t *testing.T){var l List[int];l.Append(2);l.Prepend(1);l.Reverse();v,_:=l.RemoveFirst();if v!=2||l.Len()!=1{t.Fatal("list operations failed")}}
