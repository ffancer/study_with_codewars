def multiply_all(lst):
    return lambda n: [i * n for i in lst]


print(multiply_all([1], 1))
print(multiply_all([1, 2], 1))
print(multiply_all([1, 2, 3], 1))
print(multiply_all([1, 2, 3], 2))
print(multiply_all([1, 2, 3], 0))
print(multiply_all([], 10))
