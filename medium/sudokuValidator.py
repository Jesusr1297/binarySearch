"""

Sudoku is a puzzle where you're given a 9 by 9 grid with digits.
The objective is to fill the grid with the constraint that every row,
column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9,
and numbers shouldn't repeat within a row, column, or box.

Given a filled out sudoku board, return whether it's valid.

Constraints
n = 9 where n is number of rows and columns in matrix

"""


def solve(matrix):
    valid = {num + 1 for num in range(9)}
    count = {num: [] for num in range(1, 10)}
    block = {(i, j): set() for i in range(3) for j in range(3)}

    for index, row in enumerate(matrix):
        for index2, num in enumerate(row):
            if num not in valid or num in block[(index // 3, index2 // 3)] or index2 in count[num]:
                return False
            else:
                count[num].append(index2)
                block[(index // 3, index2 // 3)].add(num)
    return sum(sum(row) for row in count.values()) == 324


matrix = [
    [4, 2, 6, 5, 7, 1, 3, 9, 8],
    [8, 5, 7, 2, 9, 3, 1, 4, 6],
    [1, 3, 9, 4, 6, 8, 2, 7, 5],
    [9, 7, 1, 3, 8, 5, 6, 2, 4],
    [5, 4, 3, 7, 2, 6, 8, 1, 9],
    [6, 8, 2, 1, 4, 9, 7, 5, 3],
    [7, 9, 4, 6, 3, 2, 5, 8, 1],
    [2, 6, 5, 8, 1, 4, 9, 3, 7],
    [3, 1, 8, 9, 5, 7, 4, 6, 2]
]
assert solve(matrix) is True

matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [2, 3, 4, 5, 6, 7, 8, 9, 1]
]
assert solve(matrix) is False

matrix = [
    [4, 2, 6, 5, 7, 1, 3, 20, 8],
    [8, 5, 7, 2, 9, 3, 1, 4, 6],
    [1, 3, 9, 4, 6, 8, 2, 7, 5],
    [9, 7, 1, 3, 8, 5, 6, 2, 4],
    [5, 4, 3, 7, 2, 6, 8, 1, 9],
    [6, 8, 2, 1, 4, 9, 7, 5, 3],
    [7, 9, 4, 6, 3, 2, 5, 8, 1],
    [2, 6, 5, 8, 1, 4, 9, 3, 7],
    [3, 1, 8, 9, 5, 7, 4, 6, 2]
]
assert solve(matrix) is False
