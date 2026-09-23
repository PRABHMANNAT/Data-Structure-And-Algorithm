package search

import "sort"
func TopK(scores map[string]int,k int)[]Result{out:=make([]Result,0,len(scores));for id,score:=range scores{out=append(out,Result{id,score})};sort.Slice(out,func(i,j int)bool{if out[i].Score==out[j].Score{return out[i].ID<out[j].ID};return out[i].Score>out[j].Score});if k<len(out){out=out[:k]};return out}
