# 7 kyu
# Simple Fun #13: Magical Well

def magical_well(a, b, n):
    return sum((a + i) * (b + i) for i in range(n))



print(magical_well(1, 2, 2), 8)
print(magical_well(1, 1, 1), 1)
print(magical_well(6, 5, 3), 128)