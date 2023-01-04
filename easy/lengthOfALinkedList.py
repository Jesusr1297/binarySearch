"""

Given a singly linked list node, return its length.
The linked list has fields next and val.

Constraints
n ≤ 100,000 where n is the number of nodes in node

"""


class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solve(node):
    try:
        length = 1
        while node.next:
            length += 1
            node = node.next

        return length
    except AttributeError:
        return 0


def solve2(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length
