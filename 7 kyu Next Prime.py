def next_prime(n):
    lst = all(x % i for i in range(2, x))


# print(next_prime(0), 2)
print(next_prime(2), 3)
print(next_prime(3), 5)
print(next_prime(13), 17)
print(next_prime(181), 191)
print(next_prime(911), 919)
