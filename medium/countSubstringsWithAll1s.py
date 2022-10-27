"""

You are given a string s containing "1"s and "0"s.
Return the number of substrings that contain only "1"s.
Mod the result by 10 ** 9 + 7.

Constraints
0 ≤ n ≤ 100,000 where n is the length of s

"""


# 1:1, 2:3, 3:6, 4:10, 5:15 -> n*(n+1)/2
def solve(s):
    split = s.split('0')
    return sum([len(num)*(len(num)+1)/2 for num in split if num])


s = "111001"
assert solve(s) == 7

s = "11"
assert solve(s) == 3
