package main

import (
	"fmt"
	"github.com/your-account/go-data-structures-journey/structures"
)

func main() { var q structures.Queue[string]; q.Enqueue("first"); q.Enqueue("second"); v, _ := q.Dequeue(); fmt.Println(v) }
