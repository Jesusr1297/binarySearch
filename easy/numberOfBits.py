"""

Given an integer n, return the number of 1 bits in n.

Constraints
0 ≤ n < 2 ** 31

"""


def solve(n):
    return bin(n).count('1')


n = 0
print(solve(n))

n = 1
print(solve(n))

n = 2
print(solve(n))

n = 3
print(solve(n))

n = 4
print(solve(n))

n = 2**32 - 1
print(solve(n))
