package validsudoku

import "strconv"

type coords [2]int

func isValidSudoku(board [][]byte) bool {
	numMap := make(map[int][]coords)

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if num, err := strconv.Atoi(string(board[i][j])); err == nil {
				numMap[num] = append(numMap[num], [...]int{i, j})
			}
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
