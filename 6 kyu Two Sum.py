def two_sum(numbers, target):
    i, j = 0, 1
    lst = []
    while i < j:
        if numbers[i] + numbers[j] != target:
            j += 1
        else:
            lst.append(i)
            lst.append(j)

    return lst



print(two_sum([1, 2, 3], 4), [0, 2])
print(two_sum([1234, 5678, 9012], 14690), [1, 2])
print(two_sum([2, 2, 3], 4), [0, 1])
