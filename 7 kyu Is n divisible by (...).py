# 7 kyu
# Is n divisible by (...)?


def is_divisible(*args):
    return [i for i in args[1::] if args[0] % i != 0] == []


print(is_divisible(3, 3, 4), False)
print(is_divisible(12, 3, 4), True)
print(is_divisible(8, 3, 4, 2, 5), False)
