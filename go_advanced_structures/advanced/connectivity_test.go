package advanced
import "testing"
func TestConnectivity(t *testing.T){d:=NewDSU(3);d.Union(0,1);if !d.Connected(0,1)||d.Connected(0,2){t.Fatal("dsu")};var tr Treap;tr.Insert(7);if !tr.Contains(7){t.Fatal("treap")}}
