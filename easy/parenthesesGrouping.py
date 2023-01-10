"""

Given a string s containing balanced parentheses "(" and ")",
split them into the maximum number of balanced groups.

Constraints

n ≤ 100,000 where n is length of s.

"""


def solve(s):
    output = []
    balance = 0
    stack = ''

    for parentheses in s:
        if parentheses == '(':
            balance += 1
            stack += parentheses
        else:
            balance -= 1
            stack += parentheses
            if balance == 0:
                output.append(stack)
                stack = ''
    return output


s = "()()(()())"
print(solve(s))
assert solve(s) == ["()", "()", "(()())"]
