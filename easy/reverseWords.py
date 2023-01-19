"""

Given a string s of words delimited by spaces, reverse the order of words.

Constraints
n ≤ 100,000 where n is the length of s

"""


def solve(sentence):
    lst = sentence.split()
    string = ''
    for word in reversed(lst):
        string += word + ' '
    return string[:-1]


sentence = "hello there my friend"
print(solve(sentence))

