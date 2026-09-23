package search

import "hash/fnv"
type Bloom struct{ bits []bool }
func NewBloom(size int)*Bloom{return &Bloom{bits:make([]bool,size)}}
func hashWord(word string,seed uint32)uint32{h:=fnv.New32a();h.Write([]byte(word));return h.Sum32()^seed}
func (b *Bloom) Add(word string){for _,seed:=range []uint32{17,29,43}{b.bits[hashWord(word,seed)%uint32(len(b.bits))]=true}}
func (b *Bloom) MightContain(word string)bool{for _,seed:=range []uint32{17,29,43}{if !b.bits[hashWord(word,seed)%uint32(len(b.bits))]{return false}};return true}
