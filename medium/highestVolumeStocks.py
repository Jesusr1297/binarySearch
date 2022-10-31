"""

Implement a data structure StockMarket which has the following methods:

    StockMarket(String[] stocks, int[] amounts) which creates a new instance.
    stocks and amounts has the same length and each stock stocks[i] initially
    has amounts[i] volume in the market

    add(String stock, int amount) which cumulatively adds stock with volume amount

    top(int k) which returns the top k the highest volume stocks, sorted in descending
    order by volume. If there are ties in volume, return lexicographically the smallest
    stocks first.

Constraints
n ≤ 100,000 where n is the number of calls to add and top.

"""


class StockMarket:
    def __init__(self, stocks, amounts):
        self.stock_dict = {stock: amount for stock, amount in zip(stocks, amounts)}

    def add(self, s, amount):
        if s in self.stock_dict:
            self.stock_dict[s] += amount
        else:
            self.stock_dict[s] = amount
        return

    def top(self, k):
        sorted_dict = {k: v for k, v in sorted(self.stock_dict.items())}
        return [k for k, v in sorted(sorted_dict.items(), key=lambda v: v[1], reverse=True)][:k]


s = StockMarket(["NFLX"], [300])
s.add("AMZN", 100)
s.add("GOOG", 300)
s.add("AMZN", 300)
s.top(2)  # == ["AMZN", "GOOG"]
assert s.top(2) == ["AMZN", "GOOG"]
