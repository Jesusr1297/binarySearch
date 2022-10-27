"""

You are given a list of integers nums which contains at least one 1.
Return whether all the 1s appear consecutively.

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    number_of_ones = nums.count(1)
    first_one = nums.index(1)

    for num in nums[first_one:first_one+number_of_ones]:
        if num != 1:
            return False
    return True


nums = [0, 1, 1, 1, 2, 3]
print(solve(nums))

nums = [1, 1, 0, 1, 1]
print(solve(nums))
