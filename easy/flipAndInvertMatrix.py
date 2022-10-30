"""

You are given a two-dimensional integer matrix 'matrix' containing 1s and 0s.
For each row in matrix, reverse the row.
Then, flip each value in the matrix such that any 1 becomes 0 and any 0 becomes 1.

Constraints
n, m ≤ 250 where n and m are the number of rows and columns in matrix

"""


def solve(matrix):
    new_matrix = []

    def invert(row):
        return [0 if num == 1 else 1 for num in row][::-1]

    for row in matrix:
        new_matrix.append(invert(row))
    return new_matrix


matrix = [
    [1, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]
print(solve(matrix))
