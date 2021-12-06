def digits(n):
    cnt = 0

    for i in str(n):
        if i.isdigit():
            cnt += 1

    return cnt


print(digits(5), 1)
print(digits(12345), 5)
print(digits(9876543210), 10)
