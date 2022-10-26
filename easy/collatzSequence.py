"""

Given a positive integer n, find the length of its Collatz sequence.
The Collatz sequence is generated sequentially where

n = n / 2 if n is even
n = 3 * n + 1 if n is odd
And the sequence ends if n = 1

"""


def solve(n):
    sequence = 1
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n /= 2
        sequence += 1
    return sequence


n = 11
print(solve(n))
