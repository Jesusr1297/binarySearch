"""

You are given a list nums of length n + 1 picked from the range 1, 2, ..., n. By the pigeonhole principle,
there must be a duplicate. Find and return it. There is guaranteed to be exactly one duplicate.

Bonus: Can you do this in O(n) time and O(1) space?

Constraints
n ≤ 10,000

"""


def solve(nums):
    n_set = set()
    for num in nums:
        if num in n_set:
            return num
        else:
            n_set.add(num)
    return


def solve2(nums):
    nums_sum = sum(nums)
    supposed_sum = int((len(nums) - 1) * len(nums) / 2)
    return nums_sum - supposed_sum


nums = [1, 2, 3, 1]
print(solve(nums))
print(solve2(nums))

nums = [4, 2, 1, 3, 2]
print(solve(nums))
print(solve2(nums))
