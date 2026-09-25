package algorithms
import "testing"
func TestBinarySearch(t *testing.T){i,ok:=BinarySearch([]int{1,3,5},3);if !ok||i!=1{t.Fatal("search failed")}}
