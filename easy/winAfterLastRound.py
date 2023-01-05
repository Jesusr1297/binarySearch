"""

You are given a list of integers nums of length n representing the
current score of swimmers in a competition. There is one more round
to swim and the first place winner for this round gets n points, second
place n-1 points, etc. and the last place gets 1 point.

Return the number of swimmers that can still win the competition
after the last round. If you tie for first in points, this still counts as winning.

Constraints
n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    if not nums:
        return 0
    n = len(nums)
    ans = 0
    nums.sort()
    a = 0
    for i in range(n - 1, -1, -1):
        cand = nums[i] + n - i
        if cand > a:
            a = cand
    for x in nums:
        if x + n >= a:
            ans += 1
    return ans


nums = [8, 7, 10, 11]
assert solve(nums) == 3

nums = []
assert solve(nums) == 0

nums = [0, 2, 2]
assert solve(nums) == 2
