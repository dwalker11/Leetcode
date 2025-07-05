from typing import List


def canJump(nums: List[int]) -> bool:
    def recurse(idx):
        if idx == 0:
            return True

        reachable = []

        # save every index that's reachable from idx
        for i in range(idx - 1, -1, -1):
            val = nums[i]
            if val >= idx - i:
                reachable.append(i)

        # pop an element off of the reachable list and call recurse with it
        while reachable:
            j = reachable.pop()
            if recurse(j):
                return True

        return False

    return recurse(len(nums) - 1)


def main():
    result = canJump([2, 3, 1, 1, 4])
    print(result)

    result = canJump([3, 2, 1, 0, 4])
    print(result)


if __name__ == "__main__":
    main()
