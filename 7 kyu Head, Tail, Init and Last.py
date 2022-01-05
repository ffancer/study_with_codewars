def head(lst):
    return lst[0]


def tail(lst):
    return lst[1:]


def init(lst):
    return lst[:-1]


def last(lst):
    return lst[-1]


print(head([5, 1]), 5)
print(tail([1]), [])
print(init([1, 5, 7, 9]), [1, 5, 7])
print(last([7, 2]), 2)
