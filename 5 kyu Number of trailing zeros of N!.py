def zeros(n):
    m = 5
    s = 0

    while n >= m:
        s = s + (n / m)
        m = m * 5

    return round(s)


print(zeros(0), 0, "Testing with n = 0")
print(zeros(6), 1, "Testing with n = 6")
print(zeros(30), 7, "Testing with n = 30")
