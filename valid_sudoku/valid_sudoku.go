package validsudoku

import "strconv"

type coords [2]int
type set map[int]bool

func isValidSudoku(board [][]byte) bool {
	squareMaps := map[coords]set{
		[...]int{0,0}: make(set),
		[...]int{0,1}: make(set),
		[...]int{0,2}: make(set),
		[...]int{1,0}: make(set),
		[...]int{1,1}: make(set),
		[...]int{1,2}: make(set),
		[...]int{2,0}: make(set),
		[...]int{2,1}: make(set),
		[...]int{2,2}: make(set),
	}
	numMap := make(map[int][]coords)

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] == '.' {
				continue
			}
			
			key := [...]int{i / 3, j / 3}
			square := squareMaps[key]
			num, _ := strconv.Atoi(string(board[i][j]))

			if _, ok := square[num]; ok {
				return false
			}

			square[num] = true
			numMap[num] = append(numMap[num], [...]int{i, j})
		}
	}

	for _, v := range numMap {
		visitedRows := map[int]bool{v[0][0]: true}
		visitedCols := map[int]bool{v[0][1]: true}

		for i := 1; i < len(v); i++ {
			row, col := v[i][0], v[i][1]

			_, hasVisitedRow := visitedRows[row]
			_, hasVisitedCol := visitedCols[col]

			if hasVisitedRow || hasVisitedCol {
				return false
			} else {
				visitedRows[row] = true
				visitedCols[col] = true
			}
		}
	}

	return true
}
