from typing import List


def canJump(nums: List[int]) -> bool:
    lookup = {i: [] for i in range(len(nums))}

    # build a hash of reachable elements
    for i, n in enumerate(nums):
        if i == len(nums) - 1:
            break
        for j in range(n):
            pos = i + 1 + j
            if pos < len(nums):
                lookup.get(pos).append(i)

    def is_reachable(idx):
        if idx == 0:
            return True

        if not lookup[idx]:
            return False

        new_idx = min(lookup[idx])
        return True if is_reachable(new_idx) else False

    return is_reachable(len(nums) - 1)


def main():
    result = canJump([2, 3, 1, 1, 4])
    print(result)

    result = canJump([3, 2, 1, 0, 4])
    print(result)


if __name__ == "__main__":
    main()
