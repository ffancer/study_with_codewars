def is_prime(n):
    if n < 2:
        return False
    return n % 1 == n and n % n == 1


print(is_prime(0), False)
print(is_prime(1), False)
print(is_prime(2), True)
print(is_prime(3), True)
print(is_prime(11), True)
print(is_prime(12), False)
print(is_prime(571), True)
print(is_prime(25), False)
