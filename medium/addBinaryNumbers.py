"""

Given two strings a and b that represent binary numbers,
add them and return their sum, also as a string.

The input strings are guaranteed to be non-empty and contain only 1s and 0s.

Constraints

n ≤ 100,000 where n is the length of a
m ≤ 100,000 where m is the length of b

"""


def solve(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''

    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    return result


a = "1"
b = "1"
assert solve(a, b) == '10'

a = "111"
b = "1"
assert solve(a, b) == '1000'
