package structures
import "testing"
func TestStack(t *testing.T){var s Stack[int];s.Push(1);s.Push(2);v,_:=s.Pop();if v!=2||s.Len()!=1{t.Fatal("stack LIFO failed")}}
