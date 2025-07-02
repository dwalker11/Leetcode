from typing import List


def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True


def partition(s: str) -> List[List[str]]:
    results = [[c for c in s]]

    def backtrack(s, r, flip=False):
        if len(s) == 1:
            return

        if is_palindrome(s):
            if flip:
                results.append(r + [s])
            else:
                results.append([s] + r)

        l, r = 1, len(s) - 1

        subject, rest = s[:r], s[r:]
        backtrack(subject, [rest])

        subject, rest = s[l:], s[:l]
        backtrack(subject, [rest], True)

    backtrack(s, [], 0)

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


if __name__ == "__main__":
    main()
