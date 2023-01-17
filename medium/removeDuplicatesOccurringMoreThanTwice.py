"""

Given a list of integers nums sorted in ascending order,
remove in-place duplicates that appear more than twice.

This should be done in O(1) space.

Constraints
n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    count = {}
    out = []
    for num in nums:
        if num not in count:
            count[num] = 1
            out.append(num)
        elif count[num] == 1:
            count[num] += 1
            out.append(num)
    return out


nums = [3, 3, 3, 3, 4, 4, 8]
assert solve(nums) == [3, 3, 4, 4, 8]

nums = [1, 1]
assert solve(nums) == [1, 1]
