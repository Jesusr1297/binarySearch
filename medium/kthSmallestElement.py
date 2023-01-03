"""

Given a list of unsorted integers nums, and an integer k,
return the kth (0-indexed) smallest element in the list.

This should be done in O(n) time on average.

Constraints
0 ≤ k < n ≤ 100,000 where n is the length of nums

"""


def solve(nums: list, k):
    while k > -1:
        num = min(nums)
        nums.remove(num)
        k -= 1
    return num


def solve2(nums, k):

    def quick_select(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        if p > k:
            return quick_select(l, p - 1)
        elif p < k:
            return quick_select(p + 1, r)
        else:
            print(nums[p])
            return nums[p]

    return quick_select(0, len(nums) - 1)


nums = [5, 3, 8, 2, 0]
k = 2
assert solve(nums, k) == 3

nums = [5, 3, 8, 2, 0]
k = 2
assert solve2(nums, k) == 3
