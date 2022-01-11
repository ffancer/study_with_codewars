def insert_dash(num):
    num = str(num)
    s = ''
    i, j = 0, 1

    while j < len(num):
        if int(num[i]) % 2 != 0 and int(num[j]) % 2 != 0:
            s += num[j] + '-'
        else:
            s += num[i]
            # s += num[j]
        i += 1
        j += 1

    return s




print(insert_dash(454793), '4547-9-3')
print(insert_dash(123456), '123456')
print(insert_dash(1003567), '1003-567')
print(insert_dash(24680), '24680')
print(insert_dash(13579), '1-3-5-7-9')
