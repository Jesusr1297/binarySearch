"""

Given a two-dimensional integer matrix of 1s and 0s where 0 represents empty cell
and 1 represents a block that forms a shape, return the perimeter of the shape.
There is guaranteed to be exactly one shape, and the shape has no holes in it.

Constraints
1 ≤ n, m ≤ 250 where n and m are the number of rows and columns in matrix

"""


def solution(mat):
    row_len = len(mat)
    col_len = len(mat[0])

    print(f'matrix dimensions: ({row_len}, {col_len})')

    perimeter = 0

    for row in range(row_len):
        for col in range(col_len):
            if mat[row][col]:
                perimeter += (4 - check_neighbour(mat, row, col, row_len, col_len))
    return perimeter


def check_neighbour(mat, row, col, row_len, col_len):
    neighbours = 0

    # check up
    if row > 0 and mat[row - 1][col]:
        print(f'{mat[row][col]} up @ ({row}, {col})')
        neighbours += True

    # check right
    if col < col_len - 1 and mat[row][col + 1]:
        print(f'{mat[row][col]} right @ ({row}, {col})')
        neighbours += True

    # check down
    if row < row_len - 1 and mat[row + 1][col]:
        print(f'{mat[row][col]} down @ ({row}, {col})')
        neighbours += True

    # check left
    if col > 0 and mat[row][col - 1]:
        print(f'{mat[row][col]} left @ ({row}, {col})')
        neighbours += True

    print(f'neighbours counted: {neighbours}')
    return int(neighbours)


matrix = [
    [0, 1, 1],
    [0, 1, 0]
]
print(solution(matrix))
