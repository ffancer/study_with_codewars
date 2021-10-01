# 7 kyu
# Simple Fun #13: Magical Well
def magical_well(a, b, n):
    total = 0

    for i in range(1, n + 1):
        total += a * b
        a += 1
        b += 1

    return total



print(magical_well(1, 2, 2), 8)
print(magical_well(1, 1, 1), 1)
print(magical_well(6, 5, 3), 128)
