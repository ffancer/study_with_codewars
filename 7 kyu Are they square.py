# 7 kyu
# Are they square?

def is_square(arr):
    if not arr:
        return None

    lst = []

    for i in arr:
        if i**0.5 == int(i**0.5):
            lst.append(i)

    return arr == lst


print(is_square([1, 4, 9, 16, 25, 36]), True)
print(is_square([1, 2, 3, 4, 5, 6]), False)
print(is_square([]), None)
print(is_square([1, 4, 9, 16, 25]), True)
print(is_square([1, 2, 4, 15]), False)