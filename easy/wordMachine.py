"""

You are given a list of strings ops where each element is either:

A non-negative integer that should be pushed into a stack
"POP" meaning pop the top element in the stack
"DUP" meaning duplicate the top element in the stack
"+" meaning pop the top two and push the sum
"-" meaning pop the top two and push top - second
Return the top element in the stack after applying all operations. If there are any invalid operations, return -1.

Constraints
1 ≤ n ≤ 100,000 where n is the length of ops

"""


def solve(ops):
    def pop(lst: list):
        lst.pop()
        return

    def dup(lst: list):
        return lst[-1]

    def plus(lst: list):
        max_1 = lst.pop()
        max_2 = lst.pop()
        return max_1 + max_2

    def minus(lst: list):
        max_1 = lst.pop()
        max_2 = lst.pop()
        return max_1 - max_2

    operations = {'POP': pop, 'DUP': dup, '-': minus, '+': plus}
    new_list = []

    try:
        for op in ops:
            if op.isdigit():
                new_list.append(int(op))
            elif op == 'POP':
                operations[op](new_list)
            else:
                val = operations[op](new_list)
                new_list.append(val)
        return new_list.pop()
    except (ValueError, IndexError, KeyError):
        return -1


ops = ["1", "5", "DUP", "3", "-"]
print(solve(ops))

ops = ["+"]
print(solve(ops))

ops = ["0", "POP", "0"]
print(solve(ops))

ops = ['pull', '0']
print(solve(ops))
