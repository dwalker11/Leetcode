from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    results = []

    nums.sort()

    def dfs(i, subset):
        if i == len(nums):
            results.append(subset.copy())
            return

        subset.append(nums[i])

        dfs(i+1, subset)

        subset.pop()

        # Advance the pointer until next value is not equal to the current
        while i+1 < len(nums) and nums[i+1] == nums[i]:
            i += 1

        dfs(i+1, subset)

    dfs(0, [])

    return results


def main():
    results = subsetsWithDup([1, 2, 2])
    print(results)

    results = subsetsWithDup([1, 1])
    print(results)


if __name__ == "__main__":
    main()
