def max_redigit(num):
    if 99 < num < 1000:
        return None
    lst = [i for i in str(num) if i.isdigit()]
    return int(''.join(sorted(lst, reverse=True)))

print(max_redigit(82), None)
print(max_redigit(33), None)
print(max_redigit(29), None)
print(max_redigit(123), 321)
print(max_redigit(555), 555)
print(max_redigit(-1), None)
print(max_redigit(0), None)
print(max_redigit(99), None)
print(max_redigit(1000), None)
