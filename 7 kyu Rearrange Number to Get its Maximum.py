def max_redigit(num):
    lst = [i for i in str(num)]
    return int(''.join(sorted(lst, reverse=True)))

print(max_redigit(123), 321)
print(max_redigit(555), 555)
print(max_redigit(-1), None)
print(max_redigit(0), None)
print(max_redigit(99), None)
print(max_redigit(1000), None)
