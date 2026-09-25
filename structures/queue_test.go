package structures
import "testing"
func TestQueue(t *testing.T){var q Queue[int];q.Enqueue(1);q.Enqueue(2);v,_:=q.Dequeue();if v!=1||q.Len()!=1{t.Fatal("queue FIFO failed")}}
