"""

Given an integer n, return its corresponding Roman numeral.

Roman numerals contain the symbols representing values in the following list:
- "I" = 1
- "V" = 5
- "X" = 10
- "L" = 50
- "C" = 100
- "D" = 500
- "M" = 1000

Symbols are typically written largest to smallest, from left to right,
and can be computed by summing the values of all the symbols. However,
in some cases, when a symbol of lower value is to the left of a symbol
of higher value, then the lower value is subtracted from the higher one.

There are 6 cases where this is possible:
- When "I" is before "V", we get 4.
- When "I" is before "X", we get 9.
- When "X" is before "L", we get 40.
- When "X" is before "C", we get 90.
- When "C" is before "D", we get 400.
- When "C" is before "M", we get 900.

Roman numerals must also follow these rules:
- No symbol is repeated more than 3 times.
- The symbols "V", "L", and "D" are not repeated.

Constraints
1 ≤ n ≤ 3000

"""


def solve(n):
    before = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
    nums = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', '': ''}
    decomposed = [str(int(num) * 10 ** index) for index, num in enumerate(reversed(str(n)))][::-1]
    roman = ''
    for num in decomposed:
        if int(num) in before:
            roman += before[int(num)]
        else:
            if int(num[0]) > 3:
                index1 = 5 * (1 + (int(num[0]) - 5) // 4) * 10 ** (len(num) - 1)
                index2 = (1 + (int(num[0]) - 5) // 4) * 10 ** (len(num) - 1)
                roman += nums[index1] + nums[index2] * (int(num[0]) - 5)
            else:
                index = (1 + int(num[0]) // 4) * 10 ** (len(num) - 1)
                roman += nums[index] * int(num[0])
    return roman


def solve2(n):
    nums = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
            4: 'IV', 1: 'I'}
    roman = ''
    for num, val in nums.items():
        floor, n = n // num, n % num  # divmod(x, y) = (x//y, x%y)
        roman += val * floor
    return roman


def solve3(n):
    res = ""
    table = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    for cap, roman in table:
        d, m = divmod(n, cap)
        res += roman * d
        n = m

    return res


i = 333
print(solve3(i))
print(solve2(i))
