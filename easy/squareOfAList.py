"""

Given a list of integers sorted in ascending order nums,
square the elements and give the output in sorted order.

Constraints
n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    return sorted([num ** 2 for num in nums])


nums = [num for num in range(-50000, 50000, 1)]
print(solve(nums))
