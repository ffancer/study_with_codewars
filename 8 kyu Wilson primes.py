def am_i_wilson(n):
    return n in (5, 13, 563)


print(am_i_wilson(0), False)
print(am_i_wilson(1), False)
print(am_i_wilson(5), True)
print(am_i_wilson(8), False)
print(am_i_wilson(9), False)
