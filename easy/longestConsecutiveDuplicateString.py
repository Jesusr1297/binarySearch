"""

Given a lowercase alphabet string s, return the length of
the longest substring with same characters.

Constraints
0 ≤ n ≤ 100,000 where n is the length of s


"""


def solve(s):
    previous = ''
    count = 1
    max_count = 0
    for char in s:
        if char == previous:
            count += 1
        else:
            previous = char
            count = 1
        if count > max_count:
            max_count = count
    return max_count


def solve2(s):
    from itertools import groupby
    return max(len(list(group)) for key, group in groupby(s)) if s else 0


s = "abbbba"
assert solve(s) == 4
assert solve2(s) == 4

s = "aaabbb"
assert solve(s) == 3
assert solve2(s) == 3
