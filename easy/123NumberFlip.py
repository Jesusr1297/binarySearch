"""

You are given an integer n consisting of digits 1, 2, and 3 and you can flip one digit to a 3.
Return the maximum number you can make.

Constraints
1 ≤ n < 2 ** 31

"""


def solve(n):
    string = str(n)
    for index, num in enumerate(string):
        if num < '3':
            bigger_num = string[:index] + '3' + string[index+1:]
            return int(bigger_num)
    return n


n = 123             # 323
print(solve(n))

n = 333             # 333
print(solve(n))
