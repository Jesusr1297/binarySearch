"""

Given a list of sorted unique integers nums and an integer k,
return the kth (0-indexed) missing number from the first element of the list.

Constraints
n ≤ 100,000 where n is the length of nums.

"""


def solve(nums, k):
    num_set = set(nums)
    n = nums[0]
    missing = 0
    while missing < k + 1:
        n += 1
        if n not in num_set:
            missing += 1
    return n


def solve(nums, k):
    missing = 0
    for i in range(1, len(nums)):
        different = nums[i] - nums[i - 1]
        if missing + different - 1 > k:
            return nums[i - 1] + k + 1 - missing
        missing += different - 1
    return nums[len(nums) - 1] + k + 1 - missing


nums = [5, 6, 8, 9]  # 7
k = 0
print(solve(nums, k))

nums = [5, 6, 8, 9]  # 12
k = 3
print(solve(nums, k))
