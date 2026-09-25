package structures
import "testing"
func TestDisjointSet(t *testing.T){d:=NewDisjointSet(3);d.Union(0,1);if !d.Connected(0,1)||d.Connected(0,2){t.Fatal("union find failed")}}
