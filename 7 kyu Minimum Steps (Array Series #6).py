def minimum_steps(numbers, value):
    n = 0
    lst = sorted(numbers)
    # while n < value:
    #     n = sum(lst[2:])
    return sum(lst[:2])


print(minimum_steps([4, 6, 3], 7), 1)
print(minimum_steps([10, 9, 9, 8], 17), 1)
print(minimum_steps([8, 9, 10, 4, 2], 23), 3)
print(minimum_steps([19, 98, 69, 28, 75, 45, 17, 98, 67], 464), 8)
print(minimum_steps([4, 6, 3], 2), 0)
