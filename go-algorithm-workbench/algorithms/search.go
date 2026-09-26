package algorithms

// BinarySearch returns the index of target in ascending values, or -1.
func BinarySearch[T constraintsOrdered](values []T, target T) int {
	low, high := 0, len(values)-1
	for low <= high {
		mid := low + (high-low)/2
		if values[mid] < target {
			low = mid + 1
		} else if values[mid] > target {
			high = mid - 1
		} else {
			return mid
		}
	}
	return -1
}

// LowerBound returns the first index where target can be inserted while ordered.
func LowerBound[T constraintsOrdered](values []T, target T) int {
	low, high := 0, len(values)
	for low < high {
		mid := low + (high-low)/2
		if values[mid] < target {
			low = mid + 1
		} else {
			high = mid
		}
	}
	return low
}
