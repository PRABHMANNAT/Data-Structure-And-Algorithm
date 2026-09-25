package structures
import "testing"
func TestPriorityQueue(t *testing.T){p:=NewPriorityQueue(func(a,b int)bool{return a<b});p.Push(3);p.Push(1);v,_:=p.Pop();if v!=1{t.Fatal("heap order failed")}}
