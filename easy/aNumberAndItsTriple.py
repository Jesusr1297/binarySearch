"""

Given a list of integers nums, return whether there's two numbers such that one is a triple of another.

Constraints
n ≤ 100,000 where n is the length of nums.

"""


def solve(nums):
    num_set = set()
    for num in sorted(nums):
        if num in num_set:
            return True
        else:
            num_set.add(num*3)
            if not num % 3:
                num_set.add(int(num/3))
    return False


nums = [2, 3, 10, 7, 6]     # True
print(solve(nums))

nums = [3, 4, 5]            # False
print(solve(nums))

nums = [0]                  # False
print(solve(nums))

nums = [3, 0]               # False
print(solve(nums))

nums = [0, 0]               # True
print(solve(nums))

nums = [3, 1]               # True
print(solve(nums))

nums = [1, 0]               # False
print(solve(nums))

nums = [-3, -1]             # True
print(solve(nums))
