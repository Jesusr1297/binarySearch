"""

Given two lists of integers a and b sorted in ascending order,
merge them into one large sorted list.

Constraints
0 ≤ n ≤ 200,000 where n is the length of a
0 ≤ m ≤ 200,000 where m is the length of b

"""


def solve(a, b):
    i = 0
    j = 0
    new_list = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            new_list.append(a[i])
            i += 1
        else:
            new_list.append(b[j])
            j += 1

    while i < len(a):
        new_list.append(a[i])
        i += 1

    while j < len(b):
        new_list.append(b[j])
        j += 1
    return new_list


a = [5, 10, 15]
b = [3, 8, 9]
print(solve(a, b))
