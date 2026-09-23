package main
import("fmt"; a "github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go_advanced_structures/advanced")
func main(){t:=a.NewSegmentTree([]int{5,2,7});sum,_:=t.Sum(0,2);fmt.Println("range sum:",sum)}
