def all(seq, fun):
    for i in seq:
        if not fun(i):
            return False
    return True


greater_than_9 = lambda x: x > 9
less_than_9 = lambda x: x < 9

print(all((1, 2, 3, 4, 5), greater_than_9), False)
print(all((1, 2, 3, 4, 5), less_than_9), True)
