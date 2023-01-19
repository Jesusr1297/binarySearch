"""

Given a string s and an integer k, repeatedly delete the earliest k consecutive duplicate characters.

Constraints
k, n ≤ 100,000 where n is the length of s.


"""


def solve(s, k):
    n = 0
    while n < len(s):
        if s[n:n + k] == k * s[n]:
            s = s.replace(k * s[n], '')
            n = 0
        else:
            n += 1
    return s


s = "baaabbdddd"
k = 3
print(solve(s, k))

s = 'abcaabbccaaabbbccccba'
k = 2
print(solve(s, k))
