"""

Given a string s, consisting of digits and lowercase alphabet characters,
that's a run-length encoded string, return its decoded version.

Note: The original string is guaranteed not to have numbers in it.

Constraints
0 ≤ n ≤ 100,000 where n is the length of s

"""


def solve(s):
    final_string = ''
    num = ''
    for i in s:
        if i.isnumeric():
            num += i
        else:
            final_string += int(num) * i
            num = ''
    return final_string


s = "4a3b2c1d2a"
assert "aaaabbbccdaa" == solve(s)

s = "10a"
assert "aaaaaaaaaa" == solve(s)
