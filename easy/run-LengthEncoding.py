"""

Given a string s, return its run-length encoding.
You can assume the string to be encoded have no digits and
consists solely of alphabetic characters.

Constraints
n ≤ 100,000 where n is the length of s

"""
import itertools


def solve(s):
    previous = s[0]
    count = 1
    output = ''

    for char in s[1::]:
        if char == previous:
            count += 1
        else:
            output += str(count) + previous
            previous = char
            count = 1
    return output + str(count) + previous


def solve2(s):
    return "".join([str(len(list(j))) + i for i, j in itertools.groupby(s)])


s = 'aaaabbbccdaa'
assert solve(s) == "4a3b2c1d2a"
assert solve2(s) == '4a3b2c1d2a'
