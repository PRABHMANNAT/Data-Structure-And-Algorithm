package structures
import "testing"
func TestDoublyLinkedList(t *testing.T){var l DoublyLinkedList[string];l.PushFront("a");l.PushBack("b");v,_:=l.PopBack();if v!="b"||l.Len()!=1{t.Fatal("list endpoints failed")}}
