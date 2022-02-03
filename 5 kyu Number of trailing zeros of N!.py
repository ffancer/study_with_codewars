from math import floor


def zeros(n):
    num = 0

    while n > 4:
        n = floor(n / 5)
        num += n

    return num


print(zeros(0), 0, "Testing with n = 0")
print(zeros(6), 1, "Testing with n = 6")
print(zeros(30), 7, "Testing with n = 30")
