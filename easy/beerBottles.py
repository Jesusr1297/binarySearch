"""

You are given an integer n representing n full beer bottles.
Given that you can exchange 3 empty beer bottles for 1 full beer bottle,
return the number of beer bottles you can drink.

Constraints
0 ≤ n < 2 ** 31

"""


def solve(n):
    total = n
    while n >= 3:
        exchange = n // 3
        total += exchange
        n = (n % 3) + exchange
    return total


n = 2**31
print(solve(n))
