def prime_num(n):
    if n < 2:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    if prime_num(n):
        n += 1
    while not prime_num(n):
        n += 1
    return n


print(next_prime(0), 2)
print(next_prime(2), 3)
print(next_prime(3), 5)
print(next_prime(13), 17)
print(next_prime(181), 191)
print(next_prime(911), 919)
