"""

You are given a list of strings orders. Each element in orders starts with either "P"
meaning pickup or "D" meaning delivery followed by the order id. For example, "P12"
means pick up order 12.

Return whether orders are valid given the following rules:
- A delivery cannot happen for an order before pickup
- Every pickup must be delivered
- An order that's already been picked up and delivered cannot be picked up or delivered again

Constraints
0 ≤ n ≤ 100,000 where n is the length of orders

"""


def solve(orders):
    count = {'P': 0, 'D': 0}
    order_dict = {'P': set(), 'D': set()}

    for order in orders:
        count[order[0]] += 1
        if order[1:] in order_dict[order[0]] or (count['D'] > count['P']):
            return False
        else:
            order_dict[order[0]].add(order[1:])
    return count['P'] == count['D']


def solve2(orders):     # own
    order_dict = {'P': set(), 'D': set()}

    for order in orders:
        if order[1:] in order_dict[order[0]] or (len(order_dict['D']) > len(order_dict['P'])):
            return False
        else:
            order_dict[order[0]].add(order[1:])
    return len(order_dict['P']) == len(order_dict['D'])


orders = ["P1", "P2", "D2", "D1"]  # True
print(solve(orders))

orders = ["P1", "P2", "P3"]  # False
print(solve(orders))

orders = ["D1", "P1"]  # False
print(solve(orders))

orders = ["P1", "D1", "P1", "D1"]  # False
print(solve(orders))

orders = ['P'+str(num) for num in range(50_000)] + ['D'+str(num) for num in range(50_000)]  # True
print(solve(orders))

