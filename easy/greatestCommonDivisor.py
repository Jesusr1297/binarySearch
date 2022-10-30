"""

Given a list of positive integers nums, return the largest positive integer that divides each of the integers.

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    rank = set()
    for i in range(2, max(nums) + 1):
        count = 0
        for j in nums:
            if j % i == 0:
                count += 1
        rank.add(count)

    m = max(rank)
    return m


nums = [6, 12, 9]  # ans = 3
print(solve(nums))
