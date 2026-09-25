package structures

// DisjointSet tracks connected components using union by size and path compression.
type DisjointSet struct{ parent,size []int }
func NewDisjointSet(n int)*DisjointSet{p:=make([]int,n);s:=make([]int,n);for i:=range p{p[i]=i;s[i]=1};return &DisjointSet{p,s}}
func(d *DisjointSet) Find(x int)int{if d.parent[x]!=x{d.parent[x]=d.Find(d.parent[x])};return d.parent[x]}
func(d *DisjointSet) Union(a,b int)bool{a,b=d.Find(a),d.Find(b);if a==b{return false};if d.size[a]<d.size[b]{a,b=b,a};d.parent[b]=a;d.size[a]+=d.size[b];return true}
func(d *DisjointSet) Connected(a,b int)bool{return d.Find(a)==d.Find(b)}
