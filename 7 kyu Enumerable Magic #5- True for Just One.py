# 7 kyu
# Enumerable Magic #5- True for Just One?


def one(sq, fun):
    for i in sq:
        if i not in fun:
            return False
    return True


equals_9 = lambda x: x == 9
less_than_9 = lambda x: x < 9
greater_than_9 = lambda x: x > 9
arr = (6, 7, 8, 9, 10, 11)

print(one(arr, equals_9), True)
print(one(arr, less_than_9), False)
print(one(arr, greater_than_9), False)
