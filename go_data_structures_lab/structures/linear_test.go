package structures
import "testing"
func TestLinear(t *testing.T){var s Stack[int];s.Push(3);if v,_:=s.Pop();v!=3{t.Fatal("stack")};var q Queue[string];q.Enqueue("a");if v,_:=q.Dequeue();v!="a"{t.Fatal("queue")};var d Deque[int];d.PushBack(1);if v,_:=d.PopBack();v!=1{t.Fatal("deque")}}
