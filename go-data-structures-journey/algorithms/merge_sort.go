package algorithms

import "cmp"

// MergeSort returns a sorted copy of values using divide and conquer.
func MergeSort[T cmp.Ordered](values []T) []T { if len(values)<2{return append([]T(nil),values...)}; mid:=len(values)/2; left,right:=MergeSort(values[:mid]),MergeSort(values[mid:]); out:=make([]T,0,len(values));for len(left)>0&&len(right)>0{if left[0]<=right[0]{out=append(out,left[0]);left=left[1:]}else{out=append(out,right[0]);right=right[1:]}};return append(out,append(left,right...)...) }
