def next_prime(n):
    n += 1

    for i in range(1, n-2):
        if n % i == 0:
            n += 1
        if n % n == 0 and n % 1 == 0:
            return n

print(next_prime(0), 2)
print(next_prime(2), 3)
print(next_prime(3), 5)
print(next_prime(13), 17)
print(next_prime(181), 191)
print(next_prime(911), 919)
