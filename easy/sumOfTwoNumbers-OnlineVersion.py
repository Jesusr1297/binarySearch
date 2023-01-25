"""

Implement a data structure with the following methods:

add(int val) adds the value val to the data structure
find(int val) returns whether there are two elements whose sum equals to val

Constraints
n ≤ 10,000 where n is the number of times add will be called
m ≤ 1,000 where m is the number of times find will be called


"""


class TwoSum:
    def __init__(self):
        self.numbers = {}

    def add(self, val):
        self.numbers.append(val)
        return

    def find(self, val):
        num_set = set()
        for num in self.numbers:
            if val - num in num_set:
                return True
            else:
                num_set.add(num)
        return False
