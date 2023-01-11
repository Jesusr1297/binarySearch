"""

Given a string s containing brackets ( and  ),
return the minimum number of brackets that can
be inserted so that the brackets are balanced.

Constraints
n ≤ 100,000 where n is the length of s

"""

def solve(s):
    stack = []
    count = 0
    for bracket in s:
        if bracket == ')':
            if not stack:
                count+=1
            else:
                stack.pop()
        else:
            stack.append(bracket)
    return count + len(stack)


s = ")))(("
assert solve(s)==5

s = '()'
print(solve(s))
