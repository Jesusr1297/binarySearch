"""

Given a binary tree root, convert it to a singly
linked list using level order traversal.

Constraints
1 ≤ n ≤ 100,000 where n is the number of nodes in root

"""
import collections


def solve(root):
    q = collections.deque