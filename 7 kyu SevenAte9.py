def seven_ate9(str_):
    for i in range(len(str_)-2):
        if str_[i] == '7' and str_[i+1] == '9' and str_[i+2] == '7':
            str_.replace(str_[i+1], '')
    return str_


print(seven_ate9('165561786121789797'), '16556178612178977')
print(seven_ate9('797'), '77')
print(seven_ate9('7979797'), '7777')
