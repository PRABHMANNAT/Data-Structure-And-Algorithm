package algorithms

// KMP returns all starting byte indices of pattern in text. Empty patterns match at zero.
func KMP(text, pattern string) []int {
	if pattern == "" {
		return []int{0}
	}
	prefix := make([]int, len(pattern))
	for i, j := 1, 0; i < len(pattern); i++ {
		for j > 0 && pattern[i] != pattern[j] {
			j = prefix[j-1]
		}
		if pattern[i] == pattern[j] {
			j++
			prefix[i] = j
		}
	}
	matches := []int{}
	for i, j := 0, 0; i < len(text); i++ {
		for j > 0 && text[i] != pattern[j] {
			j = prefix[j-1]
		}
		if text[i] == pattern[j] {
			j++
			if j == len(pattern) {
				matches = append(matches, i-j+1)
				j = prefix[j-1]
			}
		}
	}
	return matches
}
