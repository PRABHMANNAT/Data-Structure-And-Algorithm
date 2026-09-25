package structures

// Graph represents an unweighted directed graph with adjacency sets.
type Graph[T comparable] struct{ edges map[T]map[T]struct{} }
func NewGraph[T comparable]()*Graph[T]{return &Graph[T]{edges:map[T]map[T]struct{}{}}}
func(g *Graph[T]) AddEdge(from,to T){if g.edges[from]==nil{g.edges[from]=map[T]struct{}{}};g.edges[from][to]=struct{}{};if g.edges[to]==nil{g.edges[to]=map[T]struct{}{}}}
func(g *Graph[T]) Neighbors(v T)[]T{out:=[]T{};for n:=range g.edges[v]{out=append(out,n)};return out}
func(g *Graph[T]) BreadthFirst(start T)[]T{seen:=map[T]bool{start:true};q:=[]T{start};out:=[]T{};for len(q)>0{v:=q[0];q=q[1:];out=append(out,v);for n:=range g.edges[v]{if !seen[n]{seen[n]=true;q=append(q,n)}}};return out}
