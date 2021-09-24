# 8 kyu
# Enumerable Magic #3 - Does My List Include This?
def include(arr, item):
    return item in arr


print(include([1, 2, 3, 4], 3), True)
print(include([1, 2, 4, 5], 3), False)
