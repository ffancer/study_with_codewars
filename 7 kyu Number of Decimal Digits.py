def digits(n):
    cnt = 1

    while n // 10 > 0:
        n //= 10
        cnt += 1

    return cnt


print(digits(5), 1)
print(digits(12345), 5)
print(digits(9876543210), 10)
