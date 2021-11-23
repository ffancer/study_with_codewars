def find_longest(arr):
    a = [len(str(i)) for i in arr]
    return arr[a.index(max(a))]


print(find_longest([1, 10, 100]), 100)
print(find_longest([9000, 8, 800]), 9000)
print(find_longest([8, 900, 500]), 900)
print(find_longest([3, 40000, 100]), 40000)
print(find_longest([1, 200, 100000]), 100000)
