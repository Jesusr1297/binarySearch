"""

You are given a list of integers nums, representing a decimal number and nums[i] is between [0, 9].
For example, [1, 3, 9] represents the number 139.

Return the same list in the same representation except modified so that 1 is added to the number.

Constraints
1 ≤ n ≤ 100,000 where n is the length of nums.

"""


def solve(nums):
    index = len(nums) - 1
    while index >= 0 and nums[index] == 9:
        nums[index] = 0
        index -= 1
    if index < 0:
        nums.insert(0, 1)
    return nums


nums = [1, 2, 3, 4, 5, 6, 7, 9]
print(solve(nums))

nums = [9 for x in range(23)]
print(solve(nums))

nums = [9, 9]
print(solve(nums))
