"""

Implement a data structure LastValueMap which has the following methods:

- void set(int key, int value) which associates key with value.
- void remove(int key) which removes key and its associated value.
- int getLast() which returns the value of the last added key.
  If a key is updated with a value, it should become last.
  You can assume that there is always a last value.

Constraints
0 ≤ n ≤ 200,000 where n is the number of method calls

"""


class LastValueMap:
    def __init__(self):
        self.last = {}
        self.values = {}

    def set(self, key, value):
        self.values[key] = value
        self.last.
        return

    def remove(self, key):
        self.values.pop(key)
        return

    def getLast(self):
        try:
            return self.values[self.last[-1]]
        except (IndexError, KeyError):
            return None


x = LastValueMap()
x.set(1, 2)
x.set(2, 3)
assert x.getLast() == 3
x.set(1, 9)
assert x.getLast() == 9
x.remove(1)
assert x.getLast() == 3
