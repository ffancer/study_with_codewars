def numbers(*args):
    return all(type(i) in [int, float] for i in args)


print(numbers(1, 2, 3, 4), True)
print(numbers("a", 2, 4, 5), False)
print(numbers(None, 2, 3), False)
print(numbers(1, 2, 10, 50), True)
print(numbers(1, [2, 5], 10, 50), False)