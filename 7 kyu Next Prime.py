def next_prime(n):
    answer = n

    if answer + 1 % 1 == 0 and answer + 1 % answer == 0:
        return answer


print(next_prime(0), 2)
print(next_prime(2), 3)
print(next_prime(3), 5)
print(next_prime(13), 17)
print(next_prime(181), 191)
print(next_prime(911), 919)
