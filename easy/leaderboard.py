"""

You are given a list of integers nums, representing the number of chess
matches each person has won. Return a relative ranking (0-indexed) of each person.
If two players have won the same amount, their ranking should be the same.

Constraints
n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    data = sorted(set(nums), reverse=True)
    rank = {index: ranked for ranked, index in enumerate(data)}

    return [rank[n] for n in nums]


nums = [50, 30, 50, 90, 10]     # [1, 2, 1, 0, 3]
print(solve(nums))
