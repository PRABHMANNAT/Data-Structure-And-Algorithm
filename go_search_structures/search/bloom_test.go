package search
import "testing"
func TestBloom(t *testing.T){b:=NewBloom(128);b.Add("go");if !b.MightContain("go"){t.Fatal("false negative")}}
