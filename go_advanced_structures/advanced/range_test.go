package advanced
import "testing"
func TestRanges(t *testing.T){f:=NewFenwick(3);f.Add(0,2);f.Add(1,3);if v,_:=f.Range(0,1);v!=5{t.Fatal("fenwick")};s:=NewSegmentTree([]int{2,3,4});if v,_:=s.Sum(0,2);v!=9{t.Fatal("segment")};sp:=NewSparseTable([]int{4,1,3});if v,_:=sp.Min(0,2);v!=1{t.Fatal("sparse")}}
