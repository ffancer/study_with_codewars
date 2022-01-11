def insert_dash(num):
    num = str(num)
    s = ''

    for i in range(len(num)):
        if num[i] % 2 != 0 and num[i+1] % 2 != 0:
            s += '-'
        else:
            s += num[i]

    return s



print(insert_dash(454793), '4547-9-3')
print(insert_dash(123456), '123456')
print(insert_dash(1003567), '1003-567')
print(insert_dash(24680), '24680')
print(insert_dash(13579), '1-3-5-7-9')
