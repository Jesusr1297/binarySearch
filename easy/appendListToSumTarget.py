"""

You are given a list of integers nums and integers k and target.
Consider an operation where we choose an integer -k ≤ e ≤ k and append it to nums.

Return the minimum number of operations required such that the sum of nums equals to target.
Constraints

n ≤ 100,000 where n is the length of nums
1 ≤ k < 2 ** 31

"""


def solve(nums, k, target):
    num_sum = sum(nums)
    moves = 0
    if target > num_sum:
        while num_sum < target:
            num_sum += k
            moves += 1
        return moves
    elif target < num_sum:
        while target < num_sum:
            num_sum -= k
            moves += 1
        return moves
    else:
        return 0


def solve2(nums, k, target):
    import math
    return math.ceil(abs(sum(nums) - target) / k)


nums = [2, 1]  # 3
k = 3
target = 10
print(solve(nums, k, target))

nums = [2, 1]  # 4
k = 2
target = -4
print(solve(nums, k, target))

nums = [0, 1]  # 1
k = 1
target = 0
print(solve(nums, k, target))
