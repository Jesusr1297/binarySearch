"""

You are given a list of integers nums.
Return the number of pairs i < j such that nums[i] + nums[j]
is equal to 2 ** k for some 0 ≤ k.

Constraints
0 ≤ n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    max_num = 2 * max(nums)
    powers = set()
    n = 0
    while max_num >= 1:
        powers.add(2 ** n)
        n += 1
        max_num /= 2
        print(n, max_num)
    print(powers)
    # for index, num in enumerate(nums):
    #     for num2 in nums[index + 1::]:
    #         if


nums = [1, 1, 3, 5]
# assert solve(nums) == 4
solve(nums)
