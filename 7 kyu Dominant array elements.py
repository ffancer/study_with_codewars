def solve(arr):
    a = 0
    lst = []

    while a != len(arr):
        if arr[a] < max(arr[a:]):
            a += 1
        else:
            lst.append(arr[a])
            a += 1

    return lst



print(solve([16, 17, 14, 3, 14, 5, 2]), [17, 14, 5, 2])
print(solve([92, 52, 93, 31, 89, 87, 77, 105]), [105])
print(solve([75, 47, 42, 56, 13, 55]), [75, 56, 55])
print(solve([67, 54, 27, 85, 66, 88, 31, 24, 49]), [88, 49])
print(solve([76, 17, 25, 36, 29]), [76, 36, 29])
print(solve([104, 18, 37, 9, 36, 47, 28]), [104, 47, 28])
