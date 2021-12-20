def calc(x):
    total1 = ''.join(str(ord(i)) for i in x)
    total2 = total1.replace('7', '1')

    total1_sum = sum(int(i) for i in total1)
    total2_sum = sum(int(i) for i in total2)

    return total1_sum - total2_sum


print(calc('abcdef'), 6)
print(calc('ifkhchlhfd'), 6)
print(calc('aaaaaddddr'), 30)
print(calc('jfmgklf8hglbe'), 6)
print(calc('jaam'), 12)
