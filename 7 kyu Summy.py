def summy(string_of_ints):
    return sum(int(i) for i in string_of_ints.split())


print(summy("1 2 3"), 6)
print(summy("1 2 3 4"), 10)
print(summy("1 2 3 4 5"), 15)
print(summy("10 10"), 20)
print(summy("0 0"), 0)
