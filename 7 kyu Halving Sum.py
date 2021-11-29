def halving_sum(n):
    total = 0

    while n != 0:
        total += n
        n //= 2

    return total


print(halving_sum(25), 47)
print(halving_sum(127), 247)
