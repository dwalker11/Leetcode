from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(available_candidates, s):
        t = sum(s)

        if t > target:
            return

        if t == target:
            c = s[-1]
            available_candidates.remove(c)
            return result.append(s)

        for c in candidates:
            if c in available_candidates:
                dfs(available_candidates, [*s, c])

    for i, _ in enumerate(candidates):
        x = candidates[i:]
        dfs(set(x), [])

    return result


def main():
    results = combinationSum([2], 1)  # [1, 2] [2,3,5] [2, 3, 6, 7]
    print(results)


if __name__ == "__main__":
    main()
