"""

Given a non-negative integer num, return whether it is a palindrome.

Bonus: Can you solve it without using strings?

Constraints

num < 2 ** 31

"""


def solve(num):
    num_str = str(num)
    for i in range(int(len(num_str) / 2)):
        if num_str[i] != num_str[-(i + 1)]:
            return False
    return True


def solve2(num):
    return str(num) == str(num)[::-1]
