def largest_power(N):
    i = 0

    while 3 ** i < N:
        i += 1

    return i - 1


print(largest_power(3), 0)
print(largest_power(4), 1)
