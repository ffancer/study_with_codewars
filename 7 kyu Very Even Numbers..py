def is_very_even_number(n):
    # while len(str(n)) != 1:
    #     n = sum(int(str(n)))
    return sum([int(i) for i in list(str(n))])


print(is_very_even_number(0), True)
print(is_very_even_number(4), True)
print(is_very_even_number(12), False)
print(is_very_even_number(222), True)
print(is_very_even_number(5), False)
print(is_very_even_number(45), False)
print(is_very_even_number(4554), False)
print(is_very_even_number(1234), False)
print(is_very_even_number(88), False)
print(is_very_even_number(24), True)
print(is_very_even_number(400000220), True)
