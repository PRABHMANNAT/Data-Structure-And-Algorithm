// Package algorithms contains small algorithms that pair naturally with the data structures.
package algorithms

import "cmp"

// BinarySearch returns the index of target in a sorted slice.
func BinarySearch[T cmp.Ordered](values []T, target T) (int, bool) { low, high := 0, len(values)-1; for low <= high { mid := low+(high-low)/2; if values[mid] == target { return mid, true }; if values[mid] < target { low = mid+1 } else { high = mid-1 } }; return 0, false }
