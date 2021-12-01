def cube_odd(arr):
    try:
        arr = [i ** 3 for i in arr]
        total = 0

        for i in arr:
            if i % 2 != 0:
                total += i

        return total

    except:
        return None


print(cube_odd([1, 2, 3, 4]), 28)
print(cube_odd([-3, -2, 2, 3]), 0)
print(cube_odd(["a", 12, 9, "z", 42]), None)
