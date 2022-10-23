"""

Given a string s containing round, curly, and square open
and closing brackets, return whether the brackets are balanced.

Constraints
n ≤ 100,000 where n is the length of s

"""


def solve(s):
    brackets = []
    closed = {')': '(', ']': '[', '}': '{'}
    for bracket in s:
        if bracket in '([{':
            brackets.append(bracket)
        else:
            try:
                if closed[bracket] == brackets[-1]:
                    brackets.pop()
                else:
                    return False
            except IndexError:
                return False
    return len(brackets) == 0


s = "[(])"
assert solve(s) is False

s = "([])[]({})"
assert solve(s) is True

s = '{{{{[]()}}}}'
assert solve(s) is True

s = "]"
assert solve(s) is False

s = '{'
assert solve(s) is False
