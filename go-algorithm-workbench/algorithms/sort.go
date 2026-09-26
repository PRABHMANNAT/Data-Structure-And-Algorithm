// Package algorithms collects implementations arranged by technique.
package algorithms

// MergeSort returns a sorted copy of values in O(n log n) time and O(n) space.
func MergeSort[T constraintsOrdered](values []T) []T {
	if len(values) < 2 {
		return append([]T(nil), values...)
	}
	mid := len(values) / 2
	return merge(MergeSort(values[:mid]), MergeSort(values[mid:]))
}
func merge[T constraintsOrdered](a, b []T) []T {
	out := make([]T, 0, len(a)+len(b))
	i, j := 0, 0
	for i < len(a) && j < len(b) {
		if a[i] <= b[j] {
			out = append(out, a[i])
			i++
		} else {
			out = append(out, b[j])
			j++
		}
	}
	out = append(out, a[i:]...)
	return append(out, b[j:]...)
}

// QuickSort sorts values in place using an iterative partition strategy.
func QuickSort[T constraintsOrdered](v []T) {
	if len(v) < 2 {
		return
	}
	var sortRange func(int, int)
	sortRange = func(lo, hi int) {
		if lo >= hi {
			return
		}
		p := partition(v, lo, hi)
		sortRange(lo, p-1)
		sortRange(p+1, hi)
	}
	sortRange(0, len(v)-1)
}
func partition[T constraintsOrdered](v []T, lo, hi int) int {
	pivot := v[hi]
	i := lo
	for j := lo; j < hi; j++ {
		if v[j] <= pivot {
			v[i], v[j] = v[j], v[i]
			i++
		}
	}
	v[i], v[hi] = v[hi], v[i]
	return i
}

type constraintsOrdered interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 | ~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~float32 | ~float64 | ~string
}
