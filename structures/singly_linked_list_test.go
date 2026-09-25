package structures
import "testing"
func TestSinglyLinkedList(t *testing.T){var l SinglyLinkedList[int];l.Append(2);l.Prepend(1);v,ok:=l.RemoveFirst();if !ok||v!=1||l.Len()!=1{t.Fatal("list order failed")}}
