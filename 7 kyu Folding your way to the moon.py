def fold_to(distance):
    cnt = 0
    i = 0.0001

    while i < distance:
        i *= 2
        cnt += 1

    return None if distance < 0 else cnt


print(fold_to(384000000), 42)
print(fold_to(0.00005), 0)
print(fold_to(0.0000001), 0)
print(fold_to(0), 0)
print(fold_to(-1), None)
