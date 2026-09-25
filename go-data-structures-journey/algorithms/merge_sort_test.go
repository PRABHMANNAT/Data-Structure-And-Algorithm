package algorithms
import "testing"
func TestMergeSort(t *testing.T){v:=MergeSort([]int{3,1,2});if v[0]!=1||v[2]!=3{t.Fatal("sort failed")}}
