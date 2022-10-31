"""

Given an integer list nums where each number represents
the maximum number of hops you can make, determine whether
you can reach to the last index starting at index 0.

Constraints
n ≤ 100,000 where n is the length of nums.

"""


def solve(nums):
    goal = len(nums) - 1
    for i in range(goal, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


nums = [1, 0, 0, 0]
assert solve(nums) is False

nums = [2, 4, 0, 1, 0]
assert solve(nums) is True
