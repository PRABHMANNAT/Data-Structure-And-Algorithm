package algorithms

// PrefixSums prepares constant-time inclusive range sum queries.
func PrefixSums(values []int) []int {
	prefix := make([]int, len(values)+1)
	for i, v := range values {
		prefix[i+1] = prefix[i] + v
	}
	return prefix
}

// RangeSum returns the sum in half-open interval [left,right).
func RangeSum(prefix []int, left, right int) int {
	if left < 0 || right < left || right >= len(prefix) {
		panic("invalid range")
	}
	return prefix[right] - prefix[left]
}
