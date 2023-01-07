"""

You are given a list of integers nums sorted in ascending order, and integers a, b, and c.
Apply the following function for each number x in nums:
 ax^2+bx+c and return the resulting list in ascending order.

This should be done in O(n) time.

Constraints
n ≤ 100,000 where n is the length of nums

"""


def solve(nums, a, b, c):
    results = []

    for num in nums:
        results.append(a * num ** 2 + b * num + c)

    return sorted(results)


nums = [-2, 3]
a = 1
b = -3
c = 2

assert solve(nums, a, b, c) == [2, 12]
