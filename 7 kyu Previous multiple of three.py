def prev_mult_of_three(n):
    n = str(n)
    i = -1

    while i < 0:
        if int(n[i] + n[i-1]) % 3 != 0:
            i -= 1
        return int(n[i] + n[i-1])
    return None

print(prev_mult_of_three(1), None)
print(prev_mult_of_three(25), None)
print(prev_mult_of_three(36), 36)
print(prev_mult_of_three(1244), 12)
print(prev_mult_of_three(952406), 9)
