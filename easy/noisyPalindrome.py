"""

You are given a string s containing lowercase and uppercase alphabet
characters as well as digits from "0" to "9". Return whether s is a palindrome
if we only consider the lowercase alphabet characters.

Constraints
0 ≤ n ≤ 100,000 where n is the length of s

"""


def solve(s):
    new_s = [char for char in s if char.islower()]
    return new_s == new_s[::-1]


s = "a92bcbXa"
assert solve(s) is True

s = "abZ"
assert solve(s) is False
