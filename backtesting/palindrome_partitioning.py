from typing import List


def is_palindrome(s: str, l: int, r: int) -> bool:
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1

    return True


def partition(s: str) -> List[List[str]]:
    results = []
    partition = []

    def dfs(i):
        if i == len(s):
            results.append(partition.copy())
            return

        for j in range(i, len(s)):
            if is_palindrome(s, i, j):
                partition.append(s[i:j+1])
                dfs(j + 1)
                partition.pop()

    dfs(0)

    return results


def main():
    result = partition("aab")
    print(result)

    result = partition("a")
    print(result)

    result = partition("bb")
    print(result)

    result = partition("ab")
    print(result)

    result = partition("abbab")
    print(result)


if __name__ == "__main__":
    main()
