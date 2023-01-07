"""

Implement a data structure with the following methods:

RangeSum(int[] nums) constructs a new instance with the given nums.
total(int i, int j) returns the sum of integers from nums between [i, j).
That is, nums[i] + nums[i + 1] + ... + nums[j - 1].

Constraints
n ≤ 100,000 where n is the length of nums
k ≤ 100,000 where k is the number of calls to total

"""


class RangeSum:
    def __init__(self, nums):
        self.sums = [0]
        for x in nums:
            self.sums.append(x + self.sums[-1])

    def total(self, i, j):
        return self.sums[j] - self.sums[i]
