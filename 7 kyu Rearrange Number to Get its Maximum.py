def max_redigit(num):
    lst = [int(i) for i in str(num)]
    print(lst)

print(max_redigit(123), 321)
print(max_redigit(555), 555)
print(max_redigit(-1), None)
print(max_redigit(0), None)
print(max_redigit(99), None)
print(max_redigit(1000), None)
