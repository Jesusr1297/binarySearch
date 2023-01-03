"""

Given a list of integer nums, return the earliest index i such that the sum of the numbers
left of i is equal to the sum of numbers right of i. If there's no solution, return -1.

Sum of an empty list is defined to be 0.

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    for i in range(len(nums)):
        if sum(nums[0:i]) == sum(nums[i+1::]):
            return i
    return -1


def solve2(nums):
    S = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        if left_sum == (S - left_sum - x):
            return i
        left_sum += x
    return -1


nums = [2, 3, 4, 0, 5, 2, 2]
print(solve(nums=nums))

nums = [1, -2, 2]
print(solve(nums))
