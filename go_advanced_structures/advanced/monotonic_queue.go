package advanced

type MonotonicMax struct{ values []int }
func (m *MonotonicMax) Push(v int){for len(m.values)>0&&m.values[len(m.values)-1]<v{m.values=m.values[:len(m.values)-1]};m.values=append(m.values,v)}
func (m *MonotonicMax) Pop(v int){if len(m.values)>0&&m.values[0]==v{m.values=m.values[1:]}}
func (m *MonotonicMax) Max()(int,error){if len(m.values)==0{return 0,ErrInvalidRange};return m.values[0],nil}
