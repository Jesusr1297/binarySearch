"""

There's a staircase with n steps, and you can climb up either 1 or 2 steps at a time.

Given an integer n, write a function that returns the number of unique ways you can
climb the staircase. The order of the steps matters, so each different order of steps
counts as a way.

Mod the result by 10 ** 9 + 7.

Constraints
n ≤ 100,000

"""


def solve(n):
    solutions = [0, 1, 2]
    if n == 2 or n == 1 or n == 0:
        return solutions[n]
    else:
        for num in range(3, n + 1):
            solutions.append(solutions[num - 1] + solutions[num - 2])
    return solutions[-1] % (10 ** 9 + 7)


n = 4
assert solve(n) == 5

n = 1
assert solve(n) == 1

n = 3
assert solve(n) == 3

n = 417
assert solve(n) == 430965194
