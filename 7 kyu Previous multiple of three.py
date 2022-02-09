def prev_mult_of_three(n):
    if n == 1:
        return None


    while n > 0:
        if n % 3 == 0:
            return n
        n = n % 10
    return None

print(prev_mult_of_three(1), None)
print(prev_mult_of_three(25), None)
print(prev_mult_of_three(36), 36)
print(prev_mult_of_three(1244), 12)
print(prev_mult_of_three(952406), 9)
