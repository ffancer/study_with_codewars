def minimum_steps(numbers, value):
    numbers = sorted(numbers)
    i = 1
    lst = numbers[:i]
    print(lst)


print(minimum_steps([4, 6, 3], 7), 1)
print(minimum_steps([10, 9, 9, 8], 17), 1)
print(minimum_steps([8, 9, 10, 4, 2], 23), 3)
print(minimum_steps([19, 98, 69, 28, 75, 45, 17, 98, 67], 464), 8)
print(minimum_steps([4, 6, 3], 2), 0)
