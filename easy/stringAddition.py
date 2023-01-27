"""

Given two strings a and b, both representing an integer, add them and return it in the same string representation.

This should be implemented directly, instead of using eval or built-in big integers.

Constraints`

n ≤ 200 where n is the length of a
m ≤ 200 where m is the length of b

"""


def solve(a, b):
    return str(int(a) + int(b))
