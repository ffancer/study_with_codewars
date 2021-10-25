def repeats(arr):
    return sum([i for i in arr if arr.count(i) < 2])



print(repeats([4, 5, 7, 5, 4, 8]), 15)
print(repeats([9, 10, 19, 13, 19, 13]), 19)
print(repeats([16, 0, 11, 4, 8, 16, 0, 11]), 12)
print(repeats([5, 17, 18, 11, 13, 18, 11, 13]), 22)
print(repeats([5, 10, 19, 13, 10, 13]), 24)
