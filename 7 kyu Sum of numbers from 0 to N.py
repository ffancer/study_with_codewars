def show_sequence(n):
    total = 0

    for i in range(n+1):
        total += i

    return total


print((show_sequence(6)))  # "0+1+2+3+4+5+6 = 21"
print((show_sequence(7)))  # "0+1+2+3+4+5+6+7 = 28"
print((show_sequence(0)))
print((show_sequence(-1)))
print((show_sequence(-10)))