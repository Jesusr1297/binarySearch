"""

Given the mapping "a" = 1, "b" = 2, ... "z" = 26, and an encoded message
'message' (as a string), count the number of ways it can be decoded.

Constraints
n ≤ 100,000 where n is the length of message

"""


def solve(message):
    dp = {len(message): 1}

    for i in range(len(message) - 1, -1, -1):
        if message[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if (i + 1 < len(message)) and (message[i] == '1' or (message[i] == '2' and message[i + 1] in '0123456')):
            dp[i] += dp[i + 2]
    return dp[0]


message = "111"
print(solve(message))
