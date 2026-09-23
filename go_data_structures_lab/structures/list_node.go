package structures

type listNode[T any] struct { value T; next *listNode[T] }
