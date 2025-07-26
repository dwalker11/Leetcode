from typing import List


def letterCombinations(digits: str) -> List[str]:
    h = {
        "2": ["a", "b", "c",],
        "3": ["d", "e", "f",],
        "4": ["g", "h", "i",],
        "5": ["j", "k", "l",],
        "6": ["m", "n", "o",],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v",],
        "9": ["w", "x", "y", "z"],
    }

    results = []

    def dfs(s, i):
        if i == len(digits):
            if len(s) > 0:
                results.append(s)
            return

        chars = h.get(digits[i], [])
        for c in chars:
            dfs(s+c, i+1)

    dfs("", 0)

    return results


def main():
    result = letterCombinations("23")
    print(result)

    result = letterCombinations("")
    print(result)

    result = letterCombinations("2")
    print(result)


if __name__ == "__main__":
    main()
