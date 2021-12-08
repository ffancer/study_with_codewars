def seven_ate9(str_):
    cnt = 0

    while cnt != len(str_):
        str_ = str_.replace('797', '77')
        cnt += 1
    return str_


print(seven_ate9('165561786121789797'), '16556178612178977')
print(seven_ate9('797'), '77')
print(seven_ate9('7979797'), '7777')
