# Linked list

Linked lists trade cache locality for inexpensive node relinking. They are a
good fit when a caller already holds a node position; otherwise an array is
often simpler and faster in Go.
