package structures
import "testing"
func TestGraph(t *testing.T){g:=NewGraph();g.AddEdge("a","b");if len(g.BFS("a"))!=2{t.Fatal("graph")};u:=NewUnionFind(2);u.Union(0,1);if !u.Connected(0,1){t.Fatal("union find")}}
