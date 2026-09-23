package advanced
import "testing"
func TestAVL(t *testing.T){var a AVL;for _,v:=range []int{3,2,1,4}{a.Insert(v)};if got:=a.InOrder();len(got)!=4||got[0]!=1||!a.Contains(4){t.Fatal("AVL invariant failed")}}
