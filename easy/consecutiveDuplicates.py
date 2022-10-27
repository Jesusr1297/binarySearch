"""

Given a string s, consisting of "X" and "Y"s, delete the minimum number of
characters such that there's no consecutive "X" and no consecutive "Y".

Constraints
n ≤ 100,000 where n is the length of s

"""


def solve(s):
    while "XX" in s:
        s = s.replace("XX", "X")
    while "YY" in s:
        s = s.replace("YY", "Y")
    return s


s = "YYYXYXXYYYYYXXXXXXXYXYXYXYXYYYYYXXXYYYXYXYYXYYXYXYYXYXYXYX"
print(solve(s))

s = "YYX"
print(solve(s))
