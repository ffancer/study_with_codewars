def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target and i != j:
                return [i, j]



print(two_sum([1, 2, 3], 4), [0, 2])
print(two_sum([1234, 5678, 9012], 14690), [1, 2])
print(two_sum([2, 2, 3], 4), [0, 1])
