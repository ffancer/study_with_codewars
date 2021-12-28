def max_redigit(num):
    if len(str(num)) != 3:
        return None
    lst = [i for i in str(num) if i.isdigit()]
    return int(''.join(sorted(lst, reverse=True)))

print(max_redigit(123), 321)
print(max_redigit(555), 555)
print(max_redigit(-1), None)
print(max_redigit(0), None)
print(max_redigit(99), None)
print(max_redigit(1000), None)
