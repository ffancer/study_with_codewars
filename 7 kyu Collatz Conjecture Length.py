def collatz(n):
    cnt = 1

    while n != 1:
        cnt += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1

    return cnt


print(collatz(20), 8)
print(collatz(15), 18)
