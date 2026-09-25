package main

import (
	"fmt"
	"github.com/your-account/go-data-structures-journey/structures"
)

func main() { t := structures.NewTrie(); t.Insert("gopher"); fmt.Println(t.HasPrefix("go")) }
