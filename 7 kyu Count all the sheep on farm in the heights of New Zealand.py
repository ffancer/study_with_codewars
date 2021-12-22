def lost_sheep(friday,saturday,total):
    return total - sum(friday + saturday)


print(lost_sheep([1, 2], [3, 4], 15), 5)
print(lost_sheep([3, 1, 2], [4, 5], 21), 6)
print(lost_sheep([5, 1, 4], [5, 4], 29), 10)
