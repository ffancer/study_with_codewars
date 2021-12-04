def single_digit(n):
    while n > 9:
        n = bin(n).count("1")
    return n


print(single_digit(5), 5)
print(single_digit(5665), 5)
print(single_digit(123456789), 1)
