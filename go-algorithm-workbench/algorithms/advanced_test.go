package algorithms

import "testing"

func TestAdvancedHelpers(t *testing.T) {
	if GCD(54, 24) != 6 || len(Sieve(10)) != 4 || PopCount(7) != 3 || !IsPowerOfTwo(8) {
		t.Fatal("helper failure")
	}
	if NQueens(4) != 2 || len(Permutations([]int{1, 2, 3})) != 6 {
		t.Fatal("backtracking failure")
	}
	if RangeSum(PrefixSums([]int{2, 3, 4}), 1, 3) != 7 {
		t.Fatal("range sum failure")
	}
}
