from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    results = []

    def helper(s: List[int], i: int):
        if i == len(nums):
            results.append(s)
            return

        helper(s, i+1)
        u = s.copy()
        u.append(nums[i])
        helper(u, i+1)

    helper([], 0)
    return results


def main():
    result = subsets([1, 2, 3])
    print(result)


if __name__ == "__main__":
    main()
