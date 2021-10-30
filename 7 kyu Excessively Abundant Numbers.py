def abundant_number(num):
    return sum(i for i in range(1, num) if num % i == 0) > num

print(abundant_number(12), True)
print(abundant_number(18), True)
print(abundant_number(37), False)
print(abundant_number(120), True)
print(abundant_number(77), False)
print(abundant_number(118), False)
print(abundant_number(5830), True)
print(abundant_number(11410), True)
print(abundant_number(14771), False)
print(abundant_number(11690), True)