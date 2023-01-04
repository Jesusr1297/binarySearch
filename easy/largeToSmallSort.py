"""

Given a list of integers nums, sort the list in the following way:

First number is the maximum
Second number is the minimum
Third number is the 2nd maximum
Fourth number is the 2nd minimum
And so on.

Constraints
n ≤ 100,000 where n is the length of nums.

"""


def solve(nums):
    num_set = sorted(nums)
    new_nums = []
    while num_set:
        new_nums.append(num_set.pop())
        try:
            new_nums.append(num_set.pop(0))
        except:
            pass
    return new_nums


nums = [5, 2, 9, 3, 7]
print(solve(nums))
