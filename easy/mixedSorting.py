"""

Given a list of integers nums, sort the array such that:

All even numbers are sorted in increasing order
All odd numbers are sorted in decreasing order
The relative positions of the even and odd numbers remain the same

Constraints
n ≤ 100,000 where n is the length of nums

"""


def solve(nums):
    odd = []
    even = []
    pos = []
    mixed = []
    for num in nums:
        if num % 2:
            odd.append(num)
            pos.append('odd')
        else:
            even.append(num)
            pos.append('even')
    odd = sorted(odd, reverse=True)
    even = sorted(even)
    for num in pos:
        if num == 'odd':
            mixed.append(odd.pop(0))
        else:
            mixed.append(even.pop(0))
    return mixed


def solve2(nums):
    odd = sorted(filter(lambda x: x % 2, nums))
    even = sorted(filter(lambda x: not x % 2, nums))

    for i, v in enumerate(nums):
        if v % 2:
            nums[i] = odd.pop()
        else:
            nums[i] = even.pop(0)
    return nums


nums = [8, 13, 11, 90, -5, 4]
print(solve2(nums))
