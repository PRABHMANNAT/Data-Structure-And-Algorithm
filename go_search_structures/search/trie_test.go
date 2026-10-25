package search

import "testing"

func TestTrie(t *testing.T) {
	tr := NewTrie()
	tr.Insert("graph")
	tr.Insert("go")
	if got := tr.Complete("g", 2); len(got) != 2 {
		t.Fatal("completion")
	}
}
func TestTrieLimitedLexicalOrder(t *testing.T) {
	tr := NewTrie()
	for _, word := range []string{"cat", "car", "cap", "can"} {
		tr.Insert(word)
	}
	for i := 0; i < 100; i++ {
		got := tr.Complete("ca", 2)
		if len(got) != 2 || got[0] != "can" || got[1] != "cap" {
			t.Fatalf("unstable completion: %v", got)
		}
	}
	if got := tr.Complete("ca", 0); len(got) != 0 {
		t.Fatal("zero limit")
	}
}
