def find_sum(*args):
    if not args:
        return 0
    for i in args:
        if i < 0:
            return -1



print(find_sum(1, 3, 5), 9, "1 + 3 + 5 = 9")
print(find_sum(), 0, "If no arguments, function should return 0")
print(find_sum(1, -2, 4), -1, "If negative arguments are passed, function should return -1")
print(find_sum(0), 0, "The sum of 0 is 0")
print(find_sum(1, 1, 5), 7, "Your sum is incorrect")
print(find_sum(1, 1, 1, 1, 1, 1, 1, 1, 0), 8, "Your sum is incorrect")
print(find_sum(-1, -1, 5), -1, "Your sum is incorrect")
print(find_sum(-1, -1, -5), -1, "Your sum is incorrect")
print(find_sum(0, -1, 5), -1, "Your sum is incorrect")
print(find_sum(0, 0, 0), 0, "Your sum is incorrect")
