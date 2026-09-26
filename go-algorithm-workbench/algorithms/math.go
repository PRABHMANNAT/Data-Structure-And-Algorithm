package algorithms

// GCD computes the greatest common divisor using Euclid's algorithm.
func GCD(a, b int) int {
	if a < 0 {
		a = -a
	}
	if b < 0 {
		b = -b
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// Sieve returns all prime numbers not greater than limit.
func Sieve(limit int) []int {
	if limit < 2 {
		return nil
	}
	composite := make([]bool, limit+1)
	primes := []int{}
	for value := 2; value <= limit; value++ {
		if composite[value] {
			continue
		}
		primes = append(primes, value)
		if value <= limit/value {
			for multiple := value * value; multiple <= limit; multiple += value {
				composite[multiple] = true
			}
		}
	}
	return primes
}
