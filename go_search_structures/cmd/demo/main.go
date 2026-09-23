package main
import("fmt"; s "github.com/PRABHMANNAT/Data-Structure-And-Algorithm/go_search_structures/search")
func main(){i:=s.NewIndex();i.Add(s.Document{ID:"go",Text:"go graph structures"});fmt.Println(i.Search("graph",3))}
