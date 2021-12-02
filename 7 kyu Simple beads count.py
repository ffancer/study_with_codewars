def count_red_beads(n):
    return 0 if n <= 0 else (n - 1) * 2


print(count_red_beads(1), 0)
print(count_red_beads(3), 4)
print(count_red_beads(5), 8)
