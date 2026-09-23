package search
import "testing"
func TestIndex(t *testing.T){i:=NewIndex();i.Add(Document{"a","go graph go"});i.Add(Document{"b","graph"});r:=i.Search("go graph",2);if len(r)!=2||r[0].ID!="a"{t.Fatal("ranking")}}
