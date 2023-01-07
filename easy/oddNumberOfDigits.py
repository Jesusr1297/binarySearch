"""

Given a list of positive integers nums,
return the number of integers that have odd number of digits.

Constraints
n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    return len([num for num in nums if len(str(num)) % 2])


nums = [1, 800, 2, 10, 3]
assert solve(nums) == 4

