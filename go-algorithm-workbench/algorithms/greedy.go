package algorithms

import "sort"

// Activity is an interval that can be selected by ActivitySelection.
type Activity struct{ Start, End int }

// ActivitySelection returns a maximal compatible set using earliest finish time.
func ActivitySelection(activities []Activity) []Activity {
	ordered := append([]Activity(nil), activities...)
	sort.Slice(ordered, func(i, j int) bool { return ordered[i].End < ordered[j].End })
	out := []Activity{}
	lastEnd := -int(^uint(0)>>1) - 1
	for _, a := range ordered {
		if a.Start >= lastEnd {
			out = append(out, a)
			lastEnd = a.End
		}
	}
	return out
}
