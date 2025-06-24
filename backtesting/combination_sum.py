from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    results = []

    def dfs(i, s, t):
        if i >= len(candidates) or t > target:
            return

        if t == target:
            return results.append(s.copy())

        c = candidates[i]
        s.append(c)
        dfs(i, s, t + c)
        s.pop()
        dfs(i+1, s, t)

    dfs(0, [], 0)

    return results


def main():
    results = combinationSum([2, 3, 6, 7], 7)  # [1, 2] [2,3,5] [2, 3, 6, 7]
    print(results)


if __name__ == "__main__":
    main()
