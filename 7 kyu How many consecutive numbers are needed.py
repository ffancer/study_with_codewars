# 7 kyu
# How many consecutive numbers are needed?


def consecutive(arr):
    try:
        lst = []

        for i in range(min(arr), max(arr)+1):
            lst.append(i)

        return len(lst) - len(arr)
    except ValueError:
        return 0


print(consecutive([4, 8, 6]), 2)
print(consecutive([1, 2, 3, 4]), 0)
print(consecutive([]), 0)
print(consecutive([1]), 0)
print(consecutive([-10]), 0)
