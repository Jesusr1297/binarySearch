"""

Given a list of strings lst and a list of integers p,
reorder lst so that every lst[i] gets placed to p[i].

This should be done in O(1) space.

Constraints
n ≤ 100,000 where n is the length of lst

"""


def solve(lst, p):
    new_lst = [None for char in lst]
    for idx, val in zip(p, lst):
        new_lst[idx] = val
    return new_lst


lst = ["a", "b", "c", "d"]
p = [3, 0, 1, 2]
assert solve(lst, p) == ["b", "c", "d", "a"]
