"""

The factorial of a number n is defined as n! = n * (n - 1) * (n - 2) * ... * 1.

Given a positive 'integer a', return n such that n! = a.
If there is no integer n that is a factorial, then return -1.

Constraints
0 < a < 2 ** 31

"""


def solve(a):
    n = 1
    mult = 1
    while mult < a:
        n += 1
        mult *= n
    if mult == a:
        return n
    else:
        return -1


a = 6
print(solve(a), '\n\n')

a = 10
print(solve(a), '\n\n')

a = 120
print(solve(a), '\n\n')
