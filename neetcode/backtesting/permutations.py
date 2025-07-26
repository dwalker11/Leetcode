from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    results = []

    def backtrack(s, subset):
        if len(s) == len(nums):
            results.append(subset.copy())

        for n in nums:
            if n in s:
                continue

            s.add(n)
            subset.append(n)
            backtrack(s, subset)
            subset.pop()
            s.remove(n)

    s = set()
    backtrack(s, [])

    return results


def main():
    result = permute([1, 2, 3])
    print(result)
    result = permute([0, 1])
    print(result)
    result = permute([1])
    print(result)


if __name__ == "__main__":
    main()
