"""

You are given a string s containing "1"s and "0"s which
represents a binary number.
Return the number of steps it would take to reduce the number to "1" with these rules:

If the number is even, divide by 2
Otherwise, add 1

Constraints
1 ≤ n ≤ 100,000 where n is the length of s

"""


def solve(s):
    decimal = sum([int(num) * 2 ** index for index, num in enumerate(s[::-1])])
    counter = 0

    while decimal != 1:
        if decimal % 2:
            decimal += 1
        else:
            decimal /= 2
        counter += 1
    return counter


def solve2(s):
    if len(s) == 1:
        return 0

    count_ = 0
    i = len(s) - 1
    while i > 0:

        if s[i] == '0':
            count_ += 1
            i -= 1

        else:
            count_ += 1

            while s[i] == '1' and i > 0:
                count_ += 1
                i -= 1
            if i == 0:
                count_ += 1

            s = s[:i] + "1" + s[i + 1:]
    return count_


s = '101'
assert solve2(s) == 5

s = "111"
assert solve2(s) == 4

s = "10"
assert solve2(s) == 1
