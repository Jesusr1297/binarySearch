"""

You are given a list of integers cells, representing sizes of different cells.
In each iteration, the two largest cells a and b interact according to these rules:

If a = b, they both die.
Otherwise, the two cells merge and their size becomes floor((a + b) / 3).
Return the size of the last cell or return -1 if there's no cell is remaining.

Constraints
n ≤ 100,000 where n is the length of cells

"""


def solve(cells):
    import heapify, heappop, heappush
    

cells = [10, 30, 30, 20]
print(solve(cells))
