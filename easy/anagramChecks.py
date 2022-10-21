"""

Given two strings s0 and s1, return whether they are anagrams of each other.

Constraints
n ≤ 100,000 where n is the length of s0

"""


def solve(s0, s1):
    if len(s0) != len(s1):
        return False
    s0_set = set(s0)
    s1_set = set(s1)
    return s0_set.difference(s1_set) == set()


def solve2(s0, s1):

    def frequency(string):
        dictionary = {}
        for letter in string:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        return dictionary

    frequency_s0 = frequency(s0)
    frequency_s1 = frequency(s1)

    return frequency_s0 == frequency_s1


s0 = "listen"
s1 = "silent"
print(solve2(s0, s1))

s0 = "bedroom"
s1 = "bathroom"
print(solve2(s0, s1))

s0 = "aaa"
s1 = "a"
print(solve2(s0, s1))

s0 = "hah"
s1 = "aah"
print(solve2(s0, s1))


s0 = "wu"
s1 = "wutang"
print(solve2(s0, s1))
