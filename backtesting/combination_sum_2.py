from collections import Counter
from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    results = []

    # create a hash of candidates
    h = Counter(candidates)

    # create a sorted list of keys in the hash of candidates
    hash_keys = sorted(h.keys(), reverse=True)

    def dfs(i, subset, t):
        if t > target or i >= len(hash_keys):
            return

        # pick the current key in the hash
        k = hash_keys[i]

        if h[k] < 0:
            return

        if t == target:
            return results.append(subset.copy())

        # add it to the subset, update t, and decrement it's count in the hash
        subset.append(k)
        h[k] -= 1

        # recurse on it
        dfs(i, subset, t+k)

        # remove last element from the subset, and reincrement it's count in the hash
        subset.pop()
        h[k] += 1

        # recurse on the next key in the hash
        dfs(i+1, subset, t)

    dfs(0, [], 0)

    return results


def main():
    res = combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(res)

    res = combinationSum2([2, 5, 2, 1, 2], 5)
    print(res)


if __name__ == "__main__":
    main()
