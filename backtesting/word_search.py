from typing import List, Tuple


def exists(board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    visited = set()

    def findWord(direction: str, coords: Tuple[int, int], substring: str) -> bool:
        # Base cases
        if len(substring) == len(word):
            return True

        row, col = coords

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
            return False

        i = len(substring)
        current, target = board[row][col], word[i]

        if current != target:
            return False

        # General cases
        visited.add(coords)

        new_coords = (coords[0], coords[1]+1)  # Move right
        if new_coords not in visited and direction != "r":
            if findWord("l", new_coords, substring+current):
                return True

        new_coords = (coords[0], coords[1]-1)  # Move left
        if new_coords not in visited and direction != "l":
            if findWord("r", new_coords, substring+current):
                return True

        new_coords = (coords[0]+1, coords[1])  # Move down
        if new_coords not in visited and direction != "d":
            if findWord("u", new_coords, substring+current):
                return True

        new_coords = (coords[0]-1, coords[1])  # Move up
        if new_coords not in visited and direction != "u":
            if findWord("d", new_coords, substring+current):
                return True

        visited.remove(coords)

        return False

    for i in range(ROWS):
        for j in range(COLS):
            if findWord("", (i, j), ""):
                return True

    return False


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

    result = exists([["a", "a", "a", "a"], ["a", "a", "a", "a"], [
                    "a", "a", "a", "a"]], "aaaaaaaaaaaaa")
    print(result)

    result = exists([["a", "a", "a"], ["A", "A", "A"],
                    ["a", "a", "a"]], "aAaaaAaaA")
    print(result)


if __name__ == "__main__":
    main()
