package structures
import "testing"
func TestDeque(t *testing.T){var d Deque[int];d.PushFront(2);d.PushBack(3);d.PushFront(1);v,_:=d.PopBack();if v!=3||d.Len()!=2{t.Fatal("deque failed")}}
