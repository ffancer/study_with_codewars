def product(numbers):
    try:
        total = 1

        for i in numbers:
            total *= i

        return total
    except:
        return None


print(product([5, 4, 1, 3, 9]), 540)
print(product([-2, 6, 7, 8]), -672)
print(product([10]), 10)
print(product([0, 2, 9, 7]), 0)
print(product(None), None)
print(product([]), None)
