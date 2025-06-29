from typing import List


def exists(board: List[List[str]], word: str) -> bool:
    def findWord(direction: str, row: int, col: int, substring: str) -> bool:
        # Base cases
        if len(substring) == len(word):
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
            return False

        i = len(substring)
        current, target = board[row][col], word[i]

        if current != target and substring != "":
            return False

        # General cases

        # 1 - We don't have a match
        while current != target:
            # keep advancing on the current row unless we're at the last character
            if col == len(board[row]) - 1:
                col, row = 0, row + 1
            else:
                col += 1

            if row == len(board):
                return False

            if findWord(direction, row, col, substring):
                return True

        # 2 - We have a match
        if direction != "r" and findWord("l", row, col+1, substring+current):
            return True

        if direction != "l" and findWord("r", row, col-1, substring+current):
            return True

        if direction != "d" and findWord("u", row+1, col, substring+current):
            return True

        if direction != "u" and findWord("d", row-1, col, substring+current):
            return True

        return False

    return findWord("", 0, 0, "")


def main():
    result = exists([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                    "A", "D", "E", "E"]], "ABCCED")
    print(result)

    result = exists([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                    "A", "D", "E", "E"]], "SEE")
    print(result)

    result = exists([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                    "A", "D", "E", "E"]], "ABCB")
    print(result)


if __name__ == "__main__":
    main()
