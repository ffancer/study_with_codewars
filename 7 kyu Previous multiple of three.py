def prev_mult_of_three(n):
    while n % 3:
        n = n // 10
    return n or None


print(prev_mult_of_three(1), None)
print(prev_mult_of_three(25), None)
print(prev_mult_of_three(36), 36)
print(prev_mult_of_three(1244), 12)
print(prev_mult_of_three(952406), 9)
