"""

You are given a two-dimensional list of integers reviews and a positive integer threshold.
Each element reviews[i] contains [x, y] meaning product i had x number of 5-star reviews and a total of y reviews.
All reviews are for one store.

Return the minimum number of additional 5-star reviews we need such that the percentage of 5-star reviews in the store
is at least threshold. You can assume that it's possible to reach threshold% of 5-star reviews.

Constraints
1 ≤ n ≤ 100,000 where n is the length of reviews
0 ≤ threshold ≤ 100


"""


def solve(reviews, threshold):
    five_stars = 0
    total = 0
    added = 0
    for i in reviews:
        five_stars += i[0]
        total += i[1]
    while five_stars / total < threshold / 100:
        five_stars += 1
        total += 1
        added +=1
    return added


reviews = [
    [4, 4],
    [1, 2],
    [3, 6]
]
threshold = 77
assert solve(reviews, threshold) == 6

reviews = [
    [10, 20]
]
threshold = 50
assert solve(reviews, threshold) == 0

reviews = [
    [1, 1]
]
threshold = 100
assert solve(reviews, threshold) == 0
