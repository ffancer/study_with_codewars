def modified_sum(a, n):
    return sum(i ** n for i in a) - sum(a)

print(modified_sum([1, 2, 3], 3), 30)
print(modified_sum([1, 2], 5), 30)
