"""

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", "AC", ..., "ZZ",
"AAA", "AAB", "AAC", ....

Given a string s representing an alphabetical column id, return its column number. For example, given "A", return 1.
Given "AA", return 27.

"""


def solve(s):
    letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
               'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
               'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
               'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    col_id = 0
    for index, char in enumerate(s[::-1]):
        col_id += 26 ** index * letters[char]
    return col_id


s = "AXC"
print(solve(s))
