from functools import cache


@cache
def climbStairs(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)


def main():
    assert climbStairs(3) == 3, "Error: Wrong value!"

    assert climbStairs(2) == 2, "Error: Wrong value!"

    assert climbStairs(1) == 1, "Error: Wrong value!"


if __name__ == "__main__":
    main()
