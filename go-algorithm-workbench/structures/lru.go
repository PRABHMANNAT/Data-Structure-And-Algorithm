package structures

import "container/list"

// LRUCache evicts the least recently used item once capacity is reached.
type LRUCache[K comparable, V any] struct {
	capacity int
	items    map[K]*list.Element
	order    *list.List
}
type cacheEntry[K comparable, V any] struct {
	key   K
	value V
}

// NewLRUCache creates a cache with positive capacity.
func NewLRUCache[K comparable, V any](capacity int) *LRUCache[K, V] {
	if capacity < 1 {
		panic("LRU capacity must be positive")
	}
	return &LRUCache[K, V]{capacity: capacity, items: make(map[K]*list.Element), order: list.New()}
}

// Get retrieves and marks a value as most recently used.
func (c *LRUCache[K, V]) Get(key K) (V, bool) {
	var zero V
	element, ok := c.items[key]
	if !ok {
		return zero, false
	}
	c.order.MoveToFront(element)
	return element.Value.(cacheEntry[K, V]).value, true
}

// Put inserts or updates a value and returns the evicted key, if any.
func (c *LRUCache[K, V]) Put(key K, value V) (K, bool) {
	var zero K
	if e, ok := c.items[key]; ok {
		e.Value = cacheEntry[K, V]{key, value}
		c.order.MoveToFront(e)
		return zero, false
	}
	e := c.order.PushFront(cacheEntry[K, V]{key, value})
	c.items[key] = e
	if c.order.Len() <= c.capacity {
		return zero, false
	}
	old := c.order.Back()
	entry := old.Value.(cacheEntry[K, V])
	delete(c.items, entry.key)
	c.order.Remove(old)
	return entry.key, true
}

// Len returns values currently cached.
func (c *LRUCache[K, V]) Len() int { return c.order.Len() }
