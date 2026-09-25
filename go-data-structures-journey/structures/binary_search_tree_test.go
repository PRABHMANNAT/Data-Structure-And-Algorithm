package structures
import "testing"
func TestBinarySearchTree(t *testing.T){var tree BinarySearchTree[int];tree.Insert(2);tree.Insert(1);tree.Insert(3);if !tree.Contains(3)||len(tree.InOrder())!=3{t.Fatal("tree failed")}}
