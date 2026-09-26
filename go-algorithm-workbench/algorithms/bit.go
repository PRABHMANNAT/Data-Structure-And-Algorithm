package algorithms

// PopCount counts set bits using Kernighan's method.
func PopCount(value uint) int {
	count := 0
	for value != 0 {
		value &= value - 1
		count++
	}
	return count
}

// IsPowerOfTwo reports whether value is a positive power of two.
func IsPowerOfTwo(value uint) bool { return value != 0 && value&(value-1) == 0 }
