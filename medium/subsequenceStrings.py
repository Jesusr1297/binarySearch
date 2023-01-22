"""

Given two lowercase alphabet strings s1 and s2, determine if s1 is a subsequence of s2.

Constraints
n ≤ 100,000 where n is the length of s1
m ≤ 100,000 where m is the length of s2

"""


def solve(s1, s2):
    p = 0
    try:
        for letter in s1:
            while True:
                if letter == s2[p]:
                    p += 1
                    break
                else:
                    p += 1
                if p == len(s2):
                    return False
        return True
    except IndexError:
        return False


def solve2(s1, s2):
    n = len(s1)
    m = len(s2)
    s1_ptr = 0
    s2_ptr = 0
    while s1_ptr < n and s2_ptr < m:
        if s1[s1_ptr] == s2[s2_ptr]:
            s1_ptr += 1
        s2_ptr += 1
    return s1_ptr == n


s1 = "ppl"
s2 = "apple"
assert solve(s1, s2) is True

s1 = "ale"
s2 = "apple"
assert solve(s1, s2) is True

s1 = "elppa"
s2 = "apple"
assert solve(s1, s2) is False

s1 = ""
s2 = ""
assert solve(s1, s2) is True

s1 = "acc"
s2 = ""
assert solve(s1, s2) is False

s1 = "aa"
s2 = "bac"
assert solve(s1, s2) is False
