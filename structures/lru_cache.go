package structures

import "container/list"

// LRUCache evicts the least recently used item when full.
type LRUCache[K comparable,V any] struct{ cap int; order *list.List; items map[K]*list.Element }
type cacheEntry[K comparable,V any] struct{ key K; value V }
func NewLRUCache[K comparable,V any](capacity int)*LRUCache[K,V]{return &LRUCache[K,V]{cap:capacity,order:list.New(),items:map[K]*list.Element{}}}
func(c *LRUCache[K,V]) Get(k K)(V,bool){var z V;e,ok:=c.items[k];if !ok{return z,false};c.order.MoveToFront(e);return e.Value.(cacheEntry[K,V]).value,true}
func(c *LRUCache[K,V]) Put(k K,v V){if e,ok:=c.items[k];ok{e.Value=cacheEntry[K,V]{k,v};c.order.MoveToFront(e);return};e:=c.order.PushFront(cacheEntry[K,V]{k,v});c.items[k]=e;if c.order.Len()>c.cap{last:=c.order.Back();delete(c.items,last.Value.(cacheEntry[K,V]).key);c.order.Remove(last)}}
func(c *LRUCache[K,V]) Len()int{return c.order.Len()}
