def array_leaders(numbers):
    i = 0
    lst = []

    while i < len(numbers):
        if numbers[i] > sum(numbers[i+1::]):
            lst.append(numbers[i])
        i += 1

    return lst


print(array_leaders([1, 2, 3, 4, 0]), [4])
print(array_leaders([16, 17, 4, 3, 5, 2]), [17, 5, 2])

print(array_leaders([-1, -29, -26, -2]), [-1])
print(array_leaders([-36, -12, -27]), [-36, -12])

print(array_leaders([5, 2]), [5, 2])
print(array_leaders([0, -1, -29, 3, 2]), [0, -1, 3, 2])
