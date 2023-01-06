"""

Given a singly linked list node, convert it to a binary tree path using these rules:

The head of the linked list is the root.
Each subsequent node is the left child of the parent if its value is smaller,
otherwise it's the right child.

Constraints
n ≤ 100,000 where n is the number of nodes in node

"""


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solve(node):
    if not node:
        return None
    root = Tree(node.val)
    if node.next:
        if node.next.val < node.val:
            root.left = solve(node.next)
        else:
            root.right = solve(node.next)
    return root


node = LLNode(1)
node.next = 0
node.next = 2
assert solve(node) == [1, [0, null, [2, null, null]], null]

# node = [1, 2, 0, 7]
# [1, null, [2, [0, null, [7, null, null]], null]]
