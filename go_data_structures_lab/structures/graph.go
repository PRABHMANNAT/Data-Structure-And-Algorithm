package structures

type Graph struct { edges map[string][]string }
func NewGraph()*Graph{return &Graph{edges:map[string][]string{}}}
func (g *Graph) AddVertex(v string){if _,ok:=g.edges[v];!ok{g.edges[v]=nil}}
func (g *Graph) AddEdge(from,to string){g.AddVertex(from);g.AddVertex(to);g.edges[from]=append(g.edges[from],to)}
func (g *Graph) BFS(start string)[]string{if _,ok:=g.edges[start];!ok{return nil};seen:=map[string]bool{start:true};q:=[]string{start};out:=[]string{};for len(q)>0{v:=q[0];q=q[1:];out=append(out,v);for _,n:=range g.edges[v]{if !seen[n]{seen[n]=true;q=append(q,n)}}};return out}
func (g *Graph) DFS(start string)[]string{seen:=map[string]bool{};out:=[]string{};var walk func(string);walk=func(v string){if seen[v]{return};seen[v]=true;out=append(out,v);for _,n:=range g.edges[v]{walk(n)}};if _,ok:=g.edges[start];ok{walk(start)};return out}
