package search

type Postings struct{ terms map[string]map[string]int }
func NewPostings()*Postings{return &Postings{terms:map[string]map[string]int{}}}
func (p *Postings) Add(term,doc string){if p.terms[term]==nil{p.terms[term]=map[string]int{}};p.terms[term][doc]++}
func (p *Postings) Lookup(term string)map[string]int{out:=map[string]int{};for id,count:=range p.terms[term]{out[id]=count};return out}
