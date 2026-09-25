package structures
import "testing"
func TestGraph(t *testing.T){g:=NewGraph[string]();g.AddEdge("a","b");g.AddEdge("b","c");if len(g.BreadthFirst("a"))!=3{t.Fatal("BFS failed")}}
