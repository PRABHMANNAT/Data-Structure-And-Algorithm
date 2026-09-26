package algorithms

// Knapsack01 returns the largest value within capacity; each item is selectable once.
func Knapsack01(weights, values []int, capacity int) int {
	if len(weights) != len(values) || capacity < 0 {
		panic("invalid knapsack inputs")
	}
	dp := make([]int, capacity+1)
	for i, w := range weights {
		for c := capacity; c >= w; c-- {
			if candidate := dp[c-w] + values[i]; candidate > dp[c] {
				dp[c] = candidate
			}
		}
	}
	return dp[capacity]
}

// LongestIncreasingSubsequence returns LIS length in O(n log n).
func LongestIncreasingSubsequence(values []int) int {
	tails := []int{}
	for _, v := range values {
		index := LowerBound(tails, v)
		if index == len(tails) {
			tails = append(tails, v)
		} else {
			tails[index] = v
		}
	}
	return len(tails)
}

// LongestCommonSubsequence returns the common subsequence length in O(mn).
func LongestCommonSubsequence(a, b string) int {
	runesA, runesB := []rune(a), []rune(b)
	previous := make([]int, len(runesB)+1)
	for _, x := range runesA {
		current := make([]int, len(runesB)+1)
		for j, y := range runesB {
			if x == y {
				current[j+1] = previous[j] + 1
			} else if previous[j+1] > current[j] {
				current[j+1] = previous[j+1]
			} else {
				current[j+1] = current[j]
			}
		}
		previous = current
	}
	return previous[len(runesB)]
}
