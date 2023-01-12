"""

You are given a list of integers nums of length n where all numbers in the list are from the interval
[1,n] and some elements appear twice while others only once.
Return all the numbers from [1,n] that are not in the list, sorted in ascending order.

Can you do it in O(n) time, modify nums in-place and use O(1) additional space?

Constraints
n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    n = len(nums)
    nums_set = set(nums)
    missing = []
    for i in range(1, n + 1):
        if i not in nums_set:
            missing.append(i)
    return missing


nums = [3, 3, 1, 1, 5, 5]
print(solve(nums))
