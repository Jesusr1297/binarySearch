"""

You can write out a number as a product of prime numbers, which are its prime factors.
The same prime factor may occur more than once.

Given an integer n greater than 1, find all of its prime factors and return them in sorted order.
"""


def solve(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


n = 81983948
print(solve(n))

n = 89130408
print(solve(n))
