package algorithms

// Permutations returns all permutations of values using backtracking.
func Permutations[T any](values []T) [][]T {
	work := append([]T(nil), values...)
	out := [][]T{}
	var visit func(int)
	visit = func(at int) {
		if at == len(work) {
			out = append(out, append([]T(nil), work...))
			return
		}
		for i := at; i < len(work); i++ {
			work[at], work[i] = work[i], work[at]
			visit(at + 1)
			work[at], work[i] = work[i], work[at]
		}
	}
	visit(0)
	return out
}

// NQueens counts valid ways to place n queens on an n-by-n board.
func NQueens(n int) int {
	columns, diagonalA, diagonalB := map[int]bool{}, map[int]bool{}, map[int]bool{}
	var place func(int) int
	place = func(row int) int {
		if row == n {
			return 1
		}
		count := 0
		for col := 0; col < n; col++ {
			if columns[col] || diagonalA[row-col] || diagonalB[row+col] {
				continue
			}
			columns[col], diagonalA[row-col], diagonalB[row+col] = true, true, true
			count += place(row + 1)
			delete(columns, col)
			delete(diagonalA, row-col)
			delete(diagonalB, row+col)
		}
		return count
	}
	return place(0)
}
