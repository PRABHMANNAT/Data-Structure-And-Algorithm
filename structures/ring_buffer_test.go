package structures
import "testing"
func TestRingBuffer(t *testing.T){r:=NewRingBuffer[int](2);r.Add(1);r.Add(2);r.Add(3);v:=r.Values();if len(v)!=2||v[0]!=2{t.Fatal("ring buffer failed")}}
