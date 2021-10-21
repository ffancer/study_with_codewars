def dating_range(age):
    mn = age // 2 + 7
    mx = (age - 7) * 2
    return f'{int(age - 0.10 * age)}-{int(age + 0.10 * age)}' if age <= 14 else f'{mn}-{mx}'


print(dating_range(17), "15-20")
print(dating_range(40), "27-66")
print(dating_range(15), "14-16")
print(dating_range(35), "24-56")
print(dating_range(10), "9-11")
