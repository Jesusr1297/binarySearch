"""

Given a string s containing "0"s and "1"s, consider an operation where
you pick a character and toggle its value from "0" to "1" or from "1" to "0".
Return the minimum number of operations required to obtain a string containing
no instances of three identical consecutive characters.

Constraints
0 ≤ n ≤ 100,000 where n is the length of s

"""


def solve(s):
    count = {1: 0, 0: 0}
    for idx, val in enumerate(s[:-2]):
        if s[idx] == s[idx + 1] == s[idx + 2]:
            s = s[:idx + 1] + replacement[s[idx + 1]] + s[idx + 1 + 1:]
            count += 1
    return count


def solve2(s):
    ones = s.count('111')
    zeros = s.count('000')
    return zeros + ones


s = "1100011"
print(solve2(s))

s = "0001000"
print(solve2(s))

s = '1'*8
print(solve2(s))
