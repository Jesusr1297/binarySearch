"""

You are given a list of integers nums and an integer k.
Return the number of pairs i < j such that (nums[i] + nums[j]) % k = 0

Constraints
n ≤ 100,000 where n is the length of nums
1 ≤ k ≤ 100

"""


def solve(nums, k):
    for num in nums:
        for num2 in nums[num+1::]:
            print(num2)


nums = [2, 4, 5, 1, 2]
k = 6
print(solve(nums, k))
