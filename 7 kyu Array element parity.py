# best practice 1
def solve(arr): return sum(set(arr))

# best practice 2
def solve(arr):
    for a in arr:
        if -a not in arr:
            return a


# best practice 3
def solve(arr):
    return [i for i in arr if -i not in arr][0]

print(solve([1, -1, 2, -2, 3]), 3)
print(solve([-3, 1, 2, 3, -1, -4, -2]), -4)
print(solve([1, -1, 2, -2, 3, 3]), 3)
print(solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]), -38)
print(solve([-9, -105, -9, -9, -9, -9, 105]), -9)
