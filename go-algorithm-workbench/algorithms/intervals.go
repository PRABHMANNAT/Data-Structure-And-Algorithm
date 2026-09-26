package algorithms

import "sort"

// Interval has inclusive start and end bounds.
type Interval struct{ Start, End int }

// MergeIntervals coalesces overlapping intervals in O(n log n).
func MergeIntervals(intervals []Interval) []Interval {
	if len(intervals) == 0 {
		return nil
	}
	ordered := append([]Interval(nil), intervals...)
	sort.Slice(ordered, func(i, j int) bool { return ordered[i].Start < ordered[j].Start })
	out := []Interval{ordered[0]}
	for _, next := range ordered[1:] {
		last := &out[len(out)-1]
		if next.Start <= last.End {
			if next.End > last.End {
				last.End = next.End
			}
		} else {
			out = append(out, next)
		}
	}
	return out
}
