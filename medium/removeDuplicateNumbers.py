"""

Given a list of integers nums, remove numbers that appear multiple times in the list,
while maintaining order of the appearance in the original list.

It should use O(k) space where k is the number of unique integers.

Constraints
n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    return [num for num in count if count[num] == 1]


nums = [1, 3, 5, 0, 3, 5, 8]  # [1, 0, 8]
print(solve(nums))
