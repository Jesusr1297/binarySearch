"""

The Fibonacci sequence goes like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number can be found by adding up the two numbers before it, and the first two numbers are always 1.
Write a function that takes an integer n and returns the nth Fibonacci number in the sequence.

Constraints
n ≤ 30

"""


def solve(n):
    if n < 3:
        return 1
    return solve(n-1) + solve(n-2)


n = 1           # 1
print(solve(n))

n = 6           # 8
print(solve(n))

n = 7           # 13
print(solve(n))

n = 14          # 377
print(solve(n))
