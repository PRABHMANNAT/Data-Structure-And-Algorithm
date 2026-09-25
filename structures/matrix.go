package structures

// Matrix stores a fixed-size rectangular grid.
type Matrix[T any] struct{ rows,cols int; data []T }
func NewMatrix[T any](rows,cols int)*Matrix[T]{return &Matrix[T]{rows:rows,cols:cols,data:make([]T,rows*cols)}}
func(m *Matrix[T]) Set(r,c int,v T){m.data[r*m.cols+c]=v}
func(m *Matrix[T]) At(r,c int)T{return m.data[r*m.cols+c]}
func(m *Matrix[T]) Dimensions()(int,int){return m.rows,m.cols}
