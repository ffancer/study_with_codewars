import math


def next_prime(n):
    n += 1
    while True:
        if n % 1 == 0 and n % n ==0:
            return n
        else:
            n += 1

print(next_prime(0), 2)
print(next_prime(2), 3)
print(next_prime(3), 5)
print(next_prime(13), 17)
print(next_prime(181), 191)
print(next_prime(911), 919)
