package search

type Index struct{ bloom *Bloom; trie *Trie; postings *Postings; cache *LRU }
func NewIndex()*Index{return &Index{NewBloom(4096),NewTrie(),NewPostings(),NewLRU(32)}}
func (i *Index) Add(doc Document){for _,term:=range tokens(doc.Text){i.bloom.Add(term);i.trie.Insert(term);i.postings.Add(term,doc.ID)}}
func (i *Index) Search(query string,k int)[]Result{q:=tokens(query);key:=query;if cached,ok:=i.cache.Get(key);ok{return cached};scores:=map[string]int{};for _,term:=range q{if !i.bloom.MightContain(term){continue};for id,count:=range i.postings.Lookup(term){scores[id]+=count}};out:=TopK(scores,k);i.cache.Put(key,out);return out}
func (i *Index) Complete(prefix string,limit int)[]string{return i.trie.Complete(prefix,limit)}
